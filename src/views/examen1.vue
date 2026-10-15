<template>
  <PaginaPaso titulo="Evalúa tu comprensión: Densidad Mineral Ósea y Edad">
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Verificando…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Terminado
      </span>
      <span v-else class="chip">Cuestionario y 2 juegos</span>
    </template>
    <template #intro>
      Evaluación de la comprensión de la Situación 1 planteada sobre la Densidad Mineral Ósea y la Edad.
    </template>

    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Verificando tu participación…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
    </div>

    <!-- Ya participó: resultados del grupo -->
    <template v-else-if="usuarioYaParticipo">
      <div class="aviso aviso-ok mb-8">
        <span class="material-symbols-outlined" aria-hidden="true">check_circle</span>
        <div>
          <p class="font-semibold">Examen Terminado</p>
          <p class="font-normal">Ya has enviado tus respuestas.</p>
        </div>
      </div>

      <Seccion titulo="Resultados del grupo" :resumen="`${listaRespuestas.length} respuestas`">
        <p v-if="listaRespuestas.length === 0" class="py-6 text-tenue">Aún no hay respuestas registradas.</p>
        <ul v-else class="grid gap-4">
          <li v-for="(item, index) in listaRespuestas" :key="index" class="ficha">
            <div class="mb-4 flex items-start justify-between gap-4">
              <div class="flex items-center gap-3">
                <span class="avatar">{{ obtenerIniciales(item.nombre, item.apellidos) }}</span>
                <div>
                  <p class="font-semibold leading-snug">{{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}</p>
                  <p class="text-sm text-tenue">{{ formatearFecha(item.fecha) }}</p>
                </div>
              </div>
              <span class="chip numeral">Puntaje: {{ item.r6 }}</span>
            </div>
            <dl class="grid gap-3 text-[0.9375rem] sm:grid-cols-2">
              <div class="rounded-xl bg-hundido p-3"><dt class="font-semibold">P1</dt><dd class="text-tenue">{{ item.r1 }}</dd></div>
              <div class="rounded-xl bg-hundido p-3"><dt class="font-semibold">P2</dt><dd class="text-tenue">{{ item.r2 }}</dd></div>
              <div class="rounded-xl bg-hundido p-3"><dt class="font-semibold">P3</dt><dd class="text-tenue">{{ item.r3 }}</dd></div>
              <div class="rounded-xl bg-hundido p-3"><dt class="font-semibold">Juego Oración</dt><dd class="text-tenue">{{ item.r4 }}</dd></div>
              <div class="rounded-xl bg-hundido p-3 sm:col-span-2"><dt class="font-semibold">Juego Parejas</dt><dd class="text-tenue">{{ item.r5 }}</dd></div>
            </dl>
          </li>
        </ul>
      </Seccion>
    </template>

    <!-- Examen activo -->
    <section v-else class="border-t border-linea pt-8" aria-labelledby="titulo-examen">
      <!-- Fases del examen -->
      <ol class="mb-8 grid grid-cols-2 gap-2 sm:grid-cols-4" aria-label="Fases del examen">
        <li
          v-for="(f, i) in fasesExamen"
          :key="f.id"
          class="flex items-center gap-2 rounded-full px-3 py-2 text-sm font-semibold"
          :class="
            i === indiceFase
              ? 'bg-tinta text-fondo'
              : i < indiceFase
                ? 'bg-hundido text-tinta'
                : 'border border-linea text-tenue'
          "
          :aria-current="i === indiceFase ? 'step' : undefined"
        >
          <span class="material-symbols-outlined text-[18px]" aria-hidden="true">{{ i < indiceFase ? 'check' : f.icono }}</span>
          {{ f.nombre }}
        </li>
      </ol>

      <h2 id="titulo-examen" class="mb-4 text-2xl font-bold tracking-[-0.02em] md:text-3xl">
        Analiza y responde el siguiente cuestionario
      </h2>

      <!-- Barra de avance del cuestionario -->
      <div v-if="faseActual === 'quiz'" class="mb-8 max-w-xl">
        <div class="h-2 overflow-hidden rounded-full bg-hundido">
          <div
            class="h-full rounded-full bg-a1 transition-all duration-500"
            :style="{ width: (quizFinalizado ? 100 : ((preguntaActual + 1) / preguntas.length) * 100) + '%' }"
          />
        </div>
        <p class="numeral mt-2 text-sm text-tenue">
          Pregunta {{ quizFinalizado ? preguntas.length : preguntaActual + 1 }} de {{ preguntas.length }}
        </p>
      </div>

      <!-- FASE 0: CUESTIONARIO -->
      <div v-if="!quizFinalizado" class="ficha max-w-3xl !p-6 sm:!p-8">
        <p class="text-xl font-semibold leading-snug sm:text-2xl">{{ preguntas[preguntaActual].texto }}</p>
        <figure v-if="preguntaActual === 2" class="figura mt-6">
          <img src="/src/imagenes/EXAMEN.png" alt="Figuras A, B, C y D de posibles gráficas de la DMO a lo largo de la vida" />
        </figure>

        <fieldset class="mt-6 space-y-3">
          <legend class="sr-only">Opciones</legend>
          <label
            v-for="op in preguntas[preguntaActual].opciones"
            :key="op"
            class="opcion"
            :class="{
              '!border-ok !bg-ok-fondo': mostrandoFeedback && op === preguntas[preguntaActual].correcta,
              '!border-error !bg-error-fondo': mostrandoFeedback && op === respuestaUsuario && op !== preguntas[preguntaActual].correcta,
              'opacity-50': mostrandoFeedback && op !== preguntas[preguntaActual].correcta && op !== respuestaUsuario,
            }"
          >
            <input type="radio" name="opcion-examen1" v-model="respuestaUsuario" :value="op" :disabled="mostrandoFeedback" />
            <span class="text-base sm:text-[1.0625rem]">{{ op }}</span>
          </label>
        </fieldset>

        <div v-if="mostrandoFeedback" role="status" class="aviso mt-6" :class="esRespuestaCorrecta ? 'aviso-ok' : 'aviso-error'">
          <span class="material-symbols-outlined" aria-hidden="true">{{ esRespuestaCorrecta ? 'check_circle' : 'cancel' }}</span>
          <div>
            <p class="font-semibold">{{ esRespuestaCorrecta ? '¡Correcto!' : 'Respuesta Incorrecta' }}</p>
            <p v-if="!esRespuestaCorrecta" class="font-normal">
              La respuesta correcta es: <strong>{{ preguntas[preguntaActual].correcta }}</strong>
            </p>
          </div>
        </div>

        <div class="mt-8">
          <button v-if="!mostrandoFeedback" type="button" class="boton boton-primario" @click="verificarRespuesta">
            Enviar respuesta
          </button>
          <button v-else type="button" class="boton boton-primario" @click="siguientePregunta">
            {{ preguntaActual < preguntas.length - 1 ? 'Siguiente pregunta' : 'Finalizar quiz' }}
            <span class="material-symbols-outlined -mr-1 text-[20px]" aria-hidden="true">arrow_forward</span>
          </button>
        </div>
      </div>

      <!-- FASE INTERMEDIA: RESULTADO DEL CUESTIONARIO -->
      <div v-if="quizFinalizado && faseActual === 'quiz'" class="ficha max-w-2xl !p-8">
        <p class="font-display numeral text-6xl font-extrabold tracking-[-0.04em]">
          {{ puntajeQuiz }}<span class="text-3xl text-tenue"> / {{ preguntas.length }}</span>
        </p>
        <h3 class="mt-3 text-2xl font-bold">Quiz completado</h3>
        <p class="mt-1 text-tenue">Obtuviste {{ puntajeQuiz }} de {{ preguntas.length }} aciertos.</p>
        <button type="button" class="boton boton-primario mt-8" @click="avanzarAJuegos">
          Continuar a juegos didácticos
          <span class="material-symbols-outlined -mr-1 text-[20px]" aria-hidden="true">arrow_forward</span>
        </button>
      </div>

      <!-- FASE 1: ORDENA LA FRASE -->
      <div v-if="faseActual === 'juego1'" class="ficha max-w-3xl !p-6 sm:!p-8">
        <h3 class="flex items-center gap-2 text-2xl font-bold">
          <span class="material-symbols-outlined text-a2-texto" aria-hidden="true">format_quote</span> Ordena la frase
        </h3>
        <p class="mt-2 text-tenue">Selecciona las palabras en el orden correcto para formar la oración.</p>

        <div
          class="mt-6 flex min-h-[84px] flex-wrap gap-2 rounded-2xl border-2 border-dashed p-4 transition-colors"
          :class="
            juego1Completado
              ? juego1Correcto
                ? 'border-ok bg-ok-fondo'
                : 'border-error bg-error-fondo'
              : 'border-linea-fuerte bg-hundido'
          "
          aria-live="polite"
        >
          <button
            v-for="palabra in oracionUsuario"
            :key="palabra"
            type="button"
            class="rounded-full bg-tinta px-4 py-2 font-medium text-fondo transition-transform hover:-translate-y-0.5 disabled:cursor-default"
            :disabled="juego1Completado"
            @click="moverPalabra(palabra, 'oracion')"
          >{{ palabra }}</button>
          <span v-if="oracionUsuario.length === 0" class="self-center text-tenue">Tus palabras aparecerán aquí...</span>
        </div>

        <div class="mt-4 flex flex-wrap justify-center gap-2.5 p-2">
          <button
            v-for="palabra in palabrasDesordenadas"
            :key="palabra"
            type="button"
            class="rounded-full border border-linea-fuerte bg-superficie px-4 py-2 font-medium transition-[transform,background-color] hover:-translate-y-0.5 hover:bg-hundido"
            :disabled="juego1Completado"
            @click="moverPalabra(palabra, 'banco')"
          >{{ palabra }}</button>
        </div>

        <div v-if="juego1Completado" class="mt-6 rounded-2xl bg-hundido p-6 text-center" role="status">
          <p v-if="juego1Correcto" class="flex items-center justify-center gap-2 text-xl font-bold text-ok">
            <span class="material-symbols-outlined" aria-hidden="true">check_circle</span> ¡Respuesta Correcta!
          </p>
          <div v-else>
            <p class="flex items-center justify-center gap-2 text-lg font-bold text-error">
              <span class="material-symbols-outlined" aria-hidden="true">cancel</span> Incorrecto
            </p>
            <p class="mt-2 text-sm text-tenue">La correcta era: <br />"{{ oracionCorrecta.join(" ") }}"</p>
          </div>
          <button type="button" class="boton boton-primario mt-5" @click="siguienteJuego">Siguiente juego</button>
        </div>
        <div v-else class="mt-6 text-center">
          <button type="button" class="boton boton-primario" :disabled="oracionUsuario.length === 0" @click="verificarOracion">
            Comprobar
          </button>
        </div>
      </div>

      <!-- FASE 2: ENCUENTRA LA PAREJA -->
      <div v-if="faseActual === 'juego2'" class="ficha !p-6 sm:!p-8">
        <h3 class="flex items-center gap-2 text-2xl font-bold">
          <span class="material-symbols-outlined text-a2-texto" aria-hidden="true">extension</span> Encuentra la pareja
        </h3>
        <p class="mt-2 text-tenue">Relaciona cada término con su definición correcta.</p>

        <div class="mb-6 mt-6 max-w-md">
          <div class="mb-2 flex items-center justify-between text-sm text-tenue">
            <span>Progreso</span>
            <span class="numeral">{{ parejasEncontradas }} / {{ parejas.length }}</span>
          </div>
          <div class="h-2 rounded-full bg-hundido">
            <div class="h-2 rounded-full bg-a1 transition-all duration-500" :style="{ width: `${(parejasEncontradas / parejas.length) * 100}%` }"></div>
          </div>
        </div>

        <div class="grid gap-6 md:grid-cols-2">
          <div>
            <h4 class="mb-3 text-sm font-semibold text-tenue">Términos</h4>
            <div class="space-y-3">
              <button
                v-for="item in terminos"
                :key="'term-' + item.id"
                type="button"
                class="opcion w-full text-left"
                :class="{
                  '!border-ok !bg-ok-fondo text-ok opacity-70': item.matched,
                  '!border-a1 !bg-[color-mix(in_srgb,var(--c-a1)_12%,var(--c-superficie))]': !item.matched && seleccionActual === item,
                }"
                :aria-pressed="seleccionActual === item"
                :disabled="item.matched"
                @click="seleccionarItem(item)"
              >{{ item.text }}</button>
            </div>
          </div>
          <div>
            <h4 class="mb-3 text-sm font-semibold text-tenue">Definiciones</h4>
            <div class="space-y-3">
              <button
                v-for="item in definiciones"
                :key="'def-' + item.id"
                type="button"
                class="opcion w-full text-left"
                :class="{
                  '!border-ok !bg-ok-fondo text-ok opacity-70': item.matched,
                  '!border-a1 !bg-[color-mix(in_srgb,var(--c-a1)_12%,var(--c-superficie))]': !item.matched && seleccionActual === item,
                }"
                :aria-pressed="seleccionActual === item"
                :disabled="item.matched"
                @click="seleccionarItem(item)"
              >{{ item.text }}</button>
            </div>
          </div>
        </div>

        <div
          v-if="mostrarFeedback"
          role="status"
          class="fixed bottom-28 left-1/2 z-50 -translate-x-1/2 rounded-full px-6 py-3 font-semibold shadow-[var(--sombra-elevada)]"
          :class="feedbackTipo === 'exito' ? 'bg-ok text-white dark:text-[#0e1420]' : 'bg-error text-white dark:text-[#0e1420]'"
        >
          {{ feedbackMensaje }}
        </div>

        <div v-if="parejasEncontradas === parejas.length" class="mt-8">
          <button type="button" class="boton boton-primario" @click="finalizarTodo">Ver calificación final</button>
        </div>
      </div>

      <!-- FASE FINAL: RESUMEN -->
      <div v-if="faseActual === 'final'" class="ficha max-w-3xl !p-8">
        <h3 class="text-3xl font-bold">Resumen de Actividades</h3>
        <p class="mt-1 text-tenue">Has completado todas las secciones del Examen 1.</p>

        <p class="font-display numeral mt-8 text-7xl font-extrabold tracking-[-0.04em]">
          {{ puntajeTotal }}<span class="text-3xl text-tenue"> / {{ totalPosible }} pts</span>
        </p>

        <dl class="mt-8 grid gap-3 sm:grid-cols-3">
          <div class="rounded-2xl bg-hundido p-4">
            <dt class="text-sm text-tenue">Cuestionario</dt>
            <dd class="numeral text-2xl font-bold">{{ puntajeQuiz }} / {{ preguntas.length }}</dd>
          </div>
          <div class="rounded-2xl bg-hundido p-4">
            <dt class="text-sm text-tenue">Frase</dt>
            <dd class="numeral text-2xl font-bold">{{ juego1Correcto ? 1 : 0 }} / 1</dd>
          </div>
          <div class="rounded-2xl bg-hundido p-4">
            <dt class="text-sm text-tenue">Parejas</dt>
            <dd class="numeral text-2xl font-bold">{{ parejasEncontradas }} / {{ parejas.length }}</dd>
          </div>
        </dl>

        <button type="button" class="boton boton-primario mt-8" :disabled="enviando" @click="enviarExamen">
          <span v-if="enviando" class="material-symbols-outlined animate-spin text-[20px]" aria-hidden="true">progress_activity</span>
          {{ enviando ? "Guardando…" : "Guardar y finalizar" }}
        </button>
      </div>
    </section>
  </PaginaPaso>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import axios from 'axios'; // Asegúrate de tener axios importado si no lo usas global
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";

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
// Fases del examen (solo para mostrar el avance en la interfaz)
const fasesExamen = [
  { id: "quiz", nombre: "Cuestionario", icono: "quiz" },
  { id: "juego1", nombre: "Ordena la frase", icono: "format_quote" },
  { id: "juego2", nombre: "Parejas", icono: "extension" },
  { id: "final", nombre: "Resumen", icono: "flag" },
];
const indiceFase = computed(() => fasesExamen.findIndex((f) => f.id === faseActual.value));
</script>
