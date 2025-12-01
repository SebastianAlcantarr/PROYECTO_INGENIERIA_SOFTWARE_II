<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <!-- Foro preguntas -->
    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12 min-h-screen">
        <div class="mx-auto max-w-7xl">
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
                      class="text-white text-4xl @[480px]:text-5xl font-extrabold leading-tight tracking-tight"
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
          <section class="scroll-mt-20" id="rules">
            <h2
              class="text-white text-2xl sm:text-3xl font-bold leading-tight tracking-[-0.015em] px-4 pb-1 pt-10"
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

          <div class="text-white text-2xl">
            <!-- FASE 0: QUIZ -->
            <div class="mt-10" v-if="!quizFinalizado">
              <div
                class="bg-[#161d2b] rounded-2xl p-6 sm:p-8 shadow-lg ring-1 ring-white/10"
              >
                <h2 class="text-2xl sm:text-3xl font-semibold leading-snug">
                  {{ preguntas[preguntaActual].texto }}
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
                <h2 class="text-white text-3xl font-bold">¡Quiz Completado!</h2>
                <p class="mt-4 text-xl text-white/80">
                  Ahora pasemos a unos juegos interactivos para reforzar lo
                  aprendido.
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
                  Toca las palabras para formar la oración correcta sobre la
                  actividad física.
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
                    ¡Correcto! 🎉
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
                <h2 class="text-2xl font-bold mb-4">Encuentra las parejas</h2>
                <p class="text-white/70 mb-8">
                  Selecciona un término y su definición correspondiente.
                </p>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                  <!-- Columna Términos -->
                  <div class="space-y-4">
                    <h3 class="text-lg font-semibold text-white/50 text-center">
                      Términos
                    </h3>
                    <button
                      v-for="item in terminos"
                      :key="item.id"
                      @click="seleccionarItem(item)"
                      class="w-full p-4 rounded-xl border-2 transition-all duration-200 text-left relative overflow-hidden"
                      :class="[
                        item.matched
                          ? 'border-green-500 bg-green-500/10 text-green-200 opacity-50'
                          : seleccionActual === item
                          ? 'border-[#2c5a8f] bg-[#2c5a8f]/20 scale-[1.02]'
                          : 'border-white/10 bg-white/5 hover:bg-white/10',
                      ]"
                      :disabled="item.matched"
                    >
                      {{ item.text }}
                      <div
                        v-if="item.matched"
                        class="absolute right-4 top-1/2 -translate-y-1/2 text-green-500"
                      >
                        ✓
                      </div>
                    </button>
                  </div>

                  <!-- Columna Definiciones -->
                  <div class="space-y-4">
                    <h3 class="text-lg font-semibold text-white/50 text-center">
                      Definiciones
                    </h3>
                    <button
                      v-for="item in definiciones"
                      :key="item.id"
                      @click="seleccionarItem(item)"
                      class="w-full p-4 rounded-xl border-2 transition-all duration-200 text-left relative overflow-hidden"
                      :class="[
                        item.matched
                          ? 'border-green-500 bg-green-500/10 text-green-200 opacity-50'
                          : seleccionActual === item
                          ? 'border-[#2c5a8f] bg-[#2c5a8f]/20 scale-[1.02]'
                          : 'border-white/10 bg-white/5 hover:bg-white/10',
                      ]"
                      :disabled="item.matched"
                    >
                      {{ item.text }}
                      <div
                        v-if="item.matched"
                        class="absolute right-4 top-1/2 -translate-y-1/2 text-green-500"
                      >
                        ✓
                      </div>
                    </button>
                  </div>
                </div>

                <div
                  v-if="parejasEncontradas === parejas.length"
                  class="mt-8 text-center animate-in zoom-in"
                >
                  <div class="text-green-400 text-xl font-bold mb-4">
                    ¡Excelente! Completaste todas las parejas.
                  </div>
                  <button
                    @click="finalizarTodo"
                    class="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-full transition-transform hover:scale-105"
                  >
                    Ver Resultados Finales
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
                  ¡Actividad Completada!
                </h2>
                <p class="mt-4 text-2xl text-white/90">
                  Puntaje Total:
                  <span class="font-semibold text-[#2c5a8f]">{{
                    puntajeTotal
                  }}</span>
                  / {{ totalPosible }}
                </p>

                <div
                  class="mt-8 grid grid-cols-1 sm:grid-cols-3 gap-4 text-left max-w-2xl mx-auto"
                >
                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-sm text-white/60">Quiz</div>
                    <div class="text-xl font-bold">
                      {{ puntajeQuiz }} / {{ preguntas.length }}
                    </div>
                  </div>
                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-sm text-white/60">Oración</div>
                    <div class="text-xl font-bold">
                      {{ juego1Correcto ? 1 : 0 }} / 1
                    </div>
                  </div>
                  <div class="bg-white/5 p-4 rounded-xl border border-white/10">
                    <div class="text-sm text-white/60">Parejas</div>
                    <div class="text-xl font-bold">
                      {{ parejasEncontradas }} / {{ parejas.length }}
                    </div>
                  </div>
                </div>

                <div
                  class="mt-8 h-4 w-full rounded-full bg-white/10 overflow-hidden"
                >
                  <div
                    class="h-full bg-gradient-to-r from-[#2c5a8f] to-green-500 transition-all duration-1000"
                    :style="{
                      width: (puntajeTotal / totalPosible) * 100 + '%',
                    }"
                  />
                </div>

                <button
                  class="mt-10 text-white/50 hover:text-white underline"
                  @click="$router.go(0)"
                >
                  Reiniciar Actividad
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import Sidebar from "@/views/sidebar.vue";

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
const faseActual = ref("quiz"); // 'quiz', 'juego1', 'juego2', 'final'

