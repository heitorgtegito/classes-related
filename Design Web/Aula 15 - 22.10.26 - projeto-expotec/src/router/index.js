import NoticiasView from '@/views/NoticiasView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Noticias',
        component: NoticiasView
    }
    ]
const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router