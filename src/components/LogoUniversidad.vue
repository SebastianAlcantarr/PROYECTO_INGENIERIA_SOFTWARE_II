<template>
  <img
    :src="logo"
    :width="size"
    :height="size"
    alt="Escudo de la Universidad de Sonora"
    class="shrink-0 select-none"
    draggable="false"
  />
</template>

<script setup>
import logo from "@/imagenes/logo-unison.webp";

defineProps({
  size: { type: Number, default: 40 },
});
</script>
