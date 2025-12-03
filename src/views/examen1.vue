<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <!-- Foro preguntas -->
    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12 min-h-screen">
        <div class="mx-auto max-w-5xl">
          <section class="scroll-mt-20" id="introduction">
            <div class="@container">
              <div
                class="flex flex-col gap-6 py-10 @[480px]:gap-8 @[864px]:flex-row bg-[#161d2b] rounded-2xl p-8 shadow-xl ring-1 ring-white/10"
              >
                <div
                  class="flex flex-col gap-6 @[480px]:min-w-[400px] @[480px]:gap-8 @[864px]:justify-center"
                >
                  <div class="flex flex-col gap-2 text-left">
                    <h1
                      class="text-white text-2xl @[480px]:text-3xl font-semibold leading-tight tracking-tight"
                    >
                      E1. Evalúa tu comprensión de la Situación 1: Densidad
                      Mineral Ósea y la Edad
                    </h1>
                    <p class="text-white/80 text-lg @[480px]:text-xl mt-7">
                      Evaluación de la comprensión de la Situación 1 planteada
                      sobre la Densidad Mineral Ósea y la Edad.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </section>
            <div v-if="cargandoEstado" class="text-center py-10">
              <p class="text-white text-xl animate-pulse">Verificando tu participación...</p>
            </div>

            <div v-else-if="usuarioYaParticipo" class="mt-8 animate-fade-in">
              <div class="bg-green-900/30 border border-green-500/50 p-4 rounded-xl mb-8 flex items-center gap-4 text-green-200">
                <span class="material-symbols-outlined text-3xl">check_circle</span>
                <div>
                  <h3 class="font-bold text-xl">Examen Terminado</h3>
                  <p class="text-base opacity-80">Ya has enviado tus respuestas.</p>
                </div>
              </div>

              <h2 class="text-white text-xl font-bold mb-6 border-b border-gray-700 pb-2 flex items-center gap-2">
                <span class="material-symbols-outlined">analytics</span>
                Resultados del Grupo
              </h2>
              
              <div class="space-y-6">
                <div v-if="listaRespuestas.length === 0" class="text-center text-gray-400 py-8">
                  Aún no hay respuestas registradas.
                </div>
                <div v-for="(item, index) in listaRespuestas" :key="index" class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-500 shadow-md">
                  <div class="flex justify-between items-start mb-4">
                    <div class="flex items-center gap-3">
                      <div class="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">
                        {{ obtenerIniciales(item.nombre, item.apellidos) }}
                      </div>
                      <div>
                        <span class="text-blue-400 font-bold text-base">
                          {{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}
                        </span>
                        <p class="text-gray-500 text-xs">{{ formatearFecha(item.fecha) }}</p>
                      </div>
                    </div>
                    <span class="bg-blue-900/50 text-blue-200 text-sm px-2 py-1 rounded">Puntaje: {{ item.r6 }}</span>
                  </div>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-gray-300 mt-4">
                    <div class="bg-white/5 p-3 rounded">
                      <span class="text-blue-300 text-sm block">Pregunta 1</span>
                      {{ item.r1 }}
                    </div>
                    <div class="bg-white/5 p-3 rounded">
                      <span class="text-blue-300 text-sm block">Pregunta 2</span>
                      {{ item.r2 }}
                    </div>
                    <div class="bg-white/5 p-3 rounded">
                      <span class="text-blue-300 text-sm block">Pregunta 3</span>
                      {{ item.r3 }}
                    </div>
                    <div class="bg-white/5 p-3 rounded">
                      <span class="text-blue-300 text-sm block">Juego Oración</span>
                      {{ item.r4 }}
                    </div>
                    <div class="bg-white/5 p-3 rounded">
                      <span class="text-blue-300 text-sm block">Juego Parejas</span>
                      {{ item.r5 }}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div v-else>
              <section class="scroll-mt-20" id="rules">
            <h2
              class="text-white text-xl sm:text-2xl  leading-tight tracking-[-0.015em] px-4 pb-1 pt-10"
            >
              Analiza y responde el siguiente cuestionario
            </h2>

            <!-- Progress bar -->
            <div class="px-4 mt-4" v-if="faseActual === 'quiz'">
              <div class="h-2 w-full rounded-full bg-white/10 overflow-hidden">
                <div
                  class="h-full bg-[#2c5a8f] transition-all duration-500"
                  :style="{
                    width:
                      (quizFinalizado
                        ? 100
                        : ((preguntaActual + 1) / preguntas.length) * 100) +
                      '%',
                  }"
                />
              </div>
              <div class="mt-2 text-white/70 text-sm">
                Pregunta
                {{ quizFinalizado ? preguntas.length : preguntaActual + 1 }} de
                {{ preguntas.length }}
              </div>
            </div>
          </section>

          <div class="text-white text-base">
            <!-- FASE 0: QUIZ -->
            <div class="mt-10" v-if="!quizFinalizado">
              <div
                class="bg-[#161d2b] rounded-2xl p-6 sm:p-8 shadow-lg ring-1 ring-white/10"
              >
                <h2 class="text-2xl sm:text-xl font-semibold leading-snug">
                  {{ preguntas[preguntaActual].texto }}
                  <img
                    v-if="preguntaActual === 2"
                    src="/src/imagenes/EXAMEN.png"
                    alt="Gráfico de Densidad Mineral Ósea"
                    class="w-1/2 mx-auto p-1"
                  />
                </h2>

                <div class="mt-8 space-y-3">
                  <div
                    v-for="op in preguntas[preguntaActual].opciones"
                    :key="op"
                    class="group rounded-xl border border-white/10 hover:border-[#2c5a8f] bg-white/5 hover:bg-white/10 transition-colors duration-200"
                  >
                    <label class="flex items-start gap-3 p-4 cursor-pointer">
                      <input
                        type="radio"
                        class="mt-1 h-4 w-4 text-[#2c5a8f] focus:ring-[#2c5a8f] border-white/20 bg-transparent"
                        v-model="respuestaUsuario"
                        :value="op"
                      />
                      <span class="text-base sm:text-lg">{{ op }}</span>
                    </label>
                  </div>
                </div>

                <button
                  class="inline-flex items-center justify-center bg-[#2c5a8f] hover:bg-[#2b4f7b] text-white font-medium rounded-xl px-6 sm:px-8 py-3 sm:py-3.5 mt-6 transition duration-300 shadow-md"
                  type="button"
                  @click="
                    respuestaUsuario === null || respuestaUsuario === ''
                      ? alert('No se seleccionó ninguna respuesta')
                      : enviarRespuesta()
                  "
                >
                  Enviar
                </button>
              </div>
            </div>

            <!-- FASE INTERMEDIA: RESULTADO QUIZ -->
            <div v-if="quizFinalizado && faseActual === 'quiz'" class="mt-10">
              <div
                class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10 text-center"
              >
                <h2 class="text-white text-3xl font-bold">
                  Respuestas Completadas
                </h2>
                <p class="mt-4 text-xl text-white/80">
                  Iniciar juego de Foro 2
                </p>
                <div class="mt-8">
                  <button
                    @click="avanzarAJuegos"
                    class="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-full text-xl transition-transform hover:scale-105 shadow-lg"
                  >
                    Continuar a Juegos
                  </button>
                </div>
              </div>
            </div>

            <!-- FASE 1: JUEGO ORDENAR ORACIÓN -->
            <div v-if="faseActual === 'juego1'" class="mt-10">
              <div
                class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10"
              >
                <h2 class="text-2xl font-bold mb-4">Ordena la frase</h2>
                <p class="text-white/70 mb-8">
                  Escribe la oracion de la manera correcta
                </p>

                <!-- Zona de respuesta -->
                <div
                  class="min-h-[80px] border-b-2 border-white/20 mb-8 flex flex-wrap gap-2 p-4 bg-white/5 rounded-t-xl"
                >
                  <button
                    v-for="palabra in oracionUsuario"
                    :key="palabra"
                    @click="moverPalabra(palabra, 'oracion')"
                    class="bg-[#2c5a8f] text-white px-4 py-2 rounded-lg font-medium hover:bg-[#3d6ca3] transition-all animate-in fade-in zoom-in duration-200"
                    :disabled="juego1Completado"
                  >
                    {{ palabra }}
                  </button>
                </div>

                <!-- Banco de palabras -->
                <div class="flex flex-wrap gap-3 justify-center mb-8">
                  <button
                    v-for="palabra in palabrasDesordenadas"
                    :key="palabra"
                    @click="moverPalabra(palabra, 'banco')"
                    class="bg-white/10 border border-white/20 text-white px-4 py-2 rounded-lg font-medium hover:bg-white/20 transition-all"
                    :disabled="juego1Completado"
                  >
                    {{ palabra }}
                  </button>
                </div>

                <!-- Feedback y Botón -->
                <div
                  v-if="juego1Completado"
                  class="text-center animate-in slide-in-from-bottom-4"
                >
                  <div
                    v-if="juego1Correcto"
                    class="text-green-400 text-xl font-bold mb-4"
                  >
                    Respuesta correcta
                  </div>
                  <div v-else class="text-red-400 text-xl font-bold mb-4">
                    La respuesta correcta era: "{{ oracionCorrecta.join(" ") }}"
                  </div>
                  <button
                    @click="siguienteJuego"
                    class="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-full transition-transform hover:scale-105"
                  >
                    Siguiente Juego
                  </button>
                </div>
                <div v-else class="text-center">
                  <button
                    @click="verificarOracion"
                    class="bg-[#2c5a8f] hover:bg-[#2b4f7b] text-white font-bold py-3 px-8 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed"
                    :disabled="oracionUsuario.length === 0"
                  >
                    Comprobar
                  </button>
                </div>
              </div>
            </div>

            <!-- FASE 2: JUEGO PAREJAS -->
            <div v-if="faseActual === 'juego2'" class="mt-10">
              <div
                class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10"
              >
                <h2 class="text-2xl font-bold mb-4">Encuentra la pareja</h2>
                <p class="text-white/70 mb-8">
                  Segun el foro anterior encuntre las parejas
                </p>

                <div class="relative">
                  <!-- Progress Bar -->
                  <div class="mb-6">
                    <div class="flex justify-between items-center mb-2">
                      <span class="text-xl font-medium text-white/70"
                        >Progreso</span
                      >
                      <span class="text-xl font-medium text-white/70"
                        >{{ parejasEncontradas }} / {{ parejas.length }}</span
                      >
                    </div>
                    <div class="w-full bg-white/10 rounded-full h-2.5">
                      <div
                        class="bg-blue-300 h-2.5 rounded-full transition-all duration-500"
                        :style="{
                          width: `${
                            (parejasEncontradas / parejas.length) * 100
                          }%`,
                        }"
                      ></div>
                    </div>
                  </div>

                  <!-- Game Grid -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Términos Column -->
                    <div class="space-y-4">
                      <h3
                        class="text-lg font-semibold text-white/80 text-center bg-[#1e293b] py-2 rounded-lg"
                      >
                        Términos
                      </h3>
                      <div class="grid grid-cols-1 gap-3">
                        <button
                          v-for="item in terminos"
                          :key="'term-' + item.id"
                          @click="seleccionarItem(item)"
                          class="w-full p-4 rounded-xl transition-all duration-300 text-left relative overflow-hidden group"
                          :class="{
                            'bg-green-400/50 ': item.matched,

                            ' border-5 border-blue-500/10 hover:border-blue-500/50 hover:bg-blue-500/10':
                              !item.matched && seleccionActual !== item,
                            'bg-blue-500/20 border-2 border-blue-500 scale-[1.02] shadow-lg ':
                              seleccionActual === item,
                            'cursor-not-allowed': item.matched,
                            'transform hover:-translate-x-0.5': !item.matched,
                          }"
                          :disabled="item.matched"
                        >
                          <div class="flex items-center">
                            <span class="text-xl mr-3 text-blue-400">
                              <svg
                                v-if="!item.matched"
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                              >
                                <path
                                  stroke-linecap="round"
                                  stroke-linejoin="round"
                                  stroke-width="2"
                                  d="M9 5l7 7-7 7"
                                />
                              </svg>
                              <svg
                                v-else
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-green-500"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                              >
                                <path
                                  stroke-linecap="round"
                                  stroke-linejoin="round"
                                  stroke-width="2"
                                  d="M5 13l4 4L19 7"
                                />
                              </svg>
                            </span>
                            <span class="text-white/90">{{ item.text }}</span>
                          </div>
                        </button>
                      </div>
                    </div>

                    <!-- Definiciones Column -->
                    <div class="space-y-4">
                      <h3
                        class="text-lg font-semibold text-white/80 text-center bg-[#1e293b] py-2 rounded-lg"
                      >
                        Definiciones
                      </h3>
                      <div class="grid grid-cols-1 gap-3">
                        <button
                          v-for="item in definiciones"
                          :key="'def-' + item.id"
                          @click="seleccionarItem(item)"
                          class="w-full p-4 rounded-xl transition-all duration-300 text-left relative overflow-hidden group"
                          :class="{
                            'bg-green-400/50 ': item.matched,

                            ' border-5 border-blue-500/10 hover:border-blue-500/50 hover:bg-blue-500/10':
                              !item.matched && seleccionActual !== item,
                            'bg-blue-500/20 border-2 border-blue-500 scale-[1.02] shadow-lg shadow-blue-500/20':
                              seleccionActual === item,
                            'cursor-not-allowed': item.matched,
                            'transform hover:-translate-x-0.5': !item.matched,
                          }"
                          :disabled="item.matched"
                        >
                          <p class="text-white/90">
                            {{ item.text }}
                          </p>
                          <div
                            v-if="item.matched"
                            class="absolute right-4 top-1/2 -translate-y-1/2 text-green-500"
                          >
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              class="h-5 w-5"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M5 13l4 4L19 7"
                              />
                            </svg>
                          </div>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <div
                  v-if="parejasEncontradas === parejas.length"
                  class="mt-8 text-center animate-in zoom-in"
                >
                  <div class="text-green-400 text-xl font-bold mb-4">
                    Correcto
                  </div>
                  <button
                    @click="finalizarTodo"
                    class="bg-green-900 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-xl transition-transform hover:scale-120"
                  >
                    Ver Calificacion Final
                  </button>
                </div>
              </div>
            </div>

            <!-- FASE FINAL: RESULTADOS TOTALES -->
            <div v-if="faseActual === 'final'" class="mt-10">
              <div
                class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10 text-center"
              >
                <h2 class="text-white text-3xl font-bold">Examen Terminado</h2>
                <p class="mt-4 text-2xl text-white/90">
                  Puntaje
                  <span class="font-semibold text-blue-200">{{
                    puntajeTotal
                  }}</span>
                  / {{ totalPosible }}
                </p>

                <div
                  class="mt-8 grid grid-cols-1 sm:grid-cols-3 gap-4 text-left max-w-2xl mx-auto"
                >
                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-sm text-white/60">Preguntas Abiertas</div>
                    <div class="text-xl font-bold">
                      {{ puntajeQuiz }} / {{ preguntas.length }}
                    </div>
                  </div>
                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-sm text-white/60">Acomodar la Oracion</div>
                    <div class="text-xl font-bold">
                      {{ juego1Correcto ? 1 : 0 }} / 1
                    </div>
                  </div>
                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-sm text-white/60">Encontrar Parejas</div>
                    <div class="text-xl font-bold">
                      {{ parejasEncontradas }} / {{ parejas.length }}
                    </div>
                  </div>
                </div>

                <div
                  class="mt-8 h-4 w-full rounded-full bg-white/10 overflow-hidden"
                >
                  <div
                    class="h-full bg-green-500 transition-all duration-1000"
                    :style="{
                      width: (puntajeTotal / totalPosible) * 100 + '%',
                    }"
                  />
                </div>

                <div class="mt-10 flex flex-col items-center gap-4">
                  <button
                    @click="enviarExamen"
                    :disabled="enviando"
                    class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-xl shadow-lg transition-transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                  >
                    <span v-if="enviando" class="material-symbols-outlined animate-spin">refresh</span>
                    {{ enviando ? "Enviando..." : "Enviar Resultados" }}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
        </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import Sidebar from "@/views/sidebar.vue";
