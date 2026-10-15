<template>
  <PaginaPaso titulo="Relación entre edad y DMO">
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Verificando…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Completado
      </span>
      <span v-else class="chip">Pendiente · 8 preguntas</span>
    </template>

    <template #figura>
      <figure class="figura">
        <img src="/src/imagenes/img.png" alt="Gráfica de DMO vs Edad" />
        <figcaption>Gráfica de dispersión de la DMO en mujeres según la edad.</figcaption>
      </figure>
    </template>

    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Verificando tu participación…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
    </div>

    <template v-else-if="!usuarioYaParticipo">
      <Seccion titulo="Modelación de la Situación Problema" resumen="Lectura">
        <div class="lectura">
          <p>
            Para modelar la relación que existe entre la edad y la densidad mineral ósea (DMO), partiendo de los datos en una tabla, se pueden utilizar herramientas que aproximan los puntos a una curva, como por ejemplo Excel, Hojas de cálculo de Google o cualquier otra
            <a
              href="https://www.researchgate.net/publication/259608747_Age-Related_Changes_in_the_Prevalence_of_Osteoporosis_according_to_Gender_and_Skeletal_Site_The_Korea_National_Health_and_Nutrition_Examination_Survey_2008-2010#fullTextFileContent"
              target="_blank"
              rel="noopener noreferrer"
            >herramienta disponible en Internet.</a>
            La mayoría de estas herramientas proporcionan la expresión algebraica de la curva que mejor aproxima los puntos. Es decir, aquella curva que minimiza la distancia a los puntos.
          </p>
          <p>
            Una vez que se obtiene la expresión algebraica, se pueden obtener más datos o realizar una gráfica más completa (con más puntos) para realizar análisis más profundos como identificar la edad en que se alcanza una densidad mineral ósea máxima (este valor es se conoce como óptimo o pico de masa ósea).
          </p>
        </div>
      </Seccion>

      <Seccion titulo="Foro 3: Densidad mineral ósea de la cadera de mujeres" resumen="Datos de la tabla">
        <div class="grid gap-10 lg:grid-cols-[minmax(0,1fr)_300px]">
          <p class="lectura">
            Utilizando los datos del
            <a
              href="https://www.researchgate.net/publication/259608747_Age-Related_Changes_in_the_Prevalence_of_Osteoporosis_according_to_Gender_and_Skeletal_Site_The_Korea_National_Health_and_Nutrition_Examination_Survey_2008-2010#fullTextFileContent"
              target="_blank"
              rel="noopener noreferrer"
            >artículo de investigación</a>
            de Lee y colaboradores (2013, p. 184), se eligieron los datos
            de la densidad mineral ósea de la cadera (Total hip) del grupo
            de mujeres. La elección de la cadera se debe a que es un hueso
            que se fractura con mayor frecuencia en edades mayores.
          </p>
          <div class="overflow-hidden rounded-2xl border border-linea bg-superficie">
            <table class="numeral w-full text-center text-[0.9375rem]">
              <caption class="sr-only">DMO de la cadera de mujeres por edad</caption>
              <thead class="bg-hundido text-sm">
                <tr><th scope="col" class="px-4 py-2.5 font-semibold">Edad</th><th scope="col" class="px-4 py-2.5 font-semibold">Mujeres</th></tr>
              </thead>
              <tbody>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">15</th><td class="px-4 py-2.5">0.847</td></tr>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">25</th><td class="px-4 py-2.5">0.89</td></tr>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">35</th><td class="px-4 py-2.5">0.896</td></tr>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">45</th><td class="px-4 py-2.5">0.913</td></tr>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">55</th><td class="px-4 py-2.5">0.938</td></tr>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">65</th><td class="px-4 py-2.5">0.769</td></tr>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">75</th><td class="px-4 py-2.5">0.696</td></tr>
              <tr class="border-t border-linea"><th scope="row" class="px-4 py-2.5 font-semibold">85</th><td class="px-4 py-2.5">0.625</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </Seccion>

      <Seccion titulo="Cuestionario de Análisis" resumen="8 preguntas">
        <div class="space-y-10">
          <Pregunta :numero="1" v-model="r1" :rows="2" placeholder="Respuesta...">
            Calcula, con base en los datos de la tabla, ¿cuánto
            cambia la densidad mineral ósea (DMO) si la edad cambia
            15 a 25 años?
          </Pregunta>
          <Pregunta :numero="2" v-model="r2" :rows="2" placeholder="Respuesta...">
            Escríbelo como una razón de cambio promedio (DMO /
            edad) y exprésalo de forma verbal.
          </Pregunta>
          <Pregunta :numero="3" v-model="r3" :rows="2" placeholder="Respuesta...">
            En promedio por año, ¿cuánto cambia la DMO entre los
            15 y 25 años?
          </Pregunta>
          <Pregunta :numero="4" v-model="r4" :rows="3" placeholder="Respuesta...">
            Ubica esos valores en el gráfico de la mujer y traza
            una línea que una esos puntos, describe la inclinación
            de esa línea con detalle.
          </Pregunta>
          <Pregunta :numero="5" v-model="r5" :rows="3" placeholder="Respuesta...">
            Calcula la pendiente de la recta secante que une los
            dos puntos (15, 0.847) y (25, 0.890). ¿Encuentras una
            relación entre este valor y la razón promedio de cambio?
            Describe.
          </Pregunta>
          <Pregunta :numero="6" sin-campo>
            Para analizar el comportamiento de la gráfica de la
            mujer, completa la siguiente tabla:
            <template #campo>
              <div class="overflow-x-auto rounded-2xl border border-linea bg-superficie">
                <table class="w-full min-w-[640px] text-[0.9375rem]">
                  <thead class="bg-hundido text-left text-sm">
                    <tr>
                      <th scope="col" class="px-3 py-2.5 font-semibold">Intervalo</th>
                      <th scope="col" class="px-3 py-2.5 font-semibold">Razón promedio</th>
                      <th scope="col" class="px-3 py-2.5 font-semibold">Comportamiento (creciente/decreciente)</th>
                      <th scope="col" class="px-3 py-2.5 font-semibold">¿Qué pasa con la DMO?</th>
                    </tr>
                  </thead>
                  <tbody>
                  <tr class="border-t border-linea">
                    <th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[15, 25]</th>
                    <td class="p-1.5"><input v-model="t6_r1_c1" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[15, 25] · Razón promedio`" /></td>
                    <td class="p-1.5"><input v-model="t6_r1_c2" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[15, 25] · Comportamiento (creciente/decreciente)`" /></td>
                    <td class="p-1.5"><input v-model="t6_r1_c3" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[15, 25] · ¿Qué pasa con la DMO?`" /></td>
                  </tr>
                  <tr class="border-t border-linea">
                    <th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[25, 35]</th>
                    <td class="p-1.5"><input v-model="t6_r2_c1" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[25, 35] · Razón promedio`" /></td>
                    <td class="p-1.5"><input v-model="t6_r2_c2" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[25, 35] · Comportamiento (creciente/decreciente)`" /></td>
                    <td class="p-1.5"><input v-model="t6_r2_c3" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[25, 35] · ¿Qué pasa con la DMO?`" /></td>
                  </tr>
                  <tr class="border-t border-linea">
                    <th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[35, 45]</th>
                    <td class="p-1.5"><input v-model="t6_r3_c1" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[35, 45] · Razón promedio`" /></td>
                    <td class="p-1.5"><input v-model="t6_r3_c2" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[35, 45] · Comportamiento (creciente/decreciente)`" /></td>
                    <td class="p-1.5"><input v-model="t6_r3_c3" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[35, 45] · ¿Qué pasa con la DMO?`" /></td>
                  </tr>
                  <tr class="border-t border-linea">
                    <th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[45, 55]</th>
                    <td class="p-1.5"><input v-model="t6_r4_c1" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[45, 55] · Razón promedio`" /></td>
                    <td class="p-1.5"><input v-model="t6_r4_c2" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[45, 55] · Comportamiento (creciente/decreciente)`" /></td>
                    <td class="p-1.5"><input v-model="t6_r4_c3" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[45, 55] · ¿Qué pasa con la DMO?`" /></td>
                  </tr>
                  <tr class="border-t border-linea">
                    <th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[55, 65]</th>
                    <td class="p-1.5"><input v-model="t6_r5_c1" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[55, 65] · Razón promedio`" /></td>
                    <td class="p-1.5"><input v-model="t6_r5_c2" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[55, 65] · Comportamiento (creciente/decreciente)`" /></td>
                    <td class="p-1.5"><input v-model="t6_r5_c3" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[55, 65] · ¿Qué pasa con la DMO?`" /></td>
                  </tr>
                  <tr class="border-t border-linea">
                    <th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[65, 75]</th>
                    <td class="p-1.5"><input v-model="t6_r6_c1" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[65, 75] · Razón promedio`" /></td>
                    <td class="p-1.5"><input v-model="t6_r6_c2" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[65, 75] · Comportamiento (creciente/decreciente)`" /></td>
                    <td class="p-1.5"><input v-model="t6_r6_c3" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[65, 75] · ¿Qué pasa con la DMO?`" /></td>
                  </tr>
                  <tr class="border-t border-linea">
                    <th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[75, 85]</th>
                    <td class="p-1.5"><input v-model="t6_r7_c1" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[75, 85] · Razón promedio`" /></td>
                    <td class="p-1.5"><input v-model="t6_r7_c2" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[75, 85] · Comportamiento (creciente/decreciente)`" /></td>
                    <td class="p-1.5"><input v-model="t6_r7_c3" class="campo !rounded-lg !px-3 !py-2" type="text" :aria-label="`[75, 85] · ¿Qué pasa con la DMO?`" /></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </template>
          </Pregunta>
          <Pregunta :numero="7" v-model="r7" :rows="3" placeholder="Respuesta...">
            ¿Qué información aporta conocer el valor de la razón
            promedio de cambio en distintos intervalos de una
            gráfica?
          </Pregunta>
          <Pregunta :numero="8" v-model="r8" :rows="3" placeholder="Respuesta...">
            Con la información de la tabla, ¿podríamos determinar
            el valor de la DMO de una mujer de 50 años? Argumenta.
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
                <span class="avatar">{{ obtenerIniciales(item.nombre, item.apellidos || item.email) }}</span>
                <div>
                  <p class="font-semibold leading-snug">{{ item.nombre ? `${item.nombre} ${item.apellidos}` : item.email }}</p>
                  <p class="text-sm text-tenue">{{ formatearFecha(item.fecha) }}</p>
                </div>
              </div>
              <span class="chip numeral">#{{ listaRespuestas.length - index }}</span>
            </div>
            <dl class="space-y-4 text-[0.9375rem]">
              <div><dt class="font-semibold">1. Calcula, con base en los datos de la tabla</dt><dd class="mt-1 text-tenue">{{ item.r1 }}</dd></div>
              <div><dt class="font-semibold">2. Escríbelo como una razón de cambio promedio</dt><dd class="mt-1 text-tenue">{{ item.r2 }}</dd></div>
            </dl>
            <details class="group mt-4 border-t border-linea pt-3">
              <summary class="flex cursor-pointer list-none items-center gap-2 py-1 text-sm font-semibold text-a1">
                <span class="material-symbols-outlined text-[20px] transition-transform group-open:rotate-180" aria-hidden="true">expand_more</span>
                Ver respuestas completas
              </summary>
              <dl class="mt-3 space-y-4 text-[0.9375rem]">
                <div><dt class="font-semibold">3. En promedio por año</dt><dd class="mt-1 text-tenue">{{ item.r3 }}</dd></div>
                <div><dt class="font-semibold">4. Ubica esos valores en el gráfico</dt><dd class="mt-1 text-tenue">{{ item.r4 }}</dd></div>
                <div><dt class="font-semibold">5. Calcula la pendiente</dt><dd class="mt-1 text-tenue">{{ item.r5 }}</dd></div>
                <div>
                  <dt class="font-semibold">6. Completar la siguiente tabla</dt>
                  <dd class="mt-2 overflow-x-auto rounded-xl border border-linea">
                    <table class="w-full min-w-[560px] text-sm">
                      <thead class="bg-hundido text-left"><tr><th class="px-3 py-2">Intervalo</th><th class="px-3 py-2">Razón promedio</th><th class="px-3 py-2">Comportamiento</th><th class="px-3 py-2">¿Qué pasa con la DMO?</th></tr></thead>
                      <tbody class="text-tenue">
                      <tr class="border-t border-linea"><th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[15, 25]</th><td class="px-3 py-2">{{ item.t6_r1_c1 }}</td><td class="px-3 py-2">{{ item.t6_r1_c2 }}</td><td class="px-3 py-2">{{ item.t6_r1_c3 }}</td></tr>
                      <tr class="border-t border-linea"><th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[25, 35]</th><td class="px-3 py-2">{{ item.t6_r2_c1 }}</td><td class="px-3 py-2">{{ item.t6_r2_c2 }}</td><td class="px-3 py-2">{{ item.t6_r2_c3 }}</td></tr>
                      <tr class="border-t border-linea"><th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[35, 45]</th><td class="px-3 py-2">{{ item.t6_r3_c1 }}</td><td class="px-3 py-2">{{ item.t6_r3_c2 }}</td><td class="px-3 py-2">{{ item.t6_r3_c3 }}</td></tr>
                      <tr class="border-t border-linea"><th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[45, 55]</th><td class="px-3 py-2">{{ item.t6_r4_c1 }}</td><td class="px-3 py-2">{{ item.t6_r4_c2 }}</td><td class="px-3 py-2">{{ item.t6_r4_c3 }}</td></tr>
                      <tr class="border-t border-linea"><th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[55, 65]</th><td class="px-3 py-2">{{ item.t6_r5_c1 }}</td><td class="px-3 py-2">{{ item.t6_r5_c2 }}</td><td class="px-3 py-2">{{ item.t6_r5_c3 }}</td></tr>
                      <tr class="border-t border-linea"><th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[65, 75]</th><td class="px-3 py-2">{{ item.t6_r6_c1 }}</td><td class="px-3 py-2">{{ item.t6_r6_c2 }}</td><td class="px-3 py-2">{{ item.t6_r6_c3 }}</td></tr>
                      <tr class="border-t border-linea"><th scope="row" class="whitespace-nowrap px-3 py-2 text-left font-semibold">[75, 85]</th><td class="px-3 py-2">{{ item.t6_r7_c1 }}</td><td class="px-3 py-2">{{ item.t6_r7_c2 }}</td><td class="px-3 py-2">{{ item.t6_r7_c3 }}</td></tr>
                      </tbody>
                    </table>
                  </dd>
                </div>
                <div><dt class="font-semibold">7. Información de la razón promedio</dt><dd class="mt-1 text-tenue">{{ item.r7 }}</dd></div>
                <div><dt class="font-semibold">8. Determinación de DMO a los 50 años</dt><dd class="mt-1 text-tenue">{{ item.r8 }}</dd></div>
              </dl>
            </details>
          </li>
        </ul>
      </Seccion>
    </template>
  </PaginaPaso>
