import { createRouter, createWebHistory } from 'vue-router'

//importar cada archivo.vue y ponerle nombre
import Foro1 from '/src/views/foro_1.vue'
import Login from '/src/views/Login.vue'
import Foro2 from '/src/views/foro_2.vue'
import examen from '/src/views/examen1.vue'
import Foro_6 from "@/views/foro_6.vue";


//Definir cada ruta para cada archivo
const routes = [
    {
        path: '/',
        name: 'Login',
        component: Login
    },
    {
        path: '/foro1',      // /about
        name: 'Tema',
        component: Foro1
    },
    {
        path: '/foro2',
        name: 'foro2',
        component: Foro2
    },
    {
        path: '/foro2/examen1',
        name: 'examen1',
        component: examen

    },
    {
        path: '/foro6',
        name: 'foro6',
        component: Foro_6
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
