<template>
  <v-app>
    <v-app-bar fixed app>
      <v-spacer/>
        <v-toolbar-title> 
          <nuxt-link to="/">
            <img src="~/assets/seoul-bike.png" height="30" class="mt-4"/>
          </nuxt-link>
        </v-toolbar-title>
      <v-spacer/>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer app>
      <v-spacer />
      <span>&copy; {{ new Date().getFullYear() }}</span>
      <v-spacer />
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>
