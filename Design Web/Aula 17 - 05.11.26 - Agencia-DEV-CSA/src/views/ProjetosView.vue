<script setup lang="ts">
import { useProjetoStore } from '../stores/useProjetoStore';
const projetosStore = useProjetoStore()
</script>


<template>
    <article>
        <h2>Projetos</h2>
        <ul>
            <li v-for="proj in projetosStore.projetos" :key="proj.id">
                <h3>{{ proj.nome }}</h3>
                <p>{{ proj.descricao }} - {{ proj.status }}</p>
            </li>
        </ul>
    </article>
</template>