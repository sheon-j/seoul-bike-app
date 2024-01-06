<template>
  <section>
    <article class="ml-4">
      {{ describe }}
      <strong class="success--text">
        {{ typeof item.count === 'number' ? item.count.toLocaleString() : item.count }}
      </strong> 건
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
    <v-data-table 
      :headers="headers"
      :items="item.results"
      :items-per-page="-1"
      hide-default-footer
      no-data-text="조회 가능한 데이터가 없습니다."
      class="mt-8"
    />
  </section>
</template>
<script>
import { mdiRefresh } from '@mdi/js'

export default {
  props: {
    item: {
      type: Object,
      default: () => {}
    }
  },

  data() {
    return {
      mdiRefresh,
    }
  },

  computed: {
    headers() { // 테이블 헤더
      return [
        { text: '구분', value: 'rental_category', width: '112', sortable: false },
        { text: '대여소', value: 'place_name', width: '200', sortable: false },
        { text: '일시', value: 'rental_date', align: 'right', width: 100, sortable: false },
        { text: '시간', value: 'rental_time', align: 'right', width: 60, sortable: false },
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
    }
  }
}
</script>