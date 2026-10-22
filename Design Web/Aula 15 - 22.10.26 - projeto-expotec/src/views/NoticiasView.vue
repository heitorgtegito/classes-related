<script setup>
    import { useNoticiasStore } from '@/stores/useNoticiasStore.js';
    const noticiasStore = useNoticiasStore()
</script>

<template>
    <p>notícias</p>
        <div v-for="noticia in noticiasStore.noticias" :key="noticia.id" >
            <h3 >{{ noticia.titulo }}</h3>
        </div>
</template>