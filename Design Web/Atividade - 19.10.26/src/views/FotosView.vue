<script setup>
    import Carrossel from '@/components/CarrosselComponent.vue'
</script>

<template>
    <article class="main-content">
        <div class="fotos">
            <h2>Nossas Fotos</h2>
            <Carrossel></Carrossel>
        </div>
    </article>
</template>

<script>
    export default {
        name: 'FotosView'
    }
</script>