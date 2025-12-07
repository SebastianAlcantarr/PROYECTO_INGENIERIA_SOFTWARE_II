<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <!-- Contenido Principal -->
    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12 min-h-screen bg-[#244a76] dark:bg-[rgb(16,22,34)]">
        <div class="mx-auto max-w-5xl">

          <!-- Header del Examen -->
          <section class="scroll-mt-20" id="introduction">
            <div class="@container">
              <div class="flex flex-col gap-6 py-10 bg-[#161d2b] rounded-2xl p-8 shadow-xl ring-1 ring-white/10">
                <div class="flex flex-col gap-2 text-left">
                  <h1 class="text-white text-2xl sm:text-3xl font-semibold leading-tight">
                    E1. Evalúa tu comprensión: Densidad Mineral Ósea y Edad
                  </h1>
                  <p class="text-white/80 text-lg mt-4">
                    Evaluación de la comprensión de la Situación 1 planteada sobre la Densidad Mineral Ósea y la Edad.
                  </p>
                </div>
              </div>
            </div>
          </section>

          <!-- ESTADO DE CARGA -->
          <div v-if="cargandoEstado" class="text-center py-10">
            <p class="text-white text-xl animate-pulse">Verificando tu participación...</p>
          </div>

          <!-- SI YA PARTICIPÓ (Resultados) -->
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
                <!-- Grid de respuestas -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-gray-300 mt-4 text-sm">
                  <div class="bg-white/5 p-3 rounded"><strong class="text-blue-300 block">P1:</strong> {{ item.r1 }}</div>
                  <div class="bg-white/5 p-3 rounded"><strong class="text-blue-300 block">P2:</strong> {{ item.r2 }}</div>
                  <div class="bg-white/5 p-3 rounded"><strong class="text-blue-300 block">P3:</strong> {{ item.r3 }}</div>
                  <div class="bg-white/5 p-3 rounded"><strong class="text-blue-300 block">Juego Oración:</strong> {{ item.r4 }}</div>
                  <div class="bg-white/5 p-3 rounded"><strong class="text-blue-300 block">Juego Parejas:</strong> {{ item.r5 }}</div>
                </div>
              </div>
            </div>
          </div>

          <!-- SI NO HA PARTICIPADO (Juego Activo) -->
          <div v-else>
            <section class="scroll-mt-20" id="rules">
              <h2 class="text-white text-xl sm:text-2xl leading-tight px-4 pb-1 pt-10 font-bold">
                Analiza y responde el siguiente cuestionario
              </h2>

              <!-- Progress bar -->
              <div class="px-4 mt-4" v-if="faseActual === 'quiz'">
                <div class="h-2 w-full rounded-full bg-white/10 overflow-hidden">
                  <div class="h-full bg-[#2c5a8f] transition-all duration-500"
                       :style="{ width: (quizFinalizado ? 100 : ((preguntaActual + 1) / preguntas.length) * 100) + '%' }"
                  />
                </div>
                <div class="mt-2 text-white/70 text-sm">
                  Pregunta {{ quizFinalizado ? preguntas.length : preguntaActual + 1 }} de {{ preguntas.length }}
                </div>
              </div>
            </section>

            <div class="text-white text-base pb-20">

              <!-- FASE 0: QUIZ (Primeras 3 preguntas) -->
              <div class="mt-10" v-if="!quizFinalizado">
                <div class="bg-[#161d2b] rounded-2xl p-6 sm:p-8 shadow-lg ring-1 ring-white/10">
                  <h2 class="text-xl sm:text-2xl font-semibold leading-snug mb-6">
                    {{ preguntas[preguntaActual].texto }}
                    <img v-if="preguntaActual === 2" src="/src/imagenes/EXAMEN.png" alt="Gráfico DMO" class="w-full sm:w-2/3 mx-auto mt-4 rounded-lg border border-white/20"/>
                  </h2>

                  <!-- Opciones -->
                  <div class="space-y-3">
                    <div v-for="op in preguntas[preguntaActual].opciones" :key="op"
                         class="group rounded-xl border transition-all duration-200"
                         :class="{
                        'bg-white/5 border-white/10 hover:border-[#2c5a8f]': !mostrandoFeedback,
                        'bg-green-900/30 border-green-500': mostrandoFeedback && op === preguntas[preguntaActual].correcta,
                        'bg-red-900/30 border-red-500': mostrandoFeedback && op === respuestaUsuario && op !== preguntas[preguntaActual].correcta,
                        'opacity-50': mostrandoFeedback && op !== preguntas[preguntaActual].correcta && op !== respuestaUsuario
                      }"
                    >
                      <label class="flex items-start gap-3 p-4 cursor-pointer w-full">
                        <input type="radio" class="mt-1 h-4 w-4 text-[#2c5a8f] bg-transparent focus:ring-0"
                               v-model="respuestaUsuario" :value="op" :disabled="mostrandoFeedback"
                        />
                        <span class="text-base sm:text-lg">{{ op }}</span>
                      </label>
                    </div>
                  </div>

                  <!-- Retroalimentación Inmediata -->
                  <div v-if="mostrandoFeedback" class="mt-6 p-4 rounded-xl animate-fade-in"
                       :class="esRespuestaCorrecta ? 'bg-green-900/20 border border-green-500/30 text-green-200' : 'bg-red-900/20 border border-red-500/30 text-red-200'">
                    <div class="flex items-center gap-3 mb-2">
                      <span class="material-symbols-outlined text-2xl">
                        {{ esRespuestaCorrecta ? 'check_circle' : 'cancel' }}
                      </span>
                      <h3 class="font-bold text-lg">
                        {{ esRespuestaCorrecta ? '¡Correcto!' : 'Respuesta Incorrecta' }}
                      </h3>
                    </div>
                    <p v-if="!esRespuestaCorrecta">
                      La respuesta correcta es: <strong class="underline">{{ preguntas[preguntaActual].correcta }}</strong>
                    </p>
                  </div>

                  <!-- Botones de Acción -->
                  <div class="mt-8">
                    <button v-if="!mostrandoFeedback"
                            @click="verificarRespuesta"
                            class="bg-[#2c5a8f] hover:bg-[#2b4f7b] text-white font-bold py-3 px-8 rounded-xl shadow-lg transition-transform hover:scale-105"
                    >
                      Enviar Respuesta
                    </button>

                    <button v-else
                            @click="siguientePregunta"
                            class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-xl shadow-lg transition-transform hover:scale-105 flex items-center gap-2"
                    >
                      <span>{{ preguntaActual < preguntas.length - 1 ? 'Siguiente Pregunta' : 'Finalizar Quiz' }}</span>
                      <span class="material-symbols-outlined">arrow_forward</span>
                    </button>
                  </div>
                </div>
              </div>

              <!-- FASE INTERMEDIA: RESULTADO QUIZ -->
              <div v-if="quizFinalizado && faseActual === 'quiz'" class="mt-10 animate-in zoom-in duration-300">
                <div class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10 text-center max-w-2xl mx-auto">
                  <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-blue-500/20 mb-6">
                    <span class="material-symbols-outlined text-5xl text-blue-400">quiz</span>
                  </div>
                  <h2 class="text-white text-3xl font-bold mb-2">Quiz Completado</h2>
                  <p class="text-xl text-white/60 mb-8">Obtuviste <span class="text-white font-bold">{{ puntajeQuiz }}</span> de {{ preguntas.length }} aciertos.</p>

                  <button @click="avanzarAJuegos" class="bg-green-600 hover:bg-green-700 text-white font-bold py-4 px-10 rounded-xl text-lg shadow-lg hover:shadow-green-500/20 transition-all w-full sm:w-auto">
                    Continuar a Juegos Didácticos
                  </button>
                </div>
              </div>

              <!-- FASE 1: JUEGO ORDENAR ORACIÓN -->
              <div v-if="faseActual === 'juego1'" class="mt-10">
                <div class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10">
                  <h2 class="text-2xl font-bold mb-4 text-orange-400 flex items-center gap-2">
                    <span class="material-symbols-outlined">format_quote</span> Ordena la frase
                  </h2>
                  <p class="text-white/70 mb-8">Selecciona las palabras en el orden correcto para formar la oración.</p>

                  <!-- Zona de respuesta -->
                  <div class="min-h-[80px] border-2 border-dashed border-white/20 mb-8 flex flex-wrap gap-2 p-4 bg-white/5 rounded-xl transition-colors"
                       :class="{'border-green-500/50 bg-green-500/10': juego1Completado && juego1Correcto, 'border-red-500/50 bg-red-500/10': juego1Completado && !juego1Correcto}">
                    <button v-for="palabra in oracionUsuario" :key="palabra" @click="moverPalabra(palabra, 'oracion')"
                            class="bg-[#2c5a8f] text-white px-4 py-2 rounded-lg font-medium hover:bg-[#3d6ca3] transition-all"
                            :disabled="juego1Completado">
                      {{ palabra }}
                    </button>
                    <span v-if="oracionUsuario.length === 0" class="text-white/30 self-center">Tus palabras aparecerán aquí...</span>
                  </div>

                  <!-- Banco de palabras -->
                  <div class="flex flex-wrap gap-3 justify-center mb-8 p-4 bg-[#0f172a] rounded-xl">
                    <button v-for="palabra in palabrasDesordenadas" :key="palabra" @click="moverPalabra(palabra, 'banco')"
                            class="bg-white/10 border border-white/20 text-white px-4 py-2 rounded-lg font-medium hover:bg-white/20 transition-all hover:-translate-y-1"
                            :disabled="juego1Completado">
                      {{ palabra }}
                    </button>
                  </div>

                  <!-- Feedback y Botón -->
                  <div v-if="juego1Completado" class="text-center animate-in slide-in-from-bottom-4 bg-black/20 p-6 rounded-xl">
                    <div v-if="juego1Correcto" class="text-green-400 text-xl font-bold mb-4 flex items-center justify-center gap-2">
                      <span class="material-symbols-outlined">check_circle</span> ¡Respuesta Correcta!
                    </div>
                    <div v-else class="text-red-400 text-lg font-bold mb-4">
                      <div class="flex items-center justify-center gap-2 mb-2"><span class="material-symbols-outlined">cancel</span> Incorrecto</div>
                      <p class="text-white/70 text-sm font-normal">La correcta era: <br>"{{ oracionCorrecta.join(" ") }}"</p>
                    </div>
                    <button @click="siguienteJuego" class="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-xl transition-all shadow-lg">
                      Siguiente Juego
                    </button>
                  </div>
                  <div v-else class="text-center">
                    <button @click="verificarOracion" class="bg-[#2c5a8f] hover:bg-[#2b4f7b] text-white font-bold py-3 px-10 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed shadow-lg"
                            :disabled="oracionUsuario.length === 0">
                      Comprobar
                    </button>
                  </div>
                </div>
              </div>

              <!-- FASE 2: JUEGO PAREJAS -->
              <div v-if="faseActual === 'juego2'" class="mt-10">
                <div class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10">
                  <h2 class="text-2xl font-bold mb-4 text-purple-400 flex items-center gap-2">
                    <span class="material-symbols-outlined">extension</span> Encuentra la pareja
                  </h2>
                  <p class="text-white/70 mb-8">Relaciona cada término con su definición correcta.</p>

                  <div class="relative">
                    <!-- Progress Bar -->
                    <div class="mb-6">
                      <div class="flex justify-between items-center mb-2 text-sm text-white/70">
                        <span>Progreso</span>
                        <span>{{ parejasEncontradas }} / {{ parejas.length }}</span>
                      </div>
                      <div class="w-full bg-white/10 rounded-full h-2">
                        <div class="bg-purple-500 h-2 rounded-full transition-all duration-500"
                             :style="{ width: `${(parejasEncontradas / parejas.length) * 100}%` }"></div>
                      </div>
                    </div>

                    <!-- Game Grid -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div class="space-y-3">
                        <h3 class="text-sm font-bold text-white/50 uppercase tracking-wider text-center mb-2">Términos</h3>
                        <button v-for="item in terminos" :key="'term-' + item.id" @click="seleccionarItem(item)"
                                class="w-full p-4 rounded-xl transition-all duration-200 text-left relative border border-white/5"
                                :class="{
                            'bg-green-500/20 border-green-500/50 text-green-200': item.matched,
                            'bg-purple-500/20 border-purple-500 text-white scale-[1.02] shadow-lg': !item.matched && seleccionActual === item,
                            'bg-[#1e293b] hover:bg-white/5': !item.matched && seleccionActual !== item,
                            'opacity-50 cursor-not-allowed': item.matched
                          }" :disabled="item.matched">
                          {{ item.text }}
                        </button>
                      </div>

                      <div class="space-y-3">
                        <h3 class="text-sm font-bold text-white/50 uppercase tracking-wider text-center mb-2">Definiciones</h3>
                        <button v-for="item in definiciones" :key="'def-' + item.id" @click="seleccionarItem(item)"
                                class="w-full p-4 rounded-xl transition-all duration-200 text-left relative border border-white/5"
                                :class="{
                            'bg-green-500/20 border-green-500/50 text-green-200': item.matched,
                            'bg-purple-500/20 border-purple-500 text-white scale-[1.02] shadow-lg': !item.matched && seleccionActual === item,
                            'bg-[#1e293b] hover:bg-white/5': !item.matched && seleccionActual !== item,
                            'opacity-50 cursor-not-allowed': item.matched
                          }" :disabled="item.matched">
                          {{ item.text }}
                        </button>
                      </div>
                    </div>
                  </div>

                  <!-- Feedback Flotante -->
                  <div v-if="mostrarFeedback" class="fixed bottom-10 left-1/2 -translate-x-1/2 px-6 py-3 rounded-full shadow-2xl font-bold animate-in fade-in slide-in-from-bottom-4 z-50"
                       :class="feedbackTipo === 'exito' ? 'bg-green-500 text-white' : 'bg-red-500 text-white'">
                    {{ feedbackMensaje }}
                  </div>

                  <div v-if="parejasEncontradas === parejas.length" class="mt-8 text-center animate-in zoom-in">
                    <button @click="finalizarTodo" class="bg-green-600 hover:bg-green-700 text-white font-bold py-4 px-12 rounded-xl shadow-lg transition-transform hover:scale-105">
                      Ver Calificación Final
                    </button>
                  </div>
                </div>
              </div>

              <!-- FASE FINAL: RESULTADOS TOTALES -->
              <div v-if="faseActual === 'final'" class="mt-10 animate-in fade-in duration-500">
                <div class="bg-[#161d2b] rounded-2xl p-8 shadow-2xl ring-1 ring-white/10 text-center max-w-3xl mx-auto border-t-4 border-blue-500">
                  <h2 class="text-white text-3xl font-bold mb-2">Resumen de Actividades</h2>
                  <p class="text-gray-400 mb-8">Has completado todas las secciones del Examen 1.</p>

                  <div class="flex justify-center items-baseline gap-2 mb-8">
                    <span class="text-6xl font-black text-blue-400">{{ puntajeTotal }}</span>
                    <span class="text-2xl text-gray-500">/ {{ totalPosible }} pts</span>
                  </div>

                  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
                    <div class="bg-[#0f172a] p-4 rounded-xl border border-white/5">
                      <div class="text-xs text-gray-400 uppercase tracking-wider mb-1">Cuestionario</div>
                      <div class="text-2xl font-bold text-white">{{ puntajeQuiz }} / {{ preguntas.length }}</div>
                    </div>
                    <div class="bg-[#0f172a] p-4 rounded-xl border border-white/5">
                      <div class="text-xs text-gray-400 uppercase tracking-wider mb-1">Frase</div>
                      <div class="text-2xl font-bold text-white">{{ juego1Correcto ? 1 : 0 }} / 1</div>
                    </div>
                    <div class="bg-[#0f172a] p-4 rounded-xl border border-white/5">
                      <div class="text-xs text-gray-400 uppercase tracking-wider mb-1">Parejas</div>
                      <div class="text-2xl font-bold text-white">{{ parejasEncontradas }} / {{ parejas.length }}</div>
                    </div>
                  </div>

                  <button @click="enviarExamen" :disabled="enviando"
                          class="w-full sm:w-auto bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-12 rounded-xl shadow-lg transition-transform hover:scale-105 disabled:opacity-50 flex items-center justify-center gap-3">
                    <span v-if="enviando" class="material-symbols-outlined animate-spin">refresh</span>
                    {{ enviando ? "Guardando..." : "Guardar y Finalizar" }}
                  </button>
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
import axios from 'axios'; // Asegúrate de tener axios importado si no lo usas global
import Sidebar from "@/views/sidebar.vue";

