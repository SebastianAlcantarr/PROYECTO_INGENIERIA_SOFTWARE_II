<template>
  <PaginaPaso titulo="Covariación de las magnitudes">
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Cargando actividad…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Completado
      </span>
      <span v-else class="chip">Pendiente · 8 preguntas</span>
    </template>

    <template #figura>
      <div class="rounded-2xl p-6 sm:p-8" style="background: var(--c-barra); color: var(--c-barra-tinta)">
        <p class="text-sm font-semibold" style="color: var(--c-barra-tenue)">Definición Formal de Derivada</p>
        <div class="math-tex mt-2 overflow-x-auto text-xl sm:text-2xl">
          $$ f'(x) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) -
          f(x)}{\Delta x} $$
        </div>
      </div>
    </template>

    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Cargando actividad…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
    </div>

    <template v-else-if="!usuarioYaParticipo">
      <Seccion titulo="Gráficas Geogebra" resumen="Applet interactivo">
        <p class="lectura">
          Manipula el Applet para observar el comportamiento de la recta
          secante cuando <span class="math-tex">$\Delta x \to 0$</span>.
        </p>
        <div class="mt-6 overflow-x-auto rounded-2xl border border-linea bg-white p-1">
          <div id="geogebra-container" class="h-[550px] w-full"></div>
        </div>
        <a
          href="https://docs.google.com/spreadsheets/d/1Rqp6bml35xrT-5UkAyB3Qlx_c5nKijIqD6apvLbN4y4/edit?usp=sharing"
          target="_blank"
          rel="noopener noreferrer"
          class="recurso mt-5"
        ><span class="material-symbols-outlined" aria-hidden="true">table_view</span>Abrir Simulador de Google Sheets</a>
      </Seccion>

      <Seccion titulo="Cuestionario" resumen="8 preguntas">
        <div class="space-y-10">
          <Pregunta :numero="1" v-model="form.r1" :rows="3" placeholder="Escribe tu justificación...">
            ¿Qué valores puede tomar la variable
            <span class="math-tex">$x$</span> (Edad de una persona)? Es
            decir, ¿Cuál es el dominio real de esta variable? Justifica.
            <span class="cita text-[0.9375rem]">
              Nota: Observa qué pasa con la pendiente cuando el intervalo
              <span class="math-tex">$\Delta x$</span> se hace cada vez más
              pequeño (<span class="math-tex">$\Delta x \to 0$</span>).
            </span>
          </Pregunta>
          <Pregunta :numero="2" v-model="form.r2" :rows="3" placeholder="Tu argumento...">
            Argumenta con ejemplos la siguiente afirmación: Cuando los
            extremos del intervalo son iguales (<span class="math-tex">$\Delta x \to 0$</span>), la recta secante se convierte en recta tangente.
          </Pregunta>
          <Pregunta :numero="3" v-model="form.r3" :rows="5" placeholder="a) ...&#10;b) ...&#10;c) ...">
            Utiliza el simulador para observar la razón promedio cuando
            elegimos dos edades muy próximas (<span class="math-tex">$\Delta x \to 0$</span>). Responde:
            <ol class="mt-3 space-y-1.5 font-normal">
              <li><strong>a)</strong> ¿DMO y razón instantánea a los 19 años?</li>
              <li><strong>b)</strong> ¿DMO y razón instantánea a los 31 años?</li>
              <li><strong>c)</strong> ¿DMO y razón instantánea a los 84 años?</li>
            </ol>
          </Pregunta>
          <Pregunta :numero="4" v-model="form.r4" :rows="3" placeholder="Tu respuesta...">
            Manipula el Applet de Geogebra. Verifica que los resultados
            coinciden. ¿Cuánto vale la pendiente de la recta tangente en
            el valor máximo? ¿Y en el mínimo?
          </Pregunta>
          <Pregunta :numero="5" v-model="form.r5" :rows="3" placeholder="Tu respuesta...">
            Argumenta con ejemplos: ¿Cómo cambia el valor de la
            pendiente cuando es un máximo vs cuando es un mínimo?
          </Pregunta>
          <Pregunta :numero="6" v-model="form.r6" :rows="2" placeholder="Escribe aquí...">
            Definición Formal de Derivada
            <span class="math-tex mt-3 block overflow-x-auto rounded-2xl bg-hundido p-4 text-center text-xl font-normal">
              $$ f'(x) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) -
              f(x)}{\Delta x} $$
            </span>
            <span class="mt-3 block text-sm font-normal text-tenue">Tus notas sobre esta definición (Opcional):</span>
          </Pregunta>
          <Pregunta :numero="7" v-model="form.r7" :rows="6" placeholder="Desarrollo y pasos...">
            Dada la función que describe el comportamiento de la DMO:
            <span class="math-tex mt-3 block overflow-x-auto rounded-2xl bg-hundido p-4 text-center text-xl font-normal">
              $$ DMO(x) = -0.0001x^2 + 0.0075x + 0.768 $$
            </span>
            <ol class="mt-3 space-y-1.5 font-normal">
              <li><strong>a)</strong> Obtén la edad del óptimo usando la definición formal de derivada.</li>
              <li><strong>b)</strong> Lista los pasos que se deben realizar como si estuvieras dando una receta.</li>
            </ol>
          </Pregunta>
          <Pregunta :numero="8" v-model="form.r8" :rows="3" placeholder="Tu respuesta...">
            Siguiendo los pasos descritos anteriormente, obtén la edad
            en que se obtiene la DMO óptima para la cadera de los hombres
            dados los datos.
          </Pregunta>

          <div class="flex flex-col gap-4 border-t border-linea pt-8 sm:flex-row sm:items-center sm:justify-between">
            <p v-if="mensaje" role="status" class="aviso" :class="tipoMensaje === 'error' ? 'aviso-error' : 'aviso-info'">
              {{ mensaje }}
            </p>
            <p v-else class="text-sm text-tenue">Al enviar verás las respuestas de tus compañeros.</p>
            <button type="button" class="boton boton-primario sm:ml-auto" :disabled="enviando" @click="enviar">
              <span v-if="enviando" class="material-symbols-outlined animate-spin text-[20px]" aria-hidden="true">progress_activity</span>
              {{ enviando ? "Guardando…" : "Enviar respuestas" }}
            </button>
          </div>
        </div>
      </Seccion>
    </template>

    <template v-else>
      <div class="aviso aviso-ok mb-8">
        <span class="material-symbols-outlined" aria-hidden="true">check_circle</span>
        <div>
          <p class="font-semibold">Actividad Completada</p>
          <p class="font-normal">Gracias por tu aporte. Aquí están las respuestas de tus compañeros.</p>
        </div>
      </div>

      <Seccion titulo="Participaciones del grupo" :resumen="`${listaRespuestas.length} respuestas`">
        <p v-if="listaRespuestas.length === 0" class="py-6 text-tenue">
          Aún no hay respuestas de otros estudiantes.
        </p>
        <ul v-else class="grid gap-4">
          <li v-for="(item, index) in listaRespuestas" :key="index" class="ficha">
            <div class="mb-4 flex items-start justify-between gap-4">
              <div class="flex items-center gap-3">
                <span class="avatar">{{ obtenerIniciales(item.nombre, item.email) }}</span>
                <div>
                  <p class="font-semibold leading-snug">{{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}</p>
                  <p class="text-sm text-tenue">{{ formatearFecha(item.fecha) }}</p>
                </div>
              </div>
              <span class="chip numeral">#{{ listaRespuestas.length - index }}</span>
            </div>
            <dl class="space-y-4 text-[0.9375rem]">
              <div><dt class="font-semibold">1. Dominio</dt><dd class="mt-1 text-tenue">{{ item.r1 }}</dd></div>
            </dl>
            <details class="group mt-4 border-t border-linea pt-3">
              <summary class="flex cursor-pointer list-none items-center gap-2 py-1 text-sm font-semibold text-a1">
                <span class="material-symbols-outlined text-[20px] transition-transform group-open:rotate-180" aria-hidden="true">expand_more</span>
                Ver todo
              </summary>
              <dl class="mt-3 space-y-4 text-[0.9375rem]">
                <div><dt class="font-semibold">2. Argumento</dt><dd class="mt-1 text-tenue">{{ item.r2 }}</dd></div>
                <div><dt class="font-semibold">3. Utiliza el simulador</dt><dd class="mt-1 whitespace-pre-wrap text-tenue">{{ item.r3 }}</dd></div>
                <div><dt class="font-semibold">4. GeoGebra</dt><dd class="mt-1 text-tenue">{{ item.r4 }}</dd></div>
                <div><dt class="font-semibold">5. Pendientes</dt><dd class="mt-1 text-tenue">{{ item.r5 }}</dd></div>
                <div><dt class="font-semibold">6. Notas</dt><dd class="mt-1 text-tenue">{{ item.r6 }}</dd></div>
                <div><dt class="font-semibold">7. Dada la función</dt><dd class="mt-1 text-tenue">{{ item.r7 }}</dd></div>
                <div><dt class="font-semibold">8. Hombres</dt><dd class="mt-1 text-tenue">{{ item.r8 }}</dd></div>
              </dl>
            </details>
          </li>
        </ul>
      </Seccion>
    </template>
  </PaginaPaso>
</template>

<script setup>
import { ref, reactive, onMounted, nextTick } from "vue";
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";

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
