<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <v-card elevation="0">
        <!-- 타이틀 -->
        <list-title 
          class="font-weight-bold pb-0 ml-4 mr-4"
          @filter-on="filterDialog=true"
          @todo-on="todoDialog=true"
        />
        <!-- 검색 필터 다이얼로그 -->
        <v-dialog v-model="filterDialog" width="800">
          <search-filter @close="filterDialog=false"/>
        </v-dialog>
        <!-- 투두 리스트 -->
        <v-dialog v-model="todoDialog" width="600" height="80vh">
          <todo-list
            @close="todoDialog=false"
          />
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
    // 뷰의 반응성 데이터 속성
    return {
      item: null,           // fetch 할 리스트 아이템
      loading: false,       // 로딩 정보를 표시할 Boolean
      request: ApiService,  // Api 요청을 위한 클래스
      filterDialog: false,  // 다이얼로그를 표시할 Boolean
      todoDialog: false,    // Todo 다이얼로그
    }
  },

  computed: {
    // 가독성을 높히는 속성
    query() {
      return this.$route.query
    }
  },

  watch: {
    // 특정 데이터의 변화를 감지하여 자동으로 로직을 수행
    query() {
      // 쿼리 값이 바뀌면 fetch() 수행
      this.$fetch()
    }
  },

  async fetch() {
    // backend로 부터 데이터 페치
    this.loading = true
    // {k1: v1, k2: v2} -> k1=v1&k2=v2 
    const params = new URLSearchParams(this.query).toString()
    this.item = await this.request.get(`bike/?${params}`)
    this.loading = false
  },
}
</script>
