<template>
  <EncabezadoPortal modo="profesor" />
  <div
    class="flex h-[calc(100dvh-4rem)] overflow-hidden bg-fondo text-tinta"
  >
    <!-- BARRA LATERAL -->
    <aside class="flex w-80 shrink-0 flex-col border-r border-linea bg-superficie max-md:w-full" :class="seleccionado ? 'max-md:hidden' : ''">
      <div class="border-b border-linea p-5">
        <h2 class="flex items-center gap-2 text-2xl font-bold tracking-[-0.02em]">
          <span class="material-symbols-outlined text-a1" aria-hidden="true">groups</span>
          Mis estudiantes
        </h2>
        <p class="mt-1 text-sm text-tenue">
          {{ estudiantes.length }} alumnos registrados
        </p>
      </div>

      <div class="flex-1 overflow-y-auto scrollbar-thin">
        <div v-if="cargando" class="p-5 text-center text-tenue">
          Cargando lista...
        </div>

        <button
          v-for="alumno in estudiantes"
          :key="alumno.email"
          @click="cargarExpediente(alumno)"
          class="flex w-full items-center gap-3 border-b border-linea px-5 py-3.5 text-left transition-colors hover:bg-hundido"
          :class="
            seleccionado?.email === alumno.email
              ? 'bg-hundido font-semibold'
              : ''
          "
        >
          <div
            class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full text-sm font-bold transition-colors"
            :class="
              seleccionado?.email === alumno.email
                ? 'bg-a1 text-white'
                : 'bg-hundido text-tinta'
            "
          >
            {{ obtenerIniciales(alumno) }}
          </div>
          <div>
            <p
              class="font-bold text-sm truncate"
              :class="
                seleccionado?.email === alumno.email
                  ? 'text-tinta'
                  : 'text-tinta'
              "
            >
              {{ alumno.nombre || "Sin nombre" }} {{ alumno.apellidos || "" }}
            </p>
            <p class="truncate text-sm text-tenue">{{ alumno.email }}</p>
          </div>
        </button>
      </div>

      <div class="border-t border-linea p-4">
        <button
          @click="cerrarSesion"
          class="boton boton-secundario w-full"
        >
          Cerrar sesión
        </button>
      </div>
    </aside>

    <!-- AREA PRINCIPAL -->
    <main class="relative flex min-w-0 flex-1 flex-col bg-fondo" :class="seleccionado ? '' : 'max-md:hidden'">
      <!-- Si no hay seleccionado -->
      <div
        v-if="!seleccionado"
        class="flex flex-1 flex-col items-center justify-center gap-2 p-8 text-center text-tenue"
      >
        <span class="material-symbols-outlined text-6xl" aria-hidden="true"
          >person_search</span
        >
        <p class="font-display text-2xl font-bold text-tinta">Selecciona un alumno para calificar</p><p>Sus entregas y tu retroalimentación aparecerán aquí.</p>
      </div>

      <!-- Si hay alumno seleccionado -->
      <div v-else class="flex-1 overflow-y-auto px-5 py-8 sm:px-8 lg:px-12">
        <header
          class="mb-8 border-b border-linea pb-6"
        >
          <button type="button" class="boton boton-secundario mb-6 !min-h-10 md:hidden" @click="seleccionado = null">
            <span class="material-symbols-outlined text-[20px]" aria-hidden="true">arrow_back</span>Alumnos
          </button>
          <div>
            <h1 class="text-[clamp(2rem,4vw,3rem)] font-extrabold leading-tight tracking-[-0.025em]">
              {{ seleccionado.nombre }} {{ seleccionado.apellidos }}
            </h1>
            <p class="mt-1 text-tenue">{{ seleccionado.email }}</p>
          </div>
        </header>

        <div v-if="cargandoExpediente" class="text-center py-10">
          <span
            class="material-symbols-outlined animate-spin text-4xl text-a1"
            >refresh</span
          >
        </div>

        <div v-else class="max-w-4xl space-y-4 pb-20">
          <!-- ========================================== -->
          <!-- TARJETA FORO 1 (CYAN)                    -->
          <!-- ========================================== -->
          <div
            class="overflow-hidden rounded-2xl border border-linea bg-superficie"
          >
            <div
              class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0"
              @click="toggle('f1')" @keydown.enter.prevent="toggle('f1')" @keydown.space.prevent="toggle('f1')"
            >
              <h3
                class="flex items-center gap-2 font-display text-lg font-bold"
              >
                <span class="material-symbols-outlined text-a1" aria-hidden="true"
                  >forum</span
                >
                Foro 1: Densidad Mineral
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="chip"
                  :class="
                    expediente.foro1
                      ? '!bg-ok-fondo !text-ok'
                      : '!bg-error-fondo !text-error'
                  "
                  >{{ expediente.foro1 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-tenue transition-transform"
                  :class="expandido.f1 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro1 && expandido.f1"
              class="border-t border-linea p-5 text-[0.9375rem] sm:p-6"
            >
              <!-- Respuestas -->
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="font-semibold block mb-1"
                    >1. Definición:</strong
                  >
                  <p class="rounded-xl bg-hundido p-3">
                    {{ expediente.foro1.r1 }}
                  </p>
                </div>
                <!-- ... resto de preguntas resumidas para no hacer el código gigante ... -->
                <details>
                  <summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">
                    Ver todas las respuestas...
                  </summary>
                  <div class="mt-3 space-y-3">
                    <p>
                      <strong class="font-semibold">P2:</strong>
                      {{ expediente.foro1.r2 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P3:</strong>
                      {{ expediente.foro1.r3 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P4:</strong>
                      {{ expediente.foro1.r4 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P5:</strong>
                      {{ expediente.foro1.r5 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P6:</strong>
                      {{ expediente.foro1.r6 }}
                    </p>
                  </div>
                </details>
              </div>

              <!-- ZONA DE FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <label
                  class="mb-2 block text-sm font-semibold"
                  >Retroalimentación:</label
                >
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro1"
                    rows="1"
                    class="campo flex-1"
                    placeholder="Escribe un comentario..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro1')"
                    class="boton boton-primario"
                  >
                    Enviar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 2 (SKY)                     -->
          <!-- ========================================== -->
          <div
            class="overflow-hidden rounded-2xl border border-linea bg-superficie"
          >
            <div
              class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0"
              @click="toggle('f2')" @keydown.enter.prevent="toggle('f2')" @keydown.space.prevent="toggle('f2')"
            >
              <h3
                class="flex items-center gap-2 font-display text-lg font-bold"
              >
                <span class="material-symbols-outlined text-a1" aria-hidden="true"
                  >bar_chart</span
                >
                Foro 2: Gráfico Comparativo
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="chip"
                  :class="
                    expediente.foro2
                      ? '!bg-ok-fondo !text-ok'
                      : '!bg-error-fondo !text-error'
                  "
                  >{{ expediente.foro2 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-tenue transition-transform"
                  :class="expandido.f2 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro2 && expandido.f2"
              class="border-t border-linea p-5 text-[0.9375rem] sm:p-6"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="font-semibold block mb-1">1. Análisis:</strong>
                  <p class="rounded-xl bg-hundido p-3">
                    {{ expediente.foro2.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">
                    Ver más...
                  </summary>
                  <div class="mt-3 space-y-3">
                    <p>
                      <strong class="font-semibold">P2:</strong>
                      {{ expediente.foro2.r2 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P3:</strong>
                      {{ expediente.foro2.r3 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P4:</strong>
                      {{ expediente.foro2.r4 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P5:</strong>
                      {{ expediente.foro2.r5 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P6:</strong>
                      {{ expediente.foro2.r6 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro2"
                    rows="1"
                    class="campo flex-1"
                    placeholder="Retroalimentación para Foro 2..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro2')"
                    class="boton boton-primario"
                  >
                    Enviar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 3 (BLUE)                    -->
          <!-- ========================================== -->
          <div
            class="overflow-hidden rounded-2xl border border-linea bg-superficie"
          >
            <div
              class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0"
              @click="toggle('f3')" @keydown.enter.prevent="toggle('f3')" @keydown.space.prevent="toggle('f3')"
            >
              <h3
                class="flex items-center gap-2 font-display text-lg font-bold"
              >
                <span class="material-symbols-outlined text-a1" aria-hidden="true"
                  >accessibility_new</span
                >
                Foro 3: DMO Cadera
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="chip"
                  :class="
                    expediente.foro3
                      ? '!bg-ok-fondo !text-ok'
                      : '!bg-error-fondo !text-error'
                  "
                  >{{ expediente.foro3 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-tenue transition-transform"
                  :class="expandido.f3 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro3 && expandido.f3"
              class="border-t border-linea p-5 text-[0.9375rem] sm:p-6"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="font-semibold block mb-1"
                    >1. Cambio DMO:</strong
                  >
                  <p class="rounded-xl bg-hundido p-3">
                    {{ expediente.foro3.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">
                    Ver más...
                  </summary>
                  <div class="mt-3 space-y-3">
                    <p>
                      <strong class="font-semibold">P2:</strong>
                      {{ expediente.foro3.r2 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P3:</strong>
                      {{ expediente.foro3.r3 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P4:</strong>
                      {{ expediente.foro3.r4 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P5:</strong>
                      {{ expediente.foro3.r5 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P7:</strong>
                      {{ expediente.foro3.r7 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P8:</strong>
                      {{ expediente.foro3.r8 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro3"
                    rows="1"
                    class="campo flex-1"
                    placeholder="Retroalimentación para Foro 3..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro3')"
                    class="boton boton-primario"
                  >
                    Enviar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 4 (INDIGO)                  -->
          <!-- ========================================== -->
          <div
            class="overflow-hidden rounded-2xl border border-linea bg-superficie"
          >
            <div
              class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0"
              @click="toggle('f4')" @keydown.enter.prevent="toggle('f4')" @keydown.space.prevent="toggle('f4')"
            >
              <h3
                class="flex items-center gap-2 font-display text-lg font-bold"
              >
                <span class="material-symbols-outlined text-a1" aria-hidden="true"
                  >analytics</span
                >
                Foro 4: Análisis DMO
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="chip"
                  :class="
                    expediente.foro4
                      ? '!bg-ok-fondo !text-ok'
                      : '!bg-error-fondo !text-error'
                  "
                  >{{ expediente.foro4 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-tenue transition-transform"
                  :class="expandido.f4 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro4 && expandido.f4"
              class="border-t border-linea p-5 text-[0.9375rem] sm:p-6"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="font-semibold block mb-1"
                    >1. Expresión:</strong
                  >
                  <p class="rounded-xl bg-hundido p-3">
                    {{ expediente.foro4.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">
                    Ver más...
                  </summary>
                  <div class="mt-3 space-y-3">
                    <p>
                      <strong class="font-semibold">P2:</strong>
                      {{ expediente.foro4.r2 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P3:</strong>
                      {{ expediente.foro4.r3 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P4:</strong>
                      {{ expediente.foro4.r4 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P5:</strong>
                      {{ expediente.foro4.r5 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P6:</strong>
                      {{ expediente.foro4.r6 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P7:</strong>
                      {{ expediente.foro4.r7 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro4"
                    rows="1"
                    class="campo flex-1"
                    placeholder="Retroalimentación para Foro 4..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro4')"
                    class="boton boton-primario"
                  >
                    Enviar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 5 (VIOLET)                  -->
          <!-- ========================================== -->
          <div
            class="overflow-hidden rounded-2xl border border-linea bg-superficie"
          >
            <div
              class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0"
              @click="toggle('f5')" @keydown.enter.prevent="toggle('f5')" @keydown.space.prevent="toggle('f5')"
            >
              <h3
                class="flex items-center gap-2 font-display text-lg font-bold"
              >
                <span class="material-symbols-outlined text-a1" aria-hidden="true"
                  >trending_up</span
                >
                Foro 5: Razón de Cambio
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="chip"
                  :class="
                    expediente.foro5
                      ? '!bg-ok-fondo !text-ok'
                      : '!bg-error-fondo !text-error'
                  "
                  >{{ expediente.foro5 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-tenue transition-transform"
                  :class="expandido.f5 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro5 && expandido.f5"
              class="border-t border-linea p-5 text-[0.9375rem] sm:p-6"
            >
              <div class="grid gap-4 mb-6">
                <!-- Las 3 fotos de la tabla -->
                <div
                  v-if="
                    expediente.foro5.imagen_1 ||
                    expediente.foro5.imagen_2 ||
                    expediente.foro5.imagen_3
                  "
                >
                  <strong class="font-semibold block mb-1"
                    >1. Fotos de la tabla (RPC):</strong
                  >
                  <div class="grid grid-cols-3 gap-2">
                    <img
                      v-if="expediente.foro5.imagen_1"
                      :src="expediente.foro5.imagen_1"
                      class="h-32 w-full rounded-xl border border-linea object-cover"
                    />
                    <img
                      v-if="expediente.foro5.imagen_2"
                      :src="expediente.foro5.imagen_2"
                      class="h-32 w-full rounded-xl border border-linea object-cover"
                    />
                    <img
                      v-if="expediente.foro5.imagen_3"
                      :src="expediente.foro5.imagen_3"
                      class="h-32 w-full rounded-xl border border-linea object-cover"
                    />
                  </div>
                </div>

                <div>
                  <strong class="font-semibold block mb-1"
                    >2. Comportamiento RPC:</strong
                  >
                  <p class="rounded-xl bg-hundido p-3">
                    {{ expediente.foro5.r2 }}
                  </p>
                </div>

                <!-- Imagen del bosquejo (pregunta 3) -->
                <div v-if="expediente.foro5.imagen_pregunta_3">
                  <strong class="font-semibold block mb-1"
                    >3. Bosquejo de la gráfica:</strong
                  >
                  <img
                    :src="expediente.foro5.imagen_pregunta_3"
                    class="max-h-64 rounded-xl border border-linea object-contain"
                  />
                </div>

                <details>
                  <summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">
                    Ver más respuestas...
                  </summary>
                  <div class="mt-3 space-y-3">
                    <p>
                      <strong class="font-semibold">P4:</strong>
                      {{ expediente.foro5.r4 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P5:</strong>
                      {{ expediente.foro5.r5 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P6:</strong>
                      {{ expediente.foro5.r6 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro5"
                    rows="1"
                    class="campo flex-1"
                    placeholder="Retroalimentación para Foro 5..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro5')"
                    class="boton boton-primario"
                  >
                    Enviar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA FORO 6 (PURPLE)                  -->
          <!-- ========================================== -->
          <div
            class="overflow-hidden rounded-2xl border border-linea bg-superficie"
          >
            <div
              class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0"
              @click="toggle('f6')" @keydown.enter.prevent="toggle('f6')" @keydown.space.prevent="toggle('f6')"
            >
              <h3
                class="flex items-center gap-2 font-display text-lg font-bold"
              >
                <span class="material-symbols-outlined text-a1" aria-hidden="true"
                  >swap_horiz</span
                >
                Foro 6: Covariación
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="chip"
                  :class="
                    expediente.foro6
                      ? '!bg-ok-fondo !text-ok'
                      : '!bg-error-fondo !text-error'
                  "
                  >{{ expediente.foro6 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-tenue transition-transform"
                  :class="expandido.f6 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro6 && expandido.f6"
              class="border-t border-linea p-5 text-[0.9375rem] sm:p-6"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="font-semibold block mb-1"
                    >1. Dominio:</strong
                  >
                  <p class="rounded-xl bg-hundido p-3">
                    {{ expediente.foro6.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">
                    Ver más...
                  </summary>
                  <div class="mt-3 space-y-3">
                    <p>
                      <strong class="font-semibold">2. Argumento:</strong>
                      {{ expediente.foro6.r2 }}
                    </p>
                    <p>
                      <strong class="font-semibold">3. Simulador:</strong>
                      {{ expediente.foro6.r3 }}
                    </p>
                    <p>
                      <strong class="font-semibold">4. GeoGebra:</strong>
                      {{ expediente.foro6.r4 }}
                    </p>
                    <p>
                      <strong class="font-semibold">5. Pendientes:</strong>
                      {{ expediente.foro6.r5 }}
                    </p>
                    <p>
                      <strong class="font-semibold">6. Notas:</strong>
                      {{ expediente.foro6.r6 }}
                    </p>
                    <p>
                      <strong class="font-semibold">7. Óptimo M:</strong>
                      {{ expediente.foro6.r7 }}
                    </p>
                    <p>
                      <strong class="font-semibold">8. Óptimo H:</strong>
                      {{ expediente.foro6.r8 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro6"
                    rows="1"
                    class="campo flex-1"
                    placeholder="Retroalimentación para Foro 6..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro6')"
                    class="boton boton-primario"
                  >
                    Enviar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- TARJETA EXAMEN 1 (TEAL)                  -->
          <!-- ========================================== -->
          <div
            class="overflow-hidden rounded-2xl border border-linea bg-superficie"
          >
            <div
              class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0"
              @click="toggle('e1')" @keydown.enter.prevent="toggle('e1')" @keydown.space.prevent="toggle('e1')"
            >
              <h3
                class="flex items-center gap-2 font-display text-lg font-bold"
              >
                <span class="material-symbols-outlined text-a1" aria-hidden="true"
                  >assignment_turned_in</span
                >
                Examen 1
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="chip"
                  :class="
                    expediente.examen1
                      ? '!bg-ok-fondo !text-ok'
                      : '!bg-error-fondo !text-error'
                  "
                  >{{
                    expediente.examen1 ? "Completado" : "Sin entregar"
                  }}</span
                >
                <span
                  class="material-symbols-outlined text-tenue transition-transform"
                  :class="expandido.e1 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.examen1 && expandido.e1"
              class="border-t border-linea p-5 text-[0.9375rem] sm:p-6"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="font-semibold block mb-1">Puntaje:</strong>
                  <span
                    class="bg-teal-900/50 text-teal-300 px-2 py-1 rounded font-bold"
                    >{{ expediente.examen1.r6 }}</span
                  >
                </div>
                <div>
                  <strong class="font-semibold block mb-1">P1:</strong>
                  {{ expediente.examen1.r1 }}
                </div>
                <details>
                  <summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">
                    Ver más...
                  </summary>
                  <div class="mt-3 space-y-3">
                    <p>
                      <strong class="font-semibold">P2:</strong>
                      {{ expediente.examen1.r2 }}
                    </p>
                    <p>
                      <strong class="font-semibold">P3:</strong>
                      {{ expediente.examen1.r3 }}
                    </p>
                    <p>
                      <strong class="font-semibold">Oración:</strong>
                      {{ expediente.examen1.r4 }}
                    </p>
                    <p>
                      <strong class="font-semibold">Parejas:</strong>
                      {{ expediente.examen1.r5 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.examen1"
                    rows="1"
                    class="campo flex-1"
                    placeholder="Retroalimentación para Examen 1..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('examen1')"
                    class="boton boton-primario"
                  >
                    Enviar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- TARJETA EXAMEN 2 (ROSE) -->
          <div class="overflow-hidden rounded-2xl border border-linea bg-superficie">
            <div class="group flex cursor-pointer items-center justify-between gap-4 px-5 py-4 transition-colors hover:bg-hundido sm:px-6" role="button" tabindex="0" @click="toggle('e2')" @keydown.enter.prevent="toggle('e2')" @keydown.space.prevent="toggle('e2')">
              <h3 class="flex items-center gap-2 font-display text-lg font-bold">
                <span class="material-symbols-outlined text-a1" aria-hidden="true">assignment_turned_in</span> Examen 2
              </h3>
              <div class="flex items-center gap-3">
                <span class="chip" :class="expediente.examen2 ? '!bg-ok-fondo !text-ok' : '!bg-error-fondo !text-error'">{{ expediente.examen2 ? 'Completado' : 'Sin entregar' }}</span>
                <span class="material-symbols-outlined text-tenue transition-transform" :class="expandido.e2 ? 'rotate-180' : ''">expand_more</span>
              </div>
            </div>
            <div v-if="expediente.examen2 && expandido.e2" class="border-t border-linea p-5 text-[0.9375rem] sm:p-6">
              <div class="grid gap-4 mb-6">
                <!-- Mostramos las 7 preguntas del examen 2 -->
                <div><strong class="font-semibold block mb-1">P1:</strong> {{ expediente.examen2.r1 }}</div>
                <div><strong class="font-semibold block mb-1">P2:</strong> {{ expediente.examen2.r2 }}</div>
                <details><summary class="mt-1 cursor-pointer text-sm font-semibold text-a1">Ver más...</summary>
                  <div class="mt-3 space-y-3">
                    <p><strong class="font-semibold">P3:</strong> {{ expediente.examen2.r3 }}</p>
                    <p><strong class="font-semibold">P4:</strong> {{ expediente.examen2.r4 }}</p>
                    <p><strong class="font-semibold">P5:</strong> {{ expediente.examen2.r5 }}</p>
                    <p><strong class="font-semibold">P6:</strong> {{ expediente.examen2.r6 }}</p>
                    <p><strong class="font-semibold">P7:</strong> {{ expediente.examen2.r7 }}</p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 border-t border-linea pt-4">
                <div class="flex gap-2">
                  <textarea v-model="feedbackInputs.examen2" rows="1" class="campo flex-1" placeholder="Retroalimentación para Examen 2..."></textarea>
                  <button @click="enviarFeedback('examen2')" class="boton boton-primario">Enviar</button>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { API_URL } from "@/api.js";
import EncabezadoPortal from "@/components/EncabezadoPortal.vue";
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";

// URL del Backend (Asegúrate de que sea 127.0.0.1:8000 para local)

const router = useRouter();
const estudiantes = ref([]);
const cargando = ref(true);
const seleccionado = ref(null);
const expediente = ref({});
const cargandoExpediente = ref(false);

// Control de acordeón
const expandido = ref({
  f1: false,
  f2: false,
  f3: false,
  f4: false,
  f5: false,
  f6: false,
  e1: false,
  e2: false,
});

// Estado de Inputs de Feedback
const feedbackInputs = reactive({
  foro1: "",
  foro2: "",
  foro3: "",
  foro4: "",
  foro5: "",
  foro6: "",
  examen1: "",
  examen2: "",
});

function toggle(seccion) {
  expandido.value[seccion] = !expandido.value[seccion];
}

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/lista_estudiantes`);
    estudiantes.value = await res.json();
  } catch (e) {
    console.error(e);
  } finally {
    cargando.value = false;
  }
});

async function cargarExpediente(alumno) {
  seleccionado.value = alumno;
  cargandoExpediente.value = true;
  expandido.value = {
    f1: false,
    f2: false,
    f3: false,
    f4: false,
    f5: false,
    f6: false,
    e1: false,
    e2: false,
  };

  // Limpiamos feedbacks anteriores
  Object.keys(feedbackInputs).forEach((k) => (feedbackInputs[k] = ""));

  try {
    const res = await fetch(`${API_URL}/expediente_completo/${alumno.email}`);
    expediente.value = await res.json();
  } catch (e) {
    console.error(e);
  } finally {
    cargandoExpediente.value = false;
  }
}

async function enviarFeedback(actividad) {
  if (!seleccionado.value) return;
  const texto = feedbackInputs[actividad];
  if (!texto) return alert("Escribe un comentario primero.");

  try {
    const res = await fetch(`${API_URL}/guardar_feedback`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email_alumno: seleccionado.value.email,
        actividad: actividad,
        comentario: texto,
      }),
    });
    const datos = await res.json();
    if (datos.exito) {
      alert("Feedback enviado correctamente");
      feedbackInputs[actividad] = ""; // Limpiar campo
    } else {
      alert("Error al enviar");
    }
  } catch (e) {
    alert("Error de conexión");
  }
}

function obtenerIniciales(alumno) {
  if (alumno.nombre) return alumno.nombre[0].toUpperCase();
  return alumno.email[0].toUpperCase();
}

function cerrarSesion() {
  localStorage.clear();
  router.push("/");
}
</script>