const preguntas = ref([
  {
    texto: "La Densidad Mineral Ósea (DMO) que mide el volumen del esqueleto humano, si lo comparamos entre el esqueleto femenino y masculino, encontramos que:",
    opciones: [
      "A) Son diferentes solo en la vejez.",
      "B) Son diferentes desde el nacimiento.",
      "C) Son iguales en la niñez y se empiezan a diferenciar a partir de la adolescencia.",
      "D) Son iguales, no hay diferencia.",
    ],
    correcta: "C) Son iguales en la niñez y se empiezan a diferenciar a partir de la adolescencia.",
  },
  {
    texto: "¿Cómo sabemos que la densidad mineral ósea (DMO) tiene un valor máximo a lo largo de la vida?",
    opciones: [
      "A) Porque va aumentando y disminuyendo continuamente durante toda la vida, entonces tiene valores máximos y mínimos.",
      "B) Porque aumenta a medida que se va formando el esqueleto y cuando está completo, ya no aumenta ni disminuye.",
      "C) Porque siempre aumenta durante toda la vida.",
      "D) Porque aumenta conforme crecemos pero luego empieza a disminuir conforme se envejece.",
    ],
    correcta: "D) Porque aumenta conforme crecemos pero luego empieza a disminuir conforme se envejece.",
  },
  {
    texto: "De las siguientes figuras, selecciona la que representa mejor cómo varía la Densidad Mineral Ósea a lo largo de la vida:",
    opciones: ["A", "B", "C", "D"],
    correcta: "D",
  },
]);

