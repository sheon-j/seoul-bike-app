<template>
  <v-row justify="center">
    <!-- first page -->
    <v-btn
      large
      icon
      plain
      :disabled="page===1"
      class="ml-1 mr-1"
      @click="changePage(1)"
    >
      <v-icon>
        {{ mdiChevronDoubleLeft }}
      </v-icon>
    </v-btn>
    <!-- next page -->
    <v-btn
      large
      icon
      plain
      :disabled="page===1"
      class="ml-1 mr-1"
      @click="changePage(page-1)"
    >
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
      :color="page===index?'success':'grey lighten-1'"
      :outlined="page===index"
      class="ml-1 mr-1 font-weight-bold body-1"
      @click="page!==index?changePage(index):undefined"
    > {{ index }} </v-btn>

    <!-- prev page -->
    <v-btn
      large
      icon
      plain
      :disabled="page===endPage"
      class="ml-1 mr-1"
      @click="changePage(page+1)"
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
      :disabled="page===endPage"
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
import {
  mdiChevronLeft,
  mdiChevronDoubleLeft,
  mdiChevronRight,
  mdiChevronDoubleRight,
} from '@mdi/js'
import _ from 'lodash'

export default {
  props: {
    count: {
      type: Number,
      required: true,
    }
  },

  data() {
    return {
      mdiChevronLeft,
      mdiChevronDoubleLeft,
      mdiChevronRight,
      mdiChevronDoubleRight,
      page: Number(this.$route.query.page) || 1,
      limit: 20,
    }
  },

  computed: {
    endPage() {
      return Math.ceil(this.count / this.limit)
    },

    pages() {
      const startPage = parseInt((this.page - 1) / 10) * 10 + 1
      const endPage = startPage + 10 > this.endPage ? this.endPage + 1 : startPage + 10
      return _.range(startPage, endPage)
    }
  },

  methods: {
    changePage(page) {
      // change state loading
      this.$emit('is-loading')
      // update page
      this.page = page
      const query = {...this.$route.query, page}
      // push query
      this.$router.push({ query })
    }
  },
}
</script>