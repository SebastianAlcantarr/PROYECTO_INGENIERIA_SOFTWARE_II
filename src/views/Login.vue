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

            <div class="flex w-full justify-center">
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
                          class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-gray-800 dark:text-white focus:outline-0 focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-slate-700 bg-gray-50 dark:bg-slate-800/50 focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-slate-500 pl-12 pr-12 text-base font-normal leading-normal"
                          placeholder="Introducir una Contraseña"
                          type="password"
                          value=""
                      />
                      <button
                          aria-label="Toggle password visibility"
                          class="text-gray-400 dark:text-slate-400 absolute right-0 flex h-full items-center justify-center pr-4"
                      >
                          <span class="material-symbols-outlined text-xl"
                          >visibility</span
                          >
                      </button>
                    </div>
                  </label>
                  <a
                      class="text-primary text-sm font-medium leading-normal text-right -mt-3 hover:underline"
                      href="#"
                  >Olvidaste Contraseña?</a
                  >
                  <button
                      class="w-full h-12 px-6 rounded-lg bg-blue-400 hover:bg-blue-800 text-gray-900 font-semibold flex items-center justify-center duration-500 focus:ring-2 focus:ring-blue-400/50"
                  >
                    Iniciar Sesión
                  </button>
                </div>
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
              </div>


            </div>
          </div>
          <router-link to="/tema1" class="btn px-4 py-2 rounded bg-blue-600 text-white h-10">
            Ir a Tema 1
          </router-link>
        </div>
      </main>

    </div>
  </div>
  </body>
</template>

<script></script>

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