<template>
  <v-row justify="center">
    <!-- first page -->
    <v-btn large icon plain :disabled="page === 1" class="ml-1 mr-1" @click="changePage(1)">
      <v-icon>
        {{ mdiChevronDoubleLeft }}
      </v-icon>
    </v-btn>
    <!-- next page -->
    <v-btn large icon plain :disabled="page === 1" class="ml-1 mr-1" @click="changePage(page - 1)">
      <v-icon>
        {{ mdiChevronLeft }}
      </v-icon>
    </v-btn>

    <!-- number button -->
    <v-btn
      v-for="index in pages"
      :key="index"
      :value="index"
      large
      icon
      :color="page === index ? 'success' : 'grey lighten-1'"
      :outlined="page === index"
      class="ml-1 mr-1 font-weight-bold body-1"
      @click="page !== index ? changePage(index) : undefined"
    >
      {{ index }}
    </v-btn>

    <!-- prev page -->
    <v-btn
      large
      icon
      plain
      :disabled="page === endPage"
      class="ml-1 mr-1"
      @click="changePage(page + 1)"
    >
      <v-icon>
        {{ mdiChevronRight }}
      </v-icon>
    </v-btn>
    <!-- last page -->
    <v-btn
      large
      icon
      plain
      :disabled="page === endPage"
      class="ml-1 mr-1"
      @click="changePage(endPage)"
    >
      <v-icon>
        {{ mdiChevronDoubleRight }}
      </v-icon>
    </v-btn>
  </v-row>
</template>
<script>
import { ref, computed, useContext, useRouter } from '@nuxtjs/composition-api'
import {
  mdiChevronLeft,
  mdiChevronDoubleLeft,
  mdiChevronRight,
  mdiChevronDoubleRight
} from '@mdi/js'
import _ from 'lodash'

export default {
  props: {
    count: {
      type: Number,
      required: true
    }
  },

  setup(props, { emit }) {
    const { query } = useContext()
    const router = useRouter()
    const limit = 20
    const page = ref(Number(query.value.page) || 1)
    const endPage = computed(() => Math.ceil(props.count / limit))

    const changePage = (p) => {
      emit('is-loading')
      page.value = p
      const pagingQuery = { ...query.value, page: p }
      router.push({ query: pagingQuery })
    }

    const pages = computed(() => {
      const firstPage = parseInt((page.value - 1) / 10) * 10 + 1
      const lastPage = firstPage + 10 > endPage.value ? endPage.value + 1 : firstPage + 10
      return _.range(firstPage, lastPage)
    })

    return {
      limit,
      page,
      endPage,
      pages,
      changePage,
      mdiChevronLeft,
      mdiChevronDoubleLeft,
      mdiChevronRight,
      mdiChevronDoubleRight
    }
  }
}
</script>
