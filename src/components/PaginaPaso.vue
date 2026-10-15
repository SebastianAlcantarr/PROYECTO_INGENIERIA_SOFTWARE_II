<template>
  <div class="min-h-dvh bg-fondo text-tinta">
    <EncabezadoPortal />

    <div v-if="invitado" class="border-b border-linea bg-hundido">
      <p class="mx-auto max-w-[1240px] px-4 py-2.5 text-sm text-tenue sm:px-6 lg:px-10">
        <span class="material-symbols-outlined mr-1.5 align-[-4px] text-[18px] text-a1" aria-hidden="true">visibility</span>
        <span class="font-semibold text-tinta">Modo invitado.</span>
        Puedes ver todo el contenido; para responder las preguntas,
        <RouterLink to="/" class="font-semibold text-tinta underline underline-offset-4 hover:text-a1">inicia sesión</RouterLink>.
      </p>
    </div>

    <main class="mx-auto max-w-[1240px] px-4 pb-40 sm:px-6 lg:px-10">
      <!-- Cabecera de la pista -->
      <header
        class="grid items-end gap-8 pb-10 pt-10 md:pt-14 lg:gap-14"
        :class="$slots.figura ? 'lg:grid-cols-[minmax(0,1fr)_minmax(0,460px)]' : ''"
      >
        <div class="min-w-0">
          <p class="numeral font-display text-[clamp(4.5rem,13vw,9rem)] font-extrabold leading-[0.8] tracking-[-0.03em] entrada-pista" :style="{ color: colorTextoActividad }" aria-hidden="true">
            {{ numeroPista }}
          </p>
          <h1 class="mt-5 max-w-[18ch] text-[clamp(2.25rem,5.5vw,4.25rem)] font-extrabold leading-[1.04] tracking-[-0.01em]">
            {{ titulo || paso?.titulo }}
          </h1>
          <p class="mt-5 flex flex-wrap items-center gap-x-3 gap-y-2 text-base text-tenue">
            <span class="inline-flex items-center gap-2 font-semibold text-tinta">
              <span class="h-2.5 w-2.5 rounded-full" :style="{ background: colorActividad }" aria-hidden="true"></span>
              Actividad {{ paso?.actividad }}
            </span>
            <span aria-hidden="true">·</span>
            <span>{{ paso?.tipo }}</span>
            <template v-if="$slots.estado">
              <span aria-hidden="true">·</span>
              <slot name="estado" />
            </template>
          </p>
          <div v-if="$slots.intro" class="mt-6 max-w-[60ch] text-lg leading-relaxed text-tenue">
            <slot name="intro" />
          </div>
        </div>
        <div v-if="$slots.figura" class="min-w-0">
          <slot name="figura" />
        </div>
      </header>

      <slot />
    </main>

    <BarraEnCurso />
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { esInvitado } from "@/sesion.js";
import EncabezadoPortal from "@/components/EncabezadoPortal.vue";
import BarraEnCurso from "@/components/BarraEnCurso.vue";
import { pasos, indiceDe, pista, colorDeActividad, colorTextoDeActividad } from "@/ruta.js";

defineProps({
  titulo: { type: String, default: "" },
});

const route = useRoute();
const invitado = esInvitado();
const indice = computed(() => indiceDe(route.path));
const paso = computed(() => pasos[indice.value]);
const numeroPista = computed(() => (indice.value >= 0 ? pista(indice.value) : ""));
const colorActividad = computed(() => colorDeActividad(paso.value?.actividad));
const colorTextoActividad = computed(() => colorTextoDeActividad(paso.value?.actividad));
</script>

<style scoped>
.entrada-pista {
  animation: entrada 0.9s cubic-bezier(0.16, 1, 0.3, 1) both;
}
@keyframes entrada {
  from {
    clip-path: inset(0 0 100% 0);
    transform: translateY(0.25em);
  }
  to {
    clip-path: inset(0 0 0 0);
    transform: none;
  }
}
</style>
