<template>
  <section>
    <v-skeleton-loader
      v-for="index in 20"
      :key="index"
      class="mx-auto border mb-2"
      type="text, divider"
    />
  </section>
</template>