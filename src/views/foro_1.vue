<template>
  <div class="flex flex-col md:flex-row min-h-screen bg-[#244a76] dark:bg-[rgb(16,22,34)]">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-5xl">

          <!-- TÍTULO -->
          <section class="scroll-mt-20 mb-8" id="introduction">
            <div class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-blue-500">
              <h1 class="text-white text-base md:text-3xl font-black text-center">
                Foro 1: La densidad mineral ósea
              </h1>
            </div>
          </section>

          <!-- ESTADO DE CARGA INICIAL -->
          <div v-if="cargandoEstado" class="text-center py-10">
            <p class="text-blue-200 text-base animate-pulse">Verificando tu participación...</p>
          </div>

          <!-- MODO FORMULARIO: Solo se ve si NO ha participado -->
          <section v-else-if="!usuarioYaParticipo" class="space-y-6 animate-fade-in">
            <h2 class="text-white text-base font-bold px-2 flex items-center gap-2">
              <span class="material-symbols-outlined">edit_note</span>
              Tu Turno: Investiga y responde
            </h2>

            <div class="bg-[#161d2b] p-6 rounded-xl shadow-xl space-y-8 border border-gray-700">

              <!-- Pregunta 1 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  1.- Explica en qué consiste la densidad mineral ósea (DMO) y cómo se mide.
                </h3>
                <textarea v-model="r1" rows="3" placeholder="Escribe tu análisis aquí..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 2 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  2.- ¿Qué factores consideras que influyen en una buena salud ósea?
                </h3>
                <textarea v-model="r2" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 3 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  3.- ¿Relación entre edad y DMO? Justifica.
                </h3>
                <textarea v-model="r3" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 4 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  4.- ¿Cómo evoluciona la DMO a lo largo de la vida?
                </h3>
                <textarea v-model="r4" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 5 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  5.- ¿Se puede saber la edad aproximada dado un valor de DMO?
                </h3>
                <textarea v-model="r5" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 6 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  6.- ¿Diferencias entre esqueleto femenino y masculino?
                </h3>
                <textarea v-model="r6" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- BOTÓN DE ENVÍO -->
              <div class="pt-6 border-t border-gray-700 flex flex-col items-end gap-2">
                <p v-if="mensaje" :class="`text-sm font-bold ${tipoMensaje === 'error' ? 'text-red-400' : 'text-green-400'}`">
                  {{ mensaje }}
                </p>
                <button
                    @click="enviarRespuestas"
                    :disabled="enviando"
                    class="bg-blue-600 hover:bg-blue-900 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  <span v-if="enviando" class="material-symbols-outlined animate-spin">refresh</span>
                  {{ enviando ? 'Guardando...' : 'Publicar' }}
                </button>
              </div>
            </div>
          </section>

          <!-- MODO VISTA: Solo se ve si YA participó -->
          <section v-else class="animate-fade-in">
            <div class="bg-green-900/30 border border-green-500/50 p-4 rounded-xl mb-8 flex items-center gap-4 text-green-200">
              <span class="material-symbols-outlined text-3xl">check_circle</span>
              <div>
                <h3 class="font-bold text-base">Actividad Completada</h3>
                <p class="text-sm opacity-80">Gracias por tu aporte. Aquí están las respuestas de tus compañeros.</p>
              </div>
            </div>


            <!-- Lista de Respuestas (Muro) -->
            <h2 class="text-white text-base font-bold mb-6 border-b border-gray-700 pb-2 flex items-center gap-2">
              <span class="material-symbols-outlined">forum</span>
              Participaciones del Grupo
            </h2>

            <div class="space-y-6">
              <div v-if="listaRespuestas.length === 0" class="text-center text-gray-400 py-8">
                Aún no hay respuestas de otros estudiantes.
              </div>

              <div
                  v-for="(item, index) in listaRespuestas"
                  :key="index"
                  class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-500 shadow-md hover:bg-[#253042] transition-colors"
              >
                <div class="flex justify-between items-start mb-4">
                  <div class="flex items-center gap-3">
                    <div class="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">
                      {{ obtenerIniciales(item.nombre, item.apellidos || item.email) }}
                    </div>
                    <div>
                      <span class="text-blue-400 font-bold text-base">
                        {{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}
                      </span>
                      <p class="text-gray-500 text-xs">{{ formatearFecha(item.fecha) }}</p>
                    </div>
                  </div>
                  <span class="bg-blue-900/50 text-blue-200 text-sm px-2 py-1 rounded">Respuesta #{{ listaRespuestas.length - index }}</span>
                </div>

                <div class="space-y-4 text-gray-300 text-sm pl-2 border-l border-gray-700 ml-4">
                  <p><strong class="text-blue-200">1. Definición DMO:</strong> <br>{{ item.r1 }}</p>
                  <p><strong class="text-blue-200">2. Factores Salud:</strong> <br>{{ item.r2 }}</p>

                  <details class="text-gray-400 cursor-pointer group">
                    <summary class="hover:text-white list-none flex items-center gap-2 py-2">
                      <span class="material-symbols-outlined text-sm group-open:rotate-180 transition-transform">expand_more</span>
                      Ver respuestas completas...
                    </summary>
                    <div class="mt-2 space-y-4 pt-2 border-t border-gray-700/50 animate-fade-in">
                      <p><strong class="text-blue-200">3. Edad vs DMO:</strong> <br>{{ item.r3 }}</p>
                      <p><strong class="text-blue-200">4. Evolución:</strong> <br>{{ item.r4 }}</p>
                      <p><strong class="text-blue-200">5. Edad aproximada:</strong> <br>{{ item.r5 }}</p>
                      <p><strong class="text-blue-200">6. Diferencias sexo:</strong> <br>{{ item.r6 }}</p>
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
const r4 = ref(""); const r5 = ref(""); const r6 = ref("");
const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);

// ESTADO DE CONTROL
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);

