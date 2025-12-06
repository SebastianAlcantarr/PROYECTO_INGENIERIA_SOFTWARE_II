<template>
  <div class="flex flex-col md:flex-row min-h-screen bg-[#244a76] dark:bg-[rgb(16,22,34)]">
    <!-- sidebar -->
    <Sidebar class="hidden md:block" />

    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-5xl">

          <!-- titulo -->
          <section class="scroll-mt-20 mb-8">
            <div class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-blue-600">
              <h1 class="text-white text-3xl md:text-3xl font-black text-center">
                Foro 4: Análisis DMO
              </h1>
            </div>
          </section>

          <!-- cargando -->
          <div v-if="cargandoEstado" class="text-center py-10">
            <p class="text-indigo-200 text-xl animate-pulse">Cargando actividad...</p>
          </div>

          <!-- si no ha participado -->
          <section v-else-if="!usuarioYaParticipo" class="animate-fade-in">
            <div class="text-white text-2xl md:text-3xl font-black ">

Generalizando la razón instantánea de cambio
                </div>
              <div class="pregunta-texto text-base text-white/90 mb-3">
                <div class="mt-5 mb-5">
                 Hasta ahora, hemos utilizado la razón promedio de cambio como una herramienta para modelar el comportamiento de un gráfico y mostrar la relación de cambio entre dos valores consecutivos. En las actividades que siguen, buscaremos desarrollar una estrategia más precisa que nos permita obtener información más detallada sobre el comportamiento de una función que representa un problema.