// Juego 1: Ordenar Oración
const oracionCorrecta = [
  "La",
  "actividad",
  "física",
  "mejora",
  "la",
  "densidad",
  "ósea",
];
const palabrasDesordenadas = ref(
  [...oracionCorrecta].sort(() => Math.random() - 0.5)
);
const oracionUsuario = ref([]);
const juego1Completado = ref(false);
const juego1Correcto = ref(false);

// Juego 2: Parejas (Matching)
const parejas = [
  { id: 1, termino: "Osteoporosis", definicion: "Huesos porosos y frágiles" },
  { id: 2, termino: "Calcio", definicion: "Mineral esencial para huesos" },
  { id: 3, termino: "DMO", definicion: "Densidad Mineral Ósea" },
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
);

const seleccionActual = ref(null);
const parejasEncontradas = ref(0);

// --- ACTIONS ---

function enviarRespuesta() {
  const pregunta = preguntas.value[preguntaActual.value];
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
  juego1Correcto.value = oracionStr === correctaStr;
  juego1Completado.value = true;
}

function siguienteJuego() {
  faseActual.value = "juego2";
}

// Logic Juego 2
function seleccionarItem(item) {
  if (item.matched) return;

  if (!seleccionActual.value) {
    // Primer click
    seleccionActual.value = item;
  } else {
    // Segundo click - verificar match
    const item1 = seleccionActual.value;
    const item2 = item;

    if (item1.id === item2.id && item1.type !== item2.type) {
      // Match correcto
      item1.matched = true;
      item2.matched = true;
      // Actualizar en las listas originales para reactividad
      const tIndex = terminos.value.findIndex((t) => t.id === item1.id);
      if (tIndex >= 0) terminos.value[tIndex].matched = true;
      const dIndex = definiciones.value.findIndex((d) => d.id === item1.id);
      if (dIndex >= 0) definiciones.value[dIndex].matched = true;

      parejasEncontradas.value++;
    } else {
      // Error visual o simplemente reset
      // Podríamos poner un timeout para mostrar error rojo
      setTimeout(() => {
        seleccionActual.value = null;
      }, 500);
      return; // Salir para no resetear inmediatamente abajo si queremos animacion
    }
    seleccionActual.value = null;
  }
}

function finalizarTodo() {
  faseActual.value = "final";
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
