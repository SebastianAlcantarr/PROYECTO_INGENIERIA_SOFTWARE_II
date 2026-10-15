<template>
  <PaginaPaso titulo="Análisis DMO">
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Cargando actividad…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Completado
      </span>
      <span v-else class="chip">Pendiente · 7 preguntas</span>
    </template>

    <template #figura>
      <div class="overflow-hidden rounded-2xl border border-linea bg-superficie shadow-[var(--sombra-elevada)]">
        <p class="border-b border-linea px-5 py-3 text-sm font-semibold">Datos de Referencia · DMO de la cadera de las mujeres</p>
        <table class="numeral w-full text-center text-[0.9375rem]">
          <thead class="bg-hundido text-sm">
            <tr><th scope="col" class="px-4 py-2 font-semibold">Edad Promedio</th><th scope="col" class="px-4 py-2 font-semibold">DMO Cadera</th></tr>
          </thead>
          <tbody>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">15</th><td class="px-4 py-1.5">0.847</td></tr>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">25</th><td class="px-4 py-1.5">0.890</td></tr>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">35</th><td class="px-4 py-1.5">0.896</td></tr>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">45</th><td class="px-4 py-1.5">0.913</td></tr>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">55</th><td class="px-4 py-1.5">0.838</td></tr>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">65</th><td class="px-4 py-1.5">0.769</td></tr>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">75</th><td class="px-4 py-1.5">0.696</td></tr>
            <tr class="border-t border-linea"><th scope="row" class="px-4 py-1.5 font-semibold">85</th><td class="px-4 py-1.5">0.625</td></tr>
          </tbody>
        </table>
      </div>
    </template>

    <template #intro>Dada la siguiente tabla de la DMO de la cadera de las mujeres y la edad:</template>

    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Cargando actividad…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
    </div>

    <template v-else-if="!usuarioYaParticipo">
      <Seccion titulo="Cuestionario" resumen="7 preguntas">
        <div class="space-y-10">
          <Pregunta :numero="1" v-model="r1" :rows="2" placeholder="Escribe la expresión algebraica...">
            Utiliza la
            <a
              class="enlace"
              href="https://docs.google.com/spreadsheets/d/1VQdNrfdddTFhpdlPhecQD_QeMs1hLk3dhHyn3iUlkFg/edit?gid=1382532865#gid=1382532865"
              target="_blank"
              rel="noopener noreferrer"
            >hoja de cálculo de Google Drive</a>
            para generar la función que mejor aproxime los puntos y por lo
            tanto puede modelar este fenómeno. Obtén su expresión
            algebraica.
            <span class="mt-3 block">
              <a
                href="https://drive.google.com/file/d/1OgW5vZDYPk73MPUSOJ7xMfFA93FEvzUt/view?usp=sharing"
                class="recurso"
                target="_blank"
                rel="noopener noreferrer"
              ><span class="material-symbols-outlined" aria-hidden="true">play_circle</span>Ver VideoTutorial 1</a>
            </span>
          </Pregunta>
          <Pregunta :numero="2" v-model="r2" :rows="3" placeholder="Respuesta...">
            Explica las consideraciones que tomaste en cuenta para
            elegir la función que mejor aproxima los puntos.
          </Pregunta>
          <Pregunta :numero="3" v-model="r3" :rows="3" placeholder="Respuesta...">
            La función que elegiste ¿coincide con la evolución en la
            DMO a lo largo de la vida? Explica ampliamente tu respuesta.
          </Pregunta>
          <Pregunta :numero="4" v-model="r4" :rows="3" placeholder="Respuesta...">
            Calcula, usando la expresión algebraica, la densidad
            mineral ósea para una edad aleatoria de la tabla y verifica si
            el resultado obtenido es consistente. ¿Es el mismo valor? ¿A
            qué se debe?
          </Pregunta>
          <Pregunta :numero="5" v-model="r5" :rows="3" placeholder="Respuesta...">
            Con la expresión algebraica podemos obtener el valor de la
            DMO para cualquier edad. Argumenta e indica ¿qué ventajas se
            pueden tener si completamos la tabla anterior pero ahora con
            intervalos más pequeños, por ejemplo, de un año en un año?
          </Pregunta>
          <Pregunta :numero="6" v-model="r6" :rows="3" placeholder="Describe la grafica...">
            Elabora una tabla de año en año usando la segunda hoja del
            documento que subimos a Google Drive y realiza su gráfica.
            <span class="mt-3 block">
              <a
                href="https://www.canva.com/design/DAGPpllYKuA/A2O1-5xRxdaHas-Yb5jHcw/edit?utm_content=DAGPpllYKuA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
                class="recurso"
                target="_blank"
                rel="noopener noreferrer"
              ><span class="material-symbols-outlined" aria-hidden="true">play_circle</span>Ver VideoTutorial 2</a>
            </span>
          </Pregunta>
          <Pregunta :numero="7" v-model="r7" :rows="4" placeholder="Tu argumentación...">
            Argumenta ejemplificando detalladamente la siguiente
            afirmación:
            <em class="cita">
              "Con la expresión algebraica podemos obtener el valor de la
              DMO para cualquier edad, es decir se puede obtener la DMO de
              la cadera en cualquier momento de la vida, por ejemplo, a
              los 38.6 años, esto indica que el fenómeno de variación es
              continuo y la función elegida también es continua."
            </em>
          </Pregunta>

          <div class="flex flex-col gap-4 border-t border-linea pt-8 sm:flex-row sm:items-center sm:justify-between">
            <p v-if="mensaje" role="status" class="aviso" :class="tipoMensaje === 'error' ? 'aviso-error' : 'aviso-info'">
              {{ mensaje }}
            </p>
            <p v-else class="text-sm text-tenue">Al enviar verás las respuestas de tus compañeros.</p>
            <button type="button" class="boton boton-primario sm:ml-auto" :disabled="enviando" @click="enviarRespuestas">
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
              <div><dt class="font-semibold">1. Función</dt><dd class="mt-1 text-tenue">{{ item.r1 }}</dd></div>
              <div><dt class="font-semibold">2. Consideraciones</dt><dd class="mt-1 text-tenue">{{ item.r2 }}</dd></div>
            </dl>
            <details class="group mt-4 border-t border-linea pt-3">
              <summary class="flex cursor-pointer list-none items-center gap-2 py-1 text-sm font-semibold text-a1">
                <span class="material-symbols-outlined text-[20px] transition-transform group-open:rotate-180" aria-hidden="true">expand_more</span>
                Ver resto de respuestas (3-7)
              </summary>
              <dl class="mt-3 space-y-4 text-[0.9375rem]">
                <div><dt class="font-semibold">3. Coincidencia</dt><dd class="mt-1 text-tenue">{{ item.r3 }}</dd></div>
                <div><dt class="font-semibold">4. Verificación</dt><dd class="mt-1 text-tenue">{{ item.r4 }}</dd></div>
                <div><dt class="font-semibold">5. Ventajas intervalos</dt><dd class="mt-1 text-tenue">{{ item.r5 }}</dd></div>
                <div><dt class="font-semibold">6. Gráfica anual</dt><dd class="mt-1 text-tenue">{{ item.r6 }}</dd></div>
                <div><dt class="font-semibold">7. Continuidad</dt><dd class="mt-1 text-tenue">{{ item.r7 }}</dd></div>
              </dl>
            </details>
          </li>
        </ul>
      </Seccion>
    </template>
  </PaginaPaso>
