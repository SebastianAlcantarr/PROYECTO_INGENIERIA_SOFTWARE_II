<template>
  <div
    class="flex h-screen bg-gray-900 text-white overflow-hidden font-display"
  >
    <!-- BARRA LATERAL -->
    <aside class="w-80 bg-[#161d2b] border-r border-gray-700 flex flex-col">
      <div class="p-4 border-b border-gray-700 bg-blue-900/20">
        <h2 class="text-xl font-bold text-sky-300 flex items-center gap-2">
          <span class="material-symbols-outlined">school</span>
          Mis Estudiantes
        </h2>
        <p class="text-xs text-gray-400 mt-1">
          {{ estudiantes.length }} alumnos registrados
        </p>
      </div>

      <div class="flex-1 overflow-y-auto scrollbar-thin">
        <div v-if="cargando" class="p-4 text-center text-gray-500">
          Cargando lista...
        </div>

        <button
          v-for="alumno in estudiantes"
          :key="alumno.email"
          @click="cargarExpediente(alumno)"
          class="w-full text-left p-4 hover:bg-gray-800 border-b border-gray-800 transition-colors flex items-center gap-3"
          :class="
            seleccionado?.email === alumno.email
              ? 'bg-sky-900/20 border-l-4 border-l-sky-400'
              : ''
          "
        >
          <div
            class="h-10 w-10 rounded-full flex items-center justify-center text-sm font-bold text-white transition-colors"
            :class="
              seleccionado?.email === alumno.email
                ? 'bg-sky-600'
                : 'bg-gray-700'
            "
          >
            {{ obtenerIniciales(alumno) }}
          </div>
          <div>
            <p
              class="font-bold text-sm truncate"
              :class="
                seleccionado?.email === alumno.email
                  ? 'text-sky-100'
                  : 'text-gray-300'
              "
            >
              {{ alumno.nombre || "Sin nombre" }} {{ alumno.apellidos || "" }}
            </p>
            <p class="text-xs text-gray-500 truncate">{{ alumno.email }}</p>
          </div>
        </button>
      </div>

      <div class="p-4 border-t border-gray-700">
        <button
          @click="cerrarSesion"
          class="w-full py-2 bg-red-900/50 hover:bg-red-900 text-red-200 rounded text-sm transition"
        >
          Cerrar Sesión Profe
        </button>
      </div>
    </aside>

    <!-- AREA PRINCIPAL -->
    <main class="flex-1 flex flex-col bg-[#0f172a] relative">
      <!-- Si no hay seleccionado -->
      <div
        v-if="!seleccionado"
        class="flex-1 flex flex-col items-center justify-center text-gray-500 opacity-50"
      >
        <span class="material-symbols-outlined text-8xl mb-4"
          >person_search</span
        >
        <p class="text-xl">Selecciona un alumno para calificar</p>
      </div>

      <!-- Si hay alumno seleccionado -->
      <div v-else class="flex-1 overflow-y-auto p-8 scrollbar-thin">
        <header
          class="mb-8 flex justify-between items-end border-b border-gray-700 pb-4"
        >
          <div>
            <h1 class="text-3xl font-bold text-white">
              {{ seleccionado.nombre }} {{ seleccionado.apellidos }}
            </h1>
            <p class="text-sky-400">{{ seleccionado.email }}</p>
          </div>
        </header>

        <div v-if="cargandoExpediente" class="text-center py-10">
          <span
            class="material-symbols-outlined animate-spin text-4xl text-sky-500"
            >refresh</span
          >
        </div>

        <div v-else class="space-y-6 animate-fade-in pb-20">
          <!-- ========================================== -->
          <!-- TARJETA FORO 1 (CYAN)                    -->
          <!-- ========================================== -->
          <div
            class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg"
          >
            <div
              class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group"
              @click="toggle('f1')"
            >
              <h3
                class="font-bold text-lg flex items-center gap-2 text-cyan-300"
              >
                <span class="material-symbols-outlined text-cyan-400"
                  >forum</span
                >
                Foro 1: Densidad Mineral
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="text-xs px-2 py-1 rounded font-bold border"
                  :class="
                    expediente.foro1
                      ? 'bg-green-900/30 text-green-300 border-green-700'
                      : 'bg-red-900/30 text-red-300 border-red-800'
                  "
                  >{{ expediente.foro1 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-gray-400 transition-transform"
                  :class="expandido.f1 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro1 && expandido.f1"
              class="p-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-cyan-500"
            >
              <!-- Respuestas -->
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="text-cyan-200 block mb-1"
                    >1. Definición:</strong
                  >
                  <p class="bg-gray-900/50 p-2 rounded">
                    {{ expediente.foro1.r1 }}
                  </p>
                </div>
                <!-- ... resto de preguntas resumidas para no hacer el código gigante ... -->
                <details>
                  <summary class="cursor-pointer text-cyan-400 mt-1">
                    Ver todas las respuestas...
                  </summary>
                  <div class="mt-2 space-y-2 pl-2 border-l border-gray-700">
                    <p>
                      <strong class="text-cyan-200">P2:</strong>
                      {{ expediente.foro1.r2 }}
                    </p>
                    <p>
                      <strong class="text-cyan-200">P3:</strong>
                      {{ expediente.foro1.r3 }}
                    </p>
                    <p>
                      <strong class="text-cyan-200">P4:</strong>
                      {{ expediente.foro1.r4 }}
                    </p>
                    <p>
                      <strong class="text-cyan-200">P5:</strong>
                      {{ expediente.foro1.r5 }}
                    </p>
                    <p>
                      <strong class="text-cyan-200">P6:</strong>
                      {{ expediente.foro1.r6 }}
                    </p>
                  </div>
                </details>
              </div>

              <!-- ZONA DE FEEDBACK -->
              <div class="mt-4 pt-4 border-t border-gray-700">
                <label
                  class="text-xs font-bold text-cyan-500 uppercase mb-2 block"
                  >Retroalimentación:</label
                >
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro1"
                    rows="1"
                    class="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-cyan-500 outline-none transition-all"
                    placeholder="Escribe un comentario..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro1')"
                    class="bg-cyan-700 hover:bg-cyan-600 text-white px-4 rounded font-bold text-xs transition-colors"
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
            class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg"
          >
            <div
              class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group"
              @click="toggle('f2')"
            >
              <h3
                class="font-bold text-lg flex items-center gap-2 text-sky-300"
              >
                <span class="material-symbols-outlined text-sky-400"
                  >bar_chart</span
                >
                Foro 2: Gráfico Comparativo
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="text-xs px-2 py-1 rounded font-bold border"
                  :class="
                    expediente.foro2
                      ? 'bg-green-900/30 text-green-300 border-green-700'
                      : 'bg-red-900/30 text-red-300 border-red-800'
                  "
                  >{{ expediente.foro2 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-gray-400 transition-transform"
                  :class="expandido.f2 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro2 && expandido.f2"
              class="p-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-sky-500"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="text-sky-200 block mb-1">1. Análisis:</strong>
                  <p class="bg-gray-900/50 p-2 rounded">
                    {{ expediente.foro2.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="cursor-pointer text-sky-400 mt-1">
                    Ver más...
                  </summary>
                  <div class="mt-2 space-y-2 pl-2 border-l border-gray-700">
                    <p>
                      <strong class="text-sky-200">P2:</strong>
                      {{ expediente.foro2.r2 }}
                    </p>
                    <p>
                      <strong class="text-sky-200">P3:</strong>
                      {{ expediente.foro2.r3 }}
                    </p>
                    <p>
                      <strong class="text-sky-200">P4:</strong>
                      {{ expediente.foro2.r4 }}
                    </p>
                    <p>
                      <strong class="text-sky-200">P5:</strong>
                      {{ expediente.foro2.r5 }}
                    </p>
                    <p>
                      <strong class="text-sky-200">P6:</strong>
                      {{ expediente.foro2.r6 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 pt-4 border-t border-gray-700">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro2"
                    rows="1"
                    class="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-sky-500 outline-none"
                    placeholder="Retroalimentación para Foro 2..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro2')"
                    class="bg-sky-700 hover:bg-sky-600 text-white px-4 rounded font-bold text-xs"
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
            class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg"
          >
            <div
              class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group"
              @click="toggle('f3')"
            >
              <h3
                class="font-bold text-lg flex items-center gap-2 text-blue-300"
              >
                <span class="material-symbols-outlined text-blue-400"
                  >accessibility_new</span
                >
                Foro 3: DMO Cadera
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="text-xs px-2 py-1 rounded font-bold border"
                  :class="
                    expediente.foro3
                      ? 'bg-green-900/30 text-green-300 border-green-700'
                      : 'bg-red-900/30 text-red-300 border-red-800'
                  "
                  >{{ expediente.foro3 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-gray-400 transition-transform"
                  :class="expandido.f3 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro3 && expandido.f3"
              class="p-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-blue-500"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="text-blue-200 block mb-1"
                    >1. Cambio DMO:</strong
                  >
                  <p class="bg-gray-900/50 p-2 rounded">
                    {{ expediente.foro3.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="cursor-pointer text-blue-400 mt-1">
                    Ver más...
                  </summary>
                  <div class="mt-2 space-y-2 pl-2 border-l border-gray-700">
                    <p>
                      <strong class="text-blue-200">P2:</strong>
                      {{ expediente.foro3.r2 }}
                    </p>
                    <p>
                      <strong class="text-blue-200">P3:</strong>
                      {{ expediente.foro3.r3 }}
                    </p>
                    <p>
                      <strong class="text-blue-200">P4:</strong>
                      {{ expediente.foro3.r4 }}
                    </p>
                    <p>
                      <strong class="text-blue-200">P5:</strong>
                      {{ expediente.foro3.r5 }}
                    </p>
                    <p>
                      <strong class="text-blue-200">P7:</strong>
                      {{ expediente.foro3.r7 }}
                    </p>
                    <p>
                      <strong class="text-blue-200">P8:</strong>
                      {{ expediente.foro3.r8 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 pt-4 border-t border-gray-700">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro3"
                    rows="1"
                    class="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-blue-500 outline-none"
                    placeholder="Retroalimentación para Foro 3..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro3')"
                    class="bg-blue-700 hover:bg-blue-600 text-white px-4 rounded font-bold text-xs"
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
            class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg"
          >
            <div
              class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group"
              @click="toggle('f4')"
            >
              <h3
                class="font-bold text-lg flex items-center gap-2 text-indigo-300"
              >
                <span class="material-symbols-outlined text-indigo-400"
                  >analytics</span
                >
                Foro 4: Análisis DMO
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="text-xs px-2 py-1 rounded font-bold border"
                  :class="
                    expediente.foro4
                      ? 'bg-green-900/30 text-green-300 border-green-700'
                      : 'bg-red-900/30 text-red-300 border-red-800'
                  "
                  >{{ expediente.foro4 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-gray-400 transition-transform"
                  :class="expandido.f4 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro4 && expandido.f4"
              class="p-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-indigo-500"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="text-indigo-200 block mb-1"
                    >1. Expresión:</strong
                  >
                  <p class="bg-gray-900/50 p-2 rounded">
                    {{ expediente.foro4.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="cursor-pointer text-indigo-400 mt-1">
                    Ver más...
                  </summary>
                  <div class="mt-2 space-y-2 pl-2 border-l border-gray-700">
                    <p>
                      <strong class="text-indigo-200">P2:</strong>
                      {{ expediente.foro4.r2 }}
                    </p>
                    <p>
                      <strong class="text-indigo-200">P3:</strong>
                      {{ expediente.foro4.r3 }}
                    </p>
                    <p>
                      <strong class="text-indigo-200">P4:</strong>
                      {{ expediente.foro4.r4 }}
                    </p>
                    <p>
                      <strong class="text-indigo-200">P5:</strong>
                      {{ expediente.foro4.r5 }}
                    </p>
                    <p>
                      <strong class="text-indigo-200">P6:</strong>
                      {{ expediente.foro4.r6 }}
                    </p>
                    <p>
                      <strong class="text-indigo-200">P7:</strong>
                      {{ expediente.foro4.r7 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 pt-4 border-t border-gray-700">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro4"
                    rows="1"
                    class="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-indigo-500 outline-none"
                    placeholder="Retroalimentación para Foro 4..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro4')"
                    class="bg-indigo-700 hover:bg-indigo-600 text-white px-4 rounded font-bold text-xs"
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
            class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg"
          >
            <div
              class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group"
              @click="toggle('f5')"
            >
              <h3
                class="font-bold text-lg flex items-center gap-2 text-violet-300"
              >
                <span class="material-symbols-outlined text-violet-400"
                  >trending_up</span
                >
                Foro 5: Razón de Cambio
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="text-xs px-2 py-1 rounded font-bold border"
                  :class="
                    expediente.foro5
                      ? 'bg-green-900/30 text-green-300 border-green-700'
                      : 'bg-red-900/30 text-red-300 border-red-800'
                  "
                  >{{ expediente.foro5 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-gray-400 transition-transform"
                  :class="expandido.f5 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro5 && expandido.f5"
              class="p-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-violet-600"
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
                  <strong class="text-violet-200 block mb-2"
                    >1. Fotos de la tabla (RPC):</strong
                  >
                  <div class="grid grid-cols-3 gap-2">
                    <img
                      v-if="expediente.foro5.imagen_1"
                      :src="expediente.foro5.imagen_1"
                      class="rounded border border-gray-600 h-32 w-full object-cover"
                    />
                    <img
                      v-if="expediente.foro5.imagen_2"
                      :src="expediente.foro5.imagen_2"
                      class="rounded border border-gray-600 h-32 w-full object-cover"
                    />
                    <img
                      v-if="expediente.foro5.imagen_3"
                      :src="expediente.foro5.imagen_3"
                      class="rounded border border-gray-600 h-32 w-full object-cover"
                    />
                  </div>
                </div>

                <div>
                  <strong class="text-violet-200 block mb-1"
                    >2. Comportamiento RPC:</strong
                  >
                  <p class="bg-gray-900/50 p-2 rounded">
                    {{ expediente.foro5.r2 }}
                  </p>
                </div>

                <!-- Imagen del bosquejo (pregunta 3) -->
                <div v-if="expediente.foro5.imagen_pregunta_3">
                  <strong class="text-violet-200 block mb-2"
                    >3. Bosquejo de la gráfica:</strong
                  >
                  <img
                    :src="expediente.foro5.imagen_pregunta_3"
                    class="rounded border border-gray-600 max-h-64 object-contain"
                  />
                </div>

                <details>
                  <summary class="cursor-pointer text-violet-400 mt-1">
                    Ver más respuestas...
                  </summary>
                  <div class="mt-2 space-y-2 pl-2 border-l border-gray-700">
                    <p>
                      <strong class="text-violet-200">P4:</strong>
                      {{ expediente.foro5.r4 }}
                    </p>
                    <p>
                      <strong class="text-violet-200">P5:</strong>
                      {{ expediente.foro5.r5 }}
                    </p>
                    <p>
                      <strong class="text-violet-200">P6:</strong>
                      {{ expediente.foro5.r6 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 pt-4 border-t border-gray-700">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro5"
                    rows="1"
                    class="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-violet-500 outline-none"
                    placeholder="Retroalimentación para Foro 5..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro5')"
                    class="bg-violet-700 hover:bg-violet-600 text-white px-4 rounded font-bold text-xs"
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
            class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg"
          >
            <div
              class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group"
              @click="toggle('f6')"
            >
              <h3
                class="font-bold text-lg flex items-center gap-2 text-purple-300"
              >
                <span class="material-symbols-outlined text-purple-400"
                  >swap_horiz</span
                >
                Foro 6: Covariación
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="text-xs px-2 py-1 rounded font-bold border"
                  :class="
                    expediente.foro6
                      ? 'bg-green-900/30 text-green-300 border-green-700'
                      : 'bg-red-900/30 text-red-300 border-red-800'
                  "
                  >{{ expediente.foro6 ? "Completado" : "Sin entregar" }}</span
                >
                <span
                  class="material-symbols-outlined text-gray-400 transition-transform"
                  :class="expandido.f6 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.foro6 && expandido.f6"
              class="p-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-purple-600"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="text-purple-200 block mb-1"
                    >1. Dominio:</strong
                  >
                  <p class="bg-gray-900/50 p-2 rounded">
                    {{ expediente.foro6.r1 }}
                  </p>
                </div>
                <details>
                  <summary class="cursor-pointer text-purple-400 mt-1">
                    Ver más...
                  </summary>
                  <div class="mt-2 space-y-2 pl-2 border-l border-gray-700">
                    <p>
                      <strong class="text-purple-200">2. Argumento:</strong>
                      {{ expediente.foro6.r2 }}
                    </p>
                    <p>
                      <strong class="text-purple-200">3. Simulador:</strong>
                      {{ expediente.foro6.r3 }}
                    </p>
                    <p>
                      <strong class="text-purple-200">4. GeoGebra:</strong>
                      {{ expediente.foro6.r4 }}
                    </p>
                    <p>
                      <strong class="text-purple-200">5. Pendientes:</strong>
                      {{ expediente.foro6.r5 }}
                    </p>
                    <p>
                      <strong class="text-purple-200">6. Notas:</strong>
                      {{ expediente.foro6.r6 }}
                    </p>
                    <p>
                      <strong class="text-purple-200">7. Óptimo M:</strong>
                      {{ expediente.foro6.r7 }}
                    </p>
                    <p>
                      <strong class="text-purple-200">8. Óptimo H:</strong>
                      {{ expediente.foro6.r8 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 pt-4 border-t border-gray-700">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.foro6"
                    rows="1"
                    class="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-purple-500 outline-none"
                    placeholder="Retroalimentación para Foro 6..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('foro6')"
                    class="bg-purple-700 hover:bg-purple-600 text-white px-4 rounded font-bold text-xs"
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
            class="bg-[#1e293b] rounded-xl overflow-hidden border border-gray-700 shadow-lg"
          >
            <div
              class="bg-gray-800 px-6 py-4 flex justify-between items-center cursor-pointer hover:bg-gray-750 transition-colors group"
              @click="toggle('e1')"
            >
              <h3
                class="font-bold text-lg flex items-center gap-2 text-teal-300"
              >
                <span class="material-symbols-outlined text-teal-400"
                  >assignment_turned_in</span
                >
                Examen 1
              </h3>
              <div class="flex items-center gap-3">
                <span
                  class="text-xs px-2 py-1 rounded font-bold border"
                  :class="
                    expediente.examen1
                      ? 'bg-green-900/30 text-green-300 border-green-700'
                      : 'bg-red-900/30 text-red-300 border-red-800'
                  "
                  >{{
                    expediente.examen1 ? "Completado" : "Sin entregar"
                  }}</span
                >
                <span
                  class="material-symbols-outlined text-gray-400 transition-transform"
                  :class="expandido.e1 ? 'rotate-180' : ''"
                  >expand_more</span
                >
              </div>
            </div>
            <div
              v-if="expediente.examen1 && expandido.e1"
              class="p-6 text-sm text-gray-300 border-t border-gray-700 border-l-4 border-l-teal-500"
            >
              <div class="grid gap-4 mb-6">
                <div>
                  <strong class="text-teal-200 block mb-1">Puntaje:</strong>
                  <span
                    class="bg-teal-900/50 text-teal-300 px-2 py-1 rounded font-bold"
                    >{{ expediente.examen1.r6 }}</span
                  >
                </div>
                <div>
                  <strong class="text-teal-200 block mb-1">P1:</strong>
                  {{ expediente.examen1.r1 }}
                </div>
                <details>
                  <summary class="cursor-pointer text-teal-400 mt-1">
                    Ver más...
                  </summary>
                  <div class="mt-2 space-y-2 pl-2 border-l border-gray-700">
                    <p>
                      <strong class="text-teal-200">P2:</strong>
                      {{ expediente.examen1.r2 }}
                    </p>
                    <p>
                      <strong class="text-teal-200">P3:</strong>
                      {{ expediente.examen1.r3 }}
                    </p>
                    <p>
                      <strong class="text-teal-200">Oración:</strong>
                      {{ expediente.examen1.r4 }}
                    </p>
                    <p>
                      <strong class="text-teal-200">Parejas:</strong>
                      {{ expediente.examen1.r5 }}
                    </p>
                  </div>
                </details>
              </div>
              <!-- FEEDBACK -->
              <div class="mt-4 pt-4 border-t border-gray-700">
                <div class="flex gap-2">
                  <textarea
                    v-model="feedbackInputs.examen1"
                    rows="1"
                    class="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-teal-500 outline-none"
                    placeholder="Retroalimentación para Examen 1..."
                  ></textarea>
                  <button
                    @click="enviarFeedback('examen1')"
                    class="bg-teal-700 hover:bg-teal-600 text-white px-4 rounded font-bold text-xs"
                  >
                    Enviar
                  </button>
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
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";

// URL del Backend (Asegúrate de que sea 127.0.0.1:8000 para local)
const API_URL = "https://proyecto-ingenieria-software-6ccv.onrender.com";

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
    f1: true,
    f2: true,
    f3: true,
    f4: true,
    f5: true,
    f6: true,
    e1: true,
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

<style scoped>
.scrollbar-thin::-webkit-scrollbar {
  width: 6px;
}
.scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: #374151;
  border-radius: 20px;
}
.scrollbar-thin::-webkit-scrollbar-track {
  background-color: transparent;
}
</style>
