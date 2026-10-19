<script setup>

import { ref } from 'vue'

import foto01 from '@/assets/fotos/foto01.png'
import foto02 from '@/assets/fotos/foto02.png'
import foto03 from '@/assets/fotos/foto03.png'
import foto04 from '@/assets/fotos/foto04.png'
import foto05 from '@/assets/fotos/foto05.png'
import foto06 from '@/assets/fotos/foto06.png'

const fotos = ref([
    { id: 1, imagem: foto01, texto: 'Foto muito irado do baixo', descricao: 'Descrição...', class: 'foto'},
    { id: 2, imagem: foto02, texto: 'Foto muito irado da bateria', descricao: 'Descrição...', class: 'foto' },
    { id: 3, imagem: foto03, texto: 'Foto muito irado do baixopt2', descricao: 'Descrição...', class: 'foto' },
    { id: 4, imagem: foto04, texto: 'Foto muito irado da guitarra', descricao: 'Descrição...', class: 'foto' },
    { id: 5, imagem: foto05, texto: 'Foto muito irado de VINI!', descricao: 'Descrição...', class: 'foto' },
    { id: 6, imagem: foto06, texto: 'Poster Halloween AfterTrauma', descricao: 'Descrição...', class: 'poster' }
])

</script>
<template>
    <div class="section-mural-fotos">
        <ul class="mural-fotos">
            <li v-for="foto in fotos" :key="foto.id" :class="foto.class">
                <img :src="foto.imagem" :alt="foto.descricao"> <br>
                {{ foto.texto }}
            </li>
        </ul>
    </div>
</template>