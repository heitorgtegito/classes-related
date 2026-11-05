<script setup lang="ts">
  import { RouterView } from 'vue-router';
import SectionHeader from './components/SectionHeader.vue';
</script>

<template>
  <SectionHeader></SectionHeader>
  <main>
    <!-- RouterView tem que ficar dentro do main, até porque o conteúdo dos arquivos views ficarão dentro do main -->
    <RouterView></RouterView>
  </main>
</template>
