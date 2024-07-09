<template>
  <div>
    <!-- 건수 -->
    <article class="ml-4">
      {{ describe }} <strong class="primary--text">{{ itemsCount }}</strong
      >건
      <!-- 초기화 -->
      <v-btn v-if="search || filters" text x-small elevation="0" plain to="/">
        <v-icon x-small class="mr-1"> {{ mdiRefresh }} </v-icon>
        초기화
      </v-btn>
    </article>
    <!-- 데이터 리스트 -->
    <v-data-table
      v-if="count"
      :headers="headers"
      :items="items"
      :items-per-page="-1"
      hide-default-footer
      no-data-text="조회 가능한 데이터가 없습니다."
      class="mt-8"
    >
      <!-- 중요 -->
      <template #[`item.mark`]="{ item, value }">
        <v-btn icon small @click="markItem(item)">
          <v-icon v-if="value" color="accent"> {{ mdiStar }} </v-icon>
          <v-icon v-else color="grey"> {{ mdiStarOutline }} </v-icon>
        </v-btn>
      </template>

      <!-- 구분 -->
      <template #[`item.rental_category`]="{ value }">
        <span class="font-weight-bold">{{ value }}</span>
      </template>

      <!-- 일시 -->
      <template #[`item.rental_date`]="{ value }">
        <span class="caption">{{ value }}</span>
      </template>

      <!-- 시간 -->
      <template #[`item.rental_time`]="{ value }">
        <span class="caption">{{ value }}</span>
      </template>
    </v-data-table>
    <div v-else class="empty">
      <v-avatar color="green accent-2" class="ma-8">
        <v-icon large>{{ mdiExclamationThick }}</v-icon>
      </v-avatar>
      <h2>조회할 수 있는 데이터가 없습니다.</h2>
    </div>
  </div>
</template>
<script>
import { useContext, computed } from '@nuxtjs/composition-api'
import { mdiRefresh, mdiStar, mdiStarOutline, mdiExclamationThick } from '@mdi/js'
import ApiService from '@/services/api.service'

export default {
  props: {
    count: {
      type: Number,
      default: 0
    },
    items: {
      type: Array,
      default: () => {}
    }
  },

  setup(props) {
    const { query } = useContext()
    const headers = [
      { text: '중요', value: 'mark', align: 'center', width: 28, sortable: false },
      { text: '구분', value: 'rental_category', width: 112, sortable: false },
      { text: '대여소', value: 'place_name', width: '200', sortable: false },
      { text: '일시', value: 'rental_date', align: 'right', width: 100, sortable: false },
      { text: '시간', value: 'rental_time', align: 'right', width: 84, sortable: false },
      { text: '이동거리', value: 'travel_distance', align: 'right', width: 100, sortable: false },
      { text: '이동시간', value: 'travel_time', align: 'right', width: 100, sortable: false },
      { text: '성별', value: 'gender', align: 'center', width: 56, sortable: false },
      { text: '연령', value: 'age', align: 'right', width: 72, sortable: false },
      { text: '건수', value: 'count', align: 'right', width: 72, sortable: false },
      { text: '운동량', value: 'exercise', align: 'right', width: 88, sortable: false },
      { text: '탄소량', value: 'carbon', align: 'right', width: 88, sortable: false }
    ]

    // 아이템 수
    const itemsCount = computed(() => {
      return props.count.toLocaleString()
    })

    // 페이지를 제외한 필터 수
    const filters = computed(() => {
      const { page, search, ...filters } = query.value
      return Object.keys(filters).length
    })

    const search = computed(() => {
      const { search } = query.value
      return search
    })

    // 필터 개요
    const describe = computed(() => {
      if (search.value) {
        return `"${search.value}"에 대한 검색 결과`
      } else if (filters.value) {
        return `${filters.value}개 필터링 결과`
      } else {
        return '전체'
      }
    })

    // 중요 표시
    const markItem = async (item) => {
      let { id, mark } = item
      mark = !mark
      item.mark = mark
      await ApiService.patch(`bike/${id}/`, { mark })
    }

    return {
      headers,
      itemsCount,
      filters,
      search,
      describe,
      markItem,
      mdiRefresh,
      mdiStar,
      mdiStarOutline,
      mdiExclamationThick
    }
  }
}
</script>
<style>
.empty {
  text-align: center;
  margin-top: 100px;
}
</style>
