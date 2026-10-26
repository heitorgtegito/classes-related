import { defineStore } from 'pinia'
import { ref, watch } from 'vue'
import {noticiasLista} from '@/data/noticiasLista'
export const useNoticiasStore = defineStore('noticias',() => {
    const STORAGE_KEY = 'noticias_expotec2'

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
    function removerNoticias(id){
        const indice = noticias.value.findIndex(j => j.id == id)
        noticias.value.splice(indice, 1)
    }
    function favoritarNoticias(id){
        const noticia = noticias.value.find(j => j.id === id)
        noticia.favorito = !noticia.favorito
    }
    function adicionarNoticias(novaNoticia){
        const id = noticias.value.length > 0 ? Math.max(...noticias.value.map(a => a.id)) +1 : 1
        noticias.value.push({
            id,
            titulo: novaNoticia.titulo,
            autor: novaNoticia.autor,
            descricao: novaNoticia.descricao,
            favorito: false,
        })
    }


    watch(() => noticias.value,
        (novasNoticias) => {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(novasNoticias))
        },
        {deep: true}
    )
    return {noticias, removerNoticias, favoritarNoticias, adicionarNoticias}
})