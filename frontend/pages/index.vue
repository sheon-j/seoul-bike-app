<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <v-card elevation="0">
        <!-- 타이틀 -->
        <list-title 
          class="font-weight-bold pb-0 ml-4 mr-4"
          @dialog-on="dialog=true"
        />
        <!-- 검색 필터 다이얼로그 -->
        <v-dialog v-model="dialog" width="800">
          <search-filter @close="dialog=false"/>
        </v-dialog>
        <v-card-text>
          <!-- 로딩 스켈레톤 -->
          <loading-list v-if="loading"/>
          <section v-else-if="item">
            <!-- 리스트 -->
            <bike-list :item="item"/>
            <!-- 페이지 -->
            <list-pagination
              v-if="item.count>0"
              :count="item.count" 
              class="mt-4 mb-0"
              @is-loading="loading=true"
            />
          </section>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import ApiService from '@/services/api.service'

export default {
  name: 'IndexPage',
  
  data() {
    return {
      item: null,
      loading: false,
      request: ApiService,
      dialog: false
    }
  },

  computed: {
    query() {
      return this.$route.query
    }
  },

  watch: {
    query() {
      this.$fetch()
    }
  },

  async fetch() {
    this.loading = true
    const params = new URLSearchParams(this.query).toString()
    this.item = await this.request.get(`bike/?${params}`)
    this.loading = false
  },
}
</script>
