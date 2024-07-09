<template>
  <v-card-text>
    <v-row>
      <v-col v-for="({ label, chartData }, index) in items" :key="index" cols="6">
        <span class="font-weight-bold caption">{{ label }}</span>
        <bar-chart :chart-data="chartData" style="height: 140px" />
      </v-col>
    </v-row>
  </v-card-text>
</template>
<script>
import { Bar } from 'vue-chartjs'

export default {
  components: { Bar },
  props: {
    items: {
      type: Array,
      default: () => []
    }
  },
  setup() {}
}
</script>
