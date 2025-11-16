<template>
  <body
      class="bg-[#244a76] dark:bg-[rgb(16,22,34)] font-display text-[#E0E0E0] min-h-[100dvh]"
  >
  <div
      class="relative flex min-h-[100dvh] w-full flex-col dark overflow-x-hidden group/design-root"
  >
    <div class="layout-container flex h-full grow flex-col">
      <main class="flex flex-1 items-center justify-center">
        <div class="flex flex-1 w-full max-w-[1440px]">
          <div class="grid flex-1 grid-cols-1">
            <div class="hidden"></div>

            <div class="flex    w-full justify-center">
              <div
                  class="w-full max-w-md rounded-4xl border-8 border-blue-500 p-8 sm:p-10"
              >
                <div class="flex flex-col gap-3 mb-8">
                  <div class="flex items-center gap-3 mb-2">
                    <div
                        class="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10"
                    >
                        <span
                            class="material-symbols-outlined text-primary text-2xl"
                        >Login</span
                        >
                    </div>
                    <p
                        class="text-2xl font-bold text-gray-800 dark:text-white"
                    >
                      Iniciar Sesion
                    </p>
                  </div>
                  <p
                      class="text-gray-600 dark:text-slate-400 text-base font-normal leading-normal"
                  >
                    Ingresa tu Usuario y Contraseña
                  </p>
                </div>
                <div class="flex flex-col gap-6">
                  <label class="flex flex-col w-full flex-1">
                    <p
                        class="text-gray-700 dark:text-white text-sm font-medium leading-normal pb-2"
                    >
                      Email / Ususario
                    </p>
                    <div class="relative flex w-full flex-1 items-stretch">
                      <div
                          aria-hidden="true"
                          class="text-gray-400 dark:text-slate-400 absolute left-0 flex h-full items-center justify-center pl-4"
                      >
                          <span class="material-symbols-outlined text-xl"
                          >person</span
                          >
                      </div>
                      <input
                          v-model="usuario"
                          class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-gray-800 dark:text-white focus:outline-0 focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-slate-700 bg-gray-50 dark:bg-slate-800/50 focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-slate-500 pl-12 pr-4 text-base font-normal leading-normal"
                          placeholder="Introducir Usuario"
                          value=""
                      />
                    </div>
                  </label>
                  <label class="flex flex-col w-full flex-1">
                    <p
                        class="text-gray-700 dark:text-white text-sm font-medium leading-normal pb-2"
                    >
                      Contraseña
                    </p>
                    <div class="relative flex w-full flex-1 items-stretch">
                      <div
                          aria-hidden="true"
                          class="text-gray-400 dark:text-slate-400 absolute left-0 flex h-full items-center justify-center pl-4"
                      >
                          <span class="material-symbols-outlined text-xl"
                          >lock</span
                          >
                      </div>
                      <input
                          :type="mostrarContrasena ? 'text' : 'password'"
                          class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-gray-800 dark:text-white focus:outline-0 focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-slate-700 bg-gray-50 dark:bg-slate-800/50 focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-slate-500 pl-12 pr-12 text-base font-normal leading-normal"
                          placeholder="Introducir una Contraseña"
                          type="password"
                          value=""
                      />

                      <button
                          @click="mostrar"
                          aria-label="Toggle password visibility"
                          class="cursor-pointer text-gray-400 dark:text-slate-400 absolute right-0 flex h-full items-center justify-center pr-4"
                      >
                          <span class="material-symbols-outlined text-xl">
                            {{
                              mostrarContrasena
                                  ? "visibility_off"
                                  : "visibility"
                            }}
                          </span>
                      </button>
                    </div>
                  </label>
                  <a
                      class="text-primary text-sm font-medium leading-normal text-right -mt-3 hover:underline"
                      href="#"
                  >Olvidaste Contraseña?</a
                  >
                  <button
                      @click="login"
                      class="w-full h-12 px-6 rounded-lg bg-blue-400 hover:bg-blue-800 text-gray-900 font-semibold flex items-center justify-center duration-500 focus:ring-2 focus:ring-blue-400/50"
                  >
                    Iniciar Sesión
                  </button>
                </div>
                <button class="mt-10 bg-white flex items-center text-gray-700 dark:text-gray-300 justify-center gap-x-3 text-sm sm:text-base  dark:bg-gray-900 dark:border-gray-700 dark:hover:bg-gray-800 rounded-lg hover:bg-gray-100 duration-300 transition-colors border px-20 py-2">
                  <svg class="w-5 h-5 sm:h-6 sm:w-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_3033_94454)">
                      <path d="M23.766 12.2764C23.766 11.4607 23.6999 10.6406 23.5588 9.83807H12.24V14.4591H18.7217C18.4528 15.9494 17.5885 17.2678 16.323 18.1056V21.1039H20.19C22.4608 19.0139 23.766 15.9274 23.766 12.2764Z" fill="#4285F4"/>
                      <path d="M12.2401 24.0008C15.4766 24.0008 18.2059 22.9382 20.1945 21.1039L16.3276 18.1055C15.2517 18.8375 13.8627 19.252 12.2445 19.252C9.11388 19.252 6.45946 17.1399 5.50705 14.3003H1.5166V17.3912C3.55371 21.4434 7.7029 24.0008 12.2401 24.0008Z" fill="#34A853"/>
                      <path d="M5.50253 14.3003C4.99987 12.8099 4.99987 11.1961 5.50253 9.70575V6.61481H1.51649C-0.18551 10.0056 -0.18551 14.0004 1.51649 17.3912L5.50253 14.3003Z" fill="#FBBC04"/>
                      <path d="M12.2401 4.74966C13.9509 4.7232 15.6044 5.36697 16.8434 6.54867L20.2695 3.12262C18.1001 1.0855 15.2208 -0.034466 12.2401 0.000808666C7.7029 0.000808666 3.55371 2.55822 1.5166 6.61481L5.50264 9.70575C6.45064 6.86173 9.10947 4.74966 12.2401 4.74966Z" fill="#EA4335"/>
                    </g>
                    <defs>
                      <clipPath id="clip0_3033_94454">
                        <rect width="24" height="24" fill="white"/>
                      </clipPath>
                    </defs>
                  </svg>

                  <span>Iniciar Sesion con Google</span>
                </button>

                <p
                    class="text-center text-sm text-gray-500 dark:text-slate-400 mt-8"
                >
                  No tienes una cuenta?
                  <a
                      class="font-semibold text-primary hover:underline"
                      href="#"
                  >Registrate
                  </a>
                </p>
                <div v-if="mensaje" class="alerta">{{ mensaje }}</div>
              </div>
            </div>
          </div>
        </div>

        <div>
          <router-link
              to="/tema1"
              class="btn px-4 py-2 rounded bg-blue-600 text-white h-10"
          >
            Ir a Tema 1
          </router-link>
        </div>

        <div></div>
        <router-link to="/tema2"
                     class="btn px-4 py-2 rounded bg-blue-600 text-white h-10 m-10 "
                     >
          ir al tema 2
        </router-link>
      </main>
    </div>
  </div>
  </body>
</template>

<script setup>
import { ref } from "vue";

const mostrarContrasena = ref(false);

function mostrar() {
  mostrarContrasena.value = !mostrarContrasena.value;
}
</script>

<style>
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
