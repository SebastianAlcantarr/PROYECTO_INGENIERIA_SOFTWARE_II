<template>
  <div class="flex flex-col md:flex-row min-h-screen bg-slate-900 text-slate-200 font-display">

    <Sidebar class="hidden md:block" />

    <div class="flex-1 p-6 md:p-12 ml-0 md:ml-72 transition-all duration-300">
      <div class="max-w-5xl mx-auto space-y-8">

        <!-- Header -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
          <div>
            <h1 class="text-4xl font-bold text-white">Panel de Alumno</h1>
          </div>
          <div class="flex items-center gap-4 p-4 rounded-xl shadow-lg border-2 border-blue-700 bg-slate-800">
            <div class="w-12 h-12 rounded-full bg-blue-600 flex items-center justify-center text-xl font-bold text-white shadow-inner">
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

          <!-- Card: Foros -->
          <div class="bg-slate-800 p-6 rounded-xl border-3 border-slate-700 shadow-lg hover:border-blue-500/50 transition-colors">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-blue-700 rounded-lg">
                <span class="material-symbols-outlined text-2xl">forum</span>
              </div>
              <h3 class="text-lg text-white font-bold">Foros</h3>
            </div>
            <div class="space-y-3">
              <div v-for="foro in forosStatus" :key="foro.id"
                   class="flex flex-col p-3 rounded bg-slate-900/50 border border-slate-700/50">
                <div class="flex justify-between items-center mb-2">
                  <span class="text-sm text-slate-300 font-medium">{{ foro.name }}</span>
                  <span class="px-2 py-1 text-xs font-bold rounded-full"
                        :class="foro.completed ? 'bg-green-900 text-green-300' : 'bg-slate-700 text-slate-500'">
                    {{ foro.completed ? "Completado" : "Pendiente" }}
                  </span>
                </div>

                <button
                    v-if="feedbacks[foro.code]"
                    @click="verFeedback(foro.name, feedbacks[foro.code])"
                    class="text-xs flex items-center gap-1 text-yellow-400 hover:text-yellow-300 transition-colors self-end bg-yellow-400/10 px-2 py-1 rounded"
                >
                  <span class="material-symbols-outlined text-sm">mail</span>
                  Ver nota del maestro
                </button>
              </div>
            </div>
          </div>

          <!-- Card: Exámenes -->
          <div class="bg-slate-800 p-6 rounded-xl border-3 border-slate-700 shadow-lg hover:border-blue-500/50 transition-colors">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-blue-700 rounded-lg">
                <span class="material-symbols-outlined text-2xl">assignment</span>
              </div>
              <h3 class="text-lg text-white font-bold">Exámenes</h3>
            </div>
            <div class="space-y-3">
              <div v-for="examen in examenesStatus" :key="examen.id"
                   class="flex flex-col p-3 rounded bg-slate-900/50 border border-slate-700/50">
                <div class="flex justify-between items-center mb-2">
                  <span class="text-sm text-slate-300 font-medium">{{ examen.name }}</span>
                  <span class="px-2 py-1 text-xs font-bold rounded-full"
                        :class="examen.completed ? 'bg-green-900 text-green-300' : 'bg-slate-700 text-slate-500'">
                    {{ examen.completed ? "Completado" : "Pendiente" }}
                  </span>
                </div>

                <!-- boton dwe feedback -->
                <button
                    v-if="feedbacks[examen.code]"
                    @click="verFeedback(examen.name, feedbacks[examen.code])"
                    class="text-xs flex items-center gap-1 text-yellow-400 hover:text-yellow-300 transition-colors self-end bg-yellow-400/10 px-2 py-1 rounded"
                >
                  <span class="material-symbols-outlined text-sm">mail</span>
                  Ver nota del profe
                </button>
              </div>
            </div>
          </div>

          <!-- Card: Progreso -->
          <div class="bg-slate-800 p-6 rounded-xl border-3 border-slate-700 shadow-lg hover:border-blue-500/50 transition-colors">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-blue-700 rounded-lg">
                <span class="material-symbols-outlined text-2xl">analytics</span>
              </div>
              <h3 class="text-lg text-white font-bold">Progreso General</h3>
            </div>
            <div class="flex flex-col items-center justify-center h-48">
              <div class="relative w-32 h-32">
                <svg class="w-full h-full" viewBox="0 0 36 36">
                  <path class="text-slate-700" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3" />
                  <path class="text-blue-500 transition-all duration-1000 ease-out" :stroke-dasharray="`${progressPercentage}, 100`" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" />
                </svg>
                <div class="absolute inset-0 flex items-center justify-center flex-col">
                  <span class="text-2xl font-bold text-white">{{ Math.round(progressPercentage) }}%</span>
                </div>
              </div>
              <p class="mt-4 text-sm text-slate-400 text-center">Actividades completadas</p>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- ventana de feedback -->
    <div v-if="modalOpen" class="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4 animate-fade-in">
      <div class="bg-[#1e293b] w-full max-w-md rounded-2xl shadow-2xl border border-gray-700 overflow-hidden transform transition-all scale-100">
        <div class="bg-blue-900/50 p-4 border-b border-gray-700 flex justify-between items-center">
          <h3 class="font-bold text-white text-lg flex items-center gap-2">
            <span class="material-symbols-outlined text-yellow-400">rate_review</span>
            Retroalimentación
          </h3>
          <button @click="modalOpen = false" class="text-gray-400 hover:text-white transition-colors">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        <div class="p-6">
          <p class="text-xs text-blue-300 font-bold uppercase tracking-wider mb-2">{{ feedbackActual.titulo }}</p>
          <div class="bg-gray-800/50 p-4 rounded-lg border border-gray-700 text-gray-300 text-sm leading-relaxed whitespace-pre-wrap">
            {{ feedbackActual.texto }}
          </div>
        </div>
        <div class="p-4 bg-gray-800/30 flex justify-end">
          <button @click="modalOpen = false" class="bg-blue-600 hover:bg-blue-500 text-white px-4 py-2 rounded-lg text-sm font-bold transition-colors">
            Entendido
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import Sidebar from "@/views/sidebar.vue";

