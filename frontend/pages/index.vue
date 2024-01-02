<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <v-card elevation="0">
        <v-card-title class="font-weight-bold pb-0">
          서울시 공공자전거 이용현황 🚴
        </v-card-title>
        <v-card-text>
          <LoadingList v-if="loading"/>
          <BikeList v-else :item="item"/>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import ApiService from '@/services/api.service'

export default {
  name: 'IndexPage',
  data() {
    return {
      item: null,
      loading: false,
      request: ApiService
    }
  },

  async fetch() {
    this.loading = true
    this.item = await this.request.get('bike/')
    this.loading = false
  },

  methods: {
  }
}
</script>
