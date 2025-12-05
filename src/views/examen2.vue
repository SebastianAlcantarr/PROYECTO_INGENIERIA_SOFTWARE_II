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
                      E2. Evalúa tu comprensión sobre el modelo
                    </h1>
                    <p class="text-white/80 text-lg @[480px]:text-xl mt-7">
                      Evalúa tu comprensión sobre el modelo que representa la
                      covariación entre la densidad mineral ósea y la edad.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <div v-if="cargandoEstado" class="text-center py-10">
            <p class="text-white text-xl animate-pulse">
              Verificando tu participación...
            </p>
          </div>

          <div v-else-if="usuarioYaParticipo" class="mt-8 animate-fade-in">
            <div
              class="bg-green-900/30 border border-green-500/50 p-4 rounded-xl mb-8 flex items-center gap-4 text-green-200"
            >
              <span class="material-symbols-outlined text-3xl"
                >check_circle</span
              >
              <div>
                <h3 class="font-bold text-xl">Examen Terminado</h3>
                <p class="text-base opacity-80">
                  Ya has enviado tus respuestas.
                </p>
              </div>
            </div>

            <h2
              class="text-white text-xl font-bold mb-6 border-b border-gray-700 pb-2 flex items-center gap-2"
            >
              <span class="material-symbols-outlined">analytics</span>
              Resultados del Grupo
            </h2>

            <div class="space-y-6">
              <div
                v-if="listaRespuestas.length === 0"
                class="text-center text-gray-400 py-8"
              >
                Aún no hay respuestas registradas.
              </div>
              <div
                v-for="(item, index) in listaRespuestas"
                :key="index"
                class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-500 shadow-md"
              >
                <div class="flex justify-between items-start mb-4">
                  <div class="flex items-center gap-3">
                    <div
                      class="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold"
                    >
                      {{ obtenerIniciales(item.nombre, item.apellidos) }}
                    </div>
                    <div>
                      <span class="text-blue-400 font-bold text-base">
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
                    class="bg-blue-900/50 text-blue-200 text-sm px-2 py-1 rounded"
                    >Puntaje: {{ item.r6 }}</span
                  >
                </div>
                <div
                  class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-gray-300 mt-4"
                >
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
                    <span class="text-blue-300 text-sm block">Pregunta 4</span>
                    {{ item.r4 }}
                  </div>
                  <div class="bg-white/5 p-3 rounded">
                    <span class="text-blue-300 text-sm block">Pregunta 5</span>
                    {{ item.r5 }}
                  </div>
                  <div class="bg-white/5 p-3 rounded">
                    <span class="text-blue-300 text-sm block">Pregunta 6</span>
                    {{ item.r6 }}
                  </div>
                  <div class="bg-white/5 p-3 rounded">
                    <span class="text-blue-300 text-sm block">Pregunta 7</span>
                    {{ item.r7 }}
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div v-else>
            <section class="scroll-mt-20" id="rules">
              <h2
                class="text-white text-xl sm:text-2xl leading-tight tracking-[-0.015em] px-4 pb-1 pt-10"
              >
                Analiza y responde el siguiente cuestionario
              </h2>

              <!-- Progress bar -->
              <div class="px-4 mt-4" v-if="faseActual === 'quiz'">
                <div
                  class="h-2 w-full rounded-full bg-white/10 overflow-hidden"
                >
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
                  {{ quizFinalizado ? preguntas.length : preguntaActual + 1 }}
                  de
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
                      src="/src/imagenes/Grafico.jpg"
                      alt="Gráfico de Densidad Mineral Ósea"
                      class="mx-auto w-auto p-10"
                    />
                    <p v-if="preguntaActual === 2">
                      ¿Cómo se relaciona esto con los datos de la tabla? ¿Por
                      qué la DMO no comienza en cero? Escribe tú respuesta.
                    </p>
                    <textarea
                      v-if="preguntaActual === 2"
                      v-model="respuestasGuardadas.r3"
                      rows="3"
                      placeholder="Respuesta"
                      class="input-foro"
                    ></textarea>
                  </h2>

                  <textarea
                    v-if="preguntaActual === 3"
                    v-model="respuestasGuardadas.r4"
                    rows="3"
                    placeholder="Respuesta"
                    class="input-foro"
                  ></textarea>

                  <textarea
                    v-if="preguntaActual === 5"
                    v-model="respuestasGuardadas.r6"
                    rows="3"
                    placeholder="Respuesta"
                    class="input-foro"
                  ></textarea>
                  <textarea
                    v-if="preguntaActual === 6"
                    v-model="respuestasGuardadas.r7"
                    rows="3"
                    placeholder="Respuesta"
                    class="input-foro"
                  ></textarea>
                  <div class="mt-8 space-y-3">
                    <template
                      v-if="
                        !preguntas[preguntaActual].tipo ||
                        preguntas[preguntaActual].tipo === 'standard'
                      "
                    >
                      <div
                        v-for="op in preguntas[preguntaActual].opciones"
                        :key="op"
                        class="group rounded-xl border border-white/10 hover:border-[#2c5a8f] bg-white/5 hover:bg-white/10 transition-colors duration-200"
                      >
                        <label
                          class="flex items-start gap-3 p-4 cursor-pointer"
                        >
                          <input
                            type="radio"
                            class="mt-1 h-4 w-4 text-[#2c5a8f] focus:ring-[#2c5a8f] border-white/20 bg-transparent"
                            v-model="respuestaUsuario"
                            :value="op"
                          />
                          <span class="text-base sm:text-lg">{{ op }}</span>
                        </label>
                      </div>
                    </template>

                    <template
                      v-else-if="preguntas[preguntaActual].tipo === 'match'"
                    >
                      <div
                        v-for="(item, index) in preguntas[preguntaActual].items"
                        :key="index"
                        class="flex flex-col gap-2 mb-4 bg-white/5 p-4 rounded-xl border border-white/10"
                      >
                        <p class="text-white font-medium">
                          {{ item.pregunta }}
                        </p>
                        <select
                          v-model="respuestasMatch[index]"
                          class="bg-[#161d2b] text-white border border-white/20 rounded-lg p-3 w-full focus:ring-[#2c5a8f] focus:border-[#2c5a8f] outline-none"
                        >
                          <option :value="undefined" disabled selected>
                            Elegir...
                          </option>
                          <option
                            v-for="op in preguntas[preguntaActual].opciones"
                            :key="op"
                            :value="op"
                          >
                            {{ op }}
                          </option>
                        </select>
                      </div>
                    </template>
                  </div>

                  <!-- Retroalimentación Inmediata -->
                  <div
                    v-if="mostrandoFeedback"
                    class="mt-6 p-4 rounded-xl animate-fade-in"
                    :class="
                      esRespuestaCorrecta
                        ? 'bg-green-900/20 border border-green-500/30 text-green-200'
                        : 'bg-red-900/20 border border-red-500/30 text-red-200'
                    "
                  >
                    <div class="flex items-center gap-3 mb-2">
                      <span class="material-symbols-outlined text-2xl">
                        {{ esRespuestaCorrecta ? "check_circle" : "cancel" }}
                      </span>
                      <h3 class="font-bold text-lg">
                        {{
                          esRespuestaCorrecta
                            ? "¡Correcto!"
                            : "Respuesta Incorrecta"
                        }}
                      </h3>
                    </div>
                    <p
                      v-if="
                        !esRespuestaCorrecta &&
                        preguntas[preguntaActual].tipo !== 'match' &&
                        preguntas[preguntaActual].correcta
                      "
                    >
                      La respuesta correcta es:
                      <strong class="underline">{{
                        preguntas[preguntaActual].correcta
                      }}</strong>
                    </p>

                    <div
                      v-else-if="
                        !esRespuestaCorrecta &&
                        preguntas[preguntaActual].tipo === 'match'
                      "
                      class="mt-3"
                    >
                      <p class="font-bold mb-2">Solución correcta:</p>
                      <ul class="list-disc list-inside text-sm space-y-1">
                        <li
                          v-for="(item, idx) in preguntas[preguntaActual].items"
                          :key="idx"
                        >
                          {{ item.pregunta }}:
                          <strong>{{ item.correcta }}</strong>
                        </li>
                      </ul>
                    </div>
                  </div>

                  <!-- Botones -->
                  <div class="mt-8">
                    <button
                      v-if="!mostrandoFeedback"
                      class="inline-flex items-center justify-center bg-[#2c5a8f] hover:bg-[#2b4f7b] text-white font-medium rounded-xl px-6 sm:px-8 py-3 sm:py-3.5 transition duration-300 shadow-md"
                      type="button"
                      @click="verificarRespuesta"
                    >
                      Comprobar
                    </button>

                    <button
                      v-else
                      class="inline-flex items-center justify-center bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-xl px-6 sm:px-8 py-3 sm:py-3.5 transition duration-300 shadow-md flex items-center gap-2"
                      type="button"
                      @click="siguientePregunta"
                    >
                      <span>{{
                        preguntaActual < preguntas.length - 1
                          ? "Siguiente"
                          : "Finalizar"
                      }}</span>
                      <span class="material-symbols-outlined"
                        >arrow_forward</span
                      >
                    </button>
                  </div>
                </div>
              </div>

              <!-- FASE FINAL: RESULTADOS TOTALES -->
              <div v-if="faseActual === 'final'" class="mt-10">
                <div
                  class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10 text-center"
                >
                  <h2 class="text-white text-3xl font-bold">
                    Examen Terminado
                  </h2>

                  <div
                    class="mt-8 h-4 w-full rounded-full bg-white/10 overflow-hidden"
                  >
                    <div
                      class="h-full bg-green-500 transition-all duration-1000"
                    />
                  </div>

                  <div class="mt-10 flex flex-col items-center gap-4">
                    <button
                      @click="enviarExamen"
                      :disabled="enviando"
                      class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-xl shadow-lg transition-transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                    >
                      <span
                        v-if="enviando"
                        class="material-symbols-outlined animate-spin"
                        >refresh</span
                      >
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
    tipo: "standard",
    texto:
      "Al tomar un valor de edad al inicio de la tabla y comenzar a aumentarlo ¿El valor de la Densidad Mineral Ósea (DMO) siempre aumenta?",
    opciones: ["Verdadero", "Falso"],
    // La DMO primero aumenta y luego disminuye, por lo que NO siempre aumenta
    correcta: "Verdadero",
  },
  {
    tipo: "match",
    texto:
      "Relaciona cómo cambia la densidad mineral osea con respecto a la edad.",
    items: [
      {
        pregunta: "En la vida adulta",
        correcta: "La densidad mineral ósea cambia muy poco.",
      },
      {
        pregunta: "En la vejez",
        correcta: "La densidad mineral ósea disminuye.",
      },
      {
        pregunta: "Hasta la adolescencia...",
        correcta: "La densidad mineral ósea aumenta.",
      },
    ],
    opciones: [
      "La densidad mineral ósea aumenta.",
      "La densidad mineral ósea cambia muy poco.",
      "La densidad mineral ósea disminuye.",
    ],
  },
  {
    tipo: "standard",
    texto:
      "El gráfico que modela la relación entre la Densidad Mineral Ósea (DMO) y la Edad, que elaboramos en la hoja de cálculo de Google, comienzan en un valor por arriba de cero en el eje vertical. ",
    correcta: "Verdadero",
  },
  {
    tipo: "standard",
    texto:
      " La gráfica que elaboramos esta basada en datos de una tabla que cambian de un año a otro (o cambian cada 10 años). ¿podríamos representar estos valores con una gráfica continua? Justifica tu respuesta. \n" +
      "\n" +
      "Escribe tu respuesta.",
  },
  {
    tipo: "standard",
    texto:
      "¿En cuál rango de edad se presenta el mayor cambio en la densidad mineral ósea?",
    opciones: [
      "a . Niñez (6-12 años)",
      "b . Adultez (30-50 años)",
      "c . Adolescencia (12-18 años)",
      "d.  Adulto mayor (50-70 años)",
      "e . Jueventud (18-30 años)",
      "f . Vejez (70-90 años)",
    ],
    // Mayor cambio de DMO en la adolescencia
    correcta: "f . Vejez (70-90 años)",
  },
  {
    tipo: "standard",
    texto:
      "¿Cómo el gráfico da información respecto a que este problema tiene un valor máximo y no un valor mínimo?",
  },
  {
    tipo: "standard",
    texto:
      '¿Cómo podríamos estar seguros de la edad en que "suponemos" se alcanza la densidad mineral ósea máxima (conocida como el pico de masa ósea) es el correcto? \n' +
      ". Tu respuesta debe ser texto. ",
  },
]);

