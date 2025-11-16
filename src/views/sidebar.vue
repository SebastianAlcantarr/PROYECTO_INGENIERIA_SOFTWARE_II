<script setup>
import { ref } from "vue";

const actividades = ref([
  {
    nombre: "Actividad 1",
    abierta: true,
    items: ["Foro 1", "Evaluación 1", "Tarea 1"],
  },
  {
    nombre: "Actividad 2",
    abierta: false,
    items: ["Foro 2", "Evaluación 2"],
  },
]);

// ⬅ ESTA VARIABLE GUARDA EL ITEM SELECCIONADO
const seleccionado = ref("");
</script>

<template>
  <aside
    class="fixed left-0 top-0 h-screen w-72 bg-[#244a76] dark:bg-[#101622] border-r border-white/10 p-4 overflow-y-auto"
  >
    <div class="flex flex-col gap-4">
      <!-- Header -->
      <div class="flex items-center gap-3">
        <div
          class="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-15"
        ></div>

        <div class="flex flex-col">
          <h1 class="text-white text-3xl font-medium">Derivadas</h1>
          <p class="text-[#92a4c9] text-2xl">Cálculo I</p>
        </div>
      </div>

      <!-- ACTIVIDADES -->
      <div class="mt-4 flex flex-col gap-3">
        <div
          v-for="(act, index) in actividades"
          :key="index"
          class="bg-[#1d3b5c]/40 rounded-lg"
        >
          <!-- Botón de actividad -->
          <button
            @click="act.abierta = !act.abierta"
            class="w-full flex justify-between items-center px-3 py-2 text-white hover:bg-[#135bec]/20 transition"
          >
            <span class="text-lg font-medium">{{ act.nombre }}</span>

            <span class="material-symbols-outlined">
              {{ act.abierta ? "expand_less" : "expand_more" }}
            </span>
          </button>

          <!-- Contenido de la actividad -->
          <div v-if="act.abierta" class="flex flex-col">
            <a
              v-for="(item, i) in act.items"
              :key="i"
              @click="seleccionado = item"
              class="px-6 py-2 text-[#cbd6f3] hover:bg-[#135bec]/10 transition flex items-center gap-2 cursor-pointer"
              :class="{
                'bg-[#2c5a8f] text-white border-l-4 border-blue-400':
                  seleccionado === item,
              }"
            >
              <span class="material-symbols-outlined text-sm">
                radio_button_unchecked
              </span>
              {{ item }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>