const preguntaActual = ref(0);
const respuestaUsuario = ref(null);
const puntajeQuiz = ref(0);
const quizFinalizado = ref(false);

// --- ESTADOS PARA RETROALIMENTACIÓN INMEDIATA ---
const mostrandoFeedback = ref(false);
const esRespuestaCorrecta = ref(false);

const faseActual = ref("quiz");

const oracionCorrecta = ["En", "general", "la DMO", "de la", "cadera", "es mayor", "en el hombre", "que", "en", "las mujeres"];
const palabrasDesordenadas = ref([...oracionCorrecta].sort(() => Math.random() - 0.5));
const oracionUsuario = ref([]);
const juego1Completado = ref(false);
const juego1Correcto = ref(false);

// Juego 2: Parejas
const parejas = [
  { id: 1, termino: "Adolescencia y los primeros años de adultez", definicion: "Etapa en la que aumenta mas la DMO" },
  { id: 2, termino: "25 y 35 años", definicion: "Rango de edad en el que la DMO llega su valor maximo " },
  { id: 3, termino: "1.025", definicion: "Valor maximo de la DMO en el hombre" },
  { id: 4, termino: ".938", definicion: "Valor maximo de la DMO en la mujer" },
];

const terminos = ref(parejas.map((p) => ({ id: p.id, text: p.termino, type: "term", matched: false })));
const definiciones = ref(parejas.map((p) => ({ id: p.id, text: p.definicion, type: "def", matched: false })).sort(() => Math.random() - 0.5));

