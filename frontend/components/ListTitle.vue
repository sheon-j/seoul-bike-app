<template>
  <v-card-title>
    서울시 공공자전거 이용현황 🚴
    <v-spacer/>
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
      class="shrink rounded-lg"
      @keyup.enter="getSearch"
      @click:prepend-inner="getSearch"
    />
  </v-card-title>
</template>
<script>
import { mdiMagnify } from '@mdi/js'

export default {
  data() {
    return {
      search: this.$route.query.search || '',
      mdiMagnify,
    }
  }, 
  methods: {
    getSearch() {
      if (this.search) {
        console.log('act!')
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