<template>
  <PaginaPaso titulo="Razón promedio de cambio">
    <template #estado>
      <span v-if="cargandoEstado" class="chip">Verificando…</span>
      <span v-else-if="usuarioYaParticipo" class="chip !bg-ok-fondo !text-ok">
        <span class="material-symbols-outlined text-[16px]" aria-hidden="true">check</span>Completado
      </span>
      <span v-else class="chip">Pendiente · 6 preguntas</span>
    </template>

    <template #figura>
      <div class="rounded-2xl p-6 text-center sm:p-8" style="background: var(--c-barra); color: var(--c-barra-tinta)">
        <p class="text-sm font-semibold" style="color: var(--c-barra-tenue)">Modelo de la DMO de la cadera</p>
        <p class="math-tex mt-4 overflow-x-auto font-display text-2xl font-bold tracking-[-0.01em] sm:text-[1.75rem]">
          (DMO = −0.0001 (edad<sup>2</sup>) + 0.0076 (edad) + 0.7652)
        </p>
      </div>
    </template>

    <div v-if="cargandoEstado" class="space-y-4 border-t border-linea py-10" aria-live="polite">
      <p class="text-tenue">Verificando tu participación…</p>
      <div class="h-4 w-2/3 animate-pulse rounded-full bg-hundido"></div>
    </div>

    <template v-else-if="!usuarioYaParticipo">
      <Seccion titulo="La tabla de año en año" resumen="Pregunta 1">
        <div class="space-y-6">
          <Pregunta :numero="1" sin-campo>
            A la tabla de año en año, que se construyó en el
            <a
              class="enlace"
              href="https://docs.google.com/spreadsheets/d/1VQdNrfdddTFhpdlPhecQD_QeMs1hLk3dhHyn3iUlkFg/edit?gid=1382532865#gid=1382532865"
              target="_blank"
              rel="noopener noreferrer"
            >DRIVE (foro 4)</a>, le vamos a agregar una tercera columna (como se muestra en la tabla de abajo) para obtener la
            razón promedio de cambio (RPC) para puntos consecutivos.
            <template #campo>
              <div class="grid gap-6 lg:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
                <div class="overflow-x-auto rounded-2xl border border-linea bg-superficie">
                  <table class="numeral w-full text-center text-[0.9375rem]">
                    <thead class="bg-hundido text-sm">
                      <tr>
                        <th scope="col" class="px-4 py-2.5 font-semibold">Edad Promedio</th>
                        <th scope="col" class="px-4 py-2.5 font-semibold">DMO Cadera Segun el modelo</th>
                        <th scope="col" class="px-4 py-2.5 font-semibold">Razón promedio de cambio</th>
                      </tr>
                    </thead>
                    <tbody>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">1</th><td class="px-4 py-2">0.775400</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">2</th><td class="px-4 py-2">0.782600</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">3</th><td class="px-4 py-2">0.789600</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">4</th><td class="px-4 py-2">0.796400</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">5</th><td class="px-4 py-2">0.803000</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">6</th><td class="px-4 py-2">0.809400</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">7</th><td class="px-4 py-2">0.815600</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">8</th><td class="px-4 py-2">0.821600</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">9</th><td class="px-4 py-2">0.827400</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">10</th><td class="px-4 py-2">0.833000</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">...</th><td class="px-4 py-2">0.838400</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">89</th><td class="px-4 py-2">0.643400</td><td class="px-4 py-2 text-tenue"></td></tr>
                <tr class="border-t border-linea"><th scope="row" class="px-4 py-2 font-semibold">90</th><td class="px-4 py-2">0.633000</td><td class="px-4 py-2 text-tenue"></td></tr>
                    </tbody>
                  </table>
                </div>
                <div>
                  <p class="cita !mt-0 text-[0.9375rem]">
                    NOTA: En la tabla, que se muestra, la Absorbancia se obtuvo
                    con la expresión algebraica del modelo que aproxima el
                    fenómeno
                  </p>
                  <Tresfotos @updateFotos="recibirTresFotos" />
                </div>
              </div>
            </template>
          </Pregunta>
        </div>
      </Seccion>

      <Seccion titulo="Cuestionario" resumen="Preguntas 2 a 6">
        <div class="space-y-10">
          <Pregunta :numero="2" v-model="respuestas.r2" :rows="2" placeholder="Respuesta...">
            Observa y describe el comportamiento de la RPC
            conforme avanza la edad (crece cada vez más / crece cada
            vez menos /decrece cada vez más/ decrece cada vez
            menos).
          </Pregunta>
          <Pregunta :numero="3" sin-campo>
            Realiza un bosquejo de la gráfica en tu cuaderno
            usando los valores de la razón promedio de cambio
            (rectas secantes) observando cómo cambian sus
            pendientes. Sube tu bosquejo y responde si ¿coincide con
            la forma en cómo varía la DMO a lo largo de la vida?
            ¿Qué elementos de la razón promedio de cambio permiten
            asegurar que este problema tiene un valor máximo y no un
            valor mínimo? Argumenta.
            <template #campo>
              <Unafoto @updateFoto="recibirFoto" />
            </template>
          </Pregunta>
          <Pregunta :numero="4" v-model="respuestas.r4" :rows="2" placeholder="Respuesta...">
            Ubica en la tabla el valor óptimo de la DMO de la
            cadera de las mujeres ¿cómo podemos argumentar usando
            la razón promedio de cambio, que el valor es máximo y
            no mínimo?
          </Pregunta>
          <Pregunta :numero="5" v-model="respuestas.r5" :rows="3" placeholder="Respuesta...">
            ¿El valor máximo de la DMO es igual al que habías
            dado en la pregunta #4 del foro 2? Explica ampliamente
            qué otras herramientas tienes ahora que te permiten
            reafirmar o modificar el resultado anterior.
          </Pregunta>
          <Pregunta :numero="6" v-model="respuestas.r6" :rows="3" placeholder="Respuesta...">
            Argumenta, utilizando rectas secantes, la siguiente
            afirmación: La razón promedio de cambio (RPC) puede
            describir el comportamiento de una función, por
            ejemplo, aquella que es siempre creciente o aquella
            que crece cada vez menos o una que sea constante, es
            decir que no crece ni decrece, o una función que
            decrece cada vez más.
          </Pregunta>

          <div class="flex flex-col gap-4 border-t border-linea pt-8 sm:flex-row sm:items-center sm:justify-between">
            <p class="text-sm text-tenue">Al enviar verás las respuestas de tus compañeros.</p>
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
            <div class="mb-4 flex items-center gap-3">
              <span class="avatar">{{ obtenerIniciales(item.nombre, item.email) }}</span>
              <div>
                <p class="font-semibold leading-snug">{{ item.nombre }} {{ item.apellidos }}</p>
                <p class="text-sm text-tenue">{{ formatearFecha(item.fecha) }}</p>
              </div>
            </div>

            <div class="space-y-5 text-[0.9375rem]">
              <div v-if="item.imagen_1_url || item.imagen_2_url || item.imagen_3_url">
                <p class="mb-2 font-semibold">1. Fotos de la tabla con Razón Promedio de Cambio</p>
                <div class="grid grid-cols-1 gap-3 sm:grid-cols-3">
                  <a v-if="item.imagen_1_url" :href="item.imagen_1_url" target="_blank" rel="noopener noreferrer"><img :src="item.imagen_1_url" alt="Foto 1 de la tabla" class="h-44 w-full rounded-xl border border-linea object-cover" /></a>
                  <a v-if="item.imagen_2_url" :href="item.imagen_2_url" target="_blank" rel="noopener noreferrer"><img :src="item.imagen_2_url" alt="Foto 2 de la tabla" class="h-44 w-full rounded-xl border border-linea object-cover" /></a>
                  <a v-if="item.imagen_3_url" :href="item.imagen_3_url" target="_blank" rel="noopener noreferrer"><img :src="item.imagen_3_url" alt="Foto 3 de la tabla" class="h-44 w-full rounded-xl border border-linea object-cover" /></a>
                </div>
              </div>
              <div v-if="item.r2">
                <p class="font-semibold">2. Observa y describe el comportamiento de la RPC</p>
                <p class="mt-1 text-tenue">{{ item.r2 }}</p>
              </div>
              <div v-if="item.imagen_pregunta_3_url">
                <p class="mb-2 font-semibold">3. Bosquejo de la gráfica</p>
                <a :href="item.imagen_pregunta_3_url" target="_blank" rel="noopener noreferrer"><img :src="item.imagen_pregunta_3_url" alt="Bosquejo de la gráfica" class="max-h-56 rounded-xl border border-linea" /></a>
              </div>
            </div>

            <details v-if="item.r3 || item.r4 || item.r5 || item.r6" class="group mt-4 border-t border-linea pt-3">
              <summary class="flex cursor-pointer list-none items-center gap-2 py-1 text-sm font-semibold text-a1">
                <span class="material-symbols-outlined text-[20px] transition-transform group-open:rotate-180" aria-hidden="true">expand_more</span>
                Ver respuestas completas
              </summary>
              <dl class="mt-3 space-y-4 text-[0.9375rem]">
                <div v-if="item.r4"><dt class="font-semibold">4. Ubica en la tabla el valor óptimo de la DMO de la cadera de las mujeres</dt><dd class="mt-1 text-tenue">{{ item.r4 }}</dd></div>
                <div v-if="item.r5"><dt class="font-semibold">5. ¿El valor máximo de la DMO es igual al que habías dado en Foro 2?</dt><dd class="mt-1 text-tenue">{{ item.r5 }}</dd></div>
                <div v-if="item.r6"><dt class="font-semibold">6. Argumenta utilizando rectas secantes</dt><dd class="mt-1 text-tenue">{{ item.r6 }}</dd></div>
                <div v-if="item.r7"><dt class="font-semibold">7. ¿Cómo encontrar la edad donde se alcanza el valor óptimo?</dt><dd class="mt-1 text-tenue">{{ item.r7 }}</dd></div>
              </dl>
            </details>
          </li>
        </ul>
      </Seccion>
    </template>
  </PaginaPaso>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import PaginaPaso from "@/components/PaginaPaso.vue";
