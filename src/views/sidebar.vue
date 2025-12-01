<template>
  <aside
    class="fixed left-0 top-0 h-screen w-72 border-r border-slate-800 flex flex-col shadow-2xl z-50 transition-all duration-300"
  >
    <div class="p-2 border-t border-slate-800 bg-[#0f172a]">
      <button
        class="w-full flex items-center gap-3 p-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
      >
        <div
          class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center"
        >
          <span class="material-symbols-outlined text-sm">person</span>
        </div>

        <div v-if="USUARIOS" class="flex flex-col items-start">
          <span class="text-2xl font-medium text-white">{{ USUARIOS.nombre }}</span>

          <span class="text-xl text-slate-400">{{ USUARIOS.apellidos }}</span>
        </div>

        <div v-else>
          <p>Cargando usuario...</p>
        </div>
      </button>
    </div>

    <!-- Scrollable Content -->
    <div
      class="flex-1 overflow-y-auto scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-transparent p-4 space-y-6"
    >
      <!-- Activities Loop -->
      <div v-for="(act, index) in actividades" :key="index" class="group">
        <!-- Activity Header -->
        <button
          @click="act.abierta = !act.abierta"
          class="w-full flex items-center justify-between p-3 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800/50 transition-all duration-200 group-hover:shadow-md"
        >
          <div class="flex items-center gap-3">
            <span
              class="material-symbols-outlined text-[20px] transition-colors duration-200"
              :class="act.abierta ? 'text-blue-400' : ''"
              >{{ act.icon }}</span
            >
            <span class="font-mono text-2xl tracking-wide">{{
              act.nombre
            }}</span>
          </div>
          <span
            class="material-symbols-outlined text-lg transition-transform duration-300"
            :class="act.abierta ? 'rotate-180' : ''"
          >
            expand_more
          </span>
        </button>

        <!-- Items List -->
        <div
          class="grid transition-all duration-300 ease-in-out overflow-hidden"
          :class="
            act.abierta
              ? 'grid-rows-[1fr] opacity-100 mt-2'
              : 'grid-rows-[0fr] opacity-0'
          "
        >
          <div
            class="min-h-0 flex flex-col gap-1 pl-3 border-l-2 border-slate-800 ml-4"
          >
            <a
              v-for="(item, i) in act.items"
              :key="i"
              @click="router.push(item.ruta)"
              class="relative flex items-center gap-3 px-3 py-2.5 rounded-md text-sm transition-all duration-200 cursor-pointer group/item overflow-hidden"
              :class="
                route.path === item.ruta
                  ? 'bg-blue-600/10 text-blue-400 font-medium'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/30'
              "
            >
              <!-- Active Indicator -->
              <div
                v-if="route.path === item.ruta"
                class="absolute left-0 top-1/2 -translate-y-1/2 w-1 h-6 bg-blue-500 rounded-r-full"
              ></div>

              <span class="material-symbols-outlined text-[18px] z-10">{{
                item.icon
              }}</span>
              <span class="truncate z-10">{{ item.nombre }}</span>

              <!-- Hover Glow Effect -->
              <div
                class="absolute inset-0 bg-linear-to-r from-blue-500/0 via-blue-500/5 to-blue-500/0 -translate-x-full group-hover/item:translate-x-full transition-transform duration-700"
              ></div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
import {onMounted, ref} from "vue";
import {useRoute, useRouter} from "vue-router";

const router = useRouter();
const route = useRoute();

const actividades = ref([
  {
    nombre: "Actividad 1",
    abierta: true,
    icon: "science",
    items: [
      { nombre: "Foro 1: Densidad mineral", ruta: "/foro1", icon: "bar_chart" },
    ],
  },
  {
    nombre: "Actividad 2",
    abierta: true,
    icon: "analytics",
    items: [
      {
        nombre: "Foro 2: Gráfico Comparativo",
        ruta: "/foro2",
        icon: "bar_chart",
      },
      { nombre: "Examen 1", ruta: "/foro2/examen1", icon: "Assignment" },
    ],
  },
  {
    nombre: "Actividad 3",
    abierta: true,
    icon: "Function",
    items: [
      {
        nombre: "Foro 3: DMO Cadera",
        ruta: "/foro3",
        icon: "accessibility_new",
      },
      { nombre: "Foro 4: Análisis DMO", ruta: "/foro4", icon: "query_stats" },
      {
        nombre: "Foro 5: Razón de cambio",
        ruta: "/foro5",
        icon: "trending_up",
      },
      { nombre: "Foro 6: Covariación", ruta: "/foro6", icon: "swap_horiz" },
      {
        nombre: "Examen 2",
        ruta: "/actividad3/examen2",
        icon: "assignment_turned_in",
      },
    ],
  },
]);

const USUARIOS = ref(null);

async function cargarUsuario() {
  const email = localStorage.getItem("email");
  if (!email) return;

  try {
    const res = await fetch(`https://proyecto-ingenieria-software-6ccv.onrender.com/${email}`);
    // Guarda el objeto entero
    USUARIOS.value = await res.json();

  } catch (error) {
    console.error("Error cargando usuario:", error);
  }
}


onMounted(() => {
  cargarUsuario();
});
</script>

<style scoped>
/* Custom Scrollbar */
.scrollbar-thin::-webkit-scrollbar {
  width: 4px;
}
.scrollbar-thin::-webkit-scrollbar-track {
  background: transparent;
}
.scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: #334155;
  border-radius: 20px;
}
.scrollbar-thin::-webkit-scrollbar-thumb:hover {
  background-color: #475569;
}
</style>
