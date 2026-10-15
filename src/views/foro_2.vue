<template>
  <PaginaPaso titulo="Densidad mineral ósea entre hombres y mujeres">
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Verificando…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Completado
      </span>
      <span v-else class="chip">Pendiente · 6 preguntas</span>
    </template>

    <template #figura>
      <figure class="figura">
        <img src="/src/imagenes/Cadera H vs M.png" alt="Gráfico comparativo de la DMO de la cadera (Total hip) de hombres y mujeres" />
      </figure>
    </template>

    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Verificando tu participación…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
      <div class="h-4 w-1/2 animate-pulse rounded-full bg-hundido"></div>
    </div>

    <template v-else-if="!usuarioYaParticipo">
      <Seccion titulo="Modelación del problema" resumen="Lectura y figura">
        <div class="space-y-8">
          <figure class="figura">
            <img :src="foro2" alt="Gráficas de los cambios de la densidad mineral ósea por edad en espina lumbar, cadera y cuello femoral" />
          </figure>
          <div class="lectura">
            <p>
              Las graficas anteriores obtenidas del artículo: Cambios
              relacionados con la edad en la prevalencia de la
              osteoporosis según el género y la zona esquelética: Encuesta
              nacional de examen de salud y nutrición de Corea
              2008-20101,muestran los cambios en la densidad mineral ósea,
              entre los 10 y los 89 años de la espina lumbar, la cadera y
              el femur (específicamente el cuello femoral) de 17,205
              coreanos (7,837 hombres y 9,368 mujeres) como indicadores de
              la salud ósea.
            </p>
            <p class="border-t border-linea pt-4 text-[0.9375rem] text-tenue">
              1. Jongseok Lee, Sungwha Lee, Sungok Jang y Ohk Hyun Ryu
              (2013). Age-Related Changes in the Prevalence of
              Osteoporosis according to Gender and Skeletal Site: The
              Korea National Health and Nutrition Examination Survey
              2008-2010. Endocrinology and Metabolism, 28(3):180-191.
              DOI:
              <a
                class="break-all"
                href="https://e-enm.org/journal/view.php?doi=10.3803/EnM.2013.28.3.180"
                target="_blank"
                rel="noopener noreferrer"
              >https://e-enm.org/journal/view.php?doi=10.3803/EnM.2013.28.3.180</a>
            </p>
          </div>
        </div>
      </Seccion>

      <Seccion titulo="Gráfico comparativo" resumen="Cadera · hombres y mujeres">
        <p class="lectura">
          El siguiente gráfico comparativo se elaboró a partir de los
          datos del
          <a
            href="https://e-enm.org/journal/view.php?doi=10.3803/EnM.2013.28.3.180"
            target="_blank"
            rel="noopener noreferrer"
          >articulo de investigacion</a>
          de Lee y colaboradores (2013, p. 184). El gráfico muestra los
          valores de la cadera (Total hip) tanto de hombres como de
          mujeres.
        </p>
        <p class="mt-4 text-sm text-tenue">La gráfica está en la cabecera de este foro.</p>
      </Seccion>

      <Seccion titulo="Tu turno: investiga y responde" resumen="6 preguntas">
        <div class="space-y-10">
          <Pregunta :numero="1" v-model="r1" placeholder="Escribe tu análisis aquí...">
            Describe las similitudes y diferencias que observas en las
            gráficas de la DMO de la cadera entre hombres y mujeres,
            determinando aproximadamente la edad en que se presentan.
          </Pregunta>
          <Pregunta :numero="2" v-model="r2" placeholder="Tu respuesta...">
            ¿En qué etapa de la vida aumenta más la densidad mineral
            ósea en las mujeres? ¿Y de los hombres? ¿Cuál podría ser la
            causa? Justifica tu respuesta.
          </Pregunta>
          <Pregunta :numero="3" v-model="r3" placeholder="Tu respuesta...">
            ¿En qué etapa de la vida disminuye más la densidad mineral
            ósea en las mujeres? ¿Y de los hombres? ¿A qué se debe esto?
            Justifica tu respuesta.
          </Pregunta>
          <Pregunta :numero="4" v-model="r4" placeholder="Tu respuesta...">
            ¿Habrá una edad donde la densidad mineral ósea tenga un
            valor máximo? Ese valor, ¿se puede ubicar en la gráfica?
            Justifica tu respuesta.
          </Pregunta>
          <Pregunta :numero="5" v-model="r5" placeholder="Tu respuesta...">
            Analiza la siguiente afirmación argumentando por qué
            consideras que el fenómeno se comporta así: En la gráfica
            anterior se observa que la densidad mineral ósea, aumenta en
            los primeros años de vida (la gráfica crece) y luego, a partir
            de cierta edad, se comienza a perder densidad mineral ósea (la
            gráfica decrece). Entonces, hay una edad donde la densidad
            mineral ósea alcanza su valor máximo (conocido como pico de
            densidad mineral ósea) por lo que este fenómeno de variación
            (cambio) tiene un valor óptimo y es un máximo.
          </Pregunta>
          <Pregunta :numero="6" v-model="r6" placeholder="Tu respuesta...">
            ¿Cómo podemos verificar o encontrar la edad dónde se
            alcanza el valor óptimo? Lista las ideas o herramientas que
            nos pueden ayudar a encontrar la edad exacta donde se alcanza
            ese pico de masa ósea.
          </Pregunta>

          <div v-if="!invitado" class="flex flex-col gap-4 border-t border-linea pt-8 sm:flex-row sm:items-center sm:justify-between">
            <p v-if="mensaje" role="status" class="aviso" :class="tipoMensaje === 'error' ? 'aviso-error' : 'aviso-info'">
              {{ mensaje }}
            </p>
            <p v-else class="text-sm text-tenue">Al enviar verás las respuestas de tus compañeros.</p>
            <button type="button" class="boton boton-primario sm:ml-auto" :disabled="enviando" @click="enviarRespuestas">
              <span v-if="enviando" class="material-symbols-outlined animate-spin text-[20px]" aria-hidden="true">progress_activity</span>
              {{ enviando ? "Guardando…" : "Enviar respuestas" }}
            </button>
          </div>
          <AvisoInvitado v-else class="mt-2" />
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
                <span class="avatar">{{ obtenerIniciales(item.nombre, item.apellidos || item.email) }}</span>
                <div>
                  <p class="font-semibold leading-snug">{{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}</p>
                  <p class="text-sm text-tenue">{{ formatearFecha(item.fecha) }}</p>
                </div>
              </div>
              <span class="chip numeral">#{{ listaRespuestas.length - index }}</span>
            </div>
            <dl class="space-y-4 text-[0.9375rem]">
              <div><dt class="font-semibold">1. Similitudes y diferencias</dt><dd class="mt-1 text-tenue">{{ item.r1 }}</dd></div>
              <div><dt class="font-semibold">2. ¿En qué etapa de la vida aumenta más la densidad mineral?</dt><dd class="mt-1 text-tenue">{{ item.r2 }}</dd></div>
            </dl>
            <details class="group mt-4 border-t border-linea pt-3">
              <summary class="flex cursor-pointer list-none items-center gap-2 py-1 text-sm font-semibold text-a1">
                <span class="material-symbols-outlined text-[20px] transition-transform group-open:rotate-180" aria-hidden="true">expand_more</span>
                Ver respuestas completas
              </summary>
              <dl class="mt-3 space-y-4 text-[0.9375rem]">
                <div><dt class="font-semibold">3. ¿En qué etapa de la vida disminuye más la densidad mineral?</dt><dd class="mt-1 text-tenue">{{ item.r3 }}</dd></div>
                <div><dt class="font-semibold">4. ¿Habrá una edad donde la densidad mineral ósea tenga un valor máximo?</dt><dd class="mt-1 text-tenue">{{ item.r4 }}</dd></div>
                <div><dt class="font-semibold">5. Analiza la siguiente afirmación</dt><dd class="mt-1 text-tenue">{{ item.r5 }}</dd></div>
                <div><dt class="font-semibold">6. ¿Cómo podemos verificar o encontrar la edad dónde se alcanza el valor óptimo?</dt><dd class="mt-1 text-tenue">{{ item.r6 }}</dd></div>
              </dl>
            </details>
          </li>
        </ul>
      </Seccion>
    </template>
  </PaginaPaso>
</template>

<script setup>
import { esInvitado } from "@/sesion.js";
import AvisoInvitado from "@/components/AvisoInvitado.vue";
import { API_URL } from "@/api.js";
import { ref, onMounted } from "vue";
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";
import foro2 from "@/imagenes/foro2.png";
import Grafica from "@/imagenes/Grafica.png";

// Variables reactivas
const r1 = ref("");
const r2 = ref("");
const r3 = ref("");
const r4 = ref("");
const r5 = ref("");
const r6 = ref("");
const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);

