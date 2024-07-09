<script>
import { Bar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Bar,
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
        scales: {
          yAxes: [
            {
              stack: true,
              position: 'right',
              gridLines: { display: false },
              ticks: {
                beginAtZero: true,
                min: 0,
                maxTicksLimit: 5,
                userCallback: (value) => Number(value).toLocaleString()
              }
            }
          ],
          xAxes: [
            {
              stack: true,
              gridLines: {
                display: false,
                zeroLineColor: 'transparent'
              },
              ticks: {
                autoSkip: true,
                maxTicksLimit: 4,
                maxRotation: 0
              }
            }
          ]
        },
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
