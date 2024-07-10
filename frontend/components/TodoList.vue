<template>
  <v-card height="76vh">
    <!-- 타이틀 -->
    <v-card-title>
      할 일 목록
      <v-spacer />
      <v-btn icon @click="$emit('close')">
        <v-icon> {{ mdiClose }}</v-icon>
      </v-btn>
    </v-card-title>
    <!-- 콘텐츠 -->
    <v-card elevation="0" class="todo-list">
      <v-card-text class="mt-2 mb-2">
        <!-- 투두 리스트 -->
        <v-list lines="two" select-strategy="classic">
          <v-hover v-for="item in items" :key="item.id" #default="{ hover }">
            <v-list-item class="pa-0">
              <!-- 체크박스 -->
              <v-list-item-action>
                <v-checkbox v-model="item.is_checked" :ripple="false" color="accent" />
              </v-list-item-action>
              <!-- 투두아이템 -->
              <v-list-item-content>
                <v-list-item-subtitle class="caption">
                  {{ getInfo(item) }}
                </v-list-item-subtitle>
                <v-list-item-title>
                  {{ item.text }}
                </v-list-item-title>
              </v-list-item-content>
              <!-- 삭제 -->
              <v-list-item-action v-show="hover">
                <v-btn plain text small :ripple="false"> 삭제 </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-hover>
        </v-list>
      </v-card-text>
    </v-card>
    <!-- 입력창 -->
    <v-card elevation="0">
      <v-card-text>
        <v-text-field
          dense
          rounded
          outlined
          color="success"
          :hide-details="true"
          :append-icon="mdiArrowUpCircle"
        />
      </v-card-text>
    </v-card>
  </v-card>
</template>
<script>
import { ref } from '@nuxtjs/composition-api'
import ApiService from '@/services/api.service'
import { mdiClose, mdiArrowUpCircle } from '@mdi/js'

export default {
  setup() {
    const text = ref('')
    const items = ref([])

    const getInfo = ({ username, created_date }) => {
      const createdDate = created_date.replace('T', ' ').slice(0, 16)
      return `${username} | ${createdDate}`
    }

    return {
      text,
      items,
      getInfo,
      mdiClose,
      mdiArrowUpCircle
    }
  }
}
</script>
<style>
.todo-list {
  overflow-y: auto;
  height: calc(76vh - 135px);
}
</style>