import axios from "axios";

const preguntas = ref([
  {
    texto:
      "La Densidad Mineral Ósea (DMO) que mide el volumen del esqueleto humano, si lo comparamos entre el esqueleto femenino y masculino, encontramos que:",
    opciones: [
      "A) Son diferentes solo en la vejez.",
      "B) Son diferentes desde el nacimiento.",
      "C) Son iguales en la niñez y se empiezan a diferenciar a partir de la adolescencia.",
      "D) Son iguales, no hay diferencia.",
    ],
    correcta:
      "C) Son iguales en la niñez y se empiezan a diferenciar a partir de la adolescencia.",
  },
  {
    texto:
      "¿Cómo sabemos que la densidad mineral ósea (DMO) tiene un valor máximo a lo largo de la vida?",
    opciones: [
      "A) Porque va aumentando y disminuyendo continuamente durante toda la vida, entonces tiene valores máximos y mínimos.",
      "B) Porque aumenta a medida que se va formando el esqueleto y cuando está completo, ya no aumenta ni disminuye.",
      "C) Porque siempre aumenta durante toda la vida.",
      "D) Porque aumenta conforme crecemos pero luego empieza a disminuir conforme se envejece.",
    ],
    correcta:
      "D) Porque aumenta conforme crecemos pero luego empieza a disminuir conforme se envejece.",
  },
  {
    texto:
      "De las siguientes figuras, selecciona la que representa mejor cómo varía la Densidad Mineral Ósea a lo largo de la vida:",
    opciones: ["A", "B", "C", "D"],
    correcta: "D",
  },
]);

