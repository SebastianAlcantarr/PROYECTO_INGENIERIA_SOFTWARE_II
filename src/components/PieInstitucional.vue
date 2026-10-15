<template>
  <footer class="border-t border-linea bg-superficie">
    <div class="mx-auto flex max-w-[1240px] flex-col gap-6 px-4 py-8 sm:px-6 md:flex-row md:items-center md:justify-between lg:px-10">
      <div class="flex items-center gap-3">
        <LogoUniversidad :size="40" />
        <div class="leading-tight">
          <p class="font-semibold">Universidad de Sonora</p>
          <p class="text-sm text-tenue">Cálculo Diferencial I</p>
        </div>
      </div>
      <div class="text-sm text-tenue md:text-right">
        <p><span class="font-semibold text-tinta">Portal de Derivadas</span> · Proyecto de Ingeniería de Software II</p>
        <p>Secuencia didáctica: la derivada como razón de cambio (DMO y edad).</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import LogoUniversidad from "@/components/LogoUniversidad.vue";
</script>
