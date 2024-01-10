<template>
  <v-card height="76vh">
    <!-- 타이틀 -->
    <v-card-title>
      오늘 목표
      <v-spacer/>
      <v-btn icon @click="$emit('close')">
        <v-icon> {{ mdiClose }}</v-icon>
      </v-btn>
    </v-card-title>
    <!-- 콘텐츠 -->
    <v-card elevation="0" class="list-card">
      <v-card-text>
        <!-- 투두 리스트 -->
        <v-list lines="two" select-strategy="classic">
          <v-list-item 
            v-for="(item, index) in items" 
            :key="index" 
            class="pa-0"
          >
            <!-- 체크박스 -->
            <v-list-item-action>
              <v-checkbox 
                v-model="item.is_checked" 
                :ripple="false" 
                color="success" 
                @click="check(item)"
              />
            </v-list-item-action>
            <!-- 투두아이템 -->
            <v-list-item-content>
              <v-list-item-subtitle class="caption">
                {{ item.username }} | 
                {{ item.created_date.replace('T', ' ').slice(0, 16) }}
              </v-list-item-subtitle>
              <v-list-item-title>
                {{ item.text }}
              </v-list-item-title>
            </v-list-item-content>
            <!-- 삭제 -->
            <v-list-item-action>
              <v-btn icon small @click=remove(item.id)>
                <v-icon small>{{ mdiTrashCanOutline }}</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
    <!-- 입력창 -->
    <v-card elevation="0" >
      <v-card-text>  
        <v-text-field
          v-model="text"
          outlined
          dense
          color="success"
          :hide-details="true"
          :append-icon="mdiArrowUpBox"
          @keyup.enter="create"
          @click:append="create"
        />
      </v-card-text>
    </v-card>
  </v-card>
</template>
<script>
import ApiService from '@/services/api.service'
import { mdiClose, mdiTrashCanOutline, mdiArrowUpBox } from '@mdi/js'

export default {
  data() {
    return {
      request: ApiService,
      items: [],
      text: null,
      mdiClose,
      mdiTrashCanOutline,
      mdiArrowUpBox,
    }
  },

  fetch() {
    this.list()
  },
  
  methods: {
    async list() {
      this.items = await this.request.get('todo/')
    },

    async create() {
      if (this.text) {
        await this.request.post('todo/', {text: this.text})
        this.text=null
        this.$fetch()
      }
    },
    
    async remove(id) {
      await this.request.delete(`todo/${id}/`)
      this.items = this.items.filter(item => item.id !== id)
    },

    async check(item) {
      await this.request.patch(`todo/${item.id}/`, {is_checked: item.is_checked})
    }
  }
}
</script>
<style>
.list-card {
  overflow-y: auto;
  height: calc(76vh - 135px);
}
</style>