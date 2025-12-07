<template>
  <div
    class="flex flex-col md:flex-row min-h-screen bg-[#244a76] dark:bg-[rgb(16,22,34)]"
  >
    <!-- Sidebar -->
    <Sidebar class="hidden md:block" />

    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-5xl">
          <!-- TÍTULO -->
          <section class="scroll-mt-20 mb-8">
            <div
              class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-blue-600"
            >
              <h1
                class="text-white text-3xl md:text-3xl font-black text-center"
              >
                Foro 6: Covariación de las magnitudes
              </h1>
            </div>
          </section>

          <!-- CARGANDO -->
          <div v-if="cargandoEstado" class="text-center py-10">
            <p class="text-blue-200 text-xl animate-pulse">
              Cargando actividad...
            </p>
          </div>

          <!-- MODO FORMULARIO: Si no ha participado -->
          <section v-else-if="!usuarioYaParticipo" class="animate-fade-in">
            <!-- SECCIÓN GEOGEBRA -->
            <div
              class="bg-[#161d2b] p-6 rounded-xl shadow-xl mb-8 border border-gray-700"
            >
              <h2
                class="text-white text-lg font-bold mb-4 flex items-center gap-2"
              >
                <span class="material-symbols-outlined text-blue-500"
                  >function</span
                >
                Gráficas Geogebra
              </h2>
              <p class="text-gray-300 mb-6 text-base leading-relaxed">
                Manipula el Applet para observar el comportamiento de la recta
                secante cuando <span class="math-tex">$\Delta x \to 0$</span>.
              </p>

              <!-- Contenedor GeoGebra -->
              <div
                class="bg-white rounded-lg p-1 overflow-hidden flex justify-center mb-6 border-4 border-blue-900/30 shadow-inner"
              >
                <div id="geogebra-container" class="w-full h-[550px]"></div>
              </div>

              <div class="text-center">
                <a
                  href="https://docs.google.com/spreadsheets/d/1Rqp6bml35xrT-5UkAyB3Qlx_c5nKijIqD6apvLbN4y4/edit?usp=sharing"
                  target="_blank"
                  class="inline-flex items-center gap-2 text-sm bg-blue-900/30 text-blue-300 px-4 py-2 rounded-full hover:bg-blue-900/50 transition-colors border border-blue-800"
                >
                  <span class="material-symbols-outlined text-lg"
                    >table_view</span
                  >
                  Abrir Simulador de Google Sheets
                </a>
              </div>
            </div>

            <!-- CUESTIONARIO -->
            <div
              class="bg-[#161d2b] p-8 rounded-xl shadow-xl space-y-10 border border-gray-700"
            >
              <!-- P1 -->
              <div>
                <h3
                  class="text-lg text-white/95 mb-3 font-medium leading-relaxed"
                >
                  1. ¿Qué valores puede tomar la variable
                  <span class="math-tex">$x$</span> (Edad de una persona)? Es
                  decir, ¿Cuál es el dominio real de esta variable? Justifica.
                </h3>
                <p
                  class="text-blue-300/80 text-sm mb-3 italic bg-blue-900/20 p-3 rounded-lg border-l-4 border-blue-500/50"
                >
                  Nota: Observa qué pasa con la pendiente cuando el intervalo
                  <span class="math-tex">$\Delta x$</span> se hace cada vez más
                  pequeño (<span class="math-tex">$\Delta x \to 0$</span>).
                </p>
                <textarea
                  v-model="form.r1"
                  rows="3"
                  placeholder="Escribe tu justificación..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- P2 -->
              <div>
                <h3
                  class="text-lg text-white/95 mb-3 font-medium leading-relaxed"
                >
                  2. Argumenta con ejemplos la siguiente afirmación: Cuando los
                  extremos del intervalo son iguales (<span class="math-tex"
                    >$\Delta x \to 0$</span
                  >), la recta secante se convierte en recta tangente.
                </h3>
                <textarea
                  v-model="form.r2"
                  rows="3"
                  placeholder="Tu argumento..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- P3 -->
              <div>
                <h3
                  class="text-lg text-white/95 mb-4 font-medium leading-relaxed"
                >
                  3. Utiliza el simulador para observar la razón promedio cuando
                  elegimos dos edades muy próximas (<span class="math-tex"
                    >$\Delta x \to 0$</span
                  >). Responde:
                </h3>
                <div class="space-y-3 pl-5 border-l-2 border-blue-700/50 mb-4">
                  <p class="text-gray-300 text-base">
                    <strong class="text-blue-300">a)</strong> ¿DMO y razón
                    instantánea a los 19 años?
                  </p>
                  <p class="text-gray-300 text-base">
                    <strong class="text-blue-300">b)</strong> ¿DMO y razón
                    instantánea a los 31 años?
                  </p>
                  <p class="text-gray-300 text-base">
                    <strong class="text-blue-300">c)</strong> ¿DMO y razón
                    instantánea a los 84 años?
                  </p>
                </div>
                <textarea
                  v-model="form.r3"
                  rows="5"
                  placeholder="a) ...&#10;b) ...&#10;c) ..."
                  class="input-foro font-mono text-sm"
                ></textarea>
              </div>

              <!-- P4 -->
              <div>
                <h3
                  class="text-lg text-white/95 mb-3 font-medium leading-relaxed"
                >
                  4. Manipula el Applet de Geogebra. Verifica que los resultados
                  coinciden. ¿Cuánto vale la pendiente de la recta tangente en
                  el valor máximo? ¿Y en el mínimo?
                </h3>
                <textarea
                  v-model="form.r4"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- P5 -->
              <div>
                <h3
                  class="text-lg text-white/95 mb-3 font-medium leading-relaxed"
                >
                  5. Argumenta con ejemplos: ¿Cómo cambia el valor de la
                  pendiente cuando es un máximo vs cuando es un mínimo?
                </h3>
                <textarea
                  v-model="form.r5"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- P6 (Definición Formal) -->
              <div
                class="bg-blue-900/10 border-l-4 border-blue-500 p-6 rounded-r-xl shadow-sm"
              >
                <h3
                  class="text-white font-bold mb-4 text-lg flex items-center gap-2"
                >
                  <span class="material-symbols-outlined text-blue-400"
                    >menu_book</span
                  >
                  6. Definición Formal de Derivada
                </h3>
                <div
                  class="text-2xl text-center text-blue-200 tracking-wider my-6 bg-[#0f172a] p-6 rounded-lg border border-blue-900/50 shadow-inner overflow-x-auto math-tex"
                >
                  $$ f'(x) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) -
                  f(x)}{\Delta x} $$
                </div>
                <label class="block text-gray-400 text-sm mb-2 font-medium"
                  >Tus notas sobre esta definición (Opcional):</label
                >
                <textarea
                  v-model="form.r6"
                  rows="2"
                  class="input-foro"
                  placeholder="Escribe aquí..."
                ></textarea>
              </div>

              <!-- P7 -->
              <div>
                <h3
                  class="text-lg text-white/95 mb-4 font-medium leading-relaxed"
                >
                  7. Dada la función que describe el comportamiento de la DMO:
                </h3>

                <div
                  class="bg-[#0f172a] p-4 rounded-lg border border-gray-600 mb-5 text-xl text-center text-blue-300 tracking-wide shadow-md math-tex"
                >
                  $$ DMO(x) = -0.0001x^2 + 0.0075x + 0.768 $$
                </div>

                <div
                  class="mb-4 text-base text-gray-300 pl-4 border-l-2 border-gray-600"
                >
                  <p class="mb-2">
                    <strong>a)</strong> Obtén la edad del óptimo usando la
                    definición formal de derivada.
                  </p>
                  <p>
                    <strong>b)</strong> Lista los pasos que se deben realizar
                    como si estuvieras dando una receta.
                  </p>
                </div>
                <textarea
                  v-model="form.r7"
                  rows="6"
                  placeholder="Desarrollo y pasos..."
                  class="input-foro font-mono text-sm"
                ></textarea>
              </div>

              <!-- P8 -->
              <div>
                <h3
                  class="text-lg text-white/95 mb-3 font-medium leading-relaxed"
                >
                  8. Siguiendo los pasos descritos anteriormente, obtén la edad
                  en que se obtiene la DMO óptima para la cadera de los hombres
                  dados los datos.
                </h3>
                <textarea
                  v-model="form.r8"
                  rows="3"
                  placeholder="Tu respuesta..."
                  class="input-foro"
                ></textarea>
              </div>

              <!-- BOTÓN DE ENVÍO  -->
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
                  @click="enviar"
                  :disabled="enviando"
                  class="bg-blue-600 hover:bg-indigo-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all active:scale-95 disabled:opacity-50 flex items-center gap-2"
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

          <!-- si ya participo -->
          <section v-else class="animate-fade-in">
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

            <!-- MURO DE RESPUESTAS -->
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
                class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-600 shadow-md"
              >
                <div class="flex justify-between items-start mb-4">
                  <div class="flex items-center gap-3">
                    <div
                      class="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold"
                    >
                      {{ obtenerIniciales(item.nombre, item.email) }}
                    </div>
                    <div>
                      <span class="text-indigo-400 font-bold text-base">
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
                    class="bg-indigo-900/50 text-indigo-200 text-xs px-2 py-1 rounded"
                    >#{{ listaRespuestas.length - index }}</span
                  >
                </div>

                <div
                  class="space-y-5 text-gray-300 text-base pl-6 border-l-2 border-gray-700/50"
                >
                  <p>
                    <strong class="text-blue-200 block mb-2"
                      >1. Dominio:</strong
                    >
                    {{ item.r1 }}
                  </p>

                  <details class="group text-sm text-gray-400">
                    <summary
                      class="cursor-pointer hover:text-white mt-4 flex items-center gap-2 py-3 px-4 bg-gray-800/50 rounded-lg transition-colors"
                    >
                      <span
                        class="material-symbols-outlined text-lg group-open:rotate-180 transition-transform"
                        >expand_more</span
                      >
                      Ver todo
                    </summary>
                    <div class="pt-6 space-y-6 mt-4 px-2">
                      <p>
                        <strong class="text-blue-200">2. Argumento:</strong>
                        {{ item.r2 }}
                      </p>
                      <pre
                        class="bg-gray-900/30 p-2 rounded whitespace-pre-wrap font-sans"
                        >{{ item.r3 }}</pre
                      >
                      <p>
                        <strong class="text-blue-200">4. GeoGebra:</strong>
                        {{ item.r4 }}
                      </p>
                      <p>
                        <strong class="text-blue-200">5. Pendientes:</strong>
                        {{ item.r5 }}
                      </p>
                      <p>
                        <strong class="text-blue-200">6. Notas:</strong>
                        {{ item.r6 }}
                      </p>
                      <pre
                        class="bg-gray-900/30 p-2 rounded whitespace-pre-wrap font-sans"
                        >{{ item.r7 }}</pre
                      >
                      <p>
                        <strong class="text-blue-200">8. Hombres:</strong>
                        {{ item.r8 }}
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
import { ref, reactive, onMounted, nextTick } from "vue";
import Sidebar from "@/views/sidebar.vue";

