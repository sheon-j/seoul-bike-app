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
                <v-checkbox
                  v-model="item.is_checked"
                  :ripple="false"
                  color="accent"
                  @click="check(item)"
                />
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
                <v-btn plain text small :ripple="false" @click="remove(item)"> 삭제 </v-btn>
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
          v-model="text"
          dense
          rounded
          outlined
          color="success"
          :hide-details="true"
          :append-icon="mdiArrowUpCircle"
          @keyup.enter="create"
          @click:append="create"
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

    const list = async () => {
      items.value = await ApiService.get('todo/')
    }

    const create = async () => {
      if (text.value) {
        await ApiService.post('todo/', { text: text.value })
        text.value = ''
        list()
      }
    }

    const remove = async ({ id }) => {
      await ApiService.delete(`todo/${id}/`)
      items.value = items.value.filter(({ id: itemId }) => itemId !== id)
    }

    const check = async ({ id, is_checked }) => {
      await ApiService.patch(`todo/${id}/`, { is_checked })
    }

    const getInfo = ({ username, created_date }) => {
      const createdDate = created_date.replace('T', ' ').slice(0, 16)
      return `${username} | ${createdDate}`
    }

    list()

    return {
      text,
      items,
      list,
      create,
      remove,
      check,
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