Esto nos facilitará determinar el valor máximo o mínimo con mayor precisión y describir el comportamiento de cualquier función en general. Así, podremos realizar predicciones o implementar mejoras con el objetivo de optimizar o eficientar algún fenómeno en estudio.
                </div>

              </div>


            <!-- tabla -->
            <div class="bg-[#161d2b] p-6 rounded-xl shadow-xl mb-8 border border-gray-700">
              <h2 class="text-white text-base font-bold mb-4">Datos de Referencia</h2>
              <p class="text-gray-300 mb-6">
                Dada la siguiente tabla de la DMO de la cadera de las mujeres y la edad:
              </p>

              <div class="overflow-hidden rounded-lg border border-gray-600 max-w-lg mx-auto">
                <table class="w-full text-sm text-left text-gray-400">
                  <thead class="text-m text-white uppercase bg-indigo-900/50">
                  <tr>
                    <th class="px-6 py-3 text-center border-b border-gray-600">Edad Promedio</th>
                    <th class="px-6 py-3 text-center border-b border-gray-600">DMO Cadera</th>
                  </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-700">
                  <tr class="bg-[#222d3e] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">15</td><td class="px-6 py-2 text-center">0.847</td></tr>
                  <tr class="bg-[#1e2837] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">25</td><td class="px-6 py-2 text-center">0.890</td></tr>
                  <tr class="bg-[#222d3e] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">35</td><td class="px-6 py-2 text-center">0.896</td></tr>
                  <tr class="bg-[#1e2837] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">45</td><td class="px-6 py-2 text-center">0.913</td></tr>
                  <tr class="bg-[#222d3e] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">55</td><td class="px-6 py-2 text-center">0.838</td></tr>
                  <tr class="bg-[#1e2837] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">65</td><td class="px-6 py-2 text-center">0.769</td></tr>
                  <tr class="bg-[#222d3e] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">75</td><td class="px-6 py-2 text-center">0.696</td></tr>
                  <tr class="bg-[#1e2837] hover:bg-[#2a3649]"><td class="px-6 py-2 text-center font-bold text-white">85</td><td class="px-6 py-2 text-center">0.625</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- cuestionario -->
            <div class="bg-[#161d2b] p-6 rounded-xl shadow-xl space-y-8 border border-gray-700">

              <!-- P1 -->
              <div>
                <h3 class="text-base text-white/90 mb-2 font-medium">
                  1. Utiliza la <a href="https://docs.google.com/spreadsheets/d/1VQdNrfdddTFhpdlPhecQD_QeMs1hLk3dhHyn3iUlkFg/edit?gid=1382532865#gid=1382532865" class="text-blue-400 hover:underline" target="_blank"
                                   rel="noopener noreferrer">hoja de cálculo de Google Drive</a> para generar la función que mejor aproxime los puntos y por lo tanto puede modelar este fenómeno. Obtén su expresión algebraica.
                </h3>
                <a href="https://drive.google.com/file/d/1OgW5vZDYPk73MPUSOJ7xMfFA93FEvzUt/view?usp=sharing" class="inline-flex items-center gap-2 text-xs bg-red-900/30 text-red-300 px-2 py-1 rounded hover:bg-red-900/50 transition-colors mb-3 border border-red-800" target="_blank"
                   rel="noopener noreferrer">
                  <span class="material-symbols-outlined text-xs" >play_circle</span> Ver VideoTutorial 1
                </a>
                <textarea v-model="r1" rows="2" placeholder="Escribe la expresión algebraica..." class="input-foro"></textarea>
              </div>

              <!-- P2 -->
              <div>
                <h3 class="text-base text-white/90 mb-3 font-medium">
                  2. Explica las consideraciones que tomaste en cuenta para elegir la función que mejor aproxima los puntos.
                </h3>
                <textarea v-model="r2" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P3 -->
              <div>
                <h3 class="text-base text-white/90 mb-3 font-medium">
                  3. La función que elegiste ¿coincide con la evolución en la DMO a lo largo de la vida? Explica ampliamente tu respuesta.
                </h3>
                <textarea v-model="r3" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P4 -->
              <div>
                <h3 class="text-base text-white/90 mb-3 font-medium">
                  4. Calcula, usando la expresión algebraica, la densidad mineral ósea para una edad aleatoria de la tabla y verifica si el resultado obtenido es consistente. ¿Es el mismo valor? ¿A qué se debe?
                </h3>
                <textarea v-model="r4" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P5 -->
              <div>
                <h3 class="text-base text-white/90 mb-3 font-medium">
                  5. Con la expresión algebraica podemos obtener el valor de la DMO para cualquier edad. Argumenta e indica ¿qué ventajas se pueden tener si completamos la tabla anterior pero ahora con intervalos más pequeños, por ejemplo, de un año en un año?
                </h3>
                <textarea v-model="r5" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P6 -->
              <div>
                <h3 class="text-base text-white/90 mb-2 font-medium">
                  6. Elabora una tabla de año en año usando la segunda hoja del documento que subimos a Google Drive y realiza su gráfica.
                </h3>
                <a href="https://www.canva.com/design/DAGPpllYKuA/A2O1-5xRxdaHas-Yb5jHcw/edit?utm_content=DAGPpllYKuA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton" class="inline-flex items-center gap-2 text-xs bg-red-900/30 text-red-300 px-2 py-1 rounded hover:bg-red-900/50 transition-colors mb-3 border border-red-800" target="_blank"
                   rel="noopener noreferrer">
                  <span class="material-symbols-outlined text-sm">play_circle</span> Ver VideoTutorial 2
                </a>
                <textarea v-model="r6" rows="3" placeholder="Describe la grafica..." class="input-foro"></textarea>
              </div>

              <!-- P7 -->
              <div>
                <h3 class="text-base text-white/90 mb-3 font-medium">
                  7. Argumenta ejemplificando detalladamente la siguiente afirmación:
                  <em class="block mt-2 pl-4 border-l-2 border-blue-600 text-gray-400">
                    "Con la expresión algebraica podemos obtener el valor de la DMO para cualquier edad, es decir se puede obtener la DMO de la cadera en cualquier momento de la vida, por ejemplo, a los 38.6 años, esto indica que el fenómeno de variación es continuo y la función elegida también es continua."
                  </em>
                </h3>
                <textarea v-model="r7" rows="4" placeholder="Tu argumentación..." class="input-foro"></textarea>
              </div>

              <!-- btn enviar -->
              <div class="pt-6 border-t border-gray-700 flex flex-col items-end gap-2">
                <p v-if="mensaje" :class="`text-sm font-bold ${tipoMensaje === 'error' ? 'text-red-400' : 'text-green-400'}`">
                  {{ mensaje }}
                </p>
                <button
                    @click="enviarRespuestas"
                    :disabled="enviando"
                    class="bg-blue-600 hover:bg-indigo-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all active:scale-95 disabled:opacity-50 flex items-center gap-2"
                >
                  <span v-if="enviando" class="material-symbols-outlined animate-spin">refresh</span>
                  {{ enviando ? 'Guardando...' : 'Enviar Respuestas' }}
                </button>
              </div>
            </div>
          </section>

          <!-- si ya participo -->
          <section v-else class="animate-fade-in">
            <div class="bg-green-900/30 border border-green-500/50 p-4 rounded-xl mb-8 flex items-center gap-4 text-green-200">
              <span class="material-symbols-outlined text-3xl">check_circle</span>
              <div>
                <h3 class="font-bold text-base">Actividad Completada</h3>
                <p class="text-sm opacity-80">Gracias por tu aporte. Aquí están las respuestas de tus compañeros.</p>
              </div>
            </div>

            <!-- respuestas -->
            <div class="space-y-6">
              <div v-if="listaRespuestas.length === 0" class="text-center text-gray-400 py-8">
                Aún no hay respuestas de otros estudiantes.
              </div>

              <div
                  v-for="(item, index) in listaRespuestas"
                  :key="index"
                  class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-600 shadow-md"
              >
                <div class="flex justify-between items-start mb-4">
                  <div class="flex items-center gap-3">
                    <div class="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">
                      {{ obtenerIniciales(item.nombre, item.email) }}
                    </div>
                    <div>
                      <span class="text-indigo-400 font-bold text-base">
                        {{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}
                      </span>
                      <p class="text-gray-500 text-xs">{{ formatearFecha(item.fecha) }}</p>
                    </div>
                  </div>
                  <span class="bg-indigo-900/50 text-indigo-200 text-xs px-2 py-1 rounded">#{{ listaRespuestas.length - index }}</span>
                </div>

                <div class="space-y-4 text-gray-300 text-sm pl-4 border-l border-gray-700/50">
                  <p><strong class="text-indigo-200">1. Función:</strong> {{ item.r1 }}</p>
                  <p><strong class="text-indigo-200">2. Consideraciones:</strong> {{ item.r2 }}</p>

                  <details class="text-gray-400 cursor-pointer group">
                    <summary class="hover:text-white list-none flex items-center gap-2 py-2">
                      <span class="material-symbols-outlined text-sm group-open:rotate-180 transition-transform">expand_more</span>
                      Ver resto de respuestas (3-7)
                    </summary>
                    <div class="mt-2 space-y-4 pt-2 border-t border-gray-700/50 animate-fade-in">
                      <p><strong class="text-indigo-200">3. Coincidencia:</strong> {{ item.r3 }}</p>
                      <p><strong class="text-indigo-200">4. Verificación:</strong> {{ item.r4 }}</p>
                      <p><strong class="text-indigo-200">5. Ventajas intervalos:</strong> {{ item.r5 }}</p>
                      <p><strong class="text-indigo-200">6. Gráfica anual:</strong> {{ item.r6 }}</p>
                      <p><strong class="text-indigo-200">7. Continuidad:</strong> {{ item.r7 }}</p>
                    </div>
                  </details>
                </div>
              </div>
            </div>
          </section>

        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Sidebar from "@/views/sidebar.vue";

// Variables reactivas
const r1 = ref(""); const r2 = ref(""); const r3 = ref("");
const r4 = ref(""); const r5 = ref(""); const r6 = ref(""); const r7 = ref("");

const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);