const seleccionActual = ref(null);
const parejasEncontradas = ref(0);

// --- BACKEND INTEGRATION ---
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const enviando = ref(false);
const listaRespuestas = ref([]);
const respuestasGuardadas = ref({ r1: "", r2: "", r3: "", r4: "", r5: "", r6: "" });

// URL API
const API_URL = "https://proyecto-ingenieria-software-6ccv.onrender.com";

onMounted(() => {
  verificarEstado();
});

async function verificarEstado() {
  const email = localStorage.getItem("usuario"); // Cambié "email" por "usuario" para consistencia con tus otros archivos
  if (!email) {
    cargandoEstado.value = false;
    return;
  }

  try {
    const response = await fetch(`${API_URL}/verificar_examen1/${email}`);
    const data = await response.json();
    if (data.participo) {
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
    const response = await fetch(`${API_URL}/respuestas_examen1`);
    listaRespuestas.value = await response.json();
  } catch (error) {
    console.error("Error cargando respuestas:", error);
  }
}

// --- LÓGICA MODIFICADA PARA RETROALIMENTACIÓN ---
function verificarRespuesta() {
  if (respuestaUsuario.value === null || respuestaUsuario.value === '') {
    alert("Por favor selecciona una respuesta");
    return;
  }

  const pregunta = preguntas.value[preguntaActual.value];

  // Guardamos la respuesta temporalmente
  const key = `r${preguntaActual.value + 1}`;
  respuestasGuardadas.value[key] = respuestaUsuario.value;

  // Verificamos si es correcta
  if (respuestaUsuario.value === pregunta.correcta) {
    esRespuestaCorrecta.value = true;
    puntajeQuiz.value++;
  } else {
    esRespuestaCorrecta.value = false;
  }

  // Activamos el modo feedback
  mostrandoFeedback.value = true;
}

function siguientePregunta() {
  // Reseteamos estados
  mostrandoFeedback.value = false;
  respuestaUsuario.value = null;
  preguntaActual.value++;

  // Si llegamos al final del quiz
  if (preguntaActual.value === preguntas.value.length) {
    quizFinalizado.value = true;
  }
}

function avanzarAJuegos() {
  faseActual.value = "juego1";
}

// Logic Juego 1 (Oración)
function moverPalabra(palabra, origen) {
  if (juego1Completado.value) return;

  if (origen === "banco") {
    const index = palabrasDesordenadas.value.indexOf(palabra);
    if (index > -1) {
      palabrasDesordenadas.value.splice(index, 1);
      oracionUsuario.value.push(palabra);
    }
  } else {
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
  respuestasGuardadas.value.r4 = esCorrecto ? "Correcto" : "Incorrecto";
}

function siguienteJuego() {
  faseActual.value = "juego2";
}

// Lógica Juego Parejas
const mostrarFeedback = ref(false);
const feedbackMensaje = ref("");
const feedbackTipo = ref("");

function seleccionarItem(item) {
  if (item.matched) return;
  if (seleccionActual.value?.type === item.type) return;

  if (!seleccionActual.value) {
    seleccionActual.value = item;
    return;
  }

  const primerItem = seleccionActual.value;

  if (primerItem.id === item.id && primerItem.type !== item.type) {
    // Match
    primerItem.matched = true;
    item.matched = true;
    actualizarEstadoItem(primerItem, true);
    actualizarEstadoItem(item, true);
    parejasEncontradas.value++;
    mostrarFeedbackPositivo();
  } else {
    // No match
    mostrarFeedbackNegativo();
    setTimeout(() => {
      seleccionActual.value = null;
    }, 1000);
    return;
  }
  seleccionActual.value = null;
}

function actualizarEstadoItem(item, estado) {
  const lista = item.type === "term" ? terminos.value : definiciones.value;
  const index = lista.findIndex((i) => i.id === item.id);
  if (index >= 0) lista[index].matched = estado;
}

function mostrarFeedbackPositivo() {
  feedbackMensaje.value = "¡Correcto!";
  feedbackTipo.value = "exito";
  mostrarFeedback.value = true;
  setTimeout(() => { mostrarFeedback.value = false; }, 1000);
}

function mostrarFeedbackNegativo() {
  feedbackMensaje.value = "Intenta de nuevo";
  feedbackTipo.value = "error";
  mostrarFeedback.value = true;
  setTimeout(() => { mostrarFeedback.value = false; }, 1000);
}

function finalizarTodo() {
  faseActual.value = "final";
  respuestasGuardadas.value.r5 = `${parejasEncontradas.value}/${parejas.length}`;
  respuestasGuardadas.value.r6 = puntajeTotal.value.toString();
}

async function enviarExamen() {
  const email = localStorage.getItem("usuario"); // Ojo aquí, usé "usuario" que es lo que usas en el Login
  if (!email) return alert("Error: Inicia sesión.");

  enviando.value = true;
  try {
    const payload = {
      email: email,
      ...respuestasGuardadas.value,
    };

    const response = await fetch(`${API_URL}/guardar_examen1`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const data = await response.json();

    if (data.exito) {
      usuarioYaParticipo.value = true;
      await cargarRespuestas();
    } else {
      alert("Error: " + data.mensaje);
    }
  } catch (error) {
    console.error(error);
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
  const f = fecha.endsWith("Z") ? fecha : fecha + "Z";
  return new Date(f).toLocaleDateString('es-ES', {
    year: 'numeric', month: 'short', day: 'numeric',
    hour: '2-digit', minute:'2-digit'
  });
}

const puntajeTotal = computed(() => {
  let p = puntajeQuiz.value;
  if (juego1Correcto.value) p += 1;
  p += parejasEncontradas.value;
  return p;
});

const totalPosible = computed(() => preguntas.value.length + 1 + parejas.length);
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in { animation: fadeIn 0.5s ease-out forwards; }
</style>