<template>
  <div class="min-h-screen flex bg-gray-50 dark:bg-[rgb(16,22,34)] font-display">
    <!-- Left Panel (Decorative) -->
    <div class="hidden lg:flex lg:w-1/2 relative overflow-hidden bg-[#244a76] dark:bg-slate-900 items-center justify-center">
      <div class="absolute inset-0 bg-gradient-to-br from-blue-600/20 to-purple-600/40 mix-blend-overlay"></div>
      <!-- Abstract decorative circles -->
      <div class="absolute -top-24 -left-24 w-96 h-96 rounded-full bg-blue-500/10 blur-3xl"></div>
      <div class="absolute -bottom-24 -right-24 w-96 h-96 rounded-full bg-purple-500/10 blur-3xl"></div>
      
      <div class="relative z-10 p-12 text-center">

        <h1 class="text-4xl font-bold text-white mb-4 tracking-tight">Bienvenido al Portal para aprender a Derivar</h1>
        <p class="text-blue-100 text-lg max-w-md mx-auto leading-relaxed">
          Ingresa o crea una cuenta para acceder al contenido de Derivadas
        </p>
      </div>
    </div>

    <!-- Right Panel (Form) -->
    <div class="w-full lg:w-1/2 flex flex-col items-center justify-center p-6 sm:p-12 relative">
      <div class="w-full max-w-md space-y-8">
        <!-- Header -->
        <div class="text-center lg:text-left">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">
            Iniciar Sesión
          </h2>
          <p class="mt-2 text-sm text-gray-600 dark:text-slate-400">
            Ingresa tus credenciales para acceder
          </p>
        </div>

        <!-- Form -->
        <div class="mt-8 space-y-6">
          <div class="space-y-5">
            <!-- Email Input -->
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1">
                Usuario / Email
              </label>
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <span class="material-symbols-outlined text-gray-400 text-xl">person</span>
                </div>
                <input
                  id="email"
                  v-model="usuario"
                  name="email"
                  type="text"
                  required
                  class="block w-full pl-10 pr-3 py-3 border border-gray-300 dark:border-slate-600 rounded-xl leading-5 bg-white dark:bg-slate-800/50 text-gray-900 dark:text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 sm:text-sm transition-all duration-200 shadow-sm"
                  placeholder="nombre@ejemplo.com"
                />
              </div>
            </div>

            <!-- Password Input -->
            <div>
              <label for="password" class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1">
                Contraseña
              </label>
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <span class="material-symbols-outlined text-gray-400 text-xl">lock</span>
                </div>
                <input
                  id="password"
                  v-model="usuario" 
                  :type="mostrarContrasena ? 'text' : 'password'"
                  name="password"
                  required
                  class="block w-full pl-10 pr-10 py-3 border border-gray-300 dark:border-slate-600 rounded-xl leading-5 bg-white dark:bg-slate-800/50 text-gray-900 dark:text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 sm:text-sm transition-all duration-200 shadow-sm"
                  placeholder="••••••••"
                />
                <button
                  @click="mostrar"
                  type="button"
                  class="absolute inset-y-0 right-0 pr-3 flex items-center cursor-pointer text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors"
                >
                  <span class="material-symbols-outlined text-xl">
                    {{ mostrarContrasena ? "visibility" : "visibility_off" }}
                  </span>
                </button>
              </div>
              <div class="flex items-center justify-end mt-2">
                <a href="#" class="text-sm font-medium text-blue-600 hover:text-blue-500 dark:text-blue-400 hover:underline">
                  ¿Olvidaste tu contraseña?
                </a>
              </div>
            </div>
          </div>

          <!-- Actions -->
          <div class="space-y-4">
            <button
              @click="login"
              class="w-full flex justify-center py-3.5 px-4 border border-transparent rounded-xl shadow-sm text-sm font-semibold text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-200 transform hover:-translate-y-0.5"
            >
              Iniciar Sesión
            </button>

            <div class="relative">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-gray-300 dark:border-slate-700"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="px-2 bg-gray-50 dark:bg-[rgb(16,22,34)] text-gray-500">O inicar sesion con google</span>
              </div>
            </div>

            <button
              id="googleBtn"
              class="w-full flex items-center justify-center gap-3 px-4 py-3 border border-gray-300 dark:border-slate-600 rounded-xl shadow-sm bg-white dark:bg-slate-800 text-sm font-medium text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 transition-all duration-200"
            >
              <svg class="h-5 w-5" viewBox="0 0 24 24" width="24" height="24" xmlns="http://www.w3.org/2000/svg">
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
              <span>Google</span>
            </button>
          </div>

          <p class="text-center text-sm text-gray-600 dark:text-slate-400">
            ¿No tienes una cuenta?
            <a href="#" class="font-semibold text-blue-600 hover:text-blue-500 dark:text-blue-400 hover:underline">
              Regístrate
            </a>
          </p>
          
          <div v-if="mensaje" class="p-4 rounded-lg bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 text-sm text-center">
            {{ mensaje }}
          </div>
        </div>
      </div>
      
      <!-- Dev Navigation (Subtle) -->
      <div class="absolute bottom-4 right-4 flex gap-2 opacity-50 hover:opacity-100 transition-opacity">
        <router-link to="/foro1" class="text-xs bg-gray-200 dark:bg-slate-800 px-2 py-1 rounded hover:bg-gray-300 dark:hover:bg-slate-700 text-gray-600 dark:text-gray-400">Foro 1</router-link>
        <router-link to="/foro2" class="text-xs bg-gray-200 dark:bg-slate-800 px-2 py-1 rounded hover:bg-gray-300 dark:hover:bg-slate-700 text-gray-600 dark:text-gray-400">Foro 2</router-link>
        <router-link to="/foro6" class="text-xs bg-gray-200 dark:bg-slate-800 px-2 py-1 rounded hover:bg-gray-300 dark:hover:bg-slate-700 text-gray-600 dark:text-gray-400">Tema 3</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const mostrarContrasena = ref(false);
const usuario = ref("");
const mensaje = ref("");

function mostrar() {
  mostrarContrasena.value = !mostrarContrasena.value;
}

function login() {
  // Placeholder for login logic
  console.log("Login attempt", usuario.value);
}
</script>

<style>
/* Ensure full height for the page */
html, body {
  height: 100%;
  margin: 0;
}
</style>