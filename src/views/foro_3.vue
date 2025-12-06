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
              class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-blue-700"
            >
              <h1
                class="text-white text-3xl md:text-3xl font-black text-center"
              >
                Foro 3. Densidad mineral ósea de la cadera de mujeres
              </h1>
            </div>
          </section>

          <!-- contexto -->
          <section class="mb-8 animate-fade-in">
            <div class="">
              <div v-if="cargandoEstado" class="text-center py-10">
                <p class="text-blue-200 text-sm animate-pulse">
                  Verificando tu participación...
                </p>
              </div>

              <section
                v-else-if="!usuarioYaParticipo"
                class="space-y-6 animate-fade-in"
              >
                <div class="text-white text-2xl md:text-3xl font-black ">
                  Modelación de la Situación Problema
                </div>
                <div>
                 <div class="  ">

                   <div v-if="mostrarInformacion" class="animate-fade-in space-y-6">
              <div class="pregunta-texto text-base text-white/90 mb-3">
                <div class="mt-5">
                Para modelar la relación que existe entre la edad y la densidad mineral ósea (DMO), partiendo de los datos en una tabla, se pueden utilizar herramientas que aproximan los puntos a una curva, como por ejemplo Excel, Hojas de cálculo de Google o cualquier otra
                  <a
                    class="text-blue-500 hover:text-blue-700 transition-colors duration-200"
                    href="https://kidshealth.org/es/parents/bones-muscles-joints.html#:~:text=Los%20huesos%20est%C3%A1n%20compuestos%20por,en%20otras%20partes%20del%20cuerpo."
                    target="_blank"
                    rel="noopener noreferrer"
                    >herramienta disponible en Internet.</a
                  >
                  La mayoría de estas herramientas proporcionan la expresión algebraica de la curva que mejor aproxima los puntos. Es decir, aquella curva que minimiza la distancia a los puntos.
                <div class="mt-5">
                  Una vez que se obtiene la expresión algebraica, se pueden obtener más datos o realizar una gráfica más completa (con más puntos) para realizar análisis más profundos como identificar la edad en que se alcanza una densidad mineral ósea máxima (este valor es se conoce como óptimo o pico de masa ósea).
                </div>
                </div>

              </div>
            </div>
            </div>
<div class="pregunta-texto text-3xl text-white/90 mb-10 mt-15" >
                Preguntas  Foro 3
              </div>
            </div>
              <p class="text-gray-300 text-base mb-6 leading-relaxed ">
  Utilizando los datos del
  <a href="https://www.researchgate.net/publication/259608747_Age-Related_Changes_in_the_Prevalence_of_Osteoporosis_according_to_Gender_and_Skeletal_Site_The_Korea_National_Health_and_Nutrition_Examination_Survey_2008-2010#fullTextFileContent" class="font-bold text-blue-700 hover:text-blue-400 transition-colors duration-200 " target="_blank"
     rel="noopener noreferrer">
    artículo de investigación
  </a>
  de Lee y colaboradores (2013, p. 184), se eligieron los datos
  de la densidad mineral ósea de la cadera (Total hip) del grupo
  de mujeres. La elección de la cadera se debe a que es un hueso
  que se fractura con mayor frecuencia en edades mayores.
