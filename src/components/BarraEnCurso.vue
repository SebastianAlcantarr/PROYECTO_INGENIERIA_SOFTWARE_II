<template>
  <div
    v-if="indice >= 0"
    class="fixed inset-x-0 bottom-0 z-30 border-t border-white/5 text-[var(--c-barra-tinta)]"
    style="background: var(--c-barra)"
  >
    <div class="mx-auto flex h-[72px] max-w-[1240px] items-center gap-3 px-4 sm:gap-5 sm:px-6 lg:px-10">
      <!-- Pista en curso -->
      <div class="min-w-0 flex-1 sm:flex-none sm:basis-[260px]">
        <p class="flex items-center gap-2 text-xs font-semibold text-[var(--c-barra-tenue)]">
          <span class="relative flex h-2 w-2" aria-hidden="true">
            <span class="absolute inset-0 animate-ping rounded-full bg-curso opacity-60"></span>
            <span class="relative h-2 w-2 rounded-full bg-curso"></span>
          </span>
          En curso
        </p>
        <p class="truncate font-semibold leading-snug">
          <span class="numeral font-display text-curso">{{ pista(indice) }}</span>
          · {{ paso.tipo }}: {{ paso.corto }}
        </p>
      </div>

      <!-- Avance por pistas -->
      <ol class="hidden flex-1 items-center gap-1.5 md:flex" aria-label="Avance en la secuencia">
        <li v-for="(p, i) in pasos" :key="p.ruta" class="flex-1">
          <RouterLink
            :to="p.ruta"
            class="group block py-3"
            :aria-label="`${pista(i)} ${p.tipo}: ${p.corto}`"
            :aria-current="i === indice ? 'step' : undefined"
          >
            <span
              class="block h-1.5 rounded-full transition-[background-color,transform] duration-500 group-hover:scale-y-[1.6]"
              :style="{
                background:
                  i === indice ? 'var(--c-curso)' : i < indice ? 'var(--c-barra-tinta)' : 'var(--c-barra-pista)',
                opacity: i < indice ? 0.55 : 1,
              }"
            ></span>
          </RouterLink>
        </li>
      </ol>
      <span class="numeral hidden text-sm text-[var(--c-barra-tenue)] lg:inline">{{ indice + 1 }} / {{ pasos.length }}</span>

      <!-- Anterior / siguiente -->
      <div class="flex shrink-0 items-center gap-2">
        <RouterLink
          v-if="anterior"
          :to="anterior.ruta"
          class="grid h-11 w-11 place-items-center rounded-full border border-white/15 transition-colors hover:bg-white/10"
          :aria-label="`Anterior: ${anterior.tipo}`"
        >
          <span class="material-symbols-outlined" aria-hidden="true">arrow_back</span>
        </RouterLink>
        <RouterLink v-if="siguiente" :to="siguiente.ruta" class="boton boton-curso">
          <span class="hidden sm:inline">Siguiente:</span> {{ siguiente.tipo }}
          <span class="material-symbols-outlined -mr-1 text-[20px]" aria-hidden="true">arrow_forward</span>
        </RouterLink>
        <RouterLink v-else to="/panel-alumno" class="boton boton-curso">
          Ver mi progreso
          <span class="material-symbols-outlined -mr-1 text-[20px]" aria-hidden="true">insights</span>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { pasos, indiceDe, pista } from "@/ruta.js";

const route = useRoute();
const indice = computed(() => indiceDe(route.path));
const paso = computed(() => pasos[indice.value]);
const anterior = computed(() => (indice.value > 0 ? pasos[indice.value - 1] : null));
const siguiente = computed(() => (indice.value < pasos.length - 1 ? pasos[indice.value + 1] : null));
</script>
