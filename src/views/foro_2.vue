<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />
    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-5xl">
          <!-- INTRODUCCION -->
          <section class="scroll-mt-20 mb-8" id="introduction">
            <div
              class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-blue-800"
            >
              <h1
                class="text-white text-2xl md:text-3xl font-black text-center"
              >
                Densidad mineral ósea entre hombres y mujeres
              </h1>
            </div>
          </section>

          <div v-if="cargandoEstado" class="text-center py-10">
            <p class="http://127.0.0.1:8000">Verificando tu participación...</p>
          </div>

          <section
            v-else-if="!usuarioYaParticipo"
            class="space-y-6 animate-fade-in"
          >
            <div>
              <div class="  ">
                <button
                  @click="mostrarInformacion = !mostrarInformacion"
                  class="text-blue-300 hover:text-white flex items-center gap-2 text-sm bg-blue-900/30 px-3 py-1 rounded-lg transition-colors"
                >
                  <span class="material-symbols-outlined">{{
                    mostrarInformacion ? "visibility_off" : "visibility"
                  }}</span>
                  {{
                    mostrarInformacion ? "Ocultar Material" : "Mostrar Material"
                  }}
                </button>
                <div
                  v-if="mostrarInformacion"
                  class="animate-fade-in space-y-6"
                >
                  <div class="text-white text-2xl md:text-3xl font-black mt-5">
                    Modelación del problema
                  </div>
                  <img
                    :src="foro2"
                    alt="Gráfico de Densidad Mineral Ósea"
                    class="mx-auto w-200 p-5"
                  />
                  <div class="pregunta-texto text-base text-white/90 mb-3">
                    Las graficas anteriores obtenidas del artículo: Cambios
                    relacionados con la edad en la prevalencia de la
                    osteoporosis según el género y la zona esquelética: Encuesta
                    nacional de examen de salud y nutrición de Corea
                    2008-20101,muestran los cambios en la densidad mineral ósea,
                    entre los 10 y los 89 años de la espina lumbar, la cadera y
                    el femur (específicamente el cuello femoral) de 17,205
                    coreanos (7,837 hombres y 9,368 mujeres) como indicadores de
                    la salud ósea.
                    <div class="mt-5">
                      1. Jongseok Lee, Sungwha Lee, Sungok Jang y Ohk Hyun Ryu
                      (2013). Age-Related Changes in the Prevalence of
                      Osteoporosis according to Gender and Skeletal Site: The
                      Korea National Health and Nutrition Examination Survey
                      2008-2010. Endocrinology and Metabolism, 28(3):180-191.
                      DOI:
                      <a
                        class="text-blue-500 hover:text-blue-700 transition-colors duration-200"
                        href="https://e-enm.org/journal/view.php?doi=10.3803/EnM.2013.28.3.180"
                        target="_blank"
                        rel="noopener noreferrer"
                        >https://e-enm.org/journal/view.php?doi=10.3803/EnM.2013.28.3.180</a
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <section class="scroll-mt-20" id="rules">
              <div
                class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-blue-800"
              >
                <h1
                  class="text-white text-base md:text-3xl font-black text-center"
                >
                  Foro 2: Gráfico comparativo
                </h1>
              </div>

              <br />

              <h2 class="pregunta-texto text-xl text-white/90 mb-3">
                El siguiente gráfico comparativo se elaboró a partir de los
                datos del
                <a
                  class="text-blue-400 hover:text-blue-700 transition-colors duration-200"
                  href="https://e-enm.org/journal/view.php?doi=10.3803/EnM.2013.28.3.180"
                  target="_blank"
                  rel="noopener noreferrer"
                  >articulo de investigacion</a
                >
                de Lee y colaboradores (2013, p. 184). El gráfico muestra los
                valores de la cadera (Total hip) tanto de hombres como de
                mujeres.
              </h2>

              <div class="rounded-xl overflow-hidden">
                <img
                  class="w-full max-w-[700px] md:max-w-[800px] lg:max-w-[1000px] xl:max-w-[900px] mx-auto object-contain"
                  src="/src/imagenes/Cadera H vs M.png"
                  alt="Grafica"
                />
              </div>
            </section>

            <h2
              class="text-white text-xl font-bold px-2 flex items-center gap-2"
            >
              <span class="material-symbols-outlined">edit_note</span>
              Tu Turno: Investiga y responde
            </h2>

            <div
              class="bg-[#161d2b] p-6 rounded-xl shadow-xl space-y-8 border border-gray-700"
            >
              <!-- Pregunta 1 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  1. Describe las similitudes y diferencias que observas en las
                  gráficas de la DMO de la cadera entre hombres y mujeres,
                  determinando aproximadamente la edad en que se presentan.
                </h3>
                <textarea
                  v-model="r1"
                  rows="3"
                  placeholder="Escribe tu análisis aquí..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- Pregunta 2 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  2. ¿En qué etapa de la vida aumenta más la densidad mineral
                  ósea en las mujeres? ¿Y de los hombres? ¿Cuál podría ser la
                  causa? Justifica tu respuesta.
                </h3>
                <textarea
                  v-model="r2"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- Pregunta 3 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  3. ¿En qué etapa de la vida disminuye más la densidad mineral
                  ósea en las mujeres? ¿Y de los hombres? ¿A qué se debe esto?
                  Justifica tu respuesta.
                </h3>
                <textarea
                  v-model="r3"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- Pregunta 4 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  4. ¿Habrá una edad donde la densidad mineral ósea tenga un
                  valor máximo? Ese valor, ¿se puede ubicar en la gráfica?
                  Justifica tu respuesta.
                </h3>
                <textarea
                  v-model="r4"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- Pregunta 5 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  5. Analiza la siguiente afirmación argumentando por qué
                  consideras que el fenómeno se comporta así: En la gráfica
                  anterior se observa que la densidad mineral ósea, aumenta en
                  los primeros años de vida (la gráfica crece) y luego, a partir
                  de cierta edad, se comienza a perder densidad mineral ósea (la
                  gráfica decrece). Entonces, hay una edad donde la densidad
                  mineral ósea alcanza su valor máximo (conocido como pico de
                  densidad mineral ósea) por lo que este fenómeno de variación
                  (cambio) tiene un valor óptimo y es un máximo.
                </h3>
                <textarea
                  v-model="r5"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- Pregunta 6 -->
              <div>
                <h3 class="pregunta-texto text-base text-white/90 mb-3">
                  6. ¿Cómo podemos verificar o encontrar la edad dónde se
                  alcanza el valor óptimo? Lista las ideas o herramientas que
                  nos pueden ayudar a encontrar la edad exacta donde se alcanza
                  ese pico de masa ósea.
                </h3>
                <textarea
                  v-model="r6"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- BOTÓN DE ENVÍO -->
              <div
                class="pt-6 border-t border-gray-700 flex flex-col items-end gap-2"
              >
                <p
                  v-if="mensaje"
                  :class="`text-sm font-bold ${
                    tipoMensaje === 'error' ? 'text-red-400' : 'text-green-400'
                  }`"
                >
                  {{ mensaje }}
                </p>
                <button
                  @click="enviarRespuestas"
                  :disabled="enviando"
                  class="bg-blue-600 hover:bg-blue-900 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  <span
                    v-if="enviando"
                    class="material-symbols-outlined animate-spin"
                    >refresh</span
                  >
                  {{ enviando ? "Guardando..." : "Enviar Respuestas" }}
                </button>
              </div>
            </div>
          </section>

          <section v-else class="animate-fade-in">
            <!-- Aviso de "Ya cumpliste" -->
            <div
              class="bg-green-900/30 border border-green-500/50 p-4 rounded-xl mb-8 flex items-center gap-4 text-green-200"
            >
              <span class="material-symbols-outlined text-3xl"
                >check_circle</span
              >
              <div>
                <h3 class="font-bold text-base">Actividad Completada</h3>
                <p class="text-sm opacity-80">
                  Gracias por tu aporte. Aquí están las respuestas de tus
                  compañeros.
                </p>
              </div>
            </div>

            <!-- Lista de Respuestas (Muro) -->
            <h2
              class="text-white text-2xl font-bold mb-6 border-b border-gray-700 pb-2 flex items-center gap-2"
            >
              <span class="material-symbols-outlined">forum</span>
              Participaciones del Grupo
            </h2>

            <div class="space-y-6">
              <div
                v-if="listaRespuestas.length === 0"
                class="text-center text-gray-400 py-8"
              >
                Aún no hay respuestas de otros estudiantes.
              </div>

              <div
                v-for="(item, index) in listaRespuestas"
                :key="index"
                class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-500 shadow-md hover:bg-[#253042] transition-colors"
              >
                <div class="flex justify-between items-start mb-4">
                  <div class="flex items-center gap-3">
                    <div
                      class="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold"
                    >
                      {{
                        obtenerIniciales(
                          item.nombre,
                          item.apellidos || item.email
                        )
                      }}
                    </div>
                    <div>
                      <span class="text-blue-400 font-bold text-xl">
                        {{
                          item.nombre
                            ? `${item.nombre} ${item.apellidos}`
                            : item.email
                        }}
                      </span>
                      <p class="text-gray-500 text-xs">
                        {{ formatearFecha(item.fecha) }}
                      </p>
                    </div>
                  </div>
                  <span
                    class="bg-blue-900/50 text-blue-200 text-xl px-2 py-1 rounded"
                    >Respuesta #{{ listaRespuestas.length - index }}</span
                  >
                </div>

                <div
                  class="space-y-4 text-gray-300 text-xl pl-2 border-l border-gray-700 ml-4"
                >
                  <p>
                    <strong class="text-blue-200"
                      >1.Similitudes y Diferencias</strong
                    >
                    <br />{{ item.r1 }}
                  </p>
                  <p>
                    <strong class="text-blue-200"
                      >2:¿En qué etapa de la vida aumenta más la densidad
                      mineral</strong
                    >
                    <br />{{ item.r2 }}
                  </p>

                  <details class="text-gray-400 cursor-pointer group">
                    <summary
                      class="hover:text-white list-none flex items-center gap-2 py-2"
                    >
                      <span
                        class="material-symbols-outlined text-sm group-open:rotate-180 transition-transform"
                        >expand_more</span
                      >
                      Ver respuestas completas...
                    </summary>
                    <div
                      class="mt-2 space-y-4 pt-2 border-t border-gray-700/50 animate-fade-in"
                    >
                      <p>
                        <strong class="text-blue-200"
                          >3. ¿En qué etapa de la vida disminuye más la densidad
                          mineral
                        </strong>
                        <br />{{ item.r3 }}
                      </p>
                      <p>
                        <strong class="text-blue-200"
                          >4. ¿Habrá una edad donde la densidad mineral ósea
                          tenga un valor máximo?</strong
                        >
                        <br />{{ item.r4 }}
                      </p>
                      <p>
                        <strong class="text-blue-200"
                          >5. Analiza la siguiente afirmación
                        </strong>
                        <br />{{ item.r5 }}
                      </p>
                      <p>
                        <strong class="text-blue-200"
                          >6. ¿Cómo podemos verificar o encontrar la edad dónde
                          se alcanza el valor óptimo?
                        </strong>
                        <br />{{ item.r6 }}
                      </p>
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
import { ref, onMounted } from "vue";
import Sidebar from "@/views/sidebar.vue";
import foro2 from "@/imagenes/foro2.png";
import Grafica from "@/imagenes/Grafica.png";

// Variables reactivas
const r1 = ref("");
const r2 = ref("");
const r3 = ref("");
const r4 = ref("");
const r5 = ref("");
const r6 = ref("");
const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);

// ESTADO DE CONTROL
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);
const mostrarInformacion = ref(true);

// Al cargar la página, verificamos si el usuario ya hizo la tarea
onMounted(async () => {
  const email = localStorage.getItem("usuario");
  if (email) {
    await verificarEstado(email);
  } else {
    cargandoEstado.value = false; // Si no hay usuario, mostramos formulario (luego fallará al enviar, pidiendo login)
  }
});

async function verificarEstado(email) {
  try {
    // 1. Preguntamos a Python: "¿Este email ya respondió?"
    const res = await fetch(
      `https://proyecto-ingenieria-software-6ccv.onrender.com/verificar_foro2/${email}`
    );
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
  const usuarioEmail = localStorage.getItem("usuario");
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
    const respuesta = await fetch(
      "https://proyecto-ingenieria-software-6ccv.onrender.com/guardar_foro2",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: usuarioEmail,
          r1: r1.value,
          r2: r2.value,
          r3: r3.value,
          r4: r4.value,
          r5: r5.value,
          r6: r6.value,
        }),
      }
    );

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
    const res = await fetch(
      "https://proyecto-ingenieria-software-6ccv.onrender.com/respuestas_foro2"
    );
    listaRespuestas.value = await res.json();
  } catch (error) {
    console.error("Error cargando foro", error);
  }
}

// Utilidades visuales
function obtenerIniciales(nombre, apellidoOEmail) {
  if (nombre) {
    return (
      nombre[0] + (apellidoOEmail ? apellidoOEmail[0] : "")
    ).toUpperCase();
  }
  return apellidoOEmail.substring(0, 2).toUpperCase();
}

function formatearFecha(f) {
  if (!f) return "";
  const fechaStr = f.endsWith("Z") ? f : f + "Z";

  return new Date(fechaStr).toLocaleDateString("es-ES", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    hour12: true,
  });
}
</script>

<script>
import Sidebar from "@/views/sidebar.vue";
export default {
  name: "App",
  components: { Sidebar },
};
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
  border-color: #193cb8;
  box-shadow: 0 0 0 2px rgba(25, 60, 184);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}
</style>
