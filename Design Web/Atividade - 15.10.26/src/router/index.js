import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AgendaView from '@/views/AgendaView.vue'
import IntegrantesView from '@/views/IntegrantesView.vue'

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
    }
    ]
        const router = createRouter({
        history: createWebHistory(),
        routes
    })
export default router