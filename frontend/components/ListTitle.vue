<template>
  <v-card-title class="pr-0">
    <!-- 타이틀 제목 -->
    서울시 공공자전거 이용현황 🚴
    <v-spacer />
    <!-- 필터 버튼 -->
    <v-btn icon @click="$emit('todo-on')">
      <v-icon> {{ mdiStickerCheckOutline }} </v-icon>
    </v-btn>
    <!-- 필터 버튼 -->
    <v-btn icon @click="$emit('filter-on')">
      <v-icon> {{ mdiTune }} </v-icon>
    </v-btn>
    <v-btn v-show="!isSearchable" icon @click="showSearchBar">
      <v-icon>{{ mdiMagnify }}</v-icon>
    </v-btn>
    <!-- 키워드 검색 -->
    <v-text-field
      v-show="isSearchable"
      ref="searchBar"
      v-model="search"
      dense
      rounded
      outlined
      hide-details
      placeholder="키워드 검색"
      clearable
      :prepend-inner-icon="mdiMagnify"
      color="black"
      class="shrink ml-1"
      @keyup.enter="getSearch"
      @click:prepend-inner="getSearch"
      @click:clear="getClear"
    />
  </v-card-title>
</template>
<script>
import { ref, useContext, useRouter } from '@nuxtjs/composition-api'
import { mdiMagnify, mdiTune, mdiStickerCheckOutline } from '@mdi/js'

export default {
  setup() {
    const { query } = useContext()
    const router = useRouter()
    const search = ref('')
    const searchBar = ref(null)
    const isSearchable = ref(false)

    const getSearch = () => {
      if (search.value) {
        // 텍스트 입력
        const { page, ...rest } = query.value
        rest.search = search.value
        router.push({ query: rest })
        isSearchable.value = false
        search.value = ''
        searchBar.value.blur()
      }
    }

    const getClear = () => {
      const { page, search, ...rest } = query.value
      router.push({ query: rest })
      searchBar.value.blur()
    }

    const showSearchBar = () => {
      isSearchable.value = true
      setTimeout(() => searchBar.value.focus(), 200)
    }

    return {
      search,
      searchBar,
      isSearchable,
      getSearch,
      getClear,
      showSearchBar,
      mdiMagnify,
      mdiTune,
      mdiStickerCheckOutline
    }
  }
}
</script>
<style scoped>
.v-text-field {
  width: 240px;
}
</style>
