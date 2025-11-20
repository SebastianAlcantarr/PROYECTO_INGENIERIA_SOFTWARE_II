<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <!-- Foro preguntas -->
    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12  min-h-screen">
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


            <!-- Back action -->
            <div class="px-4 mt-6">
            </div>
            <div class="px-4 mt-4">
              <div class="h-2 w-full rounded-full bg-white/10 overflow-hidden">
                <div
                    class="h-full bg-[#2c5a8f] transition-all duration-500"
                    :style="{
                    width:
                      (finalizado
                        ? 100
                        : ((preguntaActual + 1) / preguntas.length) * 100) +
                      '%',
                  }"
                />
              </div>
              <div class="mt-2 text-white/70 text-sm">
                Pregunta
                {{ finalizado ? preguntas.length : preguntaActual + 1 }} de
                {{ preguntas.length }}
              </div>
            </div>
          </section>
          <div class="text-white text-2xl">
            <!-- Mostrar preguntas solo mientras no ha terminado -->
            <div class="mt-10" v-if="!finalizado">
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
                <button
                    class="ml-10 mb-10 inline-flex items-center gap-2 text-white border border-white/15 hover:bg-white/10 rounded-xl px-4 py-2 transition disabled:opacity-50 disabled:cursor-not-allowed"
                    :disabled="preguntaActual === 0 || finalizado"
                    @click="preguntaActual = Math.max(0, preguntaActual - 1)"
                >
                  Regresar a pregunta anterior
                </button>
              </div>
            </div>
          </div>

          <!-- Mostrar resultados al final -->
          <div v-if="finalizado" class="mt-10">
            <div
              class="bg-[#161d2b] rounded-2xl p-8 shadow-lg ring-1 ring-white/10 text-center"
            >
              <h2 class="text-white text-3xl font-bold">Fin del quiz</h2>
              <p class="mt-4 text-2xl text-white/90">
                Tu puntaje: <span class="font-semibold">{{ puntaje }}</span> /
                {{ preguntas.length }}
              </p>
              <div
                class="mt-6 h-2 w-full rounded-full bg-white/10 overflow-hidden"
              >
                <div
                  class="h-full bg-[#2c5a8f]"
                  :style="{ width: (puntaje / preguntas.length) * 100 + '%' }"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue";
import Sidebar from "@/views/sidebar.vue";

// Preguntas simples

  const preguntas = ref([
  {
    texto:
    "La Densidad Mineral Ósea (DMO) que mide el volumen del esqueleto humano, si lo comparamos entre el esqueleto femenino y masculino, encontramos que:",
    opciones: [
    "A) Son diferentes solo en la vejez.",
    "B) Son diferentes desde el nacimiento.",
    "C) Son iguales en la niñez y se empiezan a diferenciar a partir de la adolescencia.",
    "D) Son iguales, no hay diferencia."
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
    "D) Porque aumenta conforme crecemos pero luego empieza a disminuir conforme se envejece."
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
  const puntaje = ref(0);
  const finalizado = ref(false);

  function enviarRespuesta() {
  const pregunta = preguntas.value[preguntaActual.value];

  if (respuestaUsuario.value === pregunta.correcta) {
  puntaje.value++;
}

  respuestaUsuario.value = null;

  preguntaActual.value++;

  if (preguntaActual.value === preguntas.value.length) {
  finalizado.value = true;
}
}
</script>
