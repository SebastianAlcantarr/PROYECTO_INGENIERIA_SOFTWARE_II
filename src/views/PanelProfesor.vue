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
          <div
            class="h-10 w-10 rounded-full flex items-center justify-center text-sm font-bold text-white transition-colors"
            :class="seleccionado?.email === alumno.email ? 'bg-blue-600' : 'bg-gray-700'"
          >
            {{ obtenerIniciales(alumno) }}
          </div>
          <div>
            <p class="font-bold text-sm truncate" :class="seleccionado?.email === alumno.email ? 'text-blue-100' : 'text-gray-300'">
              {{ alumno.nombre || 'Sin nombre' }} {{ alumno.apellidos || '' }}
            </p>
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
          <span class="material-symbols-outlined animate-spin text-4xl text-blue-500">refresh</span>
        </div>

        <div v-else class="space-y-6 animate-fade-in">

          <!-- ========================================== -->
          <!-- TARJETA FORO 1 (CYAN - AZUL CLARO)       -->
          <!-- ========================================== -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group" @click="toggle('f1')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-cyan-300 group-hover:text-cyan-200 transition-colors">
                <span class="material-symbols-outlined text-cyan-400">forum</span>
                Foro 1: Densidad Mineral Ósea
              </h3>
              <div class="flex items-center gap-3">
                <!-- BADGE FIJO VERDE/ROJO -->
                <span class="text-xs px-2 py-1 rounded font-bold border" :class="expediente.foro1 ? 'bg-green-900/30 text-green-300 border-green-700' : 'bg-red-900/30 text-red-300 border-red-800'">
                  {{ expediente.foro1 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f1 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro1 && expandido.f1" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-cyan-500">
              <div class="grid gap-6">
                <div><strong class="text-cyan-200 block mb-1 text-base">1. Definición DMO:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro1.r1 }}</p></div>
                <div><strong class="text-cyan-200 block mb-1 text-base">2. Factores:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro1.r2 }}</p></div>
                <div><strong class="text-cyan-200 block mb-1 text-base">3. Relación Edad:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro1.r3 }}</p></div>
                <div><strong class="text-cyan-200 block mb-1 text-base">4. Evolución:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro1.r4 }}</p></div>
                <div><strong class="text-cyan-200 block mb-1 text-base">5. Edad aprox:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro1.r5 }}</p></div>
                <div><strong class="text-cyan-200 block mb-1 text-base">6. Diferencias sexo:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro1.r6 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro1.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 2 (SKY - AZUL CIELO)        -->
          <!-- ========================================== -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group" @click="toggle('f2')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-sky-300 group-hover:text-sky-200 transition-colors">
                <span class="material-symbols-outlined text-sky-400">bar_chart</span>
                Foro 2: Gráfico Comparativo
              </h3>
              <div class="flex items-center gap-3">
                <!-- BADGE FIJO VERDE/ROJO -->
                <span class="text-xs px-2 py-1 rounded font-bold border" :class="expediente.foro2 ? 'bg-green-900/30 text-green-300 border-green-700' : 'bg-red-900/30 text-red-300 border-red-800'">
                  {{ expediente.foro2 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f2 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro2 && expandido.f2" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-sky-500">
              <div class="grid gap-6">
                <div><strong class="text-sky-200 block mb-1 text-base">1. Análisis:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro2.r1 }}</p></div>
                <div><strong class="text-sky-200 block mb-1 text-base">2. Comparativa:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro2.r2 }}</p></div>
                <div><strong class="text-sky-200 block mb-1 text-base">3. Tendencias:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro2.r3 }}</p></div>
                <div><strong class="text-sky-200 block mb-1 text-base">4. Puntos críticos:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro2.r4 }}</p></div>
                <div><strong class="text-sky-200 block mb-1 text-base">5. Conclusiones:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro2.r5 }}</p></div>
                <div><strong class="text-sky-200 block mb-1 text-base">6. Reflexión:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro2.r6 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro2.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 3 (BLUE - AZUL REAL)        -->
          <!-- ========================================== -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group" @click="toggle('f3')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-blue-300 group-hover:text-blue-200 transition-colors">
                <span class="material-symbols-outlined text-blue-400">accessibility_new</span>
                Foro 3: DMO Cadera
              </h3>
              <div class="flex items-center gap-3">
                <!-- BADGE FIJO VERDE/ROJO -->
                <span class="text-xs px-2 py-1 rounded font-bold border" :class="expediente.foro3 ? 'bg-green-900/30 text-green-300 border-green-700' : 'bg-red-900/30 text-red-300 border-red-800'">
                  {{ expediente.foro3 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f3 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro3 && expandido.f3" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-blue-500">
              <div class="grid gap-6">
                <div><strong class="text-blue-200 block mb-1 text-base">1. Cambio DMO:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro3.r1 }}</p></div>
                <div><strong class="text-blue-200 block mb-1 text-base">2. Razón promedio:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro3.r2 }}</p></div>
                <div><strong class="text-blue-200 block mb-1 text-base">3. Cambio por año:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro3.r3 }}</p></div>
                <div><strong class="text-blue-200 block mb-1 text-base">4. Ubicación:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro3.r4 }}</p></div>
                <div><strong class="text-blue-200 block mb-1 text-base">5. Pendiente secante:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro3.r5 }}</p></div>

                <div class="bg-blue-900/20 p-3 rounded border border-blue-800/50">
                  <strong class="text-blue-200 block mb-1">6. Tabla de Análisis:</strong>
                  <p class="text-xs text-gray-400 italic">Los datos de la tabla compleja se encuentran almacenados en la base de datos.</p>
                </div>

                <div><strong class="text-blue-200 block mb-1 text-base">7. Info razón promedio:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro3.r7 }}</p></div>
                <div><strong class="text-blue-200 block mb-1 text-base">8. Valor a los 50:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro3.r8 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro3.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 4 (INDIGO - AZUL VIOLETA)   -->
          <!-- ========================================== -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group" @click="toggle('f4')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-indigo-300 group-hover:text-indigo-200 transition-colors">
                <span class="material-symbols-outlined text-indigo-400">analytics</span>
                Foro 4: Análisis DMO
              </h3>
              <div class="flex items-center gap-3">
                <!-- BADGE FIJO VERDE/ROJO -->
                <span class="text-xs px-2 py-1 rounded font-bold border" :class="expediente.foro4 ? 'bg-green-900/30 text-green-300 border-green-700' : 'bg-red-900/30 text-red-300 border-red-800'">
                  {{ expediente.foro4 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f4 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro4 && expandido.f4" class="p-6 space-y-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-indigo-500">
              <div class="grid gap-6">
                <div><strong class="text-indigo-200 block mb-1 text-base">1. Expresión Algebraica:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700 font-mono text-green-400">{{ expediente.foro4.r1 }}</p></div>
                <div><strong class="text-indigo-200 block mb-1 text-base">2. Consideraciones:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro4.r2 }}</p></div>
                <div><strong class="text-indigo-200 block mb-1 text-base">3. Coincidencia:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro4.r3 }}</p></div>
                <div><strong class="text-indigo-200 block mb-1 text-base">4. Verificación:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro4.r4 }}</p></div>
                <div><strong class="text-indigo-200 block mb-1 text-base">5. Ventajas:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro4.r5 }}</p></div>
                <div><strong class="text-indigo-200 block mb-1 text-base">6. Hallazgos:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro4.r6 }}</p></div>
                <div><strong class="text-indigo-200 block mb-1 text-base">7. Argumentación:</strong> <p class="bg-gray-900/50 p-3 rounded border border-gray-700">{{ expediente.foro4.r7 }}</p></div>
              </div>
              <p class="text-xs text-gray-500 mt-4 border-t border-gray-700 pt-2 text-right">
                Entregado el: {{ new Date(expediente.foro4.fecha).toLocaleString() }}
              </p>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 5 (VIOLET - VIOLETA)        -->
          <!-- ========================================== -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group" @click="toggle('f5')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-violet-300 group-hover:text-violet-200 transition-colors">
                <span class="material-symbols-outlined text-violet-400">trending_up</span>
                Foro 5: Razón de Cambio
              </h3>
              <div class="flex items-center gap-3">
                <!-- BADGE FIJO VERDE/ROJO -->
                <span class="text-xs px-2 py-1 rounded font-bold border" :class="expediente.foro5 ? 'bg-green-900/30 text-green-300 border-green-700' : 'bg-red-900/30 text-red-300 border-red-800'">
                  {{ expediente.foro5 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f5 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro5 && expandido.f5" class="p-6 space-y-4 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-violet-600">
              <div class="grid gap-4">
                <p><strong class="text-violet-200">P1:</strong> {{ expediente.foro5.r1 }}</p>
                <img
  v-if="expediente.foro5?.imagen"
  :src="'data:image/jpeg;base64,' + expediente.foro5.imagen"
  class="rounded-xl"
/>

                <p><strong class="text-violet-200">P2:</strong> {{ expediente.foro5.r2 }}</p>
                <p><strong class="text-violet-200">P3:</strong> {{ expediente.foro5.r3 }}</p>
                <details>
                  <summary class="cursor-pointer text-gray-400 mt-2 hover:text-white">Ver más...</summary>
                  <div class="pl-4 pt-2 space-y-2">
                    <p><strong class="text-violet-200">P4:</strong> {{ expediente.foro5.r4 }}</p>
                    <p><strong class="text-violet-200">P5:</strong> {{ expediente.foro5.r5 }}</p>
                  </div>
                </details>
              </div>
              <p class="text-xs text-gray-500 mt-4 text-right">Entregado el: {{ new Date(expediente.foro5.fecha).toLocaleString() }}</p>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 6 (PURPLE - MORADO PROFUNDO)-->
          <!-- ========================================== -->
          <div class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg">
            <div class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group" @click="toggle('f6')">
              <h3 class="font-bold text-lg flex items-center gap-2 text-purple-300 group-hover:text-purple-200 transition-colors">
                <span class="material-symbols-outlined text-purple-400">swap_horiz</span>
                Foro 6: Covariación
              </h3>
              <div class="flex items-center gap-3">
                <!-- BADGE FIJO VERDE/ROJO -->
                <span class="text-xs px-2 py-1 rounded font-bold border" :class="expediente.foro6 ? 'bg-green-900/30 text-green-300 border-green-700' : 'bg-red-900/30 text-red-300 border-red-800'">
                  {{ expediente.foro6 ? 'Completado' : 'Sin entregar' }}
                </span>
                <span class="material-symbols-outlined text-gray-400 transition-transform" :class="expandido.f6 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>

            <div v-if="expediente.foro6 && expandido.f6" class="p-6 space-y-4 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-purple-600">
              <div class="grid gap-4">
                <p><strong class="text-purple-200">1. Dominio:</strong> {{ expediente.foro6.r1 }}</p>
                <p><strong class="text-purple-200">2. Argumento:</strong> {{ expediente.foro6.r2 }}</p>
                <details>
                  <summary class="cursor-pointer text-gray-400 mt-2 hover:text-white">Ver respuestas completas (3-8)...</summary>
                  <div class="pl-4 pt-2 space-y-2">
                    <pre class="bg-gray-900/50 p-2 rounded whitespace-pre-wrap font-sans text-xs border border-gray-700"><strong class="text-purple-200">3. Simulador:</strong> {{ expediente.foro6.r3 }}</pre>
                    <p><strong class="text-purple-200">4. GeoGebra:</strong> {{ expediente.foro6.r4 }}</p>
                    <p><strong class="text-purple-200">5. Pendientes:</strong> {{ expediente.foro6.r5 }}</p>
                    <p><strong class="text-purple-200">6. Notas:</strong> {{ expediente.foro6.r6 }}</p>
                    <pre class="bg-gray-900/50 p-2 rounded whitespace-pre-wrap font-sans text-xs border border-gray-700"><strong class="text-purple-200">7. Óptimo M:</strong> {{ expediente.foro6.r7 }}</pre>
                    <p><strong class="text-purple-200">8. Óptimo H:</strong> {{ expediente.foro6.r8 }}</p>
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
    const res = await fetch('http://127.0.0.1:8000/lista_estudiantes');
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
  expandido.value = {f1: true, f2: true, f3: true, f4: true, f5: true, f6: true, e1: true};

  try {
    const res = await fetch(`http://127.0.0.1:8000/expediente_completo/${alumno.email}`);
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