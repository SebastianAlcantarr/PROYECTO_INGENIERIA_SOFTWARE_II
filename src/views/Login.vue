<template>
  <div class="grid min-h-dvh bg-fondo text-tinta lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)]">
    <!-- Panel institucional -->
    <aside class="relative hidden flex-col overflow-hidden p-12 lg:flex xl:p-16" style="background: var(--c-barra); color: var(--c-barra-tinta)">
      <div class="flex items-center gap-4">
        <LogoUniversidad :size="56" />
        <div class="leading-tight">
          <p class="text-lg font-semibold">Universidad de Sonora</p>
          <p class="text-sm" style="color: var(--c-barra-tenue)">Cálculo Diferencial I</p>
        </div>
      </div>

      <div class="my-auto py-16">
        <h1 class="text-[clamp(3.5rem,6.2vw,6.5rem)] font-extrabold leading-[0.92] tracking-[-0.02em]">
          Portal de<br />Derivadas
        </h1>
        <p class="mt-8 max-w-md text-lg leading-relaxed" style="color: var(--c-barra-tenue)">
          La derivada como razón de cambio, a partir de la relación entre la edad y la densidad mineral ósea.
        </p>
      </div>


    </aside>

    <!-- Formulario -->
    <main class="flex flex-col justify-center px-5 py-10 sm:px-10 lg:px-16">
      <div class="mx-auto w-full max-w-[440px]">
        <div class="mb-10 flex items-center gap-3 lg:hidden">
          <LogoUniversidad :size="44" />
          <div class="leading-tight">
            <p class="text-sm text-tenue">Universidad de Sonora</p>
            <p class="font-display text-xl font-extrabold tracking-[-0.02em]">Portal de Derivadas</p>
          </div>
        </div>

        <h2 class="text-4xl font-extrabold tracking-[-0.015em]">
          {{ esRegistro ? "Crear cuenta" : "Iniciar sesión" }}
        </h2>
        <p class="mt-2 text-tenue">
          {{ esRegistro ? "Registra tus datos para comenzar la secuencia." : "Ingresa con tu correo para continuar donde te quedaste." }}
        </p>

        <form class="mt-8 space-y-5" novalidate @submit.prevent="procesarFormulario">
          <div v-if="esRegistro" class="grid gap-5 sm:grid-cols-2">
            <div>
              <label for="nombre" class="mb-1.5 block text-sm font-semibold">Nombre</label>
              <div class="relative">
                <span class="material-symbols-outlined pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[20px] text-tenue" aria-hidden="true">person</span>
                <input id="nombre" v-model="nombre" type="text" required autocomplete="given-name" placeholder="Nombre" class="campo !pl-11" />
              </div>
            </div>
            <div>
              <label for="apellido" class="mb-1.5 block text-sm font-semibold">Apellidos</label>
              <div class="relative">
                <span class="material-symbols-outlined pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[20px] text-tenue" aria-hidden="true">badge</span>
                <input id="apellido" v-model="apellido" type="text" required autocomplete="family-name" placeholder="Apellidos" class="campo !pl-11" />
              </div>
            </div>
          </div>
            <div>
              <label for="email" class="mb-1.5 block text-sm font-semibold">Correo electrónico</label>
              <div class="relative">
                <span class="material-symbols-outlined pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[20px] text-tenue" aria-hidden="true">mail</span>
                <input id="email" v-model="email" type="email" required autocomplete="email" placeholder="correo@ejemplo.com" class="campo !pl-11" />
              </div>
            </div>
            <div>
              <label for="password" class="mb-1.5 block text-sm font-semibold">Contraseña</label>
              <div class="relative">
                <span class="material-symbols-outlined pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[20px] text-tenue" aria-hidden="true">lock</span>
                <input
                  id="password"
                  v-model="password"
                  :type="mostrarContrasena ? 'text' : 'password'"
                  required
                  :autocomplete="esRegistro ? 'new-password' : 'current-password'"
                  :placeholder="esRegistro ? 'Crea una contraseña' : 'Tu contraseña'"
                  class="campo !pl-11 !pr-12"
                />
                <button
                  type="button"
                  class="absolute inset-y-0 right-0 grid w-12 place-items-center rounded-r-[10px] text-tenue hover:text-tinta"
                  :aria-label="mostrarContrasena ? 'Ocultar contraseña' : 'Mostrar contraseña'"
                  @click="mostrarContrasena = !mostrarContrasena"
                >
                  <span class="material-symbols-outlined text-[20px]" aria-hidden="true">{{ mostrarContrasena ? "visibility" : "visibility_off" }}</span>
                </button>
              </div>
            </div>

            <p
              v-if="mensaje"
              role="status"
              class="aviso"
              :class="tipoMensaje === 'error' ? 'aviso-error' : tipoMensaje === 'exito' ? 'aviso-ok' : 'aviso-info'"
            >
              {{ mensaje }}
            </p>

            <button type="submit" class="boton boton-primario w-full !min-h-12 text-base" :disabled="procesando">
              <span v-if="procesando" class="material-symbols-outlined animate-spin text-[20px]" aria-hidden="true">progress_activity</span>
              {{ procesando ? "Procesando…" : esRegistro ? "Registrarse" : "Entrar" }}
            </button>
        </form>

        <div class="relative my-6 flex items-center gap-4 text-sm text-tenue" aria-hidden="true">
          <span class="h-px flex-1 bg-linea"></span>o<span class="h-px flex-1 bg-linea"></span>
        </div>

        <button type="button" class="boton boton-secundario w-full !min-h-12 text-base" @click="explorarSinSesion">
          <span class="material-symbols-outlined -ml-1 text-[20px]" aria-hidden="true">visibility</span>
          Ver el portal sin iniciar sesión
        </button>
        <p class="mt-2 text-center text-sm text-tenue">Podrás leer los foros y exámenes; para responder necesitas una cuenta.</p>

        <p class="mt-8 border-t border-linea pt-6 text-center text-tenue">
          {{ esRegistro ? "¿Ya tienes cuenta?" : "¿Aún no tienes cuenta?" }}
          <button type="button" class="ml-1 font-semibold text-tinta underline underline-offset-4 hover:text-a1" @click="cambiarModo">
            {{ esRegistro ? "Inicia sesión" : "Regístrate aquí" }}
          </button>
        </p>

        <p class="mt-10 text-center text-xs text-tenue lg:hidden">Universidad de Sonora </p>
      </div>
    </main>
  </div>
</template>

<script setup>
import { API_URL } from "@/api.js";
import { ref } from "vue";
import { useRouter } from "vue-router";
import LogoUniversidad from "@/components/LogoUniversidad.vue";
import { entrarComoInvitado } from "@/sesion.js";

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

function explorarSinSesion() {
  entrarComoInvitado();
  router.push("/bienvenida");
}

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

  const urlBase = `${API_URL}`;
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