import Seccion from "@/components/Seccion.vue";
import Pregunta from "@/components/Pregunta.vue";
import Unafoto from "./unafoto.vue";
import Tresfotos from "@/views/tresfotos.vue";

const enviando = ref(false);
const cargandoEstado = ref(true);
const usuarioYaParticipo = ref(false);
const listaRespuestas = ref([]);

const respuestas = reactive({
  r2: "",
  r3: "",
  r4: "",
  r5: "",
  r6: "",
});

const imagenPregunta3 = ref(null); // 1 foto
const imagenes3 = ref([]); // 3 fotos

onMounted(async () => {
  const email = localStorage.getItem("usuario");
  if (email) {
    await verificarEstado(email);
  } else {
    cargandoEstado.value = false;
  }
});

function recibirFoto(file) {
  imagenPregunta3.value = file;
}

function recibirTresFotos(files) {
  imagenes3.value = files;
}

async function enviarRespuestas() {
  enviando.value = true;
  const email = localStorage.getItem("usuario");
  const formData = new FormData();

  formData.append("r2", respuestas.r2);
  formData.append("r3", respuestas.r3);
  formData.append("r4", respuestas.r4);
  formData.append("r5", respuestas.r5);
  formData.append("r6", respuestas.r6);

  // Imagen de la pregunta 3 (1 foto)
  if (imagenPregunta3.value) {
    formData.append("imagen_pregunta_3", imagenPregunta3.value);
  }

  // Las 3 fotos de la tabla (pregunta 1)
  for (const file of imagenes3.value) {
    formData.append("imagenes", file);
  }

  try {
    const res = await fetch(`https://proyecto-ingenieria-software-6ccv.onrender.com/guardar_foro5/${email}`, {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    if (data.exito) {
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    }
  } catch (error) {
    console.error("Error al enviar respuestas:", error);
  } finally {
    enviando.value = false;
  }
}

async function verificarEstado(email) {
  try {
    const res = await fetch(
      `https://proyecto-ingenieria-software-6ccv.onrender.com/verificar_en_foro_5/${email}`
    );
    const datos = await res.json();

    if (datos.participo) {
      usuarioYaParticipo.value = true;
      await cargarForoCompleto();
    }
  } catch (error) {
    console.error("Error verificando estado:", error);
  } finally {
    cargandoEstado.value = false;
  }
}

async function cargarForoCompleto() {
  try {
    const res = await fetch("https://proyecto-ingenieria-software-6ccv.onrender.com/respuestas_en_foro_5");
    listaRespuestas.value = await res.json();
  } catch (error) {
    console.error("Error cargando foro", error);
  }
}

function obtenerIniciales(nombre, apellidoOEmail) {
  if (nombre) {
    return (
      nombre[0] + (apellidoOEmail ? apellidoOEmail[0] : "")
    ).toUpperCase();
  }
  return apellidoOEmail ? apellidoOEmail.substring(0, 2).toUpperCase() : "??";
}

function formatearFecha(fechaString) {
  if (!fechaString) return "";
  const fecha = new Date(fechaString);
  const opciones = {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hour12: true,
  };
  return fecha.toLocaleString("es-MX", opciones);
}
</script>
