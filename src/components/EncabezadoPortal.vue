<template>
  <header class="sticky top-0 z-40 border-b border-linea bg-fondo">
    <div class="mx-auto flex h-16 max-w-[1240px] items-center gap-4 px-4 sm:px-6 lg:px-10">
      <!-- Marca -->
      <RouterLink
        :to="modo === 'profesor' ? '/panel-profesor' : '/panel-alumno'"
        class="flex min-w-0 items-center gap-3 rounded-md text-tinta"
        aria-label="Universidad de Sonora · Portal de Derivadas, ir a mi panel"
      >
        <LogoUniversidad :size="40" />
        <span class="leading-tight">
          <span class="block text-[0.8125rem] font-medium text-tenue">Universidad de Sonora</span>
          <span class="block font-display text-lg font-extrabold tracking-[-0.02em]">Derivadas</span>
        </span>
      </RouterLink>

      <!-- Ruta por actividades (escritorio) -->
      <nav v-if="modo === 'alumno'" aria-label="Ruta del curso" class="ml-auto hidden items-center gap-1.5 md:flex" ref="navRef">
        <div v-for="act in actividades" :key="act.numero" class="relative">
          <button
            type="button"
            class="flex items-center gap-1.5 rounded-full px-4 py-2 text-sm font-semibold transition-colors"
            :class="
              actividadActual === act.numero
                ? 'bg-tinta text-fondo'
                : 'bg-hundido text-tinta hover:bg-linea'
            "
            :aria-expanded="menuAbierto === act.numero"
            :aria-controls="`menu-act-${act.numero}`"
            @click="alternarMenu(act.numero)"
          >
            <span class="h-2 w-2 rounded-full" :style="{ background: act.color }" aria-hidden="true"></span>
            {{ act.nombre }}
            <span class="material-symbols-outlined -mr-1 text-[18px] transition-transform" :class="menuAbierto === act.numero ? 'rotate-180' : ''" aria-hidden="true">expand_more</span>
          </button>

          <Transition name="menu">
            <ul
              v-if="menuAbierto === act.numero"
              :id="`menu-act-${act.numero}`"
              class="absolute right-0 top-[calc(100%+8px)] w-72 rounded-2xl border border-linea bg-superficie p-2 shadow-[var(--sombra-elevada)]"
            >
              <li v-for="paso in pasosDe(act.numero)" :key="paso.ruta">
                <RouterLink
                  :to="paso.ruta"
                  class="flex items-center gap-3 rounded-xl px-3 py-2.5 text-[0.9375rem] transition-colors hover:bg-hundido"
                  :class="paso.ruta === route.path ? 'font-semibold text-tinta' : 'text-tenue hover:text-tinta'"
                  :aria-current="paso.ruta === route.path ? 'step' : undefined"
                  @click="menuAbierto = null"
                >
                  <span class="numeral w-6 font-display font-bold" :class="paso.ruta === route.path ? 'text-curso-texto' : ''">{{ pista(indiceDe(paso.ruta)) }}</span>
                  <span class="flex-1">{{ paso.tipo }} · {{ paso.corto }}</span>
                  <span v-if="paso.ruta === route.path" class="h-2 w-2 rounded-full bg-curso" aria-hidden="true"></span>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </div>
      </nav>

      <div class="flex items-center gap-2" :class="modo === 'alumno' ? 'ml-auto md:ml-4' : 'ml-auto'">
        <!-- Ruta (móvil) -->
        <button
          v-if="modo === 'alumno'"
          type="button"
          class="boton boton-secundario !min-h-10 !px-4 md:hidden"
          :aria-expanded="hojaAbierta"
          aria-controls="hoja-ruta"
          @click="hojaAbierta = !hojaAbierta"
        >
          <span class="material-symbols-outlined text-[20px]" aria-hidden="true">route</span>
          Ruta
        </button>

        <!-- Usuario -->
        <div class="relative" ref="usuarioRef">
          <button
            type="button"
            class="avatar !h-10 !w-10 transition-shadow hover:shadow-[0_0_0_3px_var(--c-linea)]"
            :aria-expanded="menuUsuario"
            aria-controls="menu-usuario"
            :aria-label="`Cuenta de ${nombreCompleto || 'usuario'}`"
            @click="menuUsuario = !menuUsuario"
          >{{ iniciales }}</button>
          <Transition name="menu">
            <div
              v-if="menuUsuario"
              id="menu-usuario"
              class="absolute right-0 top-[calc(100%+8px)] w-64 rounded-2xl border border-linea bg-superficie p-2 shadow-[var(--sombra-elevada)]"
            >
              <div class="px-3 pb-3 pt-2">
                <p class="font-semibold leading-snug text-tinta">{{ nombreCompleto || "Cargando…" }}</p>
                <p class="truncate text-sm text-tenue">{{ correo }}</p>
              </div>
              <RouterLink
                v-if="modo === 'alumno'"
                to="/panel-alumno"
                class="flex items-center gap-3 rounded-xl px-3 py-2.5 text-[0.9375rem] text-tinta hover:bg-hundido"
                @click="menuUsuario = false"
              >
                <span class="material-symbols-outlined text-[20px] text-tenue" aria-hidden="true">insights</span>
                Mi progreso
              </RouterLink>
              <button
                type="button"
                class="flex w-full items-center gap-3 rounded-xl px-3 py-2.5 text-left text-[0.9375rem] text-tinta hover:bg-hundido"
                @click="cerrarSesion"
              >
                <span class="material-symbols-outlined text-[20px] text-tenue" aria-hidden="true">logout</span>
                Cerrar sesión
              </button>
            </div>
          </Transition>
        </div>
      </div>
    </div>

    <!-- Hoja de ruta (móvil) -->
    <Transition name="hoja">
      <div v-if="hojaAbierta && modo === 'alumno'" id="hoja-ruta" class="border-t border-linea bg-fondo md:hidden">
        <nav aria-label="Ruta del curso" class="max-h-[70dvh] overflow-y-auto px-4 pb-6 pt-2">
          <div v-for="act in actividades" :key="act.numero" class="pt-4">
            <p class="mb-1 flex items-center gap-2 px-2 text-sm font-semibold text-tenue">
              <span class="h-2 w-2 rounded-full" :style="{ background: act.color }" aria-hidden="true"></span>
              {{ act.nombre }}
            </p>
            <RouterLink
              v-for="paso in pasosDe(act.numero)"
              :key="paso.ruta"
              :to="paso.ruta"
              class="flex items-center gap-3 rounded-xl px-2 py-3 text-base"
              :class="paso.ruta === route.path ? 'bg-hundido font-semibold text-tinta' : 'text-tinta'"
              :aria-current="paso.ruta === route.path ? 'step' : undefined"
              @click="hojaAbierta = false"
            >
              <span class="numeral w-7 font-display font-bold" :class="paso.ruta === route.path ? 'text-curso-texto' : 'text-tenue'">{{ pista(indiceDe(paso.ruta)) }}</span>
              <span class="flex-1">{{ paso.tipo }} · {{ paso.corto }}</span>
              <span v-if="paso.ruta === route.path" class="text-sm font-semibold text-curso-texto">En curso</span>
            </RouterLink>
          </div>
        </nav>
      </div>
    </Transition>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch } from "vue";
