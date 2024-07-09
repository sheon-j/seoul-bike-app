<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <v-card elevation="0">
        <!-- 타이틀 -->
        <list-title
          class="font-weight-bold pb-0 ml-4 mr-4"
          @show-filter="filterDialog = true"
          @show-todo="todoDialog = true"
        />
        <v-card-text>
          <!-- 로딩 스켈레톤 -->
          <loading-list v-if="isLoading" />
          <div v-else>
            <!-- 리스트 -->
            <bike-list :count="count" :items="items" />
            <!-- 페이지 -->
            <list-pagination
              v-if="count > 0"
              :count="count"
              class="mt-8 mb-0"
              @is-loading="isLoading = true"
            />
          </div>
        </v-card-text>
      </v-card>
    </v-col>
    <!-- 필터링 다이얼로그 -->
    <v-dialog v-model="filterDialog" width="800">
      <search-filter @close="filterDialog = false" />
    </v-dialog>
    <!-- 투두 리스트 -->
    <v-dialog v-model="todoDialog" width="600" height="80vh">
      <todo-list @close="todoDialog = false" />
    </v-dialog>
  </v-row>
</template>

<script>
import { useContext, reactive, watch, useFetch, toRefs } from '@nuxtjs/composition-api'
import ApiService from '@/services/api.service'

export default {
  setup() {
    const { query } = useContext()
    // 상태 관리
    const state = reactive({
      count: 0,
      items: [],
      isLoading: false,
      filterDialog: false,
      todoDialog: false
    })

    // 리스트 페치
    const { fetch } = useFetch(async () => {
      state.isLoading = true
      const params = new URLSearchParams(query.value).toString()
      const { count, results } = await ApiService.get(`bike/?${params}`)
      state.count = count
      state.items = results
      state.isLoading = false
    })

    // 쿼리 변화
    watch(query, fetch)

    return { ...toRefs(state) }
  }
}
</script>
