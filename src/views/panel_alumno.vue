<template>
  <Sidebar class="hidden md:block" />
  <div
    class="min-h-screen bg-slate-900 text-slate-200 p-6 md:p-12 ml-0 md:ml-72 transition-all duration-300"
  >
    <div class="max-w-5xl mx-auto space-y-8">
      <!-- Header -->
      <div
        class="flex flex-col md:flex-row items-center justify-between gap-4 "
      >
        <div>
          <h1 class="text-4xl font-bold text-white">Panel de  Alumno</h1>
        </div>
        <div
          class="flex items-center gap-4  p-4 rounded-sm shadow-lg border-2 border-blue-700"
        >
          <div
            class="w-12 h-12 rounded-full bg-blue-600 flex items-center justify-center text-xl font-bold text-white shadow-inner"
          >
            {{ userInitials }}
          </div>
          <div>
            <h2 class="text-lg font-semibold text-white">
              {{ userData.nombre }} {{ userData.apellidos }}
            </h2>
            <p class="text-sm text-blue-400 font-semibold">{{ userData.email }}</p>
          </div>
        </div>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Card: Foros Completados -->
        <div
          class="bg-slate-800 p-6 rounded-xl border-3 border-slate-700 shadow-lg hover:border-blue-500/50 transition-colors"
        >
          <div class="flex items-center gap-4 mb-4">
            <div class="p-3 bg-blue-700 rounded-lg">
              <span class="material-symbols-outlined text-2xl">forum</span>
            </div>
            <h3 class="text-lg  text-white">Foros Completado y Pendientes </h3>
          </div>
          <div class="space-y-3">
            <div
              v-for="foro in forosStatus"
              :key="foro.id"
              class="flex items-center justify-between p-2 rounded bg-slate-900/50"
            >
              <span class="text-sm text-slate-300">{{ foro.name }}</span>
              <span
                class="px-2 py-1 text-xs font-bold rounded-full"
                :class="
                  foro.completed
                    ? 'p-3 bg-blue-700 rounded-lg'
                    : 'bg-slate-700 text-slate-500'
                "
              >
                {{ foro.completed ? "Completado" : "Pendiente" }}
              </span>
            </div>
          </div>
        </div>

        <!-- Card: Examenes -->
        <div
          class="bg-slate-800 p-6 rounded-xl border-3 border-slate-700 shadow-lg hover:border-blue-500/50 transition-colors"
        >
          <div class="flex items-center gap-4 mb-4">
            <div class="p-3 bg-blue-700 rounded-lg">
              <span class="material-symbols-outlined text-2xl">assignment</span>
            </div>
            <h3 class="text-lg  text-white">Exámenes</h3>
          </div>
          <div class="space-y-3">
            <div
              v-for="examen in examenesStatus"
              :key="examen.id"
              class="flex items-center justify-between p-2 rounded bg-slate-900/50"
            >
              <span class="text-sm text-slate-300">{{ examen.name }}</span>
              <span
                class="px-2 py-1 text-xs font-bold rounded-full"
                :class="
                  examen.completed
                    ? 'p-3 bg-blue-700 rounded-lg'
                    : 'bg-slate-700 text-slate-500'
                "
              >
                {{ examen.completed ? "Completado" : "Pendiente" }}
              </span>
            </div>
          </div>
        </div>

        <!-- Card: Progreso General -->
        <div
          class="bg-slate-800 p-6 rounded-xl border-3 border-slate-700 shadow-lg hover:border-blue-500/50 transition-colors"
        >
          <div class="flex items-center gap-4 mb-4">
            <div class="p-3 bg-blue-700 rounded-lg ">
              <span class="material-symbols-outlined text-2xl">analytics</span>
            </div>
            <h3 class="text-lg  text-white">Porcentaje de Actividades y Examenes  terminados</h3>
          </div>
          <div class="flex flex-col items-center justify-center h-48">
            <div class="relative w-32 h-32">
              <svg class="w-full h-full" viewBox="0 0 36 36">
                <path
                  class="text-slate-700"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="3"
                />
                <path
                  class="text-blue-600 transition-all duration-1000 ease-out"
                  :stroke-dasharray="`${progressPercentage}, 100`"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="3"
                />
              </svg>
              <div
                class="absolute inset-0 flex items-center justify-center flex-col"
              >
                <span class="text-2xl font-bold text-white"
                  >{{ Math.round(progressPercentage) }}%</span
                >
              </div>
            </div>
            <p class="mt-4 text-sm text-slate-400 text-center">
              Actividades completadas
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import Sidebar from "@/views/sidebar.vue";
const userData = ref({
  nombre: "",
  apellidos: "",
  email: "",
});

const expediente = ref({
  foro1: null,
  foro2: null,
  foro3: null,
  foro4: null,
  foro5: null,
  foro6: null,
  examen1: null,
  examen2: null,
});

const userInitials = computed(() => {
  const n = userData.value.nombre ? userData.value.nombre[0] : "";
  const a = userData.value.apellidos ? userData.value.apellidos[0] : "";
  return (n + a).toUpperCase();
});

const forosStatus = computed(() => [
  { id: 1, name: "Foro 1: Densidad", completed: !!expediente.value.foro1 },
  { id: 2, name: "Foro 2: Gráfico", completed: !!expediente.value.foro2 },
  { id: 3, name: "Foro 3: DMO Cadera", completed: !!expediente.value.foro3 } ,
  { id: 4, name: "Foro 4: Análisis", completed: !!expediente.value.foro4 },
  {id:5,name:"Foro 5: Razon de Cambio",completed:!!expediente.value.foro5},
  {id:6,name:"Foro 6: Covariación",completed:!!expediente.value.foro6}
]);

const examenesStatus = computed(() => [
  { id: 1, name: "Examen 1", completed: !!expediente.value.examen1 },
  {id:2,name:"Examen 2",completed:!!expediente.value.examen2}
]);

const progressPercentage = computed(() => {
  const total = forosStatus.value.length + examenesStatus.value.length;

  const completed =
    forosStatus.value.filter((f) => f.completed).length +
    examenesStatus.value.filter((e) => e.completed).length;
  return total > 0 ? (completed / total) * 100 :0;
});

async function fetchData() {
  const email = localStorage.getItem("email");
  if (!email) return;

  try {
    // Fetch User Data
    const userRes = await fetch(
      `https://proyecto-ingenieria-software-6ccv.onrender.com/conseguir_usuario/${email}`
    );
    if (userRes.ok) {
      userData.value = await userRes.json();
    }

    // Fetch Expediente
    const expRes = await fetch(
      `https://proyecto-ingenieria-software-6ccv.onrender.com/expediente_completo_alumno/${email}`
    );
    if (expRes.ok) {
      expediente.value = await expRes.json();
    }
  } catch (error) {
    console.error("Error fetching dashboard data:", error);
  }
}

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
/* Add any specific styles here if needed, mostly using Tailwind */
</style>
