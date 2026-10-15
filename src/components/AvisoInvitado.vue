<template>
  <div class="flex flex-col gap-4 rounded-2xl border border-linea bg-hundido p-5 sm:flex-row sm:items-center sm:justify-between sm:p-6">
    <div class="flex items-start gap-3">
      <span class="material-symbols-outlined mt-0.5 text-a1" aria-hidden="true">lock</span>
      <div>
        <p class="font-semibold">{{ titulo }}</p>
        <p class="text-[0.9375rem] text-tenue">Puedes leer todo el contenido como invitado. Para guardar tus respuestas y ver las de tus compañeros, inicia sesión.</p>
      </div>
    </div>
    <RouterLink to="/" class="boton boton-primario shrink-0">
      Iniciar sesión
      <span class="material-symbols-outlined -mr-1 text-[20px]" aria-hidden="true">login</span>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";

defineProps({
  titulo: { type: String, default: "Para responder las preguntas, inicia sesión" },
});
</script>
