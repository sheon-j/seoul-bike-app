<script>
import { Doughnut, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Doughnut,
  mixins: [reactiveProp],

  props: {
    chartData: {
      type: Object,
      default: () => {},
      required: true
    }
  },

  data() {
    return {
      options: {
        maintainAspectRatio: false,
        legend: false,
        animation: {
          duration: 0
        }
      }
    }
  },

  mounted() {
    this.renderChart(this.chartData, this.options)
  }
}
</script>
