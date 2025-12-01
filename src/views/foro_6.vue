<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <!-- Foro preguntas -->
    <main class="w-full ml-0 md:ml-72 flex flex-col">
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
                      class="text-white text-2xl p-6 leading-tight tracking-[-0.033em] @[480px]:text-5xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em]"
                    >
                      Foro 6. Covariación de las magnitudes.
                    </h1>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section class="scroll-mt-20" id="rules">
            <h2
              class="text-white text-3xl font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-10"
            >
              Manipula el Applet de Geogebra y responde las preguntas
            </h2>
            <section class="scroll-mt-20" id="grafica">
              <h2
                class="text-white text-[22px] font-bold leading-tight tracking-[-0.015em] px-10 pb-3 pt-10"
              >
                Graficas Geogebra
              </h2>

              <div class="bg-[#161d2b] rounded-xl p-10">
                <div
                  class="lg:col-span-2 bg-[#161d2b]rounded-lg flex items-center p-4 min-h-[500px]"
                >
                  <div class="relative w-full mb-1">
                    <div id="geogebra-container" class=""></div>
                  </div>
                </div>
              </div>
            </section>

            <div class="space-y-4 mt-10">
              <div class="bg-[#161d2b] p-4 rounded-xl">
                <p class="font-mono text-2xl text-white/90 mb-10">
                  1. ¿Qué valores puede tomar la variable x = Edad de una
                  persona? es decir, ¿Cuál es el dominio real de esta variable?
                  Justifica. Observa qué pasa con la pendiente de la recta
                  secante (o razón promedio de cambio) cuando los puntos se
                  aproximan entre si, es decir, cuando el intervalo de las
                  edades (Δx ) se hace cada vez más pequeño (Δx→0 ) .
                </p>

                <p class="font-mono text-2xl text-white/90 mb-10">
                  2. Argumenta con ejemplos la siguiente afirmación: Cuando los
                  extremos del intervalo en la edad sean iguales, es decir, en
                  el límite cuando ( Δx→0 ) la recta secante se convierte en
                  recta tangente y la razón promedio de cambio para dos puntos
                  deriva en razón instantánea de cambio para un punto.
                </p>

                <p class="font-mono text-2xl text-white/90 mb-10">
                  3. Utiliza el siguiente
                  <a
                    class="text-blue-400 hover:text-blue-100"
                    href="https://docs.google.com/spreadsheets/d/1Rqp6bml35xrT-5UkAyB3Qlx_c5nKijIqD6apvLbN4y4/edit?usp=sharing"
                  >
                    simulador
                  </a>
                  para observar a que valor se aproxima la razón promedio de
                  cambio cuando elegimos dos edades muy próximas ( Δx→0 ) para
                  distintos pares de puntos de la curva que mejor aproxima el
                  fenómeno. Y responde las siguientes preguntas: a) ¿Cuánto vale
                  la Densidad Mineral Ósea a los 19 años? ¿Cuál será la razón
                  instantánea de cambio a los 19 años? b) ¿Cuánto vale la
                  Densidad Mineral Ósea a los 31 años? ¿Cuál será la razón
                  instantánea de cambio a los 31 años? c) ¿Cuánto vale la
                  Densidad Mineral Ósea a los 84 años? ¿Cuál será la razón
                  instantánea de cambio a los 84 años?
                </p>

                <p class="font-mono text-2xl text-white/90 mb-10">
                  4. Manipula el Applet de Geogebra para que observes el valor
                  de la pendiente de la recta tangente sobre el gráfico.
                  Verifica que los resultados obtenidos en el punto anterior
                  coinciden con los que se muestran en el Applet de Geogebra.
                  ¿Cuánto vale la pendiente de la recta tangente en el valor
                  máximo? ¿Ocurrirá lo mismo en el valor mínimo?
                </p>

                <p class="font-mono text-2xl text-white/90 mb-10">
                  5. Argumenta con ejemplos ¿cómo cambia el valor de la
                  pendiente de la recta tangente cuando el valor óptimo es un
                  máximo? y ¿cómo cambia cuando el óptimo es un mínimo?
                </p>

                <p class="font-mono text-2xl text-white/90 mb-10">
                  6. La definición formal, en los libros de Cálculo, de función
                  derivada (o razón instantánea de cambio) es:
                  f´(x)=limΔx→0(ΔyΔx)=limΔx→0(f(x+Δx)−f(x)Δx)
                </p>
                <p class="font-mono text-2xl text-white/90 mb-10">
                  7. Dada la función (expresión algebraica) que describe el
                  comportamiento de la DMO en la cadera de las mujeres:
                  DMO(x)=−0.0001x2+0.0075x+0.768 donde x representa la edad. a)
                  Obtén la edad en que se alcanza el óptimo utilizando la
                  definición formal de derivada. b) Lista los pasos que se deben
                  realizar como si estuvieras dando una receta.
                </p>
                <p class="font-mono text-2xl text-white/90 mb-10">
                  8. Siguiendo los pasos descritos anteriormente. Obtén la edad
                  en que se obtiene la DMO óptima para la cadera de los hombres
                  dados los siguiente datos:
                </p>
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
  name: "GeoGebraEmbed",
  components: { Sidebar },
  mounted() {
    const script = document.createElement("script");
    script.src = "https://www.geogebra.org/apps/deployggb.js";
    script.onload = () => {
      const params = {
        appName: "classic",
        material_id: "au3jr5af",
        width: 1100,
        height: 500,
        showToolBar: true,
        showAlgebraInput: false,
        showMenuBar: false,
      };
      const applet = new window.GGBApplet(params, true);
      applet.inject("geogebra-container");
    };
    document.head.appendChild(script);
  },
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
