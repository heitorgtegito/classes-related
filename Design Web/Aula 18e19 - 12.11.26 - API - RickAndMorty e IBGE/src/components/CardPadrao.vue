<script setup>
import { useRoute } from 'vue-router';
const route = useRoute()
defineProps({
    name: {type: String, default: ''},
    imagem: {type: String, default: ''},
    species: {type: String, default: ''},
    status: {type: String, default: ''},
    gender: {type: String, default: ''},
    url: {type: String, default: ''},
    location: {type: String, default: ''},
    largura:{type: String,default: "300px"},
    nome: { type: String, default: '' },
    sigla: { type: String, default: '' },
    regiao: { type: String, default: '' }
})
</script>
<template>
    <div v-if="route.name === 'rickandmorty'" class="card" :style="{width: largura}">
        <img v-if="imagem" :src="imagem" :alt="name" />
        <div>
            <h3>{{name}}</h3>
            <h4>{{ species }} - {{ status }}</h4>
            <p>{{ gender }}</p>
            <p>{{location}}</p>
            <a :href="url">Visite a página do personagem</a>
        </div>
    </div>
    <div v-else-if="route.name === 'localidades'" class="card" id="localidades">
        <div>
            <h3>{{nome}}</h3>
            <h4>{{ sigla }}</h4>
            <p>{{ regiao }}</p>
        </div>
    </div>
</template>

<style scoped>
    div.card {
        width: 300px;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 1rem;
    }
    div img {
        width: 100%;
        height: 300px;
    }
    div.card div{
        padding: 12px 16px;
        color: #333333;
    }
    div.card h3 {
        font-size: 24px;
    }
    div.card h4 {
        font-size: 20px;
    }
    div.card p {
        text-align: left;
        font-size: 18px;
        color: #444444;
    }
    div.card p, h4, h3 {
        margin: 8px 0 0 0;
    }
    #localidades h3, h4, p {
        display: block;
    }
</style>