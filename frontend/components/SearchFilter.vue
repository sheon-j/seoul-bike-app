<template>
  <v-card>
    <v-card-title>
      <!-- 제목 -->
      필터링
      <v-spacer />
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
          <v-divider />
          <!-- 필터 항목 -->
          <section
            v-for="(filter, filterIndex) in item.filters"
            :key="filterIndex"
            :class="`filter-text ma-4 ml-0${
              filter.isActive ? ' font-weight-bold black--text' : ''
            }`"
            @click="getFilter(filter)"
          >
            {{ filter.text }}
          </section>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script>
import _ from 'lodash'
import { useContext, computed, useRouter } from '@nuxtjs/composition-api'
import { mdiClose } from '@mdi/js'
export default {
  setup() {
    const getDate = (diff = 0) => {
      // 차이 값 계산한 날짜 값 반환
      const today = new Date()
      const pastDate = today.setDate(today.getDate() + diff)
      return new Date(pastDate).toISOString().slice(0, 10)
    }

    const { query } = useContext()
    const router = useRouter()
    const items = computed(() => {
      const items = [
        {
          title: '일시',
          filters: [
            {
              text: '오늘',
              value: {
                rental_date__gte: getDate(),
                rental_date__lte: getDate()
              }
            },
            {
              text: '어제',
              value: {
                rental_date__gte: getDate(-1),
                rental_date__lte: getDate()
              }
            },
            {
              text: '최근 7일',
              value: {
                rental_date__gte: getDate(-7),
                rental_date__lte: getDate()
              }
            },
            {
              text: '최근 30일',
              value: {
                rental_date__gte: getDate(-30),
                rental_date__lte: getDate()
              }
            },
            {
              text: '최근 1년 ',
              value: {
                rental_date__gte: getDate(-365),
                rental_date__lte: getDate()
              }
            }
          ]
        },
        {
          title: '구분',
          filters: [
            {
              text: '중요',
              value: { mark: 'true' }
            },
            {
              text: '남자',
              value: { gender: 'M' }
            },
            {
              text: '여자',
              value: { gender: 'F' }
            },
            {
              text: '정기권',
              value: { rental_category__contains: '정기' }
            },
            {
              text: '일일권',
              value: { rental_category__contains: '일일' }
            },
            {
              text: '단체권',
              value: { rental_category__contains: '단체' }
            }
          ]
        },
        {
          title: '연령대',
          filters: [
            {
              text: '~10대',
              value: { age__contains: '10' }
            },
            {
              text: '20대',
              value: { age__contains: '20' }
            },
            {
              text: '30대',
              value: { age__contains: '30' }
            },
            {
              text: '40대',
              value: { age__contains: '40' }
            },
            {
              text: '50대',
              value: { age__contains: '50' }
            },
            {
              text: '60대',
              value: { age__contains: '60' }
            },
            {
              text: '70대~',
              value: { age__contains: '70' }
            }
          ]
        },
        {
          title: '수치',
          filters: [
            {
              text: '이동시간 1시간 이상',
              value: { travel_time__gte: '60' }
            },
            {
              text: '이동시간 1시간 미만',
              value: { travel_time__lt: '60' }
            },
            {
              text: '이동거리 5km 이상',
              value: { travel_distance__gte: '5000' }
            },
            {
              text: '이동거리 5km 미만',
              value: { travel_distance__lt: '5000' }
            }
          ]
        },
        {
          title: '정렬기준',
          filters: [
            {
              text: '오래된 순',
              value: { ordering: 'rental_date,rental_time' }
            },
            {
              text: '이동시간',
              value: { ordering: '-travel_time' }
            },
            {
              text: '이동거리',
              value: { ordering: '-travel_distance' }
            },
            {
              text: '건수',
              value: { ordering: '-count' }
            },
            {
              text: '운동량',
              value: { ordering: '-exercise' }
            },
            {
              value: { ordering: '-carbon' }
            }
          ]
        } // 각 filter 요소 마다 쿼리가 적용되었는지 확인하는 isActive 삽입
      ]
      items.map((item) => {
        item.filters.map((filter) => {
          const isActive = _.isMatch(query.value, filter.value)
          return (filter.isActive = isActive)
        })
      })
      return items
    })

    const getFilter = ({ isActive, value }) => {
      const { page, ...rest } = query.value
      console.log(page, rest)
      let filters
      if (isActive) {
        filters = Object.keys(rest).reduce((acc, cur) => {
          if (!Object.keys(value).includes(cur)) {
            acc[cur] = rest[cur]
          }
          return acc
        }, {})
      } else {
        filters = { ...rest, ...value }
      }
      router.push({ query: filters })
    }

    return {
      items,
      query,
      getFilter,
      mdiClose
    }
  }
}
</script>
<style>
.filter-text:hover {
  cursor: pointer;
}
</style>
