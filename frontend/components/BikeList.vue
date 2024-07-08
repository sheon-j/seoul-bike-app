<template>
  <section>
    <!-- 건수 -->
    <article class="ml-4">
      {{ describe }}
      <strong class="success--text">
        {{ typeof item.count === 'number' ? item.count.toLocaleString() : item.count }}
      </strong> 건
      <!-- 초기화 -->
      <v-btn
        v-if="Object.keys(query).length>0"
        text
        x-small
        elevation="0"
        plain
        to="/"
        class="ml-2 pl-0 pr-0 black--text"
      >
        <v-icon x-small class="mr-1"> {{ mdiRefresh }} </v-icon>
        초기화
      </v-btn>
    </article>
    <!-- 데이터 리스트 -->
    <v-data-table 
      :headers="headers"
      :items="item.results"
      :items-per-page="-1"
      hide-default-footer
      no-data-text="조회 가능한 데이터가 없습니다."
      class="mt-8"
    >
      <!-- 중요 -->
      <template #[`item.mark`]="{ item, value }">
        <v-btn icon small @click="mark(item)">
          <v-icon v-if="value" color="success lighten-2"> {{ mdiStar }} </v-icon>
          <v-icon v-else color="grey lighten-1"> {{ mdiStarOutline }} </v-icon>
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
  </section>
</template>
<script>
import { mdiRefresh, mdiStar, mdiStarOutline } from '@mdi/js'
import ApiService from '@/services/api.service'

export default {
  props: {
    item: {
      type: Object,
      default: () => {}
    }
  },

  data() {
    return {
      request: ApiService,
      mdiRefresh,
      mdiStar, 
      mdiStarOutline,
    }
  },

  computed: {
    headers() { // 테이블 헤더
      return [
        { text: '중요', value: 'mark', align:'center', width: 28, sortable: false,},
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
        { text: '탄소량', value: 'carbon', align: 'right', width: 88, sortable: false },
      ]
    },
    
    query() {
      const { page, ...query } = this.$route.query
      return query
    },

    describe() {
      // 조건별 건수 설명 표기
      if (this.query.search) {
        return `"${this.query.search}"에 대한 검색 결과`
      } else if (Object.keys(this.query).length > 0) {
        return '필터링 결과'
      } else {
        return '전체'
      }
    },
  },

  methods: {
    async mark(item) {
      item.mark = !item.mark
      await this.request.patch( // patch request
        `bike/${item.id}/`, 
        { mark: item.mark },
      )
    }
  },
}
</script>