</p>


                <div class="flex flex-col lg:flex-row gap-8 items-start">
                  <!-- tabla1 -->
                  <div class="w-full lg:w-1/3">
                    <table
                      class="w-full text-sm text-left text-gray-400 rounded-lg overflow-hidden"
                    >
                      <thead
                        class="text-xs text-white uppercase bg-blue-900/50"
                      >
                        <tr>
                          <th
                            scope="col"
                            class="px-6 py-3 text-center border-b border-gray-600"
                          >
                            Edad
                          </th>
                          <th
                            scope="col"
                            class="px-6 py-3 text-center border-b border-gray-600"
                          >
                            Mujeres
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            15
                          </td>
                          <td class="px-6 py-3 text-center">0.847</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            25
                          </td>
                          <td class="px-6 py-3 text-center">0.89</td>
                        </tr>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            35
                          </td>
                          <td class="px-6 py-3 text-center">0.896</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            45
                          </td>
                          <td class="px-6 py-3 text-center">0.913</td>
                        </tr>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            55
                          </td>
                          <td class="px-6 py-3 text-center">0.938</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            65
                          </td>
                          <td class="px-6 py-3 text-center">0.769</td>
                        </tr>
                        <tr
                          class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            75
                          </td>
                          <td class="px-6 py-3 text-center">0.696</td>
                        </tr>
                        <tr
                          class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]"
                        >
                          <td
                            class="px-6 py-3 text-center font-bold text-white"
                          >
                            85
                          </td>
                          <td class="px-6 py-3 text-center">0.625</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <!-- img -->
                  <div class="w-full lg:w-2/3 flex flex-col items-center">
                    <div
                      class="w-full aspect-video bg-white rounded-lg flex items-center justify-center overflow-hidden shadow-lg border-4 border-[#161d2b]"
                    >
                      <img
                        src="/src/imagenes/img.png"
                        alt="Gráfica de DMO vs Edad"
                        class="w-full h-full object-contain p-2"
                      />
                    </div>
                    <p class="mt-2 text-sm text-gray-400 italic text-center">
                      Gráfica de dispersión de la DMO en mujeres según la edad.
                    </p>
                  </div>
                </div>
                <section
                  class="space-y-6 animate-fade-in"
                  style="animation-delay: 0.2s"
                >
                  <h2
                    class="text-white text-sm font-bold px-2 flex items-center gap-2"
                  >
                    <span class="material-symbols-outlined">quiz</span>
                    Cuestionario de Análisis
                  </h2>

                  <div
                    class="bg-[#161d2b] p-6 rounded-xl shadow-xl space-y-8 border border-gray-700"
                  >
                    <!-- P1 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        1. Calcula, con base en los datos de la tabla, ¿cuánto
                        cambia la densidad mineral ósea (DMO) si la edad cambia
                        15 a 25 años?
                      </h3>
                      <textarea
                        v-model="r1"
                        rows="2"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <!-- P2 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        2. Escríbelo como una razón de cambio promedio (DMO /
                        edad) y exprésalo de forma verbal.
                      </h3>
                      <textarea
                        v-model="r2"
                        rows="2"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <!-- P3 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        3. En promedio por año, ¿cuánto cambia la DMO entre los
                        15 y 25 años?
                      </h3>
                      <textarea
                        v-model="r3"
                        rows="2"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <!-- P4 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        4. Ubica esos valores en el gráfico de la mujer y traza
                        una línea que una esos puntos, describe la inclinación
                        de esa línea con detalle.
                      </h3>
                      <textarea
                        v-model="r4"
                        rows="3"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <!-- P5 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        5. Calcula la pendiente de la recta secante que une los
                        dos puntos (15, 0.847) y (25, 0.890). ¿Encuentras una
                        relación entre este valor y la razón promedio de cambio?
                        Describe.
                      </h3>
                      <textarea
                        v-model="r5"
                        rows="3"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <!-- P6 TABLA -->
                    <div>
                      <h3 class="text-base text-white/90 mb-4 font-medium">
                        6. Para analizar el comportamiento de la gráfica de la
                        mujer, completa la siguiente tabla:
                      </h3>

                      <div class="overflow-x-auto">
                        <table
                          class="w-full text-sm text-left text-gray-300 border border-gray-600"
                        >
                          <thead
                            class="text-xs text-white bg-gray-700 uppercase"
                          >
                            <tr>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/6"
                              >
                                Intervalo
                              </th>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/4"
                              >
                                Razón promedio
                              </th>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/4"
                              >
                                Comportamiento (creciente/decreciente)
                              </th>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/3"
                              >
                                ¿Qué pasa con la DMO?
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            <!-- Fila 1 -->
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [15, 25]
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r1_c1"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r1_c2"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r1_c3"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                            </tr>
                            <!-- Fila 2 -->
                            <tr class="bg-[#1e2837]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [25, 35]
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r2_c1"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r2_c2"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r2_c3"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                            </tr>
                            <!-- Fila 3 -->
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [35, 45]
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r3_c1"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r3_c2"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r3_c3"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                            </tr>
                            <!-- Fila 4 -->
                            <tr class="bg-[#1e2837]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [45, 55]
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r4_c1"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r4_c2"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r4_c3"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                            </tr>
                            <!-- Fila 5 -->
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [55, 65]
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r5_c1"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r5_c2"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r5_c3"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                            </tr>
                            <!-- Fila 6 -->
                            <tr class="bg-[#1e2837]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [65, 75]
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r6_c1"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r6_c2"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r6_c3"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                            </tr>
                            <!-- Fila 7 -->
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [75, 85]
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r7_c1"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r7_c2"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                              <td class="border border-gray-600">
                                <input
                                  v-model="t6_r7_c3"
                                  class="input-celda"
                                  type="text"
                                />
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>

                    <!-- P7 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        7. ¿Qué información aporta conocer el valor de la razón
                        promedio de cambio en distintos intervalos de una
                        gráfica?
                      </h3>
                      <textarea
                        v-model="r7"
                        rows="3"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <!-- P8 -->
                    <div>
                      <h3 class="text-base text-white/90 mb-3 font-medium">
                        8. Con la información de la tabla, ¿podríamos determinar
                        el valor de la DMO de una mujer de 50 años? Argumenta.
                      </h3>
                      <textarea
                        v-model="r8"
                        rows="3"
                        placeholder="Respuesta..."
                        class="input-foro"
                      ></textarea>
                    </div>

                    <div class="pt-6 border-t border-gray-700 flex justify-end">
                      <button
                        @click="enviarRespuestas"
                        :disabled="enviando"
                        class="bg-blue-600 hover:bg-blue-900 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
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
                </section>
              </section>
            </div>

            <!-- preguntas -->
          </section>

          <!-- Sección de respuestas (se muestra después de participar) -->
          <section v-if="usuarioYaParticipo" class="mt-12 animate-fade-in">
            <!-- Aviso de "Ya cumpliste" -->
            <div class="bg-green-900/30 border border-green-500/50 p-4 rounded-xl mb-8 flex items-center gap-4 text-green-200">
              <span class="material-symbols-outlined text-3xl">check_circle</span>
              <div>
                <h3 class="font-bold text-base">Actividad Completada</h3>
                <p class="text-sm opacity-80">Gracias por tu aporte. Aquí están las respuestas de tus compañeros.</p>
              </div>
            </div>

            <!-- Lista de Respuestas (Muro) -->
            <h2
              class="text-white text-2xl font-bold mb-6 border-b border-gray-700 pb-2 flex items-center gap-2"
            >
              <span class="material-symbols-outlined">forum</span>
              Participaciones del Grupo
            </h2>

            <div class="space-y-6">
              <div
                v-if="listaRespuestas.length === 0"
                class="text-center text-gray-400 py-8"
              >
                Aún no hay respuestas de otros estudiantes.
              </div>

              <div
                v-for="(item, index) in listaRespuestas"
                :key="index"
                class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-700 shadow-md hover:bg-[#253042] transition-colors"
              >
                <div class="flex justify-between items-start mb-4">
                  <div class="flex items-center gap-3">
                    <div
                      class="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold"
                    >
                      {{
                        obtenerIniciales(
                          item.nombre,
                          item.apellidos || item.email
                        )
                      }}
                    </div>
                    <div>
                      <span class="text-blue-400 font-bold text-sm">
                        {{
                          item.nombre
                            ? `${item.nombre} ${item.apellidos}`
                            : item.email
                        }}
                      </span>
                      <p class="text-gray-500 text-xs">
                        {{ formatearFecha(item.fecha) }}
                      </p>
                    </div>
                  </div>
                  <span
                    class="bg-blue-900/50 text-blue-200 text-sm px-2 py-1 rounded"
                    >Respuesta #{{ listaRespuestas.length - index }}</span
                  >
                </div>

                <div
                  class="space-y-4 text-gray-300 text-sm pl-2 border-l border-gray-700 ml-4"
                >
                  <p>
                    <strong class="text-blue-200">1.Calcula,con base los datos de la tabla</strong>
                    <br />{{ item.r1 }}
                  </p>
                  <p>
                    <strong class="text-blue-200"
                      >2.Escribelo como una razon de cambio de promedio</strong
                    >
                    <br />{{ item.r2 }}
                  </p>

                  <details class="text-gray-400 cursor-pointer group">
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
                      <p>
                        <strong class="text-blue-200"
                          >3.En promedio por año,</strong
                        >
                        <br />{{ item.r3 }}
                      </p>
                      <p>
                        <strong class="text-blue-200"
                          >4.Ubica esos valores en el gráfico </strong
                        >
                        <br />{{ item.r4 }}
                      </p>
                      <p>
                        <strong class="text-blue-200"
                          >5.Calcula la pendiente </strong
                        >
                        <br />{{ item.r5 }}
                      </p>
                       <p>
                        <strong class="text-blue-200"
                          >6.Completar siguente tabla</strong
                        >
                      </p>

                      <div class="overflow-x-auto my-4">
                        <table
                          class="w-full text-sm text-left text-gray-300 border border-gray-600"
                        >
                          <thead
                            class="text-xs text-white bg-gray-700 uppercase"
                          >
                            <tr>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/6"
                              >
                                Intervalo
                              </th>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/4"
                              >
                                Razón promedio
                              </th>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/4"
                              >
                                Comportamiento
                              </th>
                              <th
                                class="px-4 py-3 border border-gray-600 w-1/3"
                              >
                                ¿Qué pasa con la DMO?
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [15, 25]
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r1_c1 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r1_c2 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r1_c3 }}
                              </td>
                            </tr>
                            <tr class="bg-[#1e2837]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [25, 35]
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r2_c1 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r2_c2 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r2_c3 }}
                              </td>
                            </tr>
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [35, 45]
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r3_c1 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r3_c2 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r3_c3 }}
                              </td>
                            </tr>
                            <tr class="bg-[#1e2837]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [45, 55]
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r4_c1 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r4_c2 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r4_c3 }}
                              </td>
                            </tr>
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [55, 65]
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r5_c1 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r5_c2 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r5_c3 }}
                              </td>
                            </tr>
                            <tr class="bg-[#1e2837]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [65, 75]
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r6_c1 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r6_c2 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r6_c3 }}
                              </td>
                            </tr>
                            <tr class="bg-[#222d3e]">
                              <td
                                class="px-4 py-2 border border-gray-600 font-bold"
                              >
                                [75, 85]
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r7_c1 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r7_c2 }}
                              </td>
                              <td class="border border-gray-600 px-2">
                                {{ item.t6_r7_c3 }}
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        <strong class="text-blue-200"
                          >7. Información de la razón promedio</strong
                        >
                        <br />{{ item.r7 }}
                      </p>
                      <p>
                        <strong class="text-blue-200"
                          >8. Determinación de DMO a los 50 años</strong
                        >
                        <br />{{ item.r8 }}
                      </p>
                    </div>
                  </details>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>




<script setup>
import { onMounted, ref } from "vue";
import Sidebar from "@/views/sidebar.vue";

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
      `http://127.0.0.1:8000/verificar_en_foro_3/${email}`
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
    const respuesta = await fetch("http://127.0.0.1:8000/guardar_en_foro_3", {
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
    const res = await fetch("http://127.0.0.1:8000/respuestas_en_foro_3");
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
