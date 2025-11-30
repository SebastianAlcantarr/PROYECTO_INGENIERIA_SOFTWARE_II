<template>
  <div class="flex flex-col md:flex-row min-h-screen bg-[#244a76] dark:bg-[rgb(16,22,34)]">
    <!-- SIDEBAR -->
    <Sidebar class="hidden md:block" />

    <main class="w-full ml-0 md:ml-72 flex flex-col">
      <div class="flex-1 p-4 sm:p-6 md:p-8 lg:p-12">
        <div class="mx-auto max-w-7xl">

          <!-- TÍTULO -->
          <section class="scroll-mt-20 mb-8" id="introduction">
            <div class="bg-[#161d2b] rounded-xl p-6 shadow-lg">
              <h1 class="text-white text-3xl md:text-5xl font-black text-center">
                Foro 1: La densidad mineral ósea
              </h1>
            </div>
          </section>

          <!-- SECCIÓN DE PREGUNTAS -->
          <section class="space-y-6">
            <h2 class="text-white text-xl font-bold px-2">
              Investiga y responde las siguientes preguntas:
            </h2>

            <div class="bg-[#161d2b] p-6 rounded-xl shadow-xl space-y-8">

              <!-- Pregunta 1 -->
              <div>
                <h3 class="pregunta-texto text-xl text-white/90 mb-3">
                  1.- Explica en qué consiste la densidad mineral ósea (DMO) y cómo se mide.
                </h3>
                <textarea v-model="r1" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 2 -->
              <div>
                <h3 class="pregunta-texto text-xl text-white/90 mb-3">
                  2.- ¿Qué factores consideras que influyen en una buena salud ósea?
                </h3>
                <textarea v-model="r2" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 3 -->
              <div>
                <h3 class="pregunta-texto text-xl text-white/90 mb-3">
                  3.- ¿Relación entre edad y DMO? Justifica.
                </h3>
                <textarea v-model="r3" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 4 -->
              <div>
                <h3 class="pregunta-texto text-xl text-white/90 mb-3">
                  4.- ¿Cómo evoluciona la DMO a lo largo de la vida?
                </h3>
                <textarea v-model="r4" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 5 -->
              <div>
                <h3 class="pregunta-texto text-xl text-white/90 mb-3">
                  5.- ¿Se puede saber la edad aproximada dado un valor de DMO?
                </h3>
                <textarea v-model="r5" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- Pregunta 6 -->
              <div>
                <h3 class="pregunta-texto text-xl text-white/90 mb-3">
                  6.- ¿Diferencias entre esqueleto femenino y masculino?
                </h3>
                <textarea v-model="r6" rows="3" placeholder="Tu respuesta..." class="input-foro"></textarea>
              </div>

              <!-- BOTÓN DE ENVÍO -->
              <div class="pt-6 border-t border-gray-700 flex flex-col items-end gap-2">
                <p v-if="mensaje" :class="`text-sm font-bold ${tipoMensaje === 'error' ? 'text-red-400' : 'text-green-400'}`">
                  {{ mensaje }}
                </p>
                <button
                    @click="enviarRespuestas"
                    :disabled="enviando"
                    class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all active:scale-95 disabled:opacity-50"
                >
                  {{ enviando ? 'Enviando...' : 'Enviar Respuestas y Ver Foro' }}
                </button>
              </div>
            </div>
          </section>

          <!-- SECCIÓN DE RESPUESTAS DE OTROS (EL MURO) -->
          <section v-if="listaRespuestas.length > 0" class="mt-12 animate-fade-in-up">
            <h2 class="text-white text-2xl font-bold mb-6 border-b border-gray-700 pb-2">
              Participaciones del Grupo
            </h2>

            <div class="space-y-6">
              <div
                  v-for="(item, index) in listaRespuestas"
                  :key="index"
                  class="bg-[#1e2736] p-6 rounded-xl border-l-4 border-blue-500 shadow-md"
              >
                <div class="flex justify-between items-start mb-4">
                  <div>
                    <span class="text-blue-400 font-bold text-lg">{{ item.email }}</span>
                    <p class="text-gray-500 text-xs mt-1">{{ new Date(item.fecha).toLocaleString() }}</p>
                  </div>
                  <span class="bg-blue-900/50 text-blue-200 text-xs px-2 py-1 rounded">Respuesta #{{ listaRespuestas.length - index }}</span>
                </div>

                <div class="space-y-4 text-gray-300 text-sm">
                  <p><strong class="text-white">P1:</strong> {{ item.r1 }}</p>
                  <p><strong class="text-white">P2:</strong> {{ item.r2 }}</p>
                  <!-- Puedes agregar más si quieres mostrar todas -->
                  <details class="text-gray-400 cursor-pointer">
                    <summary class="hover:text-white">Ver resto de respuestas...</summary>
                    <div class="mt-2 pl-4 border-l border-gray-600 space-y-2 pt-2">
                      <p><strong class="text-white">P3:</strong> {{ item.r3 }}</p>
                      <p><strong class="text-white">P4:</strong> {{ item.r4 }}</p>
                      <p><strong class="text-white">P5:</strong> {{ item.r5 }}</p>
                      <p><strong class="text-white">P6:</strong> {{ item.r6 }}</p>
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
import { ref } from 'vue';
import Sidebar from "@/views/sidebar.vue";