const API_URL = "https://proyecto-ingenieria-software-6ccv.onrender.com";

const form = reactive({
  r1: "",
  r2: "",
  r3: "",
  r4: "",
  r5: "",
  r6: "",
  r7: "",
  r8: "",
});
const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);

onMounted(async () => {
  const email = localStorage.getItem("usuario");
  if (email) {
    try {
      const res = await fetch(`${API_URL}/verificar_foro6/${email}`);
      const datos = await res.json();
      if (datos.participo) {
        usuarioYaParticipo.value = true;
        await cargarForo();
      }
    } catch (e) {
      console.error(e);
    }
  }

  cargandoEstado.value = false;

  await nextTick();

  if (window.MathJax) window.MathJax.typesetPromise();

  if (!usuarioYaParticipo.value) {
    cargarGeoGebra();
  }
});

function cargarGeoGebra() {
  if (
    document.querySelector(
      'script[src="https://www.geogebra.org/apps/deployggb.js"]'
    )
  ) {
    renderApplet();
    return;
  }

  const script = document.createElement("script");
  script.src = "https://www.geogebra.org/apps/deployggb.js";
  script.onload = renderApplet; // Al cargar, inyecta
  document.head.appendChild(script);
}

function renderApplet() {
  const params = {
    appName: "classic",
    material_id: "au3jr5af",
    width: 1100,
    height: 550,
    showToolBar: true,
    showAlgebraInput: false,
    showMenuBar: false,
    borderColor: "#3b82f6",
  };

  const container = document.getElementById("geogebra-container");
  if (container && window.GGBApplet) {
    const applet = new window.GGBApplet(params, true);
    applet.inject("geogebra-container");
  } else {
    console.warn("Contenedor GeoGebra no encontrado. Intentando de nuevo...");

    setTimeout(renderApplet, 500);
  }
}

