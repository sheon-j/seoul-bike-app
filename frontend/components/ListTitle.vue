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
    getSearch() {
      if (this.search) {
        // query routing
        const {page, ...query} = this.$route.query
        query.search = this.search
        this.$router.push({ query })
        // unset
        this.$refs.search.blur()
      }
    }
  }
}
</script>
<style scoped>
.v-text-field{
  width: 240px;
}
</style>