const preguntaActual = ref(0);
const respuestaUsuario = ref(null);
const respuestasMatch = ref({});
const puntajeQuiz = ref(0);
const quizFinalizado = ref(false);

// --- FEEDBACK STATE ---
const mostrandoFeedback = ref(false);
const esRespuestaCorrecta = ref(false);

// --- GAME STATE ---
const faseActual = ref("quiz");
const parejasEncontradas = ref(0);
const juego1Correcto = ref(false); // Placeholder
const parejas = ref([]); // Placeholder

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
  r7: "",
});

onMounted(() => {
  verificarEstado();
});

async function verificarEstado() {
  const email = localStorage.getItem("usuario");
  if (!email) {
    cargandoEstado.value = false;
    return;
  }

  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/verificar_examen2/${email}`
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
      "http://127.0.0.1:8000/respuestas_examen2"
    );
    listaRespuestas.value = response.data;
  } catch (error) {
    console.error("Error cargando respuestas:", error);
  }
}

function verificarRespuesta() {
  const pregunta = preguntas.value[preguntaActual.value];

  // 1. Validación de entrada
  if (pregunta.tipo === "match") {
    if (Object.keys(respuestasMatch.value).length < pregunta.items.length) {
      alert("Por favor completa todas las opciones");
      return;
    }
  } else if (pregunta.opciones) {
    if (!respuestaUsuario.value) {
      alert("Por favor selecciona una respuesta");
      return;
    }
  } else {
    // Validación para preguntas abiertas (Textarea)
    const key = `r${preguntaActual.value + 1}`;
    if (
      !respuestasGuardadas.value[key] ||
      !respuestasGuardadas.value[key].trim()
    ) {
      alert("Por favor escribe una respuesta");
      return;
    }
  }

  // 2. Lógica de Verificación
  let esCorrecto = false;

  if (pregunta.tipo === "match") {
    let correctas = 0;
    pregunta.items.forEach((item, index) => {
      const userRes = respuestasMatch.value[index];
      if (userRes === item.correcta) correctas++;
    });
    if (correctas === pregunta.items.length) {
      esCorrecto = true;
      puntajeQuiz.value++;
    }
    esRespuestaCorrecta.value = esCorrecto;
    mostrandoFeedback.value = true;
  } else if (pregunta.opciones) {
    if (respuestaUsuario.value === pregunta.correcta) {
      esCorrecto = true;
      puntajeQuiz.value++;
    }
    esRespuestaCorrecta.value = esCorrecto;
    mostrandoFeedback.value = true;
  } else {
    // Preguntas abiertas: No mostrar feedback, pasar directo
    siguientePregunta();
  }
}

function siguientePregunta() {
  const pregunta = preguntas.value[preguntaActual.value];

  // Guardar Respuesta
  if (pregunta.tipo === "match") {
    let respuestaString = [];
    pregunta.items.forEach((item, index) => {
      const userRes = respuestasMatch.value[index];
      respuestaString.push(`${item.pregunta}: ${userRes}`);
    });
    const key = `r${preguntaActual.value + 1}`;
    respuestasGuardadas.value[key] = respuestaString.join(" | ");
    respuestasMatch.value = {};
  } else {
    const key = `r${preguntaActual.value + 1}`;
    // Si es textarea, usamos el v-model directo de respuestasGuardadas, si es radio usamos respuestaUsuario
    if (pregunta.opciones) {
      respuestasGuardadas.value[key] = respuestaUsuario.value;
    }
    // Para textareas ya está en respuestasGuardadas por el v-model del template

    respuestaUsuario.value = null;
  }

  // Avanzar
  mostrandoFeedback.value = false;
  preguntaActual.value++;

  if (preguntaActual.value === preguntas.value.length) {
    quizFinalizado.value = true;
    faseActual.value = "final";
  }
}

async function enviarExamen() {
  const email = localStorage.getItem("usuario");
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
      "http://127.0.0.1:8000/guardar_examen2",
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

<style scoped>
.input-foro {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  background-color: #222d3e;
  border: 1px solid #b2bfd1;
  color: #cfd1de;
  resize: vertical;
}
.input-foro:focus {
  outline: none;
  border-color: #1c398e;
  box-shadow: 0 0 0 3px rgb(5, 40, 95);
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