import { useRoute, useRouter, RouterLink } from "vue-router";
import LogoUniversidad from "@/components/LogoUniversidad.vue";
import { actividades, pasos, indiceDe, pista } from "@/ruta.js";

const props = defineProps({
  modo: { type: String, default: "alumno" }, // 'alumno' | 'profesor'
});

const route = useRoute();
const router = useRouter();

const menuAbierto = ref(null);
const menuUsuario = ref(false);
const hojaAbierta = ref(false);
const navRef = ref(null);
const usuarioRef = ref(null);

const actividadActual = computed(() => pasos.find((p) => p.ruta === route.path)?.actividad ?? null);
const pasosDe = (n) => pasos.filter((p) => p.actividad === n);

function alternarMenu(n) {
  menuAbierto.value = menuAbierto.value === n ? null : n;
}

// Usuario (mismo endpoint que usaba la barra lateral)
const usuario = ref(null);
const correo = ref(localStorage.getItem("email") || localStorage.getItem("usuario") || "");
const nombreCompleto = computed(() =>
  usuario.value ? `${usuario.value.nombre ?? ""} ${usuario.value.apellidos ?? ""}`.trim() : props.modo === "profesor" ? "Profesor" : ""
);
const iniciales = computed(() => {
  const n = usuario.value?.nombre?.[0] ?? "";
  const a = usuario.value?.apellidos?.[0] ?? "";
  return (n + a).toUpperCase() || (props.modo === "profesor" ? "P" : correo.value?.[0]?.toUpperCase() || "·");
});

async function cargarUsuario() {
  const email = localStorage.getItem("email");
  if (!email || props.modo === "profesor") return;
  try {
    const res = await fetch(`https://proyecto-ingenieria-software-6ccv.onrender.com/conseguir_usuario/${email}`);
    usuario.value = await res.json();
  } catch (error) {
    console.error("Error cargando usuario:", error);
  }
}

function cerrarSesion() {
  localStorage.removeItem("usuario");
  localStorage.removeItem("email");
  localStorage.removeItem("nombre");
  router.push("/");
}

// Cerrar menús al hacer clic fuera o con Escape
function alClicFuera(e) {
  if (navRef.value && !navRef.value.contains(e.target)) menuAbierto.value = null;
  if (usuarioRef.value && !usuarioRef.value.contains(e.target)) menuUsuario.value = false;
}
function alTecla(e) {
  if (e.key === "Escape") {
    menuAbierto.value = null;
    menuUsuario.value = false;
    hojaAbierta.value = false;
  }
}

watch(
  () => route.path,
  () => {
    menuAbierto.value = null;
    menuUsuario.value = false;
    hojaAbierta.value = false;
  }
);

onMounted(() => {
  cargarUsuario();
  document.addEventListener("click", alClicFuera);
  document.addEventListener("keydown", alTecla);
});
onBeforeUnmount(() => {
  document.removeEventListener("click", alClicFuera);
  document.removeEventListener("keydown", alTecla);
});
</script>

<style scoped>
.menu-enter-active,
.menu-leave-active {
  transition: opacity 0.18s ease, transform 0.24s cubic-bezier(0.16, 1, 0.3, 1);
}
.menu-enter-from,
.menu-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
.hoja-enter-active,
.hoja-leave-active {
  transition: opacity 0.2s ease;
}
.hoja-enter-from,
.hoja-leave-to {
  opacity: 0;
}
</style>
