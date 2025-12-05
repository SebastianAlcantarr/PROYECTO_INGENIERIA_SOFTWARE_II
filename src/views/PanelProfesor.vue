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
              <h3 class="font-bold text-lg flex items-center gap-2 text-blue-600">
                <span class="material-symbols-outlined text-blue-600">forum</span>
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

          <!-- TARJETA FORO 2 -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg mt-6">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors" @click="toggle('f2')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-blue-500">
                <span class="material-symbols-outlined text-blue-500">bar_chart</span>
                Foro 2: Gráfico Comparativo
              </h3>
              <div class="flex items-center gap-3">
                <span class="text-xs px-2 py-1 rounded font-bold" :class="expediente.foro2 ? 'bg-green-900 text-green-300' : 'bg-red-900 text-red-300'">
                  {{ expediente.foro2 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f2 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro2 && expandido.f2" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700">
              <div class="grid gap-6">
                <div><strong class="text-green-300 block mb-1 text-base">1. Análisis del gráfico:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro2.r1 }}</p></div>
                <div><strong class="text-green-300 block mb-1 text-base">2. Comparativa visual:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro2.r2 }}</p></div>
                <div><strong class="text-green-300 block mb-1 text-base">3. Tendencias observadas:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro2.r3 }}</p></div>
                <div><strong class="text-green-300 block mb-1 text-base">4. Puntos críticos:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro2.r4 }}</p></div>
                <div><strong class="text-green-300 block mb-1 text-base">5. Conclusiones:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro2.r5 }}</p></div>
                <div><strong class="text-green-300 block mb-1 text-base">6. Reflexión final:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro2.r6 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro2.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

          <!-- TARJETA FORO 3 -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg mt-6">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors" @click="toggle('f3')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-blue-500">
                <span class="material-symbols-outlined text-blue-500">accessibility_new</span>
                Foro 3: DMO Cadera
              </h3>
              <div class="flex items-center gap-3">
                <span class="text-xs px-2 py-1 rounded font-bold" :class="expediente.foro3 ? 'bg-green-900 text-green-300' : 'bg-red-900 text-red-300'">
                  {{ expediente.foro3 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f3 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro3 && expandido.f3" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700">
              <div class="grid gap-6">
                <div><strong class="text-purple-300 block mb-1 text-base">1. Cambio DMO (15-25 años):</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro3.r1 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">2. Razón de cambio promedio:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro3.r2 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">3. Cambio promedio por año:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro3.r3 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">4. Ubicación en gráfico:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro3.r4 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">5. Pendiente recta secante:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro3.r5 }}</p></div>

                <!-- Nota: La tabla de la pregunta 6 es muy grande, así que mostramos un resumen o solo las preguntas de texto -->
                <div class="bg-gray-800/50 p-3 rounded border border-gray-700">
                  <strong class="text-purple-300 block mb-1">6. Tabla de Análisis:</strong>
                  <p class="text-xs text-gray-400 italic">Los datos de la tabla se encuentran almacenados en la base de datos.</p>
                </div>

                <div><strong class="text-purple-300 block mb-1 text-base">7. Información razón promedio:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro3.r7 }}</p></div>
                <div><strong class="text-purple-300 block mb-1 text-base">8. Determinar valor a los 50 años:</strong> <p class="bg-gray-900/50 p-3 rounded">{{ expediente.foro3.r8 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro3.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

          <!-- TARJETA FORO 4 (7 Preguntas) -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors" @click="toggle('f4')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-blue-400">
                <span class="material-symbols-outlined text-blue-400">analytics</span>
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

          <!-- TARJETA FORO 5: Razón de Cambio -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg mt-6">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors" @click="toggle('f5')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-orange-200">
                <span class="material-symbols-outlined text-orange-500">trending_up</span>
                Foro 5: Razón de Cambio
              </h3>
              <div class="flex items-center gap-3">
      <span class="text-xs px-2 py-1 rounded font-bold" :class="expediente.foro5 ? 'bg-green-900 text-green-300' : 'bg-red-900 text-red-300'">
        {{ expediente.foro5 ? 'Completado' : 'Sin entregar' }}
      </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f5 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro5 && expandido.f5" class="p-6 space-y-4 text-sm text-gray-300 border-t border-gray-700">
              <div class="grid gap-4">
                <!-- Asumo 7 preguntas como en el config de main.py -->
                <p><strong class="text-orange-300">P1:</strong> {{ expediente.foro5.r1 }}</p>
                <p><strong class="text-orange-300">P2:</strong> {{ expediente.foro5.r2 }}</p>
                <p><strong class="text-orange-300">P3:</strong> {{ expediente.foro5.r3 }}</p>
                <details>
                  <summary class="cursor-pointer text-gray-400 mt-2">Ver más...</summary>
                  <div class="pl-4 pt-2 space-y-2">
                    <p><strong class="text-orange-300">P4:</strong> {{ expediente.foro5.r4 }}</p>
                    <p><strong class="text-orange-300">P5:</strong> {{ expediente.foro5.r5 }}</p>
                    <p><strong class="text-orange-300">P6:</strong> {{ expediente.foro5.r6 }}</p>
                    <p><strong class="text-orange-300">P7:</strong> {{ expediente.foro5.r7 }}</p>
                  </div>
                </details>
              </div>
              <p class="text-xs text-gray-500 mt-4 text-right">Entregado el: {{ new Date(expediente.foro5.fecha).toLocaleString() }}</p>
            </div>
          </div>

          <!-- TARJETA FORO 6: Covariación -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg mt-6">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors" @click="toggle('f6')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-pink-200">
                <span class="material-symbols-outlined text-pink-500">swap_horiz</span>
                Foro 6: Covariación
              </h3>
              <div class="flex items-center gap-3">
      <span class="text-xs px-2 py-1 rounded font-bold" :class="expediente.foro6 ? 'bg-green-900 text-green-300' : 'bg-red-900 text-red-300'">
        {{ expediente.foro6 ? 'Completado' : 'Sin entregar' }}
      </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f6 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro6 && expandido.f6" class="p-6 space-y-4 text-sm text-gray-300 border-t border-gray-700">
              <div class="grid gap-4">
                <!-- 8 preguntas del Foro 6 -->
                <p><strong class="text-pink-300">1. Dominio:</strong> {{ expediente.foro6.r1 }}</p>
                <p><strong class="text-pink-300">2. Argumento:</strong> {{ expediente.foro6.r2 }}</p>
                <details>
                  <summary class="cursor-pointer text-gray-400 mt-2">Ver respuestas completas (3-8)...</summary>
                  <div class="pl-4 pt-2 space-y-2">
                    <pre class="bg-gray-900/50 p-2 rounded whitespace-pre-wrap font-sans text-xs"><strong class="text-pink-300">3. Simulador:</strong> {{ expediente.foro6.r3 }}</pre>
                    <p><strong class="text-pink-300">4. GeoGebra:</strong> {{ expediente.foro6.r4 }}</p>
                    <p><strong class="text-pink-300">5. Pendientes:</strong> {{ expediente.foro6.r5 }}</p>
                    <p><strong class="text-pink-300">6. Notas:</strong> {{ expediente.foro6.r6 }}</p>
                    <pre class="bg-gray-900/50 p-2 rounded whitespace-pre-wrap font-sans text-xs"><strong class="text-pink-300">7. Óptimo M:</strong> {{ expediente.foro6.r7 }}</pre>
                    <p><strong class="text-pink-300">8. Óptimo H:</strong> {{ expediente.foro6.r8 }}</p>
                  </div>
                </details>
              </div>
              <p class="text-xs text-gray-500 mt-4 text-right">Entregado el: {{ new Date(expediente.foro6.fecha).toLocaleString() }}</p>
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
const expandido = ref({ f1: false, f2: false, f3: false, f4: false, f5: false, f6: false, e1: false });

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
  expandido.value = { f1: true, f2: true, f3: true, f4: true, f5: true, f6: true, e1: true };

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