// Al cargar la página, verificamos si el usuario ya hizo la tarea
onMounted(async () => {
  const email = localStorage.getItem('usuario');
  if (email) {
    await verificarEstado(email);
  } else {
    cargandoEstado.value = false; // Si no hay usuario, mostramos formulario (luego fallará al enviar, pidiendo login)
  }
});

async function verificarEstado(email) {
  try {
    // 1. Preguntamos a Python: "¿Este email ya respondió?"
    const res = await fetch(`http://127.0.0.1:8000/verificar_foro1/${email}`);
    const datos = await res.json();

    if (datos.participo) {
      usuarioYaParticipo.value = true;
      // 2. Si ya respondió, cargamos la lista de todos inmediatamente
      await cargarForoCompleto();
    }
  } catch (error) {
    console.error("Error verificando estado:", error);
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

  if (!r1.value || !r2.value) {
    mensaje.value = "Por favor completa al menos las primeras respuestas.";
    tipoMensaje.value = "error";
    return;
  }

  enviando.value = true;
  mensaje.value = "Guardando...";

  try {
    const respuesta = await fetch("http://127.0.0.1:8000/guardar_foro1", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: usuarioEmail,
        r1: r1.value, r2: r2.value, r3: r3.value,
        r4: r4.value, r5: r5.value, r6: r6.value

      })
    });

    const datos = await respuesta.json();

    if (datos.exito) {
      // ÉXITO: Cambiamos el estado localmente para ocultar formulario y mostrar lista
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    } else {
      mensaje.value = "Error: " + datos.mensaje;
      tipoMensaje.value = "error";
    }

  } catch (error) {
    console.error(error);
    mensaje.value = "Error de conexión";
    tipoMensaje.value = "error";
  } finally {
    enviando.value = false;
  }
}

async function cargarForoCompleto() {
  try {
    const res = await fetch("http://127.0.0.1:8000/respuestas_foro1");
    listaRespuestas.value = await res.json();
  } catch (error) {
    console.error("Error cargando foro", error);
  }
}

// Utilidades visuales
function obtenerIniciales(nombre, apellidoOEmail) {
  if (nombre) {
    return (nombre[0] + (apellidoOEmail ? apellidoOEmail[0] : '')).toUpperCase();
  }
  return apellidoOEmail.substring(0, 2).toUpperCase();
}

function formatearFecha(fechaString) {
  if (!fechaString) return "";

  // Crear fecha y ajustar a la zona horaria de Hermosillo
  const fecha = new Date(fechaString);
  
  // Obtener la diferencia de tiempo en minutos con la zona horaria local
  const tzOffset = fecha.getTimezoneOffset();
  // Ajustar la fecha a la zona horaria de Hermosillo (UTC-7 o UTC-6 dependiendo del horario de verano)
  const hermosilloOffset = -7 * 60; // Aproximado, se ajustará según el horario de verano
  const diff = tzOffset + hermosilloOffset;
  const adjustedDate = new Date(fecha.getTime() + diff * 60 * 1000);

  // Opciones para mostrar fecha y hora
  const opciones = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'America/Hermosillo',
    hour12: true
  };

  // Usar toLocaleString con la zona horaria específica
  return adjustedDate.toLocaleString('es-MX', opciones);
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
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}
</style>