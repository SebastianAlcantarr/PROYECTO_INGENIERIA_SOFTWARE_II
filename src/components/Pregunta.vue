<template>
  <div class="grid gap-x-5 gap-y-3 sm:grid-cols-[3rem_1fr]">
    <span
      class="font-display numeral text-3xl font-bold leading-none tracking-[-0.03em] text-tenue sm:pt-1"
      aria-hidden="true"
    >{{ String(numero).padStart(2, "0") }}</span>
    <div class="min-w-0 space-y-3">
      <div :id="idEnunciado" class="pregunta-enunciado max-w-[68ch] text-[1.0625rem] font-medium leading-relaxed text-tinta">
        <slot />
      </div>
      <textarea
        v-if="!sinCampo"
        :value="modelValue"
        :rows="rows"
        :placeholder="placeholder"
        :aria-labelledby="idEnunciado"
        :disabled="disabled"
        class="campo"
        @input="$emit('update:modelValue', $event.target.value)"
      ></textarea>
      <slot name="campo" />
    </div>
  </div>
</template>

<script setup>
import { useId } from "vue";

defineProps({
  numero: { type: [Number, String], required: true },
  modelValue: { type: String, default: "" },
  placeholder: { type: String, default: "Escribe tu respuesta…" },
  rows: { type: [Number, String], default: 4 },
  disabled: { type: Boolean, default: false },
  sinCampo: { type: Boolean, default: false },
});
defineEmits(["update:modelValue"]);

const idEnunciado = `preg-${useId()}`;
</script>
