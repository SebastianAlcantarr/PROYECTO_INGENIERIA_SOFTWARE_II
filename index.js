import { createRouter, createWebHistory } from 'vue-router'

//Impotar cada archivo.vue para redireccionar con /
import tema from '/src/views/tema_1.vue'
import Login from '/src/views/Login.vue'
import tema2 from '/src/views/tema2.vue'
import Sidebar from '/src/views/sidebar.vue'

//Definir cada ruta para cada archivo
const routes = [
    {
        path: '/',
        name: 'Login',
        component: Login
    },
    {
        path: '/tema1',      // /about
        name: 'Tema',
        component: tema
    },
    {
        path: '/tema2',
        name: 'Tema2',
        component: tema2

    },
    {
        path: '/Sidebar',
        name: 'prueba',
        component: Sidebar

    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