const preguntaActual = ref(0);
const respuestaUsuario = ref(null);
const puntajeQuiz = ref(0);
const quizFinalizado = ref(false);

// --- GAME STATE ---
const faseActual = ref("quiz");

const oracionCorrecta = [
  "En",
  "general",
  "la DMO",
  "de la",
  "cadera",
  "es mayor",
  "en el hombre",
  "que",
  "en",
  "las mujeres",
];

const palabrasDesordenadas = ref(
  [...oracionCorrecta].sort(() => Math.random() - 0.5)
);
const oracionUsuario = ref([]);
const juego1Completado = ref(false);
const juego1Correcto = ref(false);

// Juego 2: Parejas (Matching)
const parejas = [
  {
    id: 1,
    termino: "Adolescencia y los primeros años de adultez",
    definicion: "Etapa en la que aumenta mas la DMO",
  },
  {
    id: 2,
    termino: "25 y 35 años",
    definicion: "Rango de edad en el que la DMO llega su valor maximo ",
  },
  {
    id: 3,
    termino: "1.025",
    definicion: "Valor maximo de la DMO en el hombre",
  },
  {
    id: 4,
    termino: ".938",
    definicion: "Valor maximo de la DMO en la mujer",
  },
];
// Mezclamos para la visualización
const terminos = ref(
  parejas.map((p) => ({
    id: p.id,
    text: p.termino,
    type: "term",
    matched: false,
  }))
);
const definiciones = ref(
  parejas
    .map((p) => ({ id: p.id, text: p.definicion, type: "def", matched: false }))
    .sort(() => Math.random() - 0.5)
  // parejas.map((p) => ({ id: p.id, text: p.definicion, type: "def", matched: false }))
);

