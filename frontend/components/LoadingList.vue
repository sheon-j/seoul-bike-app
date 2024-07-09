<template>
  <section>
    <v-skeleton-loader type="text" width="80" class="ml-4 mr-4 mt-1 mb-14" />
    <v-skeleton-loader
      v-for="index in 20"
      :key="index"
      class="mx-auto border mb-7 mr-4 ml-4"
      type="text"
    />
  </section>
</template>
