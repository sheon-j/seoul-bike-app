<template>
  <section>
    <article>
      <strong class="success--text">
        {{ typeof item.count === 'number' ? item.count.toLocaleString() : item.count }}
      </strong> 건
    </article>
    <v-data-table 
      :headers="headers"
      :items="item.results"
    />
  </section>
</template>
<script>
export default {
  props: {
    item: {
      type: Object,
      default: () => {}
    }
  },
  
  data() {
    return {}
  },

  computed: {
    headers() {
      return [
        {text: '구분', value: 'rental_category', width: '60', sortable: false},
        {text: '대여소', value: 'place_name', width: '200', sortable: false},
        {text: '일시', value: 'rental_date', align: 'right', width: 100},
        {text: '시간', value: 'rental_time', align: 'right', width: 60, sortable: false},
        {text: '이동거리', value: 'travel_distance', align: 'right', width: 100},
        {text: '이동시간', value: 'travel_time', align: 'right', width: 92},
        {text: '성별', value: 'gender', align: 'center', sortable: false, width: 56},
        {text: '연령', value: 'age', sortable: false, width: 68},
        {text: '건수', value: 'count', align: 'right', width: 72},
        {text: '운동량', value: 'exercise', align: 'right', width: 88},
        {text: '탄소량', value: 'carbon', align: 'right', width: 88},
      ]
    }
  }
}
</script>