onMounted(async () => {
  const email = localStorage.getItem('usuario');
  if (email) {
    await verificarEstado(email);
  } else {
    cargandoEstado.value = false;
  }
});

async function verificarEstado(email) {
  try {
    const res = await fetch(`http://127.0.0.1:8000/verificar_foro4/${email}`);
    const datos = await res.json();
    if (datos.participo) {
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    }
  } catch (error) {
    console.error("Error verificando:", error);
  } finally {
    cargandoEstado.value = false;
  }
}

async function enviarRespuestas() {
  const usuarioEmail = localStorage.getItem('usuario');
  if (!usuarioEmail) {
    mensaje.value = "Error: Debes iniciar sesión.";
    tipoMensaje.value = "error";
    return;
  }
  // Validacion basica
  if (!r1.value || !r2.value) {
    mensaje.value = "Por favor responde al menos las primeras preguntas.";
    tipoMensaje.value = "error";
    return;
  }

  enviando.value = true;
  mensaje.value = "Guardando...";

  try {
    const respuesta = await fetch("http://127.0.0.1:8000/guardar_foro4", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: usuarioEmail,
        r1: r1.value, r2: r2.value, r3: r3.value, r4: r4.value,
        r5: r5.value, r6: r6.value, r7: r7.value
      })
    });
    const datos = await respuesta.json();

    if (datos.exito) {
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    } else {
      mensaje.value = "Error: " + datos.mensaje;
      tipoMensaje.value = "error";
    }
  } catch (error) {
    mensaje.value = "Error de conexión";
    tipoMensaje.value = "error";
  } finally {
    enviando.value = false;
  }
}

async function cargarForoCompleto() {
  try {
    const res = await fetch("http://127.0.0.1:8000/respuestas_foro4");
    listaRespuestas.value = await res.json();
  } catch (error) {
    console.error("Error cargando foro", error);
  }
}

// Utilidades
function obtenerIniciales(nombre, email) {
  if (nombre) return nombre[0].toUpperCase();
  return email ? email.substring(0, 2).toUpperCase() : "?";
}

function formatearFecha(f) {
  if (!f) return "";
  const fechaStr = f.endsWith("Z") ? f : f + "Z";

  return new Date(fechaStr).toLocaleDateString('es-ES', {
    year: 'numeric', month: 'short', day: 'numeric',
    hour: '2-digit', minute:'2-digit', hour12: true
  });
}
</script>



<style scoped>
.input-foro {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  background-color: #222d3e;
  border: 1px solid #4b5563;
  color: white;
  resize: vertical;
}
.input-foro:focus {
  outline: none;
  border-color: #2a63cb; /* Indigo-500 */
  box-shadow: 0 0 0 3px rgb(35, 118, 229);
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}
</style>