const seleccionActual = ref(null);
const parejasEncontradas = ref(0);

// --- BACKEND INTEGRATION ---
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const enviando = ref(false);
const listaRespuestas = ref([]);
const respuestasGuardadas = ref({
  r1: "",
  r2: "",
  r3: "",
  r4: "",
  r5: "",
  r6: "",
});

onMounted(() => {
  verificarEstado();
});

async function verificarEstado() {
  const email = localStorage.getItem("email");
  if (!email) {
    cargandoEstado.value = false;
    return;
  }

  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/verificar_examen1/${email}`
    );
    if (response.data.participo) {
      usuarioYaParticipo.value = true;
      await cargarRespuestas();
    }
  } catch (error) {
    console.error("Error verificando estado:", error);
  } finally {
    cargandoEstado.value = false;
  }
}

async function cargarRespuestas() {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/respuestas_examen1"
    );
    listaRespuestas.value = response.data;
  } catch (error) {
    console.error("Error cargando respuestas:", error);
  }
}

function enviarRespuesta() {
  const pregunta = preguntas.value[preguntaActual.value];

  // Guardar respuesta
  const key = `r${preguntaActual.value + 1}`;
  respuestasGuardadas.value[key] = respuestaUsuario.value;

  if (respuestaUsuario.value === pregunta.correcta) {
    puntajeQuiz.value++;
  }
  respuestaUsuario.value = null;
  preguntaActual.value++;

  if (preguntaActual.value === preguntas.value.length) {
    quizFinalizado.value = true;
    // No cambiamos fase inmediatamente, dejamos que el usuario vea su score parcial o avance
  }
}

function avanzarAJuegos() {
  faseActual.value = "juego1";
}

// Logic Juego 1
function moverPalabra(palabra, origen) {
  if (juego1Completado.value) return;

  if (origen === "banco") {
    // Del banco a la oración
    const index = palabrasDesordenadas.value.indexOf(palabra);
    if (index > -1) {
      palabrasDesordenadas.value.splice(index, 1);
      oracionUsuario.value.push(palabra);
    }
  } else {
    // De la oración al banco
    const index = oracionUsuario.value.indexOf(palabra);
    if (index > -1) {
      oracionUsuario.value.splice(index, 1);
      palabrasDesordenadas.value.push(palabra);
    }
  }
}

function verificarOracion() {
  const oracionStr = oracionUsuario.value.join(" ");
  const correctaStr = oracionCorrecta.join(" ");
  const esCorrecto = oracionStr === correctaStr;

  juego1Correcto.value = esCorrecto;
  juego1Completado.value = true;

  // Guardar resultado juego 1
  respuestasGuardadas.value.r4 = esCorrecto ? "Correcto" : "Incorrecto";
}

function siguienteJuego() {
  faseActual.value = "juego2";
}

// Lógica mejorada para el juego de parejas
const mostrarFeedback = ref(false);
const feedbackMensaje = ref("");
const feedbackTipo = ref("");

function seleccionarItem(item) {
  if (item.matched) return;

  // Si ya hay una selección del mismo tipo, no hacer nada
  if (seleccionActual.value?.type === item.type) return;

  // Agregar clase de animación
  item.animating = true;

  if (!seleccionActual.value) {
    // Primer click
    seleccionActual.value = item;
    return;
  }

  // Segundo click - verificar match
  const primerItem = seleccionActual.value;

  if (primerItem.id === item.id && primerItem.type !== item.type) {
    // Match correcto
    primerItem.matched = true;
    item.matched = true;

    // Actualizar en las listas originales
    actualizarEstadoItem(primerItem, true);
    actualizarEstadoItem(item, true);

    parejasEncontradas.value++;
    mostrarFeedbackPositivo();
  } else {
    // Match incorrecto
    mostrarFeedbackNegativo();

    // Voltear las cartas después de un breve retraso
    setTimeout(() => {
      actualizarEstadoItem(primerItem, false);
      actualizarEstadoItem(item, false);
      seleccionActual.value = null;
    }, 1000);
    return;
  }

  // Reiniciar selección actual
  seleccionActual.value = null;
}

function actualizarEstadoItem(item, estado) {
  const lista = item.type === "term" ? terminos.value : definiciones.value;
  const index = lista.findIndex((i) => i.id === item.id);
  if (index >= 0) {
    lista[index].matched = estado;
    lista[index].animating = estado;
  }
}

function mostrarFeedbackPositivo() {
  const mensajes = ["¡Correcto!", "¡Muy bien!", "¡Excelente!", "¡Perfecto!"];
  feedbackMensaje.value = mensajes[Math.floor(Math.random() * mensajes.length)];
  feedbackTipo.value = "exito";
  mostrarFeedback.value = true;

  setTimeout(() => {
    mostrarFeedback.value = false;
  }, 1500);
}

function mostrarFeedbackNegativo() {
  const mensajes = [
    "Sigue intentando",
    "Casi, ¡inténtalo de nuevo!",
    "No es la pareja correcta",
    "Otra oportunidad",
  ];
  feedbackMensaje.value = mensajes[Math.floor(Math.random() * mensajes.length)];
  feedbackTipo.value = "error";
  mostrarFeedback.value = true;

  setTimeout(() => {
    mostrarFeedback.value = false;
  }, 1500);
}

function finalizarTodo() {
  faseActual.value = "final";
  // Guardar resultados finales
  respuestasGuardadas.value.r5 = `${parejasEncontradas.value}/${parejas.length}`;
  respuestasGuardadas.value.r6 = puntajeTotal.value.toString();
}

async function enviarExamen() {
  const email = localStorage.getItem("email");
  if (!email) {
    alert("No se encontró el email del usuario");
    return;
  }

  enviando.value = true;
  try {
    const payload = {
      email: email,
      ...respuestasGuardadas.value,
    };

    const response = await axios.post(
      "http://127.0.0.1:8000/guardar_examen1",
      payload
    );

    if (response.data.exito) {
      usuarioYaParticipo.value = true;
      await cargarRespuestas();
    } else {
      alert("Error al guardar: " + response.data.mensaje);
    }
  } catch (error) {
    console.error("Error enviando examen:", error);
    alert("Error de conexión");
  } finally {
    enviando.value = false;
  }
}



function obtenerIniciales(nombre, apellido) {
  if (!nombre) return "?";
  return (nombre[0] + (apellido ? apellido[0] : "")).toUpperCase();
}

function formatearFecha(fecha) {
  if (!fecha) return "";
  return (
    new Date(fecha).toLocaleDateString() +
    " " +
    new Date(fecha).toLocaleTimeString()
  );
}

const puntajeTotal = computed(() => {
  let p = puntajeQuiz.value;
  if (juego1Correcto.value) p += 1; // 1 punto por la oración
  p += parejasEncontradas.value; // 1 punto por cada pareja (3 total)
  return p;
});

const totalPosible = computed(() => {
  return preguntas.value.length + 1 + parejas.length;
});
</script>