</template>

<script setup>
import { ref, onMounted } from "vue";
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";

// Variables reactivas
const r1 = ref("");
const r2 = ref("");
const r3 = ref("");
const r4 = ref("");
const r5 = ref("");
const r6 = ref("");
const r7 = ref("");

const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);

onMounted(async () => {
  const email = localStorage.getItem("usuario");
  if (email) {
    await verificarEstado(email);
  } else {
    cargandoEstado.value = false;
  }
});

async function verificarEstado(email) {
  try {
    const res = await fetch(`https://proyecto-ingenieria-software-6ccv.onrender.com/verificar_foro4/${email}`);
    const datos = await res.json();
    if (datos.participo) {
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    }
  } catch (error) {
    console.error("Error verificando:", error);
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
  // Validacion basica
  if (!r1.value || !r2.value) {
    mensaje.value = "Por favor responde al menos las primeras preguntas.";
    tipoMensaje.value = "error";
    return;
  }

  enviando.value = true;
  mensaje.value = "Guardando...";

  try {
    const respuesta = await fetch("https://proyecto-ingenieria-software-6ccv.onrender.com/guardar_foro4", {
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
        r7: r7.value,
      }),
    });
    const datos = await respuesta.json();

    if (datos.exito) {
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    } else {
      mensaje.value = "Error: " + datos.mensaje;
      tipoMensaje.value = "error";
    }
  } catch (error) {
    mensaje.value = "Error de conexión";
    tipoMensaje.value = "error";
  } finally {
    enviando.value = false;
  }
}

async function cargarForoCompleto() {
  try {
    const res = await fetch("https://proyecto-ingenieria-software-6ccv.onrender.com/respuestas_foro4");
    listaRespuestas.value = await res.json();
  } catch (error) {
    console.error("Error cargando foro", error);
  }
}

// Utilidades
function obtenerIniciales(nombre, email) {
  if (nombre) return nombre[0].toUpperCase();
  return email ? email.substring(0, 2).toUpperCase() : "?";
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
