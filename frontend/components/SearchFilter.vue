<template>
  <v-card>
    <v-card-title> 
      <!-- 제목 -->
      검색 필터 
      <v-spacer/>
      <!-- 닫기 버튼 -->
      <v-btn icon @click="$emit('close')"> 
        <v-icon> {{ mdiClose }} </v-icon>
      </v-btn>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col v-for="(item, index) in items" :key="index">
          <!-- 구분 타이틀 -->
          <article class="font-weight-bold caption">
            {{ item.title }}
          </article>
          <v-divider/>
          <!-- 필터 항목 -->
          <section
            v-for="(filter, filterIndex) in item.filters" 
            :key="filterIndex"
            :class="`filter-text ma-4 ml-0${
              filter.isActive ? ' font-weight-bold black--text': ''
            }`"
            @click="getSearch(filter.isActive, filter.value)"
          >
            {{filter.text}}
          </section>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script>
import _ from 'lodash'
import { mdiClose } from '@mdi/js'
export default {
  data() {
    return {
      mdiClose,
    }
  },
  computed: {
    query() {
      return this.$route.query
    },

    today() {
      return new Date().toISOString().split('T')[0]
    },

    items() {
      return [
        {
          title: "일시",
          filters: [
            {
              text: '오늘',
              value: {
                rental_date__gte: this.getDate(),
                rental_date__lte: this.getDate(),
              },
            },
            {
              text: '어제',
              value: {
                rental_date__gte: this.getDate(-1),
                rental_date__lte: this.getDate(),
              },
            },
            {
              text: '최근 7일',
              value: {
                rental_date__gte: this.getDate(-7),
                rental_date__lte: this.getDate(),
              },
            },
            {
              text: '최근 30일',
              value: {
                rental_date__gte: this.getDate(-30),
                rental_date__lte: this.getDate(),
              },
            },
            {
              text: '최근 1년 ',
              value: {
                rental_date__gte: this.getDate(-365),
                rental_date__lte: this.getDate(),
              },
            },
          ],
        },
        {
          title: "구분",
          filters: [
            {
              text: '남자',
              value: {gender: 'M'},
            },
            {
              text: '여자',
              value: {gender: 'F'},
            },
            {
              text: '정기권',
              value: {rental_category__contains: '정기'},
            },
            {
              text: '일일권',
              value: {rental_category__contains: '일일'},
            },
            {
              text: '단체권',
              value: {rental_category__contains: '단체'},
            },
          ],
        },
        {
          title: '연령대',
          filters: [
            {
              text: '~10대',
              value: {age__contains: '10'}
            },
            {
              text: '20대',
              value: {age__contains: '20'}
            },
            {
              text: '30대',
              value: {age__contains: '30'}
            },
            {
              text: '40대',
              value: {age__contains: '40'}
            },
            {
              text: '50대',
              value: {age__contains: '50'}
            },
            {
              text: '60대',
              value: {age__contains: '60'}
            },
            {
              text: '70대~',
              value: {age__contains: '70'}
            },
          ]
        },
        {
          title: "수치",
          filters: [
            {
              text: '이동시간 1시간 이상',
              value: {travel_time__gte: '60'}
            },
            {
              text: '이동시간 1시간 미만',
              value: {travel_time__lt: '60'}
            },
            {
              text: '이동거리 5km 이상',
              value: {travel_distance__gte: '5000'}
            },
            {
              text: '이동거리 5km 미만',
              value: {travel_distance__lt: '5000'}
            },
          ],
        },
        {
          title: "정렬기준",
          filters: [
            {
              text: '오래된 순',
              value: {ordering: 'rental_date,rental_time'},
            },
            {
              text: '이동시간',
              value: {ordering: '-travel_time'},
            },
            {
              text: '이동거리',
              value: {ordering: '-travel_distance'},
            },
            {
              text: '건수',
              value: {ordering: '-count'}
            },
            {
              text: '운동량',
              value: {ordering: '-exercise'},
            },
            {
              text: '탄소량',
              value: {ordering: '-carbon'},
            },
          ],
        }, // 각 filter 요소 마다 쿼리가 적용되었는지 확인하는 isActive 삽입
      ].map( item => { 
        item.filters.map( filter => {
          // 쿼리에 필터 value 가 포함되어있는지 확인
          const isActive = _.isMatch(this.query, filter.value)
          return filter.isActive = isActive
        })
        return item 
      })
    },
  },

  methods: {
    getSearch(active, value) { // 필터 적용 로직
      const {page, ...prevQuery} = this.query
      // 쿼리 유무에 따라 로직 분기
      const query = active ? 
        // 쿼리 있음
        Object.keys(prevQuery).reduce((acc, cur) => {
          // URL 쿼리 키에 value 키가 없으면 acc 에 삽입 (있는 값은 삭제)
          if (!Object.keys(value).includes(cur)) {
            acc[cur]=prevQuery[cur]
          }
          return acc
        }, {}) : 
        // 쿼리 없음
        { ...prevQuery, ...value }
      this.$router.push({ query })
    },

    getDate(diff=0) { // 차이 값 계산한 날짜 값 반환
      const date = new Date()
      const setDate = date.setDate(date.getDate() + diff)
      return new Date(setDate).toISOString().split('T')[0]
    }
  }
}
</script>
<style>
.filter-text:hover {
  cursor: pointer;
}
</style>