// ESTADO DE CONTROL
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);
const mostrarInformacion = ref(true);

// Al cargar la página, verificamos si el usuario ya hizo la tarea
onMounted(async () => {
  const email = localStorage.getItem("usuario");
  if (email) {
    await verificarEstado(email);
  } else {
    cargandoEstado.value = false; // Si no hay usuario, mostramos formulario (luego fallará al enviar, pidiendo login)
  }
});

async function verificarEstado(email) {
  try {
    // 1. Preguntamos a Python: "¿Este email ya respondió?"
    const res = await fetch(
      `${API_URL}/verificar_foro2/${email}`
    );
    const datos = await res.json();

    if (datos.participo) {
      usuarioYaParticipo.value = true;
      // 2. Si ya respondió, cargamos la lista de todos inmediatamente
      await cargarForoCompleto();
    }
  } catch (error) {
    console.error("Error verificando estado:", error);
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

  if (!r1.value || !r2.value) {
    mensaje.value = "Por favor completa al menos las primeras respuestas.";
    tipoMensaje.value = "error";
    return;
  }

  enviando.value = true;
  mensaje.value = "Guardando...";

  try {
    const respuesta = await fetch(
      `${API_URL}/guardar_foro2`,
      {
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
        }),
      }
    );

    const datos = await respuesta.json();

    if (datos.exito) {
      // ÉXITO: Cambiamos el estado localmente para ocultar formulario y mostrar lista
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    } else {
      mensaje.value = "Error: " + datos.mensaje;
      tipoMensaje.value = "error";
    }
  } catch (error) {
    console.error(error);
    mensaje.value = "Error de conexión";
    tipoMensaje.value = "error";
  } finally {
    enviando.value = false;
  }
}

async function cargarForoCompleto() {
  try {
    const res = await fetch(
      `${API_URL}/respuestas_foro2`
    );
    listaRespuestas.value = await res.json();
  } catch (error) {
    console.error("Error cargando foro", error);
  }
}

// Utilidades visuales
function obtenerIniciales(nombre, apellidoOEmail) {
  if (nombre) {
    return (
      nombre[0] + (apellidoOEmail ? apellidoOEmail[0] : "")
    ).toUpperCase();
  }
  return apellidoOEmail.substring(0, 2).toUpperCase();
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

// Modo invitado: sin sesión se muestra el aviso en lugar del botón de enviar
const invitado = esInvitado();
</script>
