<script setup>

import { ref, onMounted} from 'vue'
import CardPadrao from '@/components/CardPadrao.vue'

const locais = ref([])
async function buscarLocais(){
    try{
        const respostas = await fetch("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
        const dados = await respostas.json()
        locais.value = dados
    }catch(erro) {
        console.error('Erro ao buscar: ', erro)
    }
}
onMounted(buscarLocais)
</script>

<template>
    <h2>Localidades</h2>
    <p><RouterLink to="/rickandmorty">Rick And Morty</RouterLink></p>
    <div class="card-grid">
        <CardPadrao v-for="item in locais" 
        :key="item.id" 
        :sigla="item.sigla" 
        :nome="item.nome"
        :regiao="item.regiao.nome"
        />
    </div>
</template>

<style scoped>
    div{
        display:flex;
        flex-wrap: wrap;
    }
</style>