<template>
  <div class="flex h-screen bg-gray-900 text-white overflow-hidden font-display">

    <!-- BARRA LATERAL (LISTA DE ALUMNOS) -->
    <aside class="w-80 bg-[#161d2b] border-r border-gray-700 flex flex-col">
      <div class="p-4 border-b border-gray-700 bg-blue-900/20">
        <h2 class="text-xl font-bold text-blue-300 flex items-center gap-2">
          <span class="material-symbols-outlined">school</span>
          Mis Estudiantes
        </h2>
        <p class="text-xs text-gray-400 mt-1">{{ estudiantes.length }} alumnos registrados</p>
      </div>

      <div class="flex-1 overflow-y-auto scrollbar-thin">
        <div v-if="cargando" class="p-4 text-center text-gray-500">Cargando lista...</div>

        <button
            v-for="alumno in estudiantes"
            :key="alumno.email"
            @click="cargarExpediente(alumno)"
            class="w-full text-left p-4 hover:bg-gray-800 border-b border-gray-800 transition-colors flex items-center gap-3"
            :class="seleccionado?.email === alumno.email ? 'bg-blue-900/30 border-l-4 border-l-blue-500' : ''"
        >
          <div class="h-10 w-10 rounded-full bg-gray-700 flex items-center justify-center text-sm font-bold text-gray-300">
            {{ obtenerIniciales(alumno) }}
          </div>
          <div>
            <p class="font-bold text-sm truncate">{{ alumno.nombre || 'Sin nombre' }} {{ alumno.apellidos || '' }}</p>
            <p class="text-xs text-gray-500 truncate">{{ alumno.email }}</p>
          </div>
        </button>
      </div>

      <div class="p-4 border-t border-gray-700">
        <button @click="cerrarSesion" class="w-full py-2 bg-red-900/50 hover:bg-red-900 text-red-200 rounded text-sm transition">
          Cerrar Sesión Profe
        </button>
      </div>
    </aside>

    <!-- AREA PRINCIPAL (DETALLES DEL ALUMNO) -->
    <main class="flex-1 flex flex-col bg-[#0f172a] relative">

      <!-- Si no hay seleccionado -->
      <div v-if="!seleccionado" class="flex-1 flex flex-col items-center justify-center text-gray-500 opacity-50">
        <span class="material-symbols-outlined text-8xl mb-4">person_search</span>
        <p class="text-xl">Selecciona un alumno de la lista para ver su trabajo</p>
      </div>

      <!-- Si hay alumno seleccionado -->
      <div v-else class="flex-1 overflow-y-auto p-8 scrollbar-thin">
        <header class="mb-8 flex justify-between items-end border-b border-gray-700 pb-4">
          <div>
            <h1 class="text-3xl font-bold text-white">{{ seleccionado.nombre }} {{ seleccionado.apellidos }}</h1>
            <p class="text-blue-400">{{ seleccionado.email }}</p>
          </div>
        </header>

        <div v-if="cargandoExpediente" class="text-center py-10">
          <span class="material-symbols-outlined animate-spin text-4xl">refresh</span>
        </div>

        <div v-else class="space-y-8 animate-fade-in">

          <!-- TARJETA FORO 1 (6 Preguntas) -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors" @click="toggle('f1')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-blue-200">
                <span class="material-symbols-outlined text-blue-500">forum</span>
                Foro 1: Densidad Mineral Ósea
              </h3>
              <div class="flex items-center gap-3">
                <span class="text-xs px-2 py-1 rounded font-bold" :class="expediente.foro1 ? 'bg-green-900 text-green-300' : 'bg-red-900 text-red-300'">
                  {{ expediente.foro1 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f1 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro1 && expandido.f1" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700">
              <!-- Grid para aprovechar espacio -->
              <div class="grid gap-6">
                <div><strong class="text-blue-300 block mb-1 text-base">1. Definición DMO y medición:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro1.r1 }}</p></div>
                <div><strong class="text-blue-300 block mb-1 text-base">2. Factores de salud ósea:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro1.r2 }}</p></div>
                <div><strong class="text-blue-300 block mb-1 text-base">3. Relación Edad vs DMO:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro1.r3 }}</p></div>
                <div><strong class="text-blue-300 block mb-1 text-base">4. Evolución de la DMO:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro1.r4 }}</p></div>
                <div><strong class="text-blue-300 block mb-1 text-base">5. Edad aproximada por valor:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro1.r5 }}</p></div>
                <div><strong class="text-blue-300 block mb-1 text-base">6. Diferencias por sexo:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro1.r6 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro1.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

          <!-- TARJETA FORO 4 (7 Preguntas) -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors" @click="toggle('f4')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-purple-200">
                <span class="material-symbols-outlined text-purple-500">analytics</span>
                Foro 4: Análisis DMO
              </h3>
              <div class="flex items-center gap-3">
                <span class="text-xs px-2 py-1 rounded font-bold" :class="expediente.foro4 ? 'bg-green-900 text-green-300' : 'bg-red-900 text-red-300'">
                  {{ expediente.foro4 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f4 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro4 && expandido.f4" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700">
              <div class="grid gap-6">
                <div><strong class="text-purple-300 block mb-1 text-base">1. Expresión Algebraica:</strong> <p class="bg-gray-900/50 p-3 rounded font-mono text-green-400">{{ expediente.foro4.r1 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">2. Consideraciones para la función:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro4.r2 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">3. Coincidencia con evolución:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro4.r3 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">4. Verificación de cálculo:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro4.r4 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">5. Ventajas de intervalos pequeños:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro4.r5 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">6. Hallazgos gráfica anual:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro4.r6 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">7. Argumentación continuidad:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro4.r7 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro4.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const estudiantes = ref([]);
const cargando = ref(true);
const seleccionado = ref(null);
const expediente = ref({});
const cargandoExpediente = ref(false);

// Control de acordeón
const expandido = ref({ f1: false, f4: false });

function toggle(seccion) {
  expandido.value[seccion] = !expandido.value[seccion];
}

onMounted(async () => {
  try {
    const res = await fetch('https://proyecto-ingenieria-software-6ccv.onrender.com/lista_estudiantes');
    estudiantes.value = await res.json();
  } catch (e) {
    console.error(e);
  } finally {
    cargando.value = false;
  }
});

async function cargarExpediente(alumno) {
  seleccionado.value = alumno;
  cargandoExpediente.value = true;
  // Reseteamos acordeones para que se abran al seleccionar nuevo alumno
  expandido.value = { f1: true, f4: true };

  try {
    const res = await fetch(`https://proyecto-ingenieria-software-6ccv.onrender.com/expediente_completo/${alumno.email}`);
    expediente.value = await res.json();
  } catch (e) {
    console.error(e);
  } finally {
    cargandoExpediente.value = false;
  }
}

function obtenerIniciales(alumno) {
  if (alumno.nombre) return alumno.nombre[0].toUpperCase();
  return alumno.email[0].toUpperCase();
}

function cerrarSesion() {
  localStorage.clear();
  router.push('/');
}
</script>

<style scoped>
.scrollbar-thin::-webkit-scrollbar { width: 6px; }
.scrollbar-thin::-webkit-scrollbar-thumb { background-color: #374151; border-radius: 20px; }
.scrollbar-thin::-webkit-scrollbar-track { background-color: transparent; }
</style>