const API_URL = "https://proyecto-ingenieria-software-6ccv.onrender.com";

const userData = ref({ nombre: "", apellidos: "", email: "" });
const expediente = ref({});
const feedbacks = ref({});

const modalOpen = ref(false);
const feedbackActual = ref({ titulo: "", texto: "" });

const userInitials = computed(() => {
  const n = userData.value.nombre ? userData.value.nombre[0] : "";
  const a = userData.value.apellidos ? userData.value.apellidos[0] : "";
  return (n + a).toUpperCase();
});

const forosStatus = computed(() => [
  { id: 1, code: 'foro1', name: "Foro 1: Densidad", completed: !!expediente.value.foro1 },
  { id: 2, code: 'foro2', name: "Foro 2: Gráfico", completed: !!expediente.value.foro2 },
  { id: 3, code: 'foro3', name: "Foro 3: DMO Cadera", completed: !!expediente.value.foro3 },
  { id: 4, code: 'foro4', name: "Foro 4: Análisis", completed: !!expediente.value.foro4 },
  { id: 5, code: 'foro5', name: "Foro 5: Razón Cambio", completed: !!expediente.value.foro5 },
  { id: 6, code: 'foro6', name: "Foro 6: Covariación", completed: !!expediente.value.foro6 }
]);

const examenesStatus = computed(() => [
  { id: 1, code: 'examen1', name: "Examen 1", completed: !!expediente.value.examen1 },
  {id:2,code : "examen2",name:"Examen2",completed: !!expediente.value.examen2},
]);

const progressPercentage = computed(() => {
  const total = forosStatus.value.length + examenesStatus.value.length;
  const completed = forosStatus.value.filter((f) => f.completed).length + examenesStatus.value.filter((e) => e.completed).length;
  return total > 0 ? (completed / total) * 100 : 0;
});

async function fetchData() {
  const email = localStorage.getItem("usuario");
  if (!email) return;

  try {

    const expRes = await fetch(`${API_URL}/expediente_completo_alumno/${email}`);
    if (expRes.ok) expediente.value = await expRes.json();

    const userRes = await fetch(`${API_URL}/conseguir_usuario/${email}`);
    if (userRes.ok) userData.value = await userRes.json();

    const feedRes = await fetch(`${API_URL}/obtener_feedback/${email}`);
    if (feedRes.ok) feedbacks.value = await feedRes.json();

  } catch (error) {
    console.error("Error cargando datos:", error);
  }
}

function verFeedback(tituloActividad, mensaje) {
  feedbackActual.value = { titulo: tituloActividad, texto: mensaje };
  modalOpen.value = true;
}

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
.animate-fade-in { animation: fadeIn 0.2s ease-out forwards; }
</style>