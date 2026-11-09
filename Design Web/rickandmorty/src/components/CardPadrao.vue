<script setup>
    defineProps({
        name: {type: String,required: true},
        imagem: {type: String, default: ''},
        largura:{type: String,default: "300px"}
    })
</script>
<template>
    <div class="card" :style="{width: largura}">
        <img v-if="imagem" :src="imagem" :alt="name" />
        <div>
            <h3>{{name}}</h3>
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
        height: 180px;
    }
    div.card div{
        padding: 12px 16px;
        color: #333333;
    }
    div.card h3 {
        margin: 0 0 4px 0;
        font-size: 1.1rem;
    }
    div.card p {
        margin: 0 0 8px 0;
        font-size: 0.9rem;
        color: #444444;
    }
</style>