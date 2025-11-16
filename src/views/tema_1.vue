<template>
  <div class="flex flex-col md:flex-row">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <!-- Foro preguntas -->
    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <!-- aqui se cambia el tamano de la pagina  -->
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
                      Foro 1 :La densidad mineral y osea
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
              Investiga y Responde las Siguentes Preguntas
            </h2>
            <div class="space-y-4">
              <div class="bg-[#161d2b] p-4 rounded-xl">
                <h1 class="font-mono text-white/90 mb-6">
                  1.- Explica en que consiste la densidad mineral ósea (DMO) y
                  cómo se mide (qué pruebas se utilizan). ¿Es peligrosa su
                  medición?
                </h1>

                <h2 class="font-mono text-white/90 mb-6">
                  2.- ¿Qué factores consideras que influyen en una buena salud
                  ósea?
                </h2>

                <h3 class="font-mono text-white/90 mb-6">
                  3.- ¿Consideras que la edad y la DMO pueden estar relacionadas
                  de manera que el valor de una magnitud dependa del valor de la
                  otra? Justifica.
                </h3>

                <h4 class="font-mono text-white/90 mb-6">
                  4.- ¿Cómo evoluciona la DMO a lo largo de la vida/edad de las
                  personas?
                </h4>

                <h5 class="font-mono text-white/90 mb-6">
                  5.- Considerando lo investigado, ¿crees que, dado un valor
                  normal de la DMO, se puede saber la edad aproximada de una
                  persona? ¿Y viceversa? Explica.
                </h5>

                <h6 class="font-mono text-white/90 mb-6">
                  6.- Investiga y responde: ¿La DMO será igual para el esqueleto
                  femenino y el masculino? ¿A qué se debe? ¿A partir de qué edad
                  se pueden obtener diferencias, si las hay? Justifica.
                </h6>
              </div>
            </div>
          </section>
          <!-- Applet de Geogebra -->
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
                  <div id="geogebra-container" class="mb-1"></div>
                </div>
              </div>
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
  name: "GeoGebraEmbed",
  components: { Sidebar },
  mounted() {
    const script = document.createElement("script");
    script.src = "https://www.geogebra.org/apps/deployggb.js";
    script.onload = () => {
      const params = {
        appName: "classic",
        material_id: "au3jr5af",
        width: 1200,
        height: 600,
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
