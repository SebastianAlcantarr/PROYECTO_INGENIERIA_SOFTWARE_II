<template>
  <div
    class="flex flex-col md:flex-row min-h-screen bg-[#244a76] dark:bg-[rgb(16,22,34)]"
  >
    <!-- sidebar -->
    <Sidebar class="hidden md:block" />

    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-5xl">
          <!-- titulo -->
          <section class="scroll-mt-20 mb-8">
            <div
              class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-blue-500"
            >
              <h1
                class="text-white text-3xl md:text-3xl font-black text-center"
              >
                Foro 5. Razón promedio de cambio
              </h1>
            </div>
          </section>

          <!-- contexto -->
          <section class="mb-8 animate-fade-in">
            <div class="">
              <div v-if="cargandoEstado" class="text-center py-10">
                <p class="text-blue-200 text-xl animate-pulse">
                  Verificando tu participación...
                </p>
              </div>

              <section
                v-else-if="!usuarioYaParticipo"
                class="space-y-6 animate-fade-in"
              >
                <h2
                  class="text-white text-sm font-bold px-2 flex items-center gap-2"
                >
                  <span class="material-symbols-outlined">quiz</span>
                  Cuestionario
                </h2>
                <p class="text-gray-300 text-base mb-6 leading-relaxed">
                  1. A la tabla de año en año, que se construyó en el
                  <a
                      href="https://docs.google.com/spreadsheets/d/1VQdNrfdddTFhpdlPhecQD_QeMs1hLk3dhHyn3iUlkFg/edit?gid=1382532865#gid=1382532865"
                      class="text-blue-400 hover:underline"
                      target="_blank"
                      rel="noopener noreferrer"
                  >DRIVE (foro 4)</a
                  >, le vamos a agregar una tercera columna (como se muestra en la tabla de abajo) para obtener la
                  razón promedio de cambio (RPC) para puntos consecutivos.
                  <tresfotos @updateFotos="recibirTresFotos" />
                </p>


                <div class="flex justify-center w-full my-6">
                  <!-- tabla1 -->
                  <div
                    class="w-full max-w-4xl bg-[#1a2232] rounded-xl overflow-hidden shadow-2xl"
                  >
                    <table class="w-full text-base text-center text-gray-300">
                      <thead class="text-base text-white uppercase bg-blue-700">
                        <tr>
                          <th
                            scope="col"
                            class="px-8 py-4 border-b-2 border-blue-600"
                          >
                            Edad Promedio
                          </th>
                          <th
                            scope="col"
                            class="px-8 py-4 border-b-2 border-blue-600"
                          >
                            DMO Cadera Segun el modelo
                          </th>
                          <th
                            scope="col"
                            class="px-8 py-4 border-b-2 border-blue-600"
                          >
                            Razón promedio de cambio
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649] transition-colors duration-200"
                        >
                          <td
                            class="px-8 py-4 text-lg font-semibold text-white"
                          >
                            1
                          </td>
                          <td class="px-8 py-4 text-lg">0.775400</td>
                          <td
                            class="px-8 py-4 text-lg font-medium text-blue-300"
                          ></td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            2
                          </td>
                          <td class="px-6 py-3 text-center">0.782600</td>
                        </tr>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            3
                          </td>
                          <td class="px-6 py-3 text-center">0.789600</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            4
                          </td>
                          <td class="px-6 py-3 text-center">0.796400</td>
                        </tr>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            5
                          </td>
                          <td class="px-6 py-3 text-center">0.803000</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            6
                          </td>
                          <td class="px-6 py-3 text-center">0.809400</td>
                        </tr>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            7
                          </td>
                          <td class="px-6 py-3 text-center">0.815600</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            8
                          </td>

                          <td class="px-6 py-3 text-center">0.821600</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            9
                          </td>

                          <td class="px-6 py-3 text-center">0.827400</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            10
                          </td>

                          <td class="px-6 py-3 text-center">0.833000</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            ...
                          </td>

                          <td class="px-6 py-3 text-center">0.838400</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            89
                          </td>

                          <td class="px-6 py-3 text-center">0.643400</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            90
                          </td>

                          <td class="px-6 py-3 text-center">0.633000</td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

                <div>
                  <em
                    class="block mt-2 pl-4 border-l-2 border-blue-600 text-gray-400"
                  >
                    NOTA: En la tabla, que se muestra, la Absorbancia se obtuvo
                    con la expresión algebraica del modelo que aproxima el
                    fenómeno
                  </em>

                  <div class="bg-blue-900/10 p-6 rounded-r-xl shadow-sm mt-6">
                    <div
                      class="text-2xl text-center text-blue-200 tracking-wider my-6 bg-[#0f172a] p-6 rounded-lg border border-blue-900/50 shadow-inner overflow-x-auto math-tex font-style: italic"
                    >
                      (DMO = −0.0001 (edad<sup>2</sup>) + 0.0076 (edad) +
                      0.7652)
                    </div>
                  </div>
                </div>


                <section
                  class="space-y-6 animate-fade-in"
                  style="animation-delay: 0.2s"
                >
                  <div
                    class="bg-[#161d2b] p-6 rounded-xl shadow-xl space-y-8 border border-gray-700"
                  >
                    <!-- P2 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        2. Observa y describe el comportamiento de la RPC
                        conforme avanza la edad (crece cada vez más / crece cada
                        vez menos /decrece cada vez más/ decrece cada vez
                        menos).
                      </h3>
                      <textarea
                        v-model="respuestas.r2"
                        rows="2"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <!-- P3 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium pb-5">
                        3. Realiza un bosquejo de la gráfica en tu cuaderno
                        usando los valores de la razón promedio de cambio
                        (rectas secantes) observando cómo cambian sus
                        pendientes. Sube tu bosquejo y responde si ¿coincide con
                        la forma en cómo varía la DMO a lo largo de la vida?
                        ¿Qué elementos de la razón promedio de cambio permiten
                        asegurar que este problema tiene un valor máximo y no un
                        valor mínimo? Argumenta.
                      </h3>
                      <!-- FOTO (Opcional) Mejorado -->
                      <div class="mt-6">
                        <Unafoto @updateFoto="recibirFoto" />
                      </div>

                      <!-- P3 -->
                      <div>
                        <h3
                          class="text-base text-white/90 mb-3 font-medium mt-10"
                        >
                          4. Ubica en la tabla el valor óptimo de la DMO de la
                          cadera de las mujeres ¿cómo podemos argumentar usando
                          la razón promedio de cambio, que el valor es máximo y
                          no mínimo?
                        </h3>
                        <textarea
                          v-model="respuestas.r4"
                          rows="2"
                          placeholder="Respuesta..."
                          class="input-foro"
                        ></textarea>
                      </div>

                      <!-- P4 -->
                      <div>
                        <h3 class="text-base text-white/90 mb-3 font-medium">
                          5. ¿El valor máximo de la DMO es igual al que habías
                          dado en la pregunta #4 del foro 2? Explica ampliamente
                          qué otras herramientas tienes ahora que te permiten
                          reafirmar o modificar el resultado anterior.
                        </h3>
                        <textarea
                          v-model="respuestas.r5"
                          rows="3"
                          placeholder="Respuesta..."
                          class="input-foro"
                        ></textarea>
                      </div>

                      <!-- P6 -->
                      <div>
                        <h3 class="text-base text-white/90 mb-3 font-medium">
                          6. Argumenta, utilizando rectas secantes, la siguiente
                          afirmación: La razón promedio de cambio (RPC) puede
                          describir el comportamiento de una función, por
                          ejemplo, aquella que es siempre creciente o aquella
                          que crece cada vez menos o una que sea constante, es
                          decir que no crece ni decrece, o una función que
                          decrece cada vez más.
                        </h3>
                        <textarea
                          v-model="respuestas.r6"
                          rows="3"
                          placeholder="Respuesta..."
                          class="input-foro"
                        ></textarea>
                      </div>

                      <div
                        class="pt-6 border-t border-gray-700 flex justify-end"
                      >
                        <button
                          @click="enviarRespuestas"
                          :disabled="enviando"
                          class="bg-blue-500 hover:bg-blue-900 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                        >
                          <span
                            v-if="enviando"
                            class="material-symbols-outlined animate-spin"
                            >refresh</span
                          >
                          {{ enviando ? "Guardando..." : "Enviar Respuestas" }}
                        </button>
                      </div>
                    </div>
                  </div>
                </section>
              </section>
            </div>

            <!-- preguntas -->
            <section v-if="usuarioYaParticipo" class="animate-fade-in mt-12">
              <div
                class="bg-green-900/30 border border-green-500/50 p-4 rounded-xl mb-8 flex items-center gap-4 text-green-200"
              >
                <span class="material-symbols-outlined text-3xl"
                  >check_circle</span
                >
                <div>
                  <h3 class="font-bold text-base">Actividad Completada</h3>
                  <p class="text-sm opacity-80">
                    Gracias por tu aporte. Aquí están las respuestas de tus
                    compañeros.
                  </p>
                </div>
              </div>

              <div
                v-for="(item, index) in listaRespuestas"
                :key="index"
                class="bg-[#161d2b] p-6 rounded-xl border border-gray-700 shadow-lg hover:border-blue-500/50 transition-colors"
              >
                <!-- 🔹 Encabezado -->
                <div
                  class="flex items-center gap-4 mb-4 border-b border-gray-700 pb-4"
                >
                  <div
                    class="w-12 h-12 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white font-bold text-lg shadow-lg"
                  >
                    {{ obtenerIniciales(item.nombre, item.email) }}
                  </div>
                  <div>
                    <h3 class="text-white font-bold text-lg">
                      {{ item.nombre }} {{ item.apellidos }}
                    </h3>
                    <p class="text-blue-300 text-sm">
                      {{ formatearFecha(item.fecha) }}
                    </p>
                  </div>
                </div>

                <!-- 🔹 Contenido de respuestas -->
                <div class="space-y-4 text-gray-300">
                  <!-- Las 3 fotos de la tabla (pregunta 1) -->
                  <div
                    v-if="
                      item.imagen_1_url ||
                      item.imagen_2_url ||
                      item.imagen_3_url
                    "
                  >
                    <p class="text-sm text-gray-500 mb-2">
                      1. Fotos de la tabla con Razón Promedio de Cambio
                    </p>
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                      <img
                        v-if="item.imagen_1_url"
                        :src="item.imagen_1_url"
                        class="rounded-lg shadow-md max-w-full h-50 object-cover border border-gray-700"
                      />
                      <img
                        v-if="item.imagen_2_url"
                        :src="item.imagen_2_url"
                        class="rounded-lg shadow-md max-w-full h-50 object-cover border  border-gray-700"
                      />
                      <img
                        v-if="item.imagen_3_url"
                        :src="item.imagen_3_url"
                        class="rounded-lg shadow-md max-w-full h-50 object-cover border border-gray-700"
                      />
                    </div>
                  </div>

                  <!-- Siempre visibles -->
                  <div v-if="item.r2">
                    <p class="text-sm text-gray-500 mb-1">
                      2. Observa y describe el comportamiento de la RPC
                    </p>
                    <p class="bg-[#0f172a] p-3 rounded-lg">{{ item.r2 }}</p>
                  </div>

                  <div v-if="item.imagen_pregunta_3_url">
                    <p class="text-sm text-gray-500 mb-1">
                      3. Bosquejo de la gráfica
                    </p>
                    <img
                      :src="item.imagen_pregunta_3_url"
                      class="rounded-lg shadow-md max-w-full h-30 border border-gray-700"
                    />
                  </div>

                  <!-- Expandibles -->
                  <details
                    class="text-gray-400 cursor-pointer group"
                    v-if="item.r3 || item.r4 || item.r5 || item.r6"
                  >
                    <summary
                      class="hover:text-white list-none flex items-center gap-2 py-2"
                    >
                      <span
                        class="material-symbols-outlined text-sm group-open:rotate-180 transition-transform"
                        >expand_more</span
                      >
                      Ver respuestas completas...
                    </summary>

                    <div
                      class="mt-2 space-y-4 pt-2 border-t border-gray-700/50 animate-fade-in"
                    >
                      <div v-if="item.r3">
                        <p class="text-sm text-gray-500 mb-1">
                          4. Ubica en la tabla el valor óptimo de la DMO de la
                          cadera de las mujeres
                        </p>
                        <p class="bg-[#0f172a] p-3 rounded-lg">{{ item.r3 }}</p>
                      </div>

                      <div v-if="item.r4">
                        <p class="text-sm text-gray-500 mb-1">
                          5. ¿El valor máximo de la DMO es igual al que habías
                          dado en Foro 2?
                        </p>
                        <p class="bg-[#0f172a] p-3 rounded-lg">{{ item.r4 }}</p>
                      </div>

                      <div v-if="item.r5">
                        <p class="text-sm text-gray-500 mb-1">
                          6. Argumenta utilizando rectas secantes:
                        </p>
                        <p class="bg-[#0f172a] p-3 rounded-lg">{{ item.r5 }}</p>
                      </div>

                      <div v-if="item.r6">
                        <p class="text-sm text-gray-500 mb-1">
                          7. ¿Cómo encontrar la edad donde se alcanza el valor
                          óptimo?
                        </p>
                        <p class="bg-[#0f172a] p-3 rounded-lg">{{ item.r6 }}</p>
                      </div>
                    </div>
                  </details>
                </div>
              </div>
              <!-- fin de cada tarjeta -->
            </section>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import Sidebar from "@/views/sidebar.vue";
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

<style scoped>
.input-foro {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  background-color: #222d3e;
  border: 1px solid #4b5563;
  color: white;
  resize: vertical;
}
.input-foro:focus {
  outline: none;
  border-color: #1447e6; /* Color morado para diferenciar este foro */
  box-shadow: 0 0 0 2px rgba(20, 70, 226);
}

.input-celda {
  width: 100%;
  height: 100%;
  background: transparent;
  border: none;
  color: white;
  padding: 8px;
  text-align: center;
}
.input-celda:focus {
  outline: none;
  background-color: #2f3e55;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}
</style>