// Variables para los inputs
const r1 = ref("");
const r2 = ref("");
const r3 = ref("");
const r4 = ref("");
const r5 = ref("");
const r6 = ref("");

// Variables de estado
const mensaje = ref("");
const tipoMensaje = ref("");
const enviando = ref(false);
const listaRespuestas = ref([]); // Aquí guardaremos lo que viene de la BD

async function enviarRespuestas() {
  // 1. validar que el usuario este logueado
  const usuarioEmail = localStorage.getItem('usuario');
  if (!usuarioEmail) {
    mensaje.value = "Error: Debes iniciar sesión primero.";
    tipoMensaje.value = "error";
    return;
  }

  // 2. validar que responda
  if (!r1.value || !r2.value || !r3.value || !r4.value || !r5.value || !r6.value) {
    mensaje.value = "Por favor responde al menos las primeras preguntas.";
    tipoMensaje.value = "error";
    return;
  }

  enviando.value = true;
  mensaje.value = "Guardando...";

  try {
    // 3. enviar a python
    const respuesta = await fetch("http://127.0.0.1:8000/guardar_foro1", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: usuarioEmail,
        r1: r1.value,
        r2: r2.value,
        r3: r3.value,
        r4: r4.value,
        r5: r5.value,
        r6: r6.value
      })
    });

    const datos = await respuesta.json();

    if (datos.exito) {
      mensaje.value = "¡Enviado con éxito!";
      tipoMensaje.value = "exito";

      // 4. limpiar campos
      r1.value = ""; r2.value = ""; r3.value = "";
      r4.value = ""; r5.value = ""; r6.value = "";

      // 5. cargar todas las respuestas
      await cargarForoCompleto();

    } else {
      mensaje.value = "Error al guardar: " + datos.mensaje;
      tipoMensaje.value = "error";
    }

  } catch (error) {
    console.error(error);
    mensaje.value = "Error de conexión con el servidor";
    tipoMensaje.value = "error";
  } finally {
    enviando.value = false;
  }
}

async function cargarForoCompleto() {
  try {
    const res = await fetch("http://127.0.0.1:8000/respuestas_foro1");
    const datos = await res.json();
    listaRespuestas.value = datos; // se guarda la lista para que el v-for la muestre
  } catch (error) {
    console.error("No se pudieron cargar las respuestas", error);
  }
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
  transition: all 0.2s;
}
.input-foro:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

/* Animación */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fadeInUp 0.5s ease-out forwards;
}
</style>