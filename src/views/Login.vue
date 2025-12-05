<template>
  <div class="min-h-screen flex bg-gray-50 dark:bg-[rgb(16,22,34)] font-display">
    <!-- Panel Izquierdo (Decorativo) - Sin cambios -->
    <div class="hidden lg:flex lg:w-1/2 relative overflow-hidden bg-[#244a76] dark:bg-slate-900 items-center justify-center">
      <div class="absolute inset-0 bg-gradient-to-br from-blue-600/20 to-purple-600/40 mix-blend-overlay"></div>
      <div class="absolute -top-24 -left-24 w-96 h-96 rounded-full bg-blue-500/10 blur-3xl"></div>
      <div class="absolute -bottom-24 -right-24 w-96 h-96 rounded-full bg-purple-500/10 blur-3xl"></div>

      <div class="relative z-10 p-12 text-center">
        <h1 class="text-4xl font-bold text-white mb-4 tracking-tight">Portal de Derivadas</h1>
        <p class="text-blue-100 text-lg max-w-md mx-auto">
          Ingresa o crea una cuenta para guardar tu progreso.
        </p>
      </div>
    </div>

    <!-- Panel Derecho (Formulario Funcional) -->
    <div
      class="w-full lg:w-1/2 flex flex-col items-center justify-center p-6 sm:p-12 relative"
    >
      <div class="w-full max-w-md space-y-8">
        <div class="text-center lg:text-left">
          <h2
            class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white"
          >
            {{ esRegistro ? "Crear Cuenta" : "Iniciar Sesión" }}
          </h2>
          <p class="mt-2 text-sm text-gray-600 dark:text-slate-400">
            {{
              esRegistro
                ? "Registra tus datos para comenzar"
                : "Ingresa tus credenciales"
            }}
          </p>
        </div>

        <div class="mt-8 space-y-6">
          <div class="space-y-5">
            <div v-if="esRegistro">
              <label
                class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1"
                >Nombre </label
              >
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
                >
                  <span class="material-symbols-outlined text-gray-400 text-xl"
                    >person</span
                  >
                </div>
                <!-- v-model conectado a variable 'email' -->
                <input
                  v-model="nombre"
                  type="text"
                  required
                  class="block w-full pl-10 pr-3 py-3 border border-gray-300 dark:border-slate-600 rounded-xl bg-white dark:bg-slate-800/50 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500"
                  placeholder="Nombre"
                  @keyup.enter="procesarFormulario"
                />
              </div>

            </div>

            <div v-if="esRegistro">
              <label
                class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1"
                >Apellidos</label
              >
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
                >
                  <span class="material-symbols-outlined text-gray-400 text-xl"
                    >person</span
                  >
                </div>
                <!-- v-model conectado a variable 'email' -->
                <input
                  v-model="apellido"
                  type="text"
                  required
                  class="block w-full pl-10 pr-3 py-3 border border-gray-300 dark:border-slate-600 rounded-xl bg-white dark:bg-slate-800/50 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500"
                  placeholder="Apellidos"
                  @keyup.enter="procesarFormulario"
                />
              </div>

            </div>

            <!-- Email Input -->
            <div>
              <label
                class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1"
                >Correo Electrónico</label
              >
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
                >
                  <span class="material-symbols-outlined text-gray-400 text-xl"
                    >person</span
                  >
                </div>
                <!-- v-model conectado a variable 'email' -->
                <input
                  v-model="email"
                  type="email"
                  required
                  class="block w-full pl-10 pr-3 py-3 border border-gray-300 dark:border-slate-600 rounded-xl bg-white dark:bg-slate-800/50 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500"
                  placeholder="Correo electrónico"
                  @keyup.enter="procesarFormulario"
                />
              </div>
            </div>

            <!-- Password Input -->
            <div>
              <label
                class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1"
                >Contraseña</label
              >
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
                >
                  <span class="material-symbols-outlined text-gray-400 text-xl"
                    >lock</span
                  >
                </div>
                <!-- v-model conectado a variable 'password' -->
                <input
                  v-model="password"
                  :type="mostrarContrasena ? 'text' : 'password'"
                  required
                  class="block w-full pl-10 pr-10 py-3 border border-gray-300 dark:border-slate-600 rounded-xl bg-white dark:bg-slate-800/50 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500"
                  :placeholder="esRegistro ? 'Crea una contraseña' : 'Contraseña'"
                  @keyup.enter="procesarFormulario"
                />

                <button
                  @click="mostrarContrasena = !mostrarContrasena"
                  type="button"
                  class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600"
                >
                  <span class="material-symbols-outlined text-xl">
                    {{ mostrarContrasena ? "visibility" : "visibility_off" }}
                  </span>
                </button>
              </div>
            </div>
          </div>

          <!-- Botones -->
          <div class="space-y-4">
            <button
              @click="procesarFormulario"
              class="w-full flex justify-center py-3.5 px-4 rounded-xl shadow-sm text-sm font-semibold text-white bg-blue-600 hover:bg-blue-700 transition-all duration-200"
              :disabled="procesando"
              :class="{'opacity-70 cursor-not-allowed': procesando}"
            >
              <span v-if="!procesando">
                {{ esRegistro ? "Registrarse" : "Entrar" }}
              </span>
              <span v-else class="flex items-center">
                <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Procesando...
              </span>
            </button>

            <!-- Mensajes de Error/Éxito -->
            <div
              v-if="mensaje"
              :class="`p-3 rounded-lg text-sm text-center font-medium ${
                tipoMensaje === 'error'
                  ? 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'
                  : 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400'
              }`"
            >
              {{ mensaje }}
            </div>

            <div class="relative py-2">
              <div class="absolute inset-0 flex items-center">
                <div
                  class="w-full border-t border-gray-300 dark:border-slate-700"
                ></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span
                  class="px-2 bg-gray-50 dark:bg-[rgb(16,22,34)] text-gray-500"
                  >O</span
                >
              </div>
            </div>

            <p class="text-center text-sm text-gray-600 dark:text-slate-400">
              {{ esRegistro ? "¿Ya tienes cuenta?" : "¿No tienes cuenta?" }}
              <button
                @click="cambiarModo"
                class="font-semibold text-blue-600 hover:text-blue-500 ml-1"
              >
                {{ esRegistro ? "Inicia Sesión" : "Regístrate aquí" }}
              </button>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// Variables del formulario
const email = ref("");
const password = ref("");
const nombre = ref("");
const apellido = ref("");
const mostrarContrasena = ref(false);

// Estado de la App
const esRegistro = ref(false); // false = Login, true = Registro
const mensaje = ref("");
const tipoMensaje = ref(""); // 'error' o 'exito'

function cambiarModo() {
  esRegistro.value = !esRegistro.value;
  mensaje.value = ""; // Limpiar mensajes al cambiar
}

function validarCampos() {
  if (esRegistro.value) {
    if (!nombre.value?.trim()) {
      mensaje.value = "Por favor ingresa tu nombre";
      tipoMensaje.value = "error";
      return false;
    }
    if (!apellido.value?.trim()) {
      mensaje.value = "Por favor ingresa tus apellidos";
      tipoMensaje.value = "error";
      return false;
    }
  }

  if (!email.value?.trim()) {
    mensaje.value = "Por favor ingresa tu correo electrónico";
    tipoMensaje.value = "error";
    return false;
  }

  if (!password.value) {
    mensaje.value = "Por favor ingresa tu contraseña";
    tipoMensaje.value = "error";
    return false;
  }

  return true;
}

async function procesarFormulario() {
  // Validar campos antes de continuar
  if (!validarCampos()) {
    return;
  }

  mensaje.value = "Procesando...";
  tipoMensaje.value = "info";

  // URL de tu backend en Python (El puerto 8000 que ya tienes corriendo)
  const urlBase = "https://proyecto-ingenieria-software-6ccv.onrender.com";
  const endpoint = esRegistro.value ? "/registrar" : "/login";

  try {
    const respuesta = await fetch(`${urlBase}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
        nombre: nombre.value,
        apellidos:apellido.value
      }),
    });

    const datos = await respuesta.json();

    if (datos.exito) {
      tipoMensaje.value = "exito";
      mensaje.value = datos.mensaje;

      const CORREO_PROFE = "admin@gmail.com";

      if (email.value.toLowerCase() === CORREO_PROFE.toLowerCase()) {
        localStorage.setItem("usuario", datos.usuario);
        mensaje.value = "Bienvenido, Profesor.";
        setTimeout(() => {
          router.push("/panel-profesor");
        }, 1000);
        return;
      }

      if (!esRegistro.value) {
        // --- CASO LOGIN EXITOSO ---
        // Guardamos usuario en memoria del navegador
        localStorage.setItem("usuario", datos.usuario);
        localStorage.setItem("email", email.value);

        // Redirigimos al Foro 1 después de 1 segundo
        setTimeout(() => {
          router.push("/bienvenida");
        }, 1000);

        const yaVioBienvenida = localStorage.getItem(`visto_bienvenida_${datos.usuario}`);

        setTimeout(() => {
          if (yaVioBienvenida === 'true') {
            // Si ya la vio, directo al foro
            router.push("/foro1");
          } else {
            // Si es la primera vez, a la bienvenida
            router.push("/bienvenida");
          }
        }, 1000);

      } else {
        // --- CASO REGISTRO EXITOSO ---
        // Cambiamos a pantalla de login para que ingrese
        setTimeout(() => {
          esRegistro.value = false;
          mensaje.value = "Cuenta creada , Ahora inicia sesión.";
          password.value = "";
        }, 1500);
      }
    } else {
      // Python nos devolvió un error (ej: contraseña mal, usuario ya existe)
      tipoMensaje.value = "error";
      mensaje.value = datos.mensaje;
    }
  } catch (error) {
    console.error(error);
    tipoMensaje.value = "error";
    mensaje.value =
      "Error conectando con el servidor. ¿Está encendido el Python?";
  }
}

</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
  animation: fadeIn 0.3s ease-out forwards;
}
</style>