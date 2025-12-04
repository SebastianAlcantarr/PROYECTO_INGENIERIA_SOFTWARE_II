import { createRouter, createWebHistory } from 'vue-router'

//importar cada archivo.vue y ponerle nombre
import Foro1 from '/src/views/foro_1.vue'
import Login from '/src/views/Login.vue'
import Foro2 from '/src/views/foro_2.vue'
import examen from '/src/views/examen1.vue'
import Foro_6 from "@/views/foro_6.vue";
import Foro_3 from "@/views/foro_3.vue";
import Foro_4 from "@/views/foro_4.vue";
import PanelProfesor from "@/views/PanelProfesor.vue";
import Bienvenida from "@/views/Bienvenida.vue";
import PanelAlumno from "@/views/panel_alumno.vue";


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
        path: '/foro3',
        name: 'Foro3',
        component: Foro_3
    },
    {
        path: '/foro4',
        name: 'Foro4',
        component: Foro_4
    },
    {
        path: '/panel-profesor',
        name: 'PanelProfesor',
        component: PanelProfesor
    },
    {
        path: '/bienvenida',
        name: 'Bienvenida',
        component: Bienvenida
    },
    {
        path: '/foro6',
        name: 'foro6',
        component: Foro_6
    },
    {
        path: '/bienvenida',
        name: 'Bienvenida',
        component: Bienvenida
    },
    {
        path: '/panel-alumno',
        name: 'PanelAlumno',
        component: PanelAlumno
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
 scrollBehavior() {
  return { left: 0, top: 0 };
}
});


export default router