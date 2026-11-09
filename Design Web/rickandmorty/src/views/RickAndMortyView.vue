<script setup>

import { ref, onMounted} from 'vue'
import CardPadrao from '@/components/CardPadrao.vue'

const personagens = ref([])
async function buscarPersonagens(){
    try{
        const respostas = await fetch("https://rickandmortyapi.com/api/character")
        const dados = await respostas.json()
        personagens.value = dados.results
    }catch(erro) {
        console.error('Erro ao buscar: ', erro)
    }
}
onMounted(buscarPersonagens)
</script>

<template>
    <h2>Rick And Morty</h2>
    <div>
        <CardPadrao v-for="item in personagens" :key="item.id" :name="item.name" :imagem="item.image"/>
    </div>
</template>

<style scoped>
    div{
        display:flex;
        flex-wrap: wrap;
    }
</style>