async function enviar() {
  const email = localStorage.getItem("usuario");
  if (!email) return alert("Inicia sesión primero");

  if (!form.r1) {
    mensaje.value = "Por favor responde al menos la primera pregunta.";
    tipoMensaje.value = "error";
    return;
  }

  enviando.value = true;
  mensaje.value = "Guardando...";

  try {
    const res = await fetch(
      `https://proyecto-ingenieria-software-6ccv.onrender.com/guardar_foro6`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, ...form }),
      }
    );
    const datos = await res.json();
    if (datos.exito) {
      usuarioYaParticipo.value = true;
      await cargarForo();
    } else {
      mensaje.value = "Error: " + datos.mensaje;
      tipoMensaje.value = "error";
    }
  } catch (e) {
    mensaje.value = "Error de conexión";
    tipoMensaje.value = "error";
  } finally {
    enviando.value = false;
  }
}

async function cargarForo() {
  try {
    const res = await fetch(
      `https://proyecto-ingenieria-software-6ccv.onrender.com/respuestas_foro6`
    );
    listaRespuestas.value = await res.json();
    await nextTick();
    if (window.MathJax) window.MathJax.typesetPromise();
  } catch (e) {
    console.error(e);
  }
}

function obtenerIniciales(n, e) {
  if (n) return n[0].toUpperCase();
  return e ? e.substring(0, 2).toUpperCase() : "?";
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

<style scoped>
.input-foro {
  width: 100%;
  padding: 16px;
  border-radius: 12px;
  background-color: #1e293b;
  border: 1px solid #475569;
  color: #f1f5f9;
  resize: vertical;
  transition: all 0.3s ease;
  font-size: 1rem;
  line-height: 1.6;
}
.input-foro:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
}
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
}
</style>
