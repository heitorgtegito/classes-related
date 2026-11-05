import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
    },
    {
      path: '/projetos',
      name: 'projetos',
      component: () => import('../views/ProjetosView.vue'),
    },
    {
      path: '/alunos',
      name: 'alunos',
      component: () => import('../views/AlunosView.vue'),
    },
    {
      path: '/noticias',
      name: 'noticias',
      component: () => import('../views/NoticiasView.vue'),
    },
    {
      path: '/contato',
      name: 'contato',
      component: () => import('../views/ContatoView.vue'),
    },
  ],
})

export default router
