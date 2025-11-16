<template>
  <div
      class="bg-blue dark:bg-[rgb(16,22,34)] font-display text-[#E0E0E0] min-h-screen"
  >
    <Sidebar class="hidden md:block" />

    <main class=" min-h-screen w-full">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-7xl">
          <section class="scroll-mt-20" id="introduction">
            <div class="@container">
              <div
                  class="flex flex-col gap-6 py-10 @[480px]:gap-8 @[864px]:flex-row bg-[#161d2b] rounded-xl p-6"
              >
                <div
                    class="flex flex-col gap-6 @[480px]:min-w-[400px] @[480px]:gap-8 @[864px]:justify-center"
                >
                  <div class="flex flex-col gap-2 text-left">
                    <h1
                        class="text-white text-4xl font-black leading-tight tracking-[-0.033em] @[480px]:text-5xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em]"
                    >
                      La densidad mineral ósea
                    </h1>
                  </div>
                </div>
                <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-lg @[480px]:h-auto @[480px]:min-w-[300px] @[864px]:w-full"
                    data-alt="An abstract visualization of a mathematical graph with glowing blue lines on a dark background"
                    style="
                    background-image: url('https://www.clikisalud.net/wp-content/uploads/2022/08/densidad-mineral-osea.jpg');
                  "
                ></div>
              </div>
            </div>
          </section>
          <section class="scroll-mt-20" id="rules">
            <h2
                class="text-white text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-10"
            >
              Investiga y Responde las Siguientes Preguntas
            </h2>
            <div class="space-y-4">
              <div class="bg-[#161d2b] p-4 rounded-xl">
                <div class="mb-6">
                  <h1 class="font-mono text-white/90 mb-2">
                    1.- Explica en que consiste la densidad mineral ósea (DMO) y
                    cómo se mide (qué pruebas se utilizan). ¿Es peligrosa su
                    medición?
                  </h1>
                  <textarea
                      rows="4"
                      placeholder="Escribe tu respuesta aquí..."
                      class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                  ></textarea>
                </div>

                <div class="mb-6">
                  <h2 class="font-mono text-white/90 mb-2">
                    2.- ¿Qué factores consideras que influyen en una buena salud
                    ósea?
                  </h2>
                  <textarea
                      rows="4"
                      placeholder="Escribe tu respuesta aquí..."
                      class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                  ></textarea>
                </div>

                <div class="mb-6">
                  <h3 class="font-mono text-white/90 mb-2">
                    3.- ¿Consideras que la edad y la DMO pueden estar
                    relacionadas de manera que el valor de una magnitud dependa
                    del valor de la otra? Justifica.
                  </h3>
                  <textarea
                      rows="4"
                      placeholder="Escribe tu respuesta aquí..."
                      class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                  ></textarea>
                </div>

                <div class="mb-6">
                  <h4 class="font-mono text-white/90 mb-2">
                    4.- ¿Cómo evoluciona la DMO a lo largo de la vida/edad de
                    las personas?
                  </h4>
                  <textarea
                      rows="4"
                      placeholder="Escribe tu respuesta aquí..."
                      class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                  ></textarea>
                </div>

                <div class="mb-6">
                  <h5 class="font-mono text-white/90 mb-2">
                    5.- Considerando lo investigado, ¿crees que, dado un valor
                    normal de la DMO, se puede saber la edad aproximada de una
                    persona? ¿Y viceversa? Explica.
                  </h5>
                  <textarea
                      rows="4"
                      placeholder="Escribe tu respuesta aquí..."
                      class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                  ></textarea>
                </div>

                <div class="mb-0">
                  <h6 class="font-mono text-white/90 mb-2">
                    6.- Investiga y responde: ¿La DMO será igual para el
                    esqueleto femenino y el masculino? ¿A qué se debe? ¿A partir
                    de qué edad se pueden obtener diferencias, si las hay?
                    Justifica.
                  </h6>
                  <textarea
                      rows="4"
                      placeholder="Escribe tu respuesta aquí..."
                      class="w-full p-3 rounded-lg bg-[#222d3e] border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400"
                  ></textarea>
                </div>
                <div
                    class="mt-8 pt-4 border-t border-gray-700 flex justify-end"
                >
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
          </section>
          <!-- Applet de Geogebra -->

        </div>
      </div>
    </main>


  </div>


</template>

<script>
import Sidebar from "@/views/sidebar.vue";

export default {
  components: { Sidebar },

};
</script>

<style>
html {
  scroll-behavior: smooth;
}
html,
body {
  min-height: 100%;
  background-color: #244a76;
}
@media (prefers-color-scheme: dark) {
  html,
  body {
    background-color: rgb(16, 22, 34);
  }
}
</style>
