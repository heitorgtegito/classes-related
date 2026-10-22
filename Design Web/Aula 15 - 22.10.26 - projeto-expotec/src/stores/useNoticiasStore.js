import { defineStore } from 'pinia'
import { ref, watch } from 'vue'
import {noticiasLista} from '@/data/noticiasLista'
export const useNoticiasStore = defineStore('noticias',() => {
    const STORAGE_KEY = 'noticias_expotec'

    const carregarNoticias = () => {
        const noticiasSalvas = localStorage.getItem(STORAGE_KEY)
            if(noticiasSalvas){ try {
                return JSON.parse(noticiasSalvas)
        } catch (e){
            console.error("erro ao ler as notícias")
        }
    }
    return noticiasLista
}
const noticias = ref(carregarNoticias())
        watch(() => noticias.value,
        (novasNoticias) => {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(novasNoticias))
        },
        {deep: true}
    )
    return {noticias}
})