</template>

<script setup>
import { onMounted, ref } from "vue";
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";

const r1 = ref("");
const r2 = ref("");
const r3 = ref("");
const r4 = ref("");
const r5 = ref("");
const r7 = ref("");
const r8 = ref("");

// Estructura: t6_fila_columna
const t6_r1_c1 = ref("");
const t6_r1_c2 = ref("");
const t6_r1_c3 = ref("");
const t6_r2_c1 = ref("");
const t6_r2_c2 = ref("");
const t6_r2_c3 = ref("");
const t6_r3_c1 = ref("");
const t6_r3_c2 = ref("");
const t6_r3_c3 = ref("");
const t6_r4_c1 = ref("");
const t6_r4_c2 = ref("");
const t6_r4_c3 = ref("");
const t6_r5_c1 = ref("");
const t6_r5_c2 = ref("");
const t6_r5_c3 = ref("");
const t6_r6_c1 = ref("");
const t6_r6_c2 = ref("");
const t6_r6_c3 = ref("");
const t6_r7_c1 = ref("");
const t6_r7_c2 = ref("");
const t6_r7_c3 = ref("");
const mostrarInformacion = ref(true);

const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);

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
    const res = await fetch(
      `https://proyecto-ingenieria-software-6ccv.onrender.com/verificar_en_foro_3/${email}`
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

  if (
    !r1.value ||
    !r2.value ||
    !r3.value ||
    !r4.value ||
    !r5.value ||
    !r7.value ||
    !r8.value
  ) {
    mensaje.value = "Por favor completa al menos las primeras respuestas.";
    tipoMensaje.value = "error";
    return;
  }

  if (
    !t6_r1_c1.value ||
    !t6_r1_c2.value ||
    !t6_r1_c3.value ||
    !t6_r2_c1.value ||
    !t6_r2_c2.value ||
    !t6_r2_c3.value ||
    !t6_r3_c1.value ||
    !t6_r3_c2.value ||
    !t6_r3_c3.value ||
    !t6_r4_c1.value ||
    !t6_r4_c2.value ||
    !t6_r4_c3.value ||
    !t6_r5_c1.value ||
    !t6_r5_c2.value ||
    !t6_r5_c3.value ||
    !t6_r6_c1.value ||
    !t6_r6_c2.value ||
    !t6_r6_c3.value ||
    !t6_r7_c1.value ||
    !t6_r7_c2.value ||
    !t6_r7_c3.value
  ) {
    mensaje.value = "Por favor complete la tabla";
    tipoMensaje.value = "error";
    return;
  }

  enviando.value = true;
  mensaje.value = "Guardando...";

  try {
    const respuesta = await fetch("https://proyecto-ingenieria-software-6ccv.onrender.com/guardar_en_foro_3", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: usuarioEmail,
        r1: r1.value,
        r2: r2.value,
        r3: r3.value,
        r4: r4.value,
        r5: r5.value,
        // Campos de la tabla
        t6_r1_c1: t6_r1_c1.value,
        t6_r1_c2: t6_r1_c2.value,
        t6_r1_c3: t6_r1_c3.value,
        t6_r2_c1: t6_r2_c1.value,
        t6_r2_c2: t6_r2_c2.value,
        t6_r2_c3: t6_r2_c3.value,
        t6_r3_c1: t6_r3_c1.value,
        t6_r3_c2: t6_r3_c2.value,
        t6_r3_c3: t6_r3_c3.value,
        t6_r4_c1: t6_r4_c1.value,
        t6_r4_c2: t6_r4_c2.value,
        t6_r4_c3: t6_r4_c3.value,
        t6_r5_c1: t6_r5_c1.value,
        t6_r5_c2: t6_r5_c2.value,
        t6_r5_c3: t6_r5_c3.value,
        t6_r6_c1: t6_r6_c1.value,
        t6_r6_c2: t6_r6_c2.value,
        t6_r6_c3: t6_r6_c3.value,
        t6_r7_c1: t6_r7_c1.value,
        t6_r7_c2: t6_r7_c2.value,
        t6_r7_c3: t6_r7_c3.value,
        r7: r7.value,
        r8: r8.value,
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
    const res = await fetch("https://proyecto-ingenieria-software-6ccv.onrender.com/respuestas_en_foro_3");
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

function formatearFecha(fechaString) {
  if (!fechaString) return "";

  // Crear fecha y ajustar a la zona horaria de Hermosillo
  const fecha = new Date(fechaString);

  // Obtener la diferencia de tiempo en minutos con la zona horaria local
  const tzOffset = fecha.getTimezoneOffset();
  // Ajustar la fecha a la zona horaria de Hermosillo (UTC-7 o UTC-6 dependiendo del horario de verano)
  const hermosilloOffset = -7 * 60; // Aproximado, se ajustará según el horario de verano
  const diff = tzOffset + hermosilloOffset;
  const adjustedDate = new Date(fecha.getTime() + diff * 60 * 1000);

  // Opciones para mostrar fecha y hora
  const opciones = {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    timeZone: "America/Hermosillo",
    hour12: true,
  };

  // Usar toLocaleString con la zona horaria específica
  return adjustedDate.toLocaleString("es-MX", opciones);
}
</script>
