<template>
  <PaginaPaso titulo="Evalúa tu comprensión sobre el modelo">
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Verificando…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Terminado
      </span>
      <span v-else class="chip numeral">{{ preguntas.length }} preguntas</span>
    </template>
    <template #intro>
      Evalúa tu comprensión sobre el modelo que representa la
      covariación entre la densidad mineral ósea y la edad.
    </template>

    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Verificando tu participación…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
    </div>

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
            <div class="mb-4 flex items-center gap-3">
              <span class="avatar">{{ obtenerIniciales(item.nombre, item.apellidos) }}</span>
              <div>
                <p class="font-semibold leading-snug">{{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}</p>
                <p class="text-sm text-tenue">{{ formatearFecha(item.fecha) }}</p>
              </div>
            </div>
            <dl class="grid gap-3 text-[0.9375rem] sm:grid-cols-2">
              <div v-for="n in 7" :key="n" class="rounded-xl bg-hundido p-3">
                <dt class="font-semibold">Pregunta {{ n }}</dt>
                <dd class="text-tenue">{{ item['r' + n] }}</dd>
              </div>
            </dl>
          </li>
        </ul>
      </Seccion>
    </template>

    <section v-else class="border-t border-linea pt-8" aria-labelledby="titulo-examen2">
      <h2 id="titulo-examen2" class="mb-4 text-2xl font-bold tracking-[-0.02em] md:text-3xl">
        Analiza y responde el siguiente cuestionario
      </h2>

      <!-- Avance por pregunta -->
      <div v-if="faseActual === 'quiz'" class="mb-8">
        <ol class="flex max-w-xl gap-1.5" aria-label="Avance del examen">
          <li
            v-for="(p, i) in preguntas"
            :key="i"
            class="h-2 flex-1 rounded-full transition-colors duration-500"
            :class="quizFinalizado || i < preguntaActual ? 'bg-tinta' : i === preguntaActual ? 'bg-a1' : 'bg-hundido'"
          ></li>
        </ol>
        <p class="numeral mt-2 text-sm text-tenue">
          Pregunta {{ quizFinalizado ? preguntas.length : preguntaActual + 1 }} de {{ preguntas.length }}
        </p>
      </div>

      <!-- CUESTIONARIO -->
      <div v-if="!quizFinalizado" class="ficha max-w-3xl !p-6 sm:!p-8">
        <p class="text-xl font-semibold leading-snug sm:text-2xl">{{ preguntas[preguntaActual].texto }}</p>

        <template v-if="preguntaActual === 2">
          <figure class="figura mt-6">
            <img src="/src/imagenes/Grafico.jpg" alt="Gráfico de Densidad Mineral Ósea" />
          </figure>
          <p class="mt-6 font-medium">
            ¿Cómo se relaciona esto con los datos de la tabla? ¿Por
            qué la DMO no comienza en cero? Escribe tú respuesta.
          </p>
          <textarea v-model="respuestasGuardadas.r3" rows="3" placeholder="Respuesta" aria-label="Tu respuesta" class="campo mt-3"></textarea>
        </template>
        <textarea v-if="preguntaActual === 3" v-model="respuestasGuardadas.r4" rows="3" placeholder="Respuesta" aria-label="Tu respuesta" class="campo mt-6"></textarea>
        <textarea v-if="preguntaActual === 5" v-model="respuestasGuardadas.r6" rows="3" placeholder="Respuesta" aria-label="Tu respuesta" class="campo mt-6"></textarea>
        <textarea v-if="preguntaActual === 6" v-model="respuestasGuardadas.r7" rows="3" placeholder="Respuesta" aria-label="Tu respuesta" class="campo mt-6"></textarea>

        <div class="mt-6 space-y-3">
          <fieldset v-if="!preguntas[preguntaActual].tipo || preguntas[preguntaActual].tipo === 'standard'" class="space-y-3">
            <legend class="sr-only">Opciones</legend>
            <label v-for="op in preguntas[preguntaActual].opciones" :key="op" class="opcion">
              <input type="radio" name="opcion-examen2" v-model="respuestaUsuario" :value="op" />
              <span class="text-base sm:text-[1.0625rem]">{{ op }}</span>
            </label>
          </fieldset>

          <template v-else-if="preguntas[preguntaActual].tipo === 'match'">
            <div
              v-for="(item, index) in preguntas[preguntaActual].items"
              :key="index"
              class="rounded-2xl border border-linea bg-superficie p-4"
            >
              <label :for="`match-${index}`" class="mb-2 block font-medium">{{ item.pregunta }}</label>
              <select :id="`match-${index}`" v-model="respuestasMatch[index]" class="campo">
                <option :value="undefined" disabled selected>Elegir...</option>
                <option v-for="op in preguntas[preguntaActual].opciones" :key="op" :value="op">{{ op }}</option>
              </select>
            </div>
          </template>
        </div>

        <div v-if="mostrandoFeedback" role="status" class="aviso mt-6" :class="esRespuestaCorrecta ? 'aviso-ok' : 'aviso-error'">
          <span class="material-symbols-outlined" aria-hidden="true">{{ esRespuestaCorrecta ? "check_circle" : "cancel" }}</span>
          <div>
            <p class="font-semibold">{{ esRespuestaCorrecta ? "¡Correcto!" : "Respuesta Incorrecta" }}</p>
            <p
              v-if="!esRespuestaCorrecta && preguntas[preguntaActual].tipo !== 'match' && preguntas[preguntaActual].correcta"
              class="font-normal"
            >
              La respuesta correcta es: <strong>{{ preguntas[preguntaActual].correcta }}</strong>
            </p>
            <div v-else-if="!esRespuestaCorrecta && preguntas[preguntaActual].tipo === 'match'" class="mt-2 font-normal">
              <p class="font-semibold">Solución correcta:</p>
              <ul class="mt-1 list-inside list-disc space-y-1 text-sm">
                <li v-for="(item, idx) in preguntas[preguntaActual].items" :key="idx">
                  {{ item.pregunta }}: <strong>{{ item.correcta }}</strong>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="mt-8">
          <button v-if="!mostrandoFeedback" type="button" class="boton boton-primario" @click="verificarRespuesta">
            Comprobar
          </button>
          <button v-else type="button" class="boton boton-primario" @click="siguientePregunta">
            {{ preguntaActual < preguntas.length - 1 ? "Siguiente" : "Finalizar" }}
            <span class="material-symbols-outlined -mr-1 text-[20px]" aria-hidden="true">arrow_forward</span>
          </button>
        </div>
      </div>

      <!-- FINAL -->
      <div v-if="faseActual === 'final'" class="ficha max-w-2xl !p-8">
        <span class="material-symbols-outlined text-5xl text-ok" aria-hidden="true">task_alt</span>
        <h3 class="mt-3 text-3xl font-bold">Examen Terminado</h3>
        <p class="mt-1 text-tenue">Guarda tus respuestas para que el profesor pueda revisarlas.</p>
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
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";

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
    const res = await fetch(`https://proyecto-ingenieria-software-6ccv.onrender.com/verificar_examen2/${email}`);

    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();

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
    const res = await fetch("https://proyecto-ingenieria-software-6ccv.onrender.com/respuestas_examen2");

    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`);
    }

    listaRespuestas.value = await res.json();
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
  const email = localStorage.getItem("usuario"); // Ojo aquí, usé "usuario" que es lo que usas en el Login
  if (!email) return alert("Error: Inicia sesión.");

  enviando.value = true;
  try {
    const payload = {
      email: email,
      ...respuestasGuardadas.value,
    };

    const response = await fetch(`https://proyecto-ingenieria-software-6ccv.onrender.com/guardar_examen2`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const data = await response.json();

    if (data.exito) {
      usuarioYaParticipo.value = true;
      await cargarRespuestas();
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
