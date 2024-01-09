<template>
  <v-card>
    <v-card-title>
      오늘 목표
      <v-spacer/>
      <v-btn icon @click="$emit('close')">
        <v-icon> {{ mdiClose }}</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-text>
      <v-list lines="two" select-strategy="classic">
        <v-list-item 
          v-for="(item, index) in items" 
          :key="index" 
          class="pa-0"
        >
          <v-list-item-action>
            <v-checkbox v-model="item.check" :ripple="false" color="success"/>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-subtitle class="caption">
              {{ item.username }} | {{ item.date }}
            </v-list-item-subtitle>
            <v-list-item-title>
              {{ item.text }}
            </v-list-item-title>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn icon small @click=remove(item.id)>
              <v-icon small>{{ mdiTrashCanOutline }}</v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </v-list>
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
</template>
<script>
import { mdiClose, mdiTrashCanOutline, mdiArrowUpBox } from '@mdi/js'

export default {
  data() {
    return {
      mdiClose,
      mdiTrashCanOutline,
      mdiArrowUpBox,
      items: [],
      text: null,
    }
  },

  fetch() {
    // 리스트 페치 추가
    this.items = [
      {id: 1, text: '서영락 대리님 정기 점검 해주세요.', check: false, username: '데이지', date: '2024.01.11 11:30'},
      {id: 2, text: '1월 2주차 이상치 파악', check: true, username: '스콧', date: '2024.01.11 11:35'},
    ]
  },

  methods: {
    create() {
      if (this.text) {
        this.items.push({
          id: this.items.length,
          text: this.text,
          check: false,
          username: '테스터',
          date: '2024.01.11 12:00',
        })
        this.text = null
      }
    },
    
    remove(id) {
      this.items = this.items.filter( item => item.id !== id )
    }
  }
}
</script>