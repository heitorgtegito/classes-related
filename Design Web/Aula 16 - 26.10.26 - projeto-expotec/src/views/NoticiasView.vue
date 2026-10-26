<script setup>
    import { useNoticiasStore } from '@/stores/useNoticiasStore.js';
    import {ref} from 'vue'
    const noticiasStore = useNoticiasStore()
    
    const titulo = ref('')
    const autor = ref('')
    const descricao = ref('')

    function adicionarNoticiasView(){
        noticiasStore.adicionarNoticias({
            titulo: titulo.value,
            autor: autor.value,
            descricao: descricao.value
        })
        titulo.value = ''
        autor.value = ''
        descricao.value = ''
    }
</script>

<template>
    <p>Notícias</p>
    <form @submit.prevent="adicionarNoticiasView">
        <label>Título <input v-model="titulo"></label>
        <label>Autor <input v-model="autor"></label>
        <label>Descrição <input v-model="descricao"></label>
        <button type="submit">ENVIAR</button>
    </form>
        <div v-for="noticia in noticiasStore.noticias" :key="noticia.id" >
            <h3 >{{ noticia.titulo }}</h3>
            <p> {{noticia.descricao}} </p>
            <button @click="noticiasStore.removerNoticias(noticia.id)">remover</button>
            <button @click="noticiasStore.favoritarNoticias(noticia.id)">{{noticia.favorito ? '❤️' : '🤍' }}</button>
        </div>
</template>