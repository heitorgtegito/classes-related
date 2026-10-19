<template>
  <HeaderSection></HeaderSection>
  <router-view></router-view>
  <FooterSection></FooterSection>
</template>

<script>
  import HeaderSection from './components/HeaderComponent.vue'
  import FooterSection from './components/FooterComponent.vue'
  import './assets/css/main.css'
export default {
  name: 'App',
  components: {
    HeaderSection,
    FooterSection
  }
}
</script>