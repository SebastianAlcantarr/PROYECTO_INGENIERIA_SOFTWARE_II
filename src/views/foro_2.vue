<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />
    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-7xl">
          <!-- INTRODUCCION -->
          <section class="scroll-mt-20" id="introduction">
            <div class="@container">
              <div class="bg-[#161d2b] rounded-xl p-6">
                <div class="flex flex-col gap-2 text-left">
                  <h1
                    class="text-white text-2xl p-6 leading-tight tracking-[-0.033em] @[480px]:text-5xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em]"
                  >
                    Foro 2 : Gráfico Comparativo
                  </h1>
                </div>
              </div>
            </div>
          </section>

          <!-- REGLAS -->
          <section class="scroll-mt-20" id="rules">
            <h2 class="text-white text-2xl font-bold px-4 pb-10 pt-20">
              El siguiente gráfico comparativo se elaboró a partir de los datos
              del
              <a
                class="text-blue-600 hover:text-blue-900 transition-colors duration-200"
                href="https://e-enm.org/journal/view.php?doi=10.3803/EnM.2013.28.3.180"
                >articulo de investigacion</a
              >
              de Lee y colaboradores (2013, p. 184). El gráfico muestra los
              valores de la cadera (Total hip) tanto de hombres como de mujeres.
            </h2>

            <div class="rounded-xl overflow-hidden">
              <img
                  class="w-full max-w-[700px] md:max-w-[800px] lg:max-w-[1000px] xl:max-w-[1400px] mx-auto object-contain"
                  src="/src/imagenes/Cadera H vs M.png"
                  alt="Grafica"
              />
            </div>

          </section>

          <!-- EJERCICIOS -->

          <div class="space-y-4 mt-10">
            <div class="bg-[#161d2b] p-4 rounded-xl">
              <div class="mb-6">
                <h1 class="font-mono text-2xl text-white/90 mb-2">
                  1. Describe las similitudes y diferencias que observas en las
                  gráficas de la DMO de la cadera entre hombres y mujeres,
                  determinando aproximadamente la edad en que se presentan.
                </h1>
                <textarea
                  rows="4"
                  placeholder="Escribe tu respuesta aquí..."
                  class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                ></textarea>
              </div>

              <div class="mb-6">
                <h2 class="font-mono text-2xl text-white/90 mb-2">
                  2. ¿En qué etapa de la vida aumenta más la densidad mineral
                  ósea en las mujeres? ¿Y de los hombres? ¿Cuál podría ser la
                  causa? Justifica tu respuesta.
                </h2>
                <textarea
                  rows="4"
                  placeholder="Escribe tu respuesta aquí..."
                  class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                ></textarea>
              </div>

              <div class="mb-6">
                <h3 class="font-mono text-2xl text-white/90 mb-2">
                  3. ¿En qué etapa de la vida disminuye más la densidad mineral
                  ósea en las mujeres? ¿Y de los hombres? ¿A qué se debe esto?
                  Justifica tu respuesta.
                </h3>
                <textarea
                  rows="4"
                  placeholder="Escribe tu respuesta aquí..."
                  class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                ></textarea>
              </div>

              <div class="mb-6">
                <h4 class="font-mono text-2xl text-white/90 mb-2">
                  4. ¿Habrá una edad donde la densidad mineral ósea tenga un
                  valor máximo? Ese valor, ¿se puede ubicar en la gráfica?
                  Justifica tu respuesta.
                </h4>
                <textarea
                  rows="4"
                  placeholder="Escribe tu respuesta aquí..."
                  class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                ></textarea>
              </div>

              <div class="mb-6">
                <h5 class="font-mono text-2xl text-white/90 mb-2">
                  5. Analiza la siguiente afirmación argumentando por qué
                  consideras que el fenómeno se comporta así: En la gráfica
                  anterior se observa que la densidad mineral ósea, aumenta en
                  los primeros años de vida (la gráfica crece) y luego, a partir
                  de cierta edad, se comienza a perder densidad mineral ósea (la
                  gráfica decrece). Entonces, hay una edad donde la densidad
                  mineral ósea alcanza su valor máximo (conocido como pico de
                  densidad mineral ósea) por lo que este fenómeno de variación
                  (cambio) tiene un valor óptimo y es un máximo.
                </h5>
                <textarea
                  rows="4"
                  placeholder="Escribe tu respuesta aquí..."
                  class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                ></textarea>
              </div>

              <div class="mb-0">
                <h6 class="text-white text-3xl">
                  6. ¿Cómo podemos verificar o encontrar la edad dónde se
                  alcanza el valor óptimo? Lista las ideas o herramientas que
                  nos pueden ayudar a encontrar la edad exacta donde se alcanza
                  ese pico de masa ósea.
                </h6>
                <textarea
                  rows="4"
                  placeholder="Escribe tu respuesta aquí..."
                  class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                ></textarea>
              </div>
              <div class="mt-8 pt-4 border-t border-gray-700 flex justify-end">
                <button
                  @click="enviarRespuestas"
                  class="group flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-all duration-300 shadow-lg hover:shadow-blue-500/20 active:scale-95"
                >
                  <span>Enviar Respuestas</span>
                  <span
                    class="material-symbols-outlined group-hover:translate-x-1 transition-transform"
                  >
                    send
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/views/sidebar.vue";
export default {
  name: "App",
  components: { Sidebar },
};
</script>
