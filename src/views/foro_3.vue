<template>
  <div class="flex flex-col md:flex-row min-h-screen bg-[#244a76] dark:bg-[rgb(16,22,34)]">
    <!-- sidebar -->
    <Sidebar class="hidden md:block" />

    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-7xl">

          <!-- titulo -->
          <section class="scroll-mt-20 mb-8">
            <div class="bg-[#161d2b] rounded-xl p-6 shadow-lg border-l-8 border-purple-500">
              <h1 class="text-white text-3xl md:text-5xl font-black text-center">
                Foro 3: DMO Cadera
              </h1>
            </div>
          </section>

          <!-- contexto -->
          <section class="mb-8 animate-fade-in">
            <div class="bg-[#161d2b] p-6 rounded-xl shadow-xl border border-gray-700">

              <!-- intro -->
              <p class="text-gray-300 text-lg mb-6 leading-relaxed">
                Utilizando los datos del <span class="font-bold text-white">artículo de investigación</span> de Lee y colaboradores (2013, p. 184), se eligieron los datos de la densidad mineral ósea de la cadera (Total hip) del grupo de mujeres. La elección de la cadera se debe a que es un hueso que se fractura con mayor frecuencia en edades mayores.
              </p>

              <div class="flex flex-col lg:flex-row gap-8 items-start">

                <!-- tabla1 -->
                <div class="w-full lg:w-1/3">
                  <table class="w-full text-sm text-left text-gray-400 rounded-lg overflow-hidden">
                    <thead class="text-xs text-white uppercase bg-blue-900/50">
                    <tr>
                      <th scope="col" class="px-6 py-3 text-center border-b border-gray-600">Edad</th>
                      <th scope="col" class="px-6 py-3 text-center border-b border-gray-600">Mujeres</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">15</td>
                      <td class="px-6 py-3 text-center">0.847</td>
                    </tr>
                    <tr class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">25</td>
                      <td class="px-6 py-3 text-center">0.89</td>
                    </tr>
                    <tr class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">35</td>
                      <td class="px-6 py-3 text-center">0.896</td>
                    </tr>
                    <tr class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">45</td>
                      <td class="px-6 py-3 text-center">0.913</td>
                    </tr>
                    <tr class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">55</td>
                      <td class="px-6 py-3 text-center">0.938</td>
                    </tr>
                    <tr class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">65</td>
                      <td class="px-6 py-3 text-center">0.769</td>
                    </tr>
                    <tr class="bg-[#222d3e] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">75</td>
                      <td class="px-6 py-3 text-center">0.696</td>
                    </tr>
                    <tr class="bg-[#1e2837] border-b border-gray-700 hover:bg-[#2a3649]">
                      <td class="px-6 py-3 text-center font-bold text-white">85</td>
                      <td class="px-6 py-3 text-center">0.625</td>
                    </tr>
                    </tbody>
                  </table>
                </div>

                <!-- img -->
                <div class="w-full lg:w-2/3 flex flex-col items-center">
                  <div class="w-full aspect-video bg-white rounded-lg flex items-center justify-center overflow-hidden shadow-lg border-4 border-[#161d2b]">
                    <img
                        src="/src/imagenes/img.png"
                        alt="Gráfica de DMO vs Edad"
                        class="w-full h-full object-contain p-2"
                    />
                  </div>
                  <p class="mt-2 text-sm text-gray-400 italic text-center">Gráfica de dispersión de la DMO en mujeres según la edad.</p>
                </div>

              </div>
            </div>
          </section>

          <!-- preguntas -->
          <section class="space-y-6 animate-fade-in" style="animation-delay: 0.2s">
            <h2 class="text-white text-xl font-bold px-2 flex items-center gap-2">
              <span class="material-symbols-outlined">quiz</span>
              Cuestionario de Análisis
            </h2>

            <div class="bg-[#161d2b] p-6 rounded-xl shadow-xl space-y-8 border border-gray-700">

              <!-- P1 -->
              <div>
                <h3 class="text-lg text-white/90 mb-3 font-medium">
                  1. Calcula, con base en los datos de la tabla, ¿cuánto cambia la densidad mineral ósea (DMO) si la edad cambia 15 a 25 años?
                </h3>
                <textarea v-model="r1" rows="2" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P2 -->
              <div>
                <h3 class="text-lg text-white/90 mb-3 font-medium">
                  2. Escríbelo como una razón de cambio promedio (DMO / edad) y exprésalo de forma verbal.
                </h3>
                <textarea v-model="r2" rows="2" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P3 -->
              <div>
                <h3 class="text-lg text-white/90 mb-3 font-medium">
                  3. En promedio por año, ¿cuánto cambia la DMO entre los 15 y 25 años?
                </h3>
                <textarea v-model="r3" rows="2" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P4 -->
              <div>
                <h3 class="text-lg text-white/90 mb-3 font-medium">
                  4. Ubica esos valores en el gráfico de la mujer y traza una línea que una esos puntos, describe la inclinación de esa línea con detalle.
                </h3>
                <textarea v-model="r4" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P5 -->
              <div>
                <h3 class="text-lg text-white/90 mb-3 font-medium">
                  5. Calcula la pendiente de la recta secante que une los dos puntos (15, 0.847) y (25, 0.890). ¿Encuentras una relación entre este valor y la razón promedio de cambio? Describe.
                </h3>
                <textarea v-model="r5" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P6 tabla2 -->
              <div>
                <h3 class="text-lg text-white/90 mb-4 font-medium">
                  6. Para analizar el comportamiento de la gráfica de la mujer, completa la siguiente tabla:
                </h3>

                <div class="overflow-x-auto">
                  <table class="w-full text-sm text-left text-gray-300 border border-gray-600">
                    <thead class="text-xs text-white bg-gray-700 uppercase">
                    <tr>
                      <th class="px-4 py-3 border border-gray-600 w-1/6">Intervalo</th>
                      <th class="px-4 py-3 border border-gray-600 w-1/4">Razón promedio</th>
                      <th class="px-4 py-3 border border-gray-600 w-1/4">Comportamiento (creciente/decreciente)</th>
                      <th class="px-4 py-3 border border-gray-600 w-1/3">¿Qué pasa con la DMO?</th>
                    </tr>
                    </thead>
                    <tbody>
                    <!-- Fila 1 -->
                    <tr class="bg-[#222d3e]">
                      <td class="px-4 py-2 border border-gray-600 font-bold">[15, 25]</td>
                      <td class="border border-gray-600"><input v-model="t6_r1_c1" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r1_c2" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r1_c3" class="input-celda" type="text"></td>
                    </tr>
                    <!-- Fila 2 -->
                    <tr class="bg-[#1e2837]">
                      <td class="px-4 py-2 border border-gray-600 font-bold">[25, 35]</td>
                      <td class="border border-gray-600"><input v-model="t6_r2_c1" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r2_c2" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r2_c3" class="input-celda" type="text"></td>
                    </tr>
                    <!-- Fila 3 -->
                    <tr class="bg-[#222d3e]">
                      <td class="px-4 py-2 border border-gray-600 font-bold">[35, 45]</td>
                      <td class="border border-gray-600"><input v-model="t6_r3_c1" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r3_c2" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r3_c3" class="input-celda" type="text"></td>
                    </tr>
                    <!-- Fila 4 -->
                    <tr class="bg-[#1e2837]">
                      <td class="px-4 py-2 border border-gray-600 font-bold">[45, 55]</td>
                      <td class="border border-gray-600"><input v-model="t6_r4_c1" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r4_c2" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r4_c3" class="input-celda" type="text"></td>
                    </tr>
                    <!-- Fila 5 -->
                    <tr class="bg-[#222d3e]">
                      <td class="px-4 py-2 border border-gray-600 font-bold">[55, 65]</td>
                      <td class="border border-gray-600"><input v-model="t6_r5_c1" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r5_c2" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r5_c3" class="input-celda" type="text"></td>
                    </tr>
                    <!-- Fila 6 -->
                    <tr class="bg-[#1e2837]">
                      <td class="px-4 py-2 border border-gray-600 font-bold">[65, 75]</td>
                      <td class="border border-gray-600"><input v-model="t6_r6_c1" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r6_c2" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r6_c3" class="input-celda" type="text"></td>
                    </tr>
                    <!-- Fila 7 -->
                    <tr class="bg-[#222d3e]">
                      <td class="px-4 py-2 border border-gray-600 font-bold">[75, 85]</td>
                      <td class="border border-gray-600"><input v-model="t6_r7_c1" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r7_c2" class="input-celda" type="text"></td>
                      <td class="border border-gray-600"><input v-model="t6_r7_c3" class="input-celda" type="text"></td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- P7 -->
              <div>
                <h3 class="text-lg text-white/90 mb-3 font-medium">
                  7. ¿Qué información aporta conocer el valor de la razón promedio de cambio en distintos intervalos de una gráfica?
                </h3>
                <textarea v-model="r7" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <!-- P8 -->
              <div>
                <h3 class="text-lg text-white/90 mb-3 font-medium">
                  8. Con la información de la tabla, ¿podríamos determinar el valor de la DMO de una mujer de 50 años? Argumenta.
                </h3>
                <textarea v-model="r8" rows="3" placeholder="Respuesta..." class="input-foro"></textarea>
              </div>

              <div class="pt-6 border-t border-gray-700 flex justify-end">
                <button
                    class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg"
                >
                  Enviar
                </button>
              </div>

            </div>
          </section>

        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Sidebar from "@/views/sidebar.vue";

// Variables para respuestas simples
const r1 = ref("");
const r2 = ref("");
const r3 = ref("");
const r4 = ref("");
const r5 = ref("");
const r7 = ref("");
const r8 = ref("");

// Estructura: t6_fila_columna
const t6_r1_c1 = ref(""); const t6_r1_c2 = ref(""); const t6_r1_c3 = ref("");
const t6_r2_c1 = ref(""); const t6_r2_c2 = ref(""); const t6_r2_c3 = ref("");
const t6_r3_c1 = ref(""); const t6_r3_c2 = ref(""); const t6_r3_c3 = ref("");
const t6_r4_c1 = ref(""); const t6_r4_c2 = ref(""); const t6_r4_c3 = ref("");
const t6_r5_c1 = ref(""); const t6_r5_c2 = ref(""); const t6_r5_c3 = ref("");
const t6_r6_c1 = ref(""); const t6_r6_c2 = ref(""); const t6_r6_c3 = ref("");
const t6_r7_c1 = ref(""); const t6_r7_c2 = ref(""); const t6_r7_c3 = ref("");

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
  border-color: #a855f7; /* Color morado para diferenciar este foro */
  box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.3);
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
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}
</style>