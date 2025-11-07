import { createRouter, createWebHistory } from 'vue-router'

//Impotar cada archivo.vue para redireccionar con /
import tema1 from '/src/views/tema_1.vue'
import Login from '/src/views/Login.vue'

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
        component: tema1
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
