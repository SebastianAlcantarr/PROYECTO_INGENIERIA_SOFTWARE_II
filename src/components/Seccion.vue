<template>
  <section class="border-t border-linea">
    <h2 class="m-0">
      <button
        type="button"
        :id="idBoton"
        :aria-expanded="abierta"
        :aria-controls="idPanel"
        class="group flex w-full items-center justify-between gap-4 py-5 text-left md:py-6"
        @click="abierta = !abierta"
      >
        <span class="flex items-baseline gap-3">
          <span class="font-display text-2xl font-bold tracking-[-0.02em] text-tinta md:text-[1.75rem]">
            {{ titulo }}
          </span>
        </span>
        <span class="flex shrink-0 items-center gap-3 text-sm font-medium text-tenue">
          <span v-if="resumen" class="hidden sm:inline">{{ resumen }}</span>
          <span
            class="material-symbols-outlined grid h-9 w-9 place-items-center rounded-full border border-linea text-[22px] transition-[transform,background-color] duration-300 group-hover:bg-hundido"
            :class="abierta ? 'rotate-180' : ''"
            aria-hidden="true"
          >expand_more</span>
        </span>
      </button>
    </h2>
    <div
      :id="idPanel"
      role="region"
      :aria-labelledby="idBoton"
      class="grid transition-[grid-template-rows] duration-300 ease-[cubic-bezier(.16,1,.3,1)]"
      :style="{ gridTemplateRows: abierta ? '1fr' : '0fr' }"
      :inert="!abierta || undefined"
    >
      <div class="min-h-0 overflow-hidden">
        <div class="px-0.5 pb-10 pt-1">
          <slot />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, watch, useId } from "vue";

const props = defineProps({
  titulo: { type: String, required: true },
  resumen: { type: String, default: "" },
  abiertaInicial: { type: Boolean, default: true },
});

const abierta = ref(props.abiertaInicial);
watch(
  () => props.abiertaInicial,
  (v) => (abierta.value = v)
);

const id = useId();
const idBoton = `sec-${id}-boton`;
const idPanel = `sec-${id}-panel`;
</script>
