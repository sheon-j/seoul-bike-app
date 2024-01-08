<template>
  <v-card-title>
    <!-- 타이틀 제목 -->
    서울시 공공자전거 이용현황 🚴
    <v-spacer/>
    <!-- 키워드 검색 -->
    <v-text-field
      ref="search"
      v-model="search"
      outlined
      dense
      hide-details
      placeholder="키워드 검색"
      clearable
      :prepend-inner-icon="mdiMagnify"
      color="black"
      class="shrink rounded-lg ml-1 mr-1"
      @keyup.enter="getSearch"
      @click:prepend-inner="getSearch"
      @click:clear="getClear"
    />
    <!-- 필터 버튼 -->
    <v-btn icon @click="$emit('dialog-on')">
      <v-icon> {{ mdiTune }} </v-icon>
    </v-btn>
  </v-card-title>
</template>
<script>
import { mdiMagnify, mdiTune } from '@mdi/js'

export default {
  data() {
    return {
      search: this.$route.query.search || '',
      mdiMagnify,
      mdiTune,
    }
  }, 
  methods: {
    // 함수 정의
    getSearch() {
      if (this.search) { // 텍스트 입력
        // 페이지 제외
        const {page, ...query} = this.$route.query
        // 이전 쿼리 값 전이
        query.search = this.search
        this.$router.push({ query })
        // 포커스 해제
        this.$refs.search.blur()
      }
    },

    getClear() {
      const {page, search, ...query} = this.$route.query
      this.$router.push({ query })
      // 포커스 해제
      this.$refs.search.blur()
    },
  }
}
</script>
<style scoped>
.v-text-field{
  width: 240px;
}
</style>