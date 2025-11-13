import { createRouter, createWebHistory } from 'vue-router'

//Impotar cada archivo.vue para redireccionar con /
import tema from '/src/views/tema_1.vue'
import Login from '/src/views/Login.vue'
import tema2 from '/src/views/Tema2.vue'

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

    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
