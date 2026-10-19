import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AgendaView from '@/views/AgendaView.vue'
import IntegrantesView from '@/views/IntegrantesView.vue'
import FotosView from '@/views/FotosView.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView
    },
    {
        path: '/agenda',
        name: 'Agenda',
        component: AgendaView
    },
    {
        path: '/integrantes',
        name: 'Integrantes',
        component: IntegrantesView
    },
    {
        path: '/fotos',
        name: 'Fotos',
        component: FotosView
    }
    ]
        const router = createRouter({
        history: createWebHistory(),
        routes
    })
export default router