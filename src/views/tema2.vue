<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />
    <main
      class="ml-0 md:ml-72 w-full min-h-screen bg-blue dark:bg-[rgb(16,22,34)] font-display text-[#E0E0E0]"
    >
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="max-w-8xl lg:ml-40 md:ml-20 sm:ml-10 ml-0">
          <!-- INTRODUCCION -->
          <section class="scroll-mt-20" id="introduction">
            <div class="@container">
              <div class="w-full lg:w-[100%] sm:p-6 bg-[#161d2b] rounded-lg">
                <div class="flex flex-col gap-2 text-left">
                  <h1 class="text-white text-4xl font-black leading-tight">
                    Foro 2 : Gráfico Comparativo
                  </h1>
                </div>
              </div>
            </div>
          </section>

          <!-- REGLAS -->
          <section class="scroll-mt-20" id="rules">
            <h2 class="text-white text-2xl font-bold px-4 pb-10 pt-20">
              El siguiente gráfico comparativo se elaboró...
            </h2>

            <div class="w-full sm:p-8 bg-[#161d2b] rounded-xl">
              <div class="rounded-xl overflow-hidden">
                <img
                  class="w-full h-auto object-contain mx-auto"
                  src="/src/imagenes/Cadera%20H%20vs%20M.png"
                  alt="Grafica"
                />
              </div>
            </div>
          </section>

          <!-- EJERCICIOS -->
          <section class="scroll-mt-20" id="ejercicios">
            <h2 class="text-white text-3xl font-bold px-4 pb-3 pt-10 mt-20">
              Ejercicios
            </h2>

            <div class="bg-[#161d2b] rounded-xl p-6 space-y-6">
              <!-- tus preguntas -->
              <p class="text-white text-2xl mb-5">
                En base a la gráfica responde:
              </p>

              <h1 class="text-white text-xl">
                1.- Describe las similitudes y diferencias...
              </h1>

              <h2 class="text-white text-xl">
                2.- ¿En qué etapa de la vida aumenta más...
              </h2>

              <h3 class="text-white text-xl">
                3.- ¿En qué etapa de la vida disminuye más...
              </h3>

              <h4 class="text-white text-xl">
                4.- ¿Habrá una edad donde la densidad...
              </h4>

              <h5 class="text-white text-xl">
                5.- Analiza la siguiente afirmación...
              </h5>

              <h6 class="text-white text-xl">
                6.- ¿Cómo podemos verificar o encontrar...
              </h6>
            </div>
          </section>

          <!-- INFORMACION -->
          <section class="scroll-mt-20" id="resources">
            <h2 class="text-white text-[22px] font-bold px-4 pb-3 pt-10">
              INFORMACIÓN
            </h2>

            <div class="bg-[#161d2b] rounded-xl p-6">
              <ul class="list-disc list-inside space-y-2 text-[#135bec]">
                <li>
                  <a class="text-white/80 hover:text-white underline"
                    >INFORMACIÓN</a
                  >
                </li>
                <li>
                  <a class="text-white/80 hover:text-white underline"
                    >INFORMACIÓN</a
                  >
                </li>
                <li>
                  <a class="text-white/80 hover:text-white underline"
                    >INFORMACIÓN</a
                  >
                </li>
              </ul>
            </div>
          </section>
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
