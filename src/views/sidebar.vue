<script setup>
import { ref } from "vue";
import {useRoute, useRouter} from "vue-router";

const router = useRouter();
const route =useRoute();

const actividades = [
  {
    nombre: "Actividad 1",
    abierta: true,
    items: [
      { nombre: "Foro 1: La densidad mineral y osea" , ruta: "/foro1" },
    ],
  },
  {
    nombre: "Actividad 2",
    abierta: true,
    items: [
        { nombre: "Foro 2: Grafico Comparativo", ruta: "/foro2" },
        {nombre : "Foro 2 : Examen 1" , ruta:"/foro2/examen1"}
        ],
  },
  {
    nombre: "Actividad 3",
    abierta: true,
    items: [
      {nombre :"Foro 3. Densidad mineral ósea de la cadera de mujeres", ruta :"/foro3"},
      {nombre :"Foro 4. Obteniendo más datos de la DMO y su análisis" ,ruta :"/foro4"},
      {nombre:"Foro 5. Razón promedio de cambio",ruta:'/foro5'},
      {nombre :"Foro 6.Covariacion de las magnitudes  ",ruta:"/foro6"},
      {nombre :"Actividad 3 :Examen 2"}
    ]
  }
];

const seleccionado = ref(null);
</script>

<template>
  <aside
      class="fixed left-0 top-0 h-screen w-72 bg-[#244a76] dark:bg-[#101622] border-r border-white/10 p-4 overflow-y-scroll scrollbar-custom"
  >
    <div class="flex flex-col gap-4">
      <!-- Header -->
      <div class="flex items-center gap-3">
        <div
            class="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-15"
        ></div>

        <div class="flex flex-col">
          <h1 class="text-white text-2xl font-medium">Derivadas</h1>
          <p class="text-[#92a4c9] text-xl">Cálculo I</p>
        </div>
      </div>

      <!-- ACTIVIDADES -->
      <div class=" flex flex-col gap-3 ">
        <div
            v-for="(act, index) in actividades"
            :key="index"
            class=" rounded-lg"
        >
          <!-- Botón de actividad -->
          <button
              @click="act.abierta = !act.abierta"
              class="w-full flex justify-between items-center px-4 py-5 text-white "
          >
            <span class="text-2xl font-medium">{{ act.nombre }}</span>


          </button>

          <!-- Contenido de la actividad -->
          <div v-if="act.abierta" class="flex flex-col">
            <a
                v-for="(item, i) in act.items"
                :key="i"
                @click="router.push(item.ruta)"
                class=" py-2 pb-10 text-[#cbd6f3] text-2xl   hover:bg-[#135bec]/10 transition flex items-center gap-2 cursor-pointer"
                :class="{
    'bg-[#2c5a8f] text-white border-l-4 ':
      route.path === item.ruta
  }"
            >

              {{ item.nombre }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </aside>

</template>


<style>
/* colores barra izquierda */
.scrollbar-custom::-webkit-scrollbar {
  width: 15px;
}

.scrollbar-custom::-webkit-scrollbar-track {
  background: rgba(44, 90, 143, 0.21);
}

.scrollbar-custom::-webkit-scrollbar-thumb {
  background-color: rgb(44, 90, 143);
  border-radius: 9999px;
  border: 2px solid #060619;
}

</style>