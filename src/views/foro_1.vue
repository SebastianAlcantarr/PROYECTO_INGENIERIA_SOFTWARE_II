<template>
  <PaginaPaso>
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Verificando…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Completado
      </span>
      <span v-else class="chip">Pendiente · 6 preguntas</span>
    </template>

    <template #figura>
      <figure class="figura">
        <img :src="Grafica" alt="Gráfica de los cambios en la densidad ósea conforme la edad, en hombres y mujeres" />
      </figure>
    </template>

    <!-- Cargando -->
    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Verificando tu participación…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
      <div class="h-4 w-1/2 animate-pulse rounded-full bg-hundido"></div>
    </div>

    <!-- Formulario: aún no participa -->
    <template v-else-if="!usuarioYaParticipo">
      <Seccion titulo="Material de lectura" resumen="Lectura y figuras">
        <div class="grid gap-10 lg:grid-cols-[minmax(0,1fr)_320px]">
          <div class="lectura">
            <p>
              La densidad ósea, también conocida como densidad mineral ósea
              (DMO), se refiere a la cantidad de tejido óseo presente en la
              estructura esquelética y se determina con la cantidad de
              minerales presentes, por lo general, calcio y fósforo (mg ) que
              contiene cierto segmento de hueso (cm2 ).
            </p>
            <p>
              Según el sitio
              <a
                href="https://kidshealth.org/es/parents/bones-muscles-joints.html#:~:text=Los%20huesos%20est%C3%A1n%20compuestos%20por,en%20otras%20partes%20del%20cuerpo."
                target="_blank"
                rel="noopener noreferrer"
              >kidshealth.org</a>, los huesos están compuestos por un armazón de colágeno y un
              mineral llamado fosfato cálcico, los cuales proporcionan
              resistencia y dureza. Desde el nacimiento hasta la edad
              adulta, el cuerpo acumula estos minerales fortaleciendo la
              densidad ósea, pero después de los 35 años, comienza la
              disminución de la densidad mineral ósea. La DMO desempeña un
              papel crucial en el control de la salud ósea del esqueleto, ya
              que se usa para diagnosticar osteoporosis (medida como
              puntuación T) y determinar si los tratamientos para aumentar
              el volumen del hueso funcionan o no.
            </p>
            <p>
              La prueba de densidad mineral ósea conocida como DEX o DEXA (o
              como BMDT, por sus siglas en inglés) mide el contenido de
              calcio y otros minerales (como fósforo) en los huesos (<strong>mg/cm<sup>2</sup></strong>).
            </p>
          </div>
          <figure class="figura self-start">
            <img :src="rango" alt="Rangos de la puntuación T de densidad mineral ósea" />
          </figure>
        </div>
      </Seccion>

      <Seccion titulo="Tu turno: investiga y responde" resumen="6 preguntas">
        <div class="space-y-10">
          <Pregunta :numero="1" v-model="r1" placeholder="Escribe tu análisis aquí...">
            Explica en qué consiste la densidad mineral ósea (DMO) y
            cómo se mide (qué pruebas se utilizan). ¿Es peligrosa su
            medición?.
          </Pregunta>
          <Pregunta :numero="2" v-model="r2" placeholder="Tu respuesta...">
            ¿Qué factores consideras que influyen en una buena salud
            ósea?
          </Pregunta>
          <Pregunta :numero="3" v-model="r3" placeholder="Tu respuesta...">
            ¿Consideras que la edad y la DMO pueden estar relacionadas
            de manera que el valor de una magnitud dependa del valor de la
            otra? Justifica..
          </Pregunta>
          <Pregunta :numero="4" v-model="r4" placeholder="Tu respuesta...">
            ¿Cómo evoluciona la DMO a lo largo de la vida/edad de las
            personas?
          </Pregunta>
          <Pregunta :numero="5" v-model="r5" placeholder="Tu respuesta...">
            Considerando lo investigado, ¿crees que, dado un valor
            normal de la DMO, se puede saber la edad aproximada de una
            persona? y ¿viceversa? Explica.
          </Pregunta>
          <Pregunta :numero="6" v-model="r6" placeholder="Tu respuesta...">
            Investiga y responde: ¿La DMO será igual para el esqueleto
            femenino y el masculino?, ¿a qué se debe?, ¿a partir de qué
            edad se pueden observar diferencias, si las hay? Justifica.
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

    <!-- Ya participó: muro del grupo -->
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
              <div><dt class="font-semibold">1. Definición DMO</dt><dd class="mt-1 text-tenue">{{ item.r1 }}</dd></div>
              <div><dt class="font-semibold">2. Factores Salud</dt><dd class="mt-1 text-tenue">{{ item.r2 }}</dd></div>
            </dl>
            <details class="group mt-4 border-t border-linea pt-3">
              <summary class="flex cursor-pointer list-none items-center gap-2 py-1 text-sm font-semibold text-a1">
                <span class="material-symbols-outlined text-[20px] transition-transform group-open:rotate-180" aria-hidden="true">expand_more</span>
                Ver respuestas completas
              </summary>
              <dl class="mt-3 space-y-4 text-[0.9375rem]">
                <div><dt class="font-semibold">3. Edad vs DMO</dt><dd class="mt-1 text-tenue">{{ item.r3 }}</dd></div>
                <div><dt class="font-semibold">4. Evolución</dt><dd class="mt-1 text-tenue">{{ item.r4 }}</dd></div>
                <div><dt class="font-semibold">5. Edad aproximada</dt><dd class="mt-1 text-tenue">{{ item.r5 }}</dd></div>
                <div><dt class="font-semibold">6. Diferencias sexo</dt><dd class="mt-1 text-tenue">{{ item.r6 }}</dd></div>
              </dl>
            </details>
          </li>
        </ul>
      </Seccion>
    </template>
  </PaginaPaso>
</template>

<script setup>
import { API_URL } from "@/api.js";
import { ref, onMounted } from "vue";
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";
import rango from "@/imagenes/rango.jpg";
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
const mostrarInformacion = ref(true);

// ESTADO DE CONTROL
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);

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
    const res = await fetch(`${API_URL}/verificar_foro1/${email}`);
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
    const respuesta = await fetch(`${API_URL}/guardar_foro1`, {
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
    });

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
    const res = await fetch(`${API_URL}/respuestas_foro1`);
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
</script>
