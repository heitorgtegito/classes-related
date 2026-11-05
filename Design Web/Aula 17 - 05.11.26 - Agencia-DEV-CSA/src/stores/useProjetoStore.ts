import { defineStore } from 'pinia'
import { ref, watch } from 'vue'
import type { projeto } from '../types/agencia'
import { projetos as projetosdev } from '../data/projetoDevData'

const CHAVE_STORAGE = 'agencia_projetos'

export const useProjetoStore = defineStore('projeto', () => {
    const projetosLS = localStorage.getItem(CHAVE_STORAGE)
    const projetos = ref<projeto[]>(
        projetosLS ? JSON.parse(projetosLS) : projetosdev
    )
    watch (
        projetos,
            (novosProjetos) => {
                localStorage.setItem(CHAVE_STORAGE, JSON.stringify(novosProjetos))
            },
            {deep: true}
    )
    return {
        projetos
    }
})