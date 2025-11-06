<template>
  <div
    class="bg-[#244a76] dark:bg-[rgb(16,22,34)] font-display text-[#E0E0E0] min-h-screen"
  >
    <!--INICIA EL LADO IZQUIERDO DE LA PAGINA  -->
    <div class="relative flex min-h-screen w-full">
      <!-- IMAGEN DEL PERFIL , NOMBRE , MATERIA ,ETC  -->
      <aside
        class="fixed left-0 top-0 h-screen w-64 bg-[#244a76] dark:bg-[#101622] border-r border-white/10 p-4 hidden lg:flex flex-col"
      >
        <div class="flex flex-col gap-4">
          <div class="flex items-center gap-3">
            <div
              class="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-10"
              data-alt="Abstract blue and purple gradient circle"
              style="
                background-image: url('data:image/png;base64,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');
              "
            ></div>
            <div class="flex flex-col">
              <h1 class="text-white text-base font-medium leading-normal">
                Derivadas
              </h1>
              <p class="text-[#92a4c9] text-sm font-normal leading-normal">
                Calculo
              </p>
            </div>

            <!-- LOGOS, QUE SON Y HACIA DONDE DIRIGEN  -->
          </div>
          <div class="flex flex-col gap-2 mt-4">
            <a
              class="flex items-center gap-3 px-3 py-2 rounded-lg bg-[#135bec]/20 dark:bg-[#232f48]"
              href="#introduction"
            >
              <span
                class="material-symbols-outlined text-[#135bec] dark:text-white"
                style="font-size: 24px"
                >school
              </span>
              <p
                class="text-[#135bec] dark:text-white text-sm font-medium leading-normal"
              >
                Material de la Sesion 1
              </p>
            </a>
            <a
              class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-[#135bec]/10 dark:hover:bg-white/5 transition-colors duration-200"
              href="#rules"
            >
              <span
                class="material-symbols-outlined text-white/70"
                style="font-size: 24px"
                >RULE</span
              >
              <p class="text-white text-sm font-medium leading-normal">
                Reglas de Derivacion
              </p>
            </a>

            <a
              class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-[#135bec]/10 dark:hover:bg-white/5 transition-colors duration-200"
              href="#exercises"
            >
              <span
                class="material-symbols-outlined text-white/70"
                style="font-size: 24px"
                >Assignment</span
              >
              <p class="text-white text-sm font-medium leading-normal">
                Ejercicios
              </p>
            </a>
          </div>
        </div>

        <!-- PROGRESO DEL ESTUDIANTE -->

        <div class="mt-auto flex flex-col gap-3 p-4">
          <div class="flex gap-6 justify-between">
            <p class="text-white text-base font-medium leading-normal">
              Progreso
            </p>
          </div>
          <div class="rounded bg-[#324467]">
            <div class="h-2 rounded bg-[#37ffcd]" style="width: 80%"></div>
          </div>
        </div>
      </aside>

      <!-- TERMINA LADO IZQUIERDO DE LA PAGINA  -->

      <main class="w-full lg:ml-64 flex flex-col">
        <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
          <div class="mx-auto max-w-4xl">
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
                        class="text-white text-5xl font-black leading-tight tracking-[-0.033em] @[480px]:text-5xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em]"
                      >
                        Material 1
                      </h1>
                      <h2
                        class=" text-white text-2xl font-bold"
                      >
                        La densidad mineral osea
                      </h2>
                    </div>
                    <button
                      class="w-full h-14 px-6 rounded-lg bg-blue-400 hover:bg-blue-800 text-gray-900 font-semibold flex items-center justify-center duration-350 focus:ring-2 focus:ring-blue-400/50"
                    >
                      <span class="truncate">Aprender</span>
                    </button>
                  </div>
                  <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-lg @[480px]:h-auto @[480px]:min-w-[300px] @[900px]:w-full"
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
                  <div class="flex justify-between items-center m-2">
                    <h3 class="text-white font-bold text-2xl m-2">Pregunta 1</h3>
                  </div>
                  <div class="bg-[#101622]  rounded-lg mt-3 p-4">
                    <pre><code class="font-mono text-white/90 text-wrap text-xl">Explica en que consiste la densidad mineral osea (DMO) y como se mide </code></pre>
                  </div>

                  <div class="flex justify-between items-center m-2">
                    <h3 class="text-white font-bold m-2 text-2xl ">Pregunta 2</h3>
                  </div>

                  <div class="bg-[#101622] p-4 rounded-lg mt-3">
                    <pre><code class="font-mono text-white/90 text-wrap text-xl">Que factores consideras que influyen en una buena salud osea?</code></pre>
                  </div>

                  <div class="flex justify-between items-center m-2">
                    <h3 class="text-white font-bold m-2 text-2xl ">Pregunta 3</h3>
                  </div>

                  <div class="bg-[#101622] p-4 rounded-lg mt-3">
                    <pre><code class="font-mono text-white/90 text-wrap text-xl">Que factores consideras que influyen en una buena salud osea?</code></pre>
                  </div>
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

              <div class="bg-[#161d2b] rounded-xl p-2">
                <div
                  class="lg:col-span-2 bg-[#161d2b]rounded-lg flex items-center p-4 min-h-[500px]"
                >
                  <div class="w-full h-full">
                    <iframe
                        src="https://www.geogebra.org/classic/au3jr5af?embed"
                        style="border:1px solid #e4e4e4; width:100%; height:80vh;"
                        allowfullscreen
                    ></iframe>
                  </div>
                </div>
              </div>
            </section>

            <section class="scroll-mt-20" id="exercises">
              <h2
                class="text-white text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-10"
              >
                Ejercicios
              </h2>
              <div class="bg-[#161d2b] rounded-xl p-6 space-y-6">
                <div>
                  <p class="text-white/90">
                    1.Derivada de
                    <span class="font-mono text-[#135bec]"
                      >f(x) = 3x² + 5x - 2</span
                    >?
                  </p>
                  <div class="flex items-center gap-4 mt-3">
                    <input v-model="respuesta"
                      type="text"
                      placeholder="Respuesta"
                      class="grow bg-[#101622] border border-white/20 rounded-lg px-3 py-2 text-white focus:ring-[#135bec] focus:border-[#135bec]"
                    />
                    <button @click="mostrar"
                      class="rounded-lg h-10 px-5 bg-[#135bec]/30 text-white hover:bg-[#135bec]/40 transition-colors text-sm font-medium"
                    >
                      Check
                    </button>
                  </div>
                </div>
                <div>
                  <p class="text-white/90">
                    2.Derivada de
                    <span class="font-mono text-[#135bec]">f(x) = sin(x)</span>.
                  </p>
                  <div class="mt-3 space-y-2">
                    <label
                      class="flex items-center gap-3 p-3 rounded-lg border border-[#E74C3C] bg-[#E74C3C]/10"
                    >
                      <input
                        class="form-radio bg-transparent border-white/50 text-[#135bec] focus:ring-[#135bec]"
                        type="radio"
                        name="ex2"
                      />
                      <span class="text-white/80">-cos(x)</span>
                    </label>
                    <label
                      class="flex items-center gap-3 p-3 rounded-lg border border-[#2ECC71] bg-[#2ECC71]/10"
                    >
                      <input
                        class="form-radio bg-transparent border-white/50 text-[#135bec] focus:ring-[#135bec]"
                        type="radio"
                        name="ex2"
                        checked
                      />
                      <span class="text-white/80">cos(x)</span>
                    </label>
                  </div>
                </div>
              </div>
            </section>

            <section class="scroll-mt-20" id="resources">
              <h2
                class="text-white text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-10"
              >
                INFORMACION
              </h2>
              <div class="bg-[#161d2b] rounded-xl p-6">
                <ul class="list-disc list-inside space-y-2 text-[#135bec]">
                  <li>
                    <a class="text-white/80 hover:text-white underline" href="#"
                      >INFORMACION</a
                    >
                  </li>
                  <li>
                    <a class="text-white/80 hover:text-white underline" href="#"
                      >INFORMACION</a
                    >
                  </li>
                  <li>
                    <a class="text-white/80 hover:text-white underline" href="#"
                      >INFORMACION</a
                    >
                  </li>

                  <p class="text-white mt-4 text-lg">Tu respuesta: {{ textoMostrado }}</p>
                </ul>
              </div>
            </section>
          </div>
        </div>
      </main>
    </div>
  </div>


</template>

<script setup>
import { ref } from "vue"

const respuesta = ref("")

const textoMostrado=ref('')

function mostrar() {
  textoMostrado.value = respuesta.value
}
</script>





<style>
html {
  scroll-behavior: smooth;
}
</style>
