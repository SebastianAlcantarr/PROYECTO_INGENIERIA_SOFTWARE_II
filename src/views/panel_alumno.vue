<template>
  <div class="min-h-dvh bg-fondo text-tinta">
    <EncabezadoPortal />

    <main class="mx-auto max-w-[1240px] px-4 pb-24 sm:px-6 lg:px-10">
      <!-- Resumen -->
      <header class="grid gap-10 pb-12 pt-10 md:pt-14 lg:grid-cols-[minmax(0,1fr)_380px] lg:items-end">
        <div>
          <p v-if="userData.nombre" class="text-lg text-tenue">Hola, <span class="font-semibold text-tinta">{{ userData.nombre }}</span></p>
          <h1 class="mt-3 text-[clamp(2.5rem,6vw,4.5rem)] font-extrabold leading-[1.02] tracking-[-0.012em]">
            Tu semestre de derivadas
          </h1>
          <p v-if="userData.email" class="mt-4 text-tenue">{{ userData.nombre }} {{ userData.apellidos }} · {{ userData.email }}</p>
        </div>

        <div class="rounded-3xl p-6 sm:p-7" style="background: var(--c-barra); color: var(--c-barra-tinta)">
          <p class="font-display numeral text-6xl font-extrabold tracking-[-0.04em]">
            {{ completados }}<span class="text-3xl" style="color: var(--c-barra-tenue)"> / {{ pasos.length }}</span>
          </p>
          <p class="mt-1 text-sm" style="color: var(--c-barra-tenue)">Actividades completadas · {{ Math.round(progressPercentage) }}%</p>
          <ol class="mt-5 flex gap-1.5" aria-hidden="true">
            <li
              v-for="p in estadoPasos"
              :key="p.ruta"
              class="h-2 flex-1 rounded-full"
              :style="{ background: p.completado ? colorDeActividad(p.actividad) : 'var(--c-barra-pista)' }"
            ></li>
          </ol>
          <RouterLink v-if="siguientePaso" :to="siguientePaso.ruta" class="boton boton-curso mt-6 w-full">
            Continuar: {{ siguientePaso.tipo }} · {{ siguientePaso.corto }}
            <span class="material-symbols-outlined -mr-1 text-[20px]" aria-hidden="true">arrow_forward</span>
          </RouterLink>
          <p v-else class="mt-6 flex items-center gap-2 font-semibold">
            <span class="material-symbols-outlined" aria-hidden="true">task_alt</span>Completaste toda la secuencia
          </p>
        </div>
      </header>

      <!-- Lista de pistas por actividad -->
      <section v-for="act in actividades" :key="act.numero" class="border-t border-linea pb-6 pt-8" :aria-labelledby="`act-${act.numero}`">
        <h2 :id="`act-${act.numero}`" class="mb-4 flex items-center gap-3 text-2xl font-bold tracking-[-0.02em]">
          <span class="h-3 w-3 rounded-full" :style="{ background: act.color }" aria-hidden="true"></span>
          {{ act.nombre }}
        </h2>
        <ol class="divide-y divide-linea">
          <li v-for="p in pasosDeActividad(act.numero)" :key="p.ruta" class="py-1">
            <div class="grid grid-cols-[3rem_1fr_auto] items-center gap-x-4 gap-y-2 py-3 sm:grid-cols-[3.5rem_1fr_auto_auto]">
              <span
                class="font-display numeral text-2xl font-extrabold tracking-[-0.03em]"
                :class="p.completado ? 'line-through decoration-2' : ''"
                :style="{ color: colorTextoDeActividad(p.actividad), textDecorationColor: 'var(--c-tinta)' }"
              >{{ pista(p.indice) }}</span>
              <RouterLink :to="p.ruta" class="min-w-0 rounded-md hover:underline hover:underline-offset-4">
                <span class="block text-sm text-tenue">{{ p.tipo }}</span>
                <span class="block truncate text-lg font-semibold">{{ p.titulo }}</span>
              </RouterLink>
              <span
                class="chip justify-self-end"
                :class="p.completado ? '!bg-ok-fondo !text-ok' : ''"
              >
                <span class="material-symbols-outlined text-[16px]" aria-hidden="true">{{ p.completado ? 'check' : 'schedule' }}</span>
                {{ p.completado ? "Completado" : "Pendiente" }}
              </span>
              <button
                v-if="p.nota"
                type="button"
                class="boton boton-secundario col-span-3 !min-h-10 justify-self-start !px-4 text-sm sm:col-span-1 sm:justify-self-end"
                :aria-expanded="notaAbierta === p.codigo"
                :aria-controls="`nota-${p.codigo}`"
                @click="notaAbierta = notaAbierta === p.codigo ? null : p.codigo"
              >
                <span class="material-symbols-outlined text-[18px] text-a2-texto" aria-hidden="true">rate_review</span>
                Nota del profesor
              </button>
              <span v-else class="hidden sm:block"></span>
            </div>
            <div
              v-if="p.nota && notaAbierta === p.codigo"
              :id="`nota-${p.codigo}`"
              class="mb-4 grid gap-2 sm:ml-[4.5rem] sm:grid-cols-[180px_1fr]"
            >
              <p class="text-sm font-semibold text-tenue">Retroalimentación · {{ p.tipo }}</p>
              <p class="whitespace-pre-wrap rounded-2xl bg-hundido p-4 text-[0.9375rem] leading-relaxed">{{ p.nota }}</p>
            </div>
          </li>
        </ol>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { RouterLink } from "vue-router";
import EncabezadoPortal from "@/components/EncabezadoPortal.vue";
import { pasos, actividades, pista, colorDeActividad, colorTextoDeActividad } from "@/ruta.js";

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

// --- Vista de la ruta (solo interfaz) ---
const estadoPasos = computed(() =>
  pasos.map((p, i) => ({
    ...p,
    indice: i,
    completado: !!expediente.value[p.codigo],
    nota: feedbacks.value[p.codigo] || "",
  }))
);
const completados = computed(() => estadoPasos.value.filter((p) => p.completado).length);
const siguientePaso = computed(() => estadoPasos.value.find((p) => !p.completado) || null);
const notaAbierta = ref(null);
const pasosDeActividad = (n) => estadoPasos.value.filter((p) => p.actividad === n);
</script>
