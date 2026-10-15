<template>
  <div class="min-h-dvh bg-fondo text-tinta">
    <EncabezadoPortal />

    <main class="mx-auto grid max-w-[1240px] gap-12 px-4 pb-20 pt-10 sm:px-6 md:pt-16 lg:grid-cols-[minmax(0,1fr)_440px] lg:gap-16 lg:px-10">
      <section class="entrada">
        <p class="text-lg text-tenue">
          Hola, <span class="font-semibold text-tinta">{{ nombreUsuario }}</span>.
        </p>
        <h1 class="mt-4 text-[clamp(2.75rem,7vw,5.5rem)] font-extrabold leading-[0.98] tracking-[-0.015em]">
          ¡Bienvenido/a!
        </h1>
        <div class="lectura mt-8 text-lg">
          <p>
            Esta plataforma está diseñada para comprender el concepto de
            <strong>derivada</strong> a través de la resolución de una situación contextualizada en la que se analiza la relación existente entre la edad de una persona y la densidad mineral ósea.
          </p>
          <p>
            Estás a punto de iniciar. Sigue las instrucciones de cada foro y actividad.
          </p>
        </div>
        <button type="button" class="boton boton-curso mt-10 !min-h-14 !px-8 text-base" @click="comenzar">
          Comenzar
          <span class="material-symbols-outlined -mr-1" aria-hidden="true">arrow_forward</span>
        </button>
      </section>

      <aside aria-labelledby="titulo-secuencia" class="rounded-3xl p-6 sm:p-8" style="background: var(--c-barra); color: var(--c-barra-tinta)">
        <h2 id="titulo-secuencia" class="text-xl font-bold">Cálculo Diferencial · Secuencia Didáctica</h2>
        <p class="mt-1 text-sm" style="color: var(--c-barra-tenue)">{{ pasos.length }} pasos en 3 actividades</p>
        <ol class="mt-6 divide-y divide-white/10">
          <li v-for="(p, i) in pasos" :key="p.ruta" class="flex items-baseline gap-4 py-3">
            <span class="font-display numeral w-8 text-lg font-extrabold" :style="{ color: i === 0 ? 'var(--c-curso)' : 'var(--c-barra-tenue)' }">{{ pista(i) }}</span>
            <span class="min-w-0 flex-1">
              <span class="block text-sm" style="color: var(--c-barra-tenue)">{{ p.tipo }} · Actividad {{ p.actividad }}</span>
              <span class="block truncate font-semibold">{{ p.titulo }}</span>
            </span>
          </li>
        </ol>
      </aside>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import EncabezadoPortal from '@/components/EncabezadoPortal.vue';
import { pasos, pista } from '@/ruta.js';

const router = useRouter();
const nombreUsuario = ref("Estudiante");

onMounted(() => {
  const nombreGuardado = localStorage.getItem('nombre');
  if (nombreGuardado && nombreGuardado !== 'null') {
    // Tomamos solo el primer nombre
    nombreUsuario.value = nombreGuardado.split(' ')[0];
  }
});

function comenzar() {
  const email = localStorage.getItem('usuario');

  // usuario ya visito la pag
  if (email) {
    localStorage.setItem(`visto_bienvenida_${email}`, 'true');
  }

  // Redirigimos al Foro 1
  router.push('/foro1');
}
</script>

<style scoped>
.entrada {
  animation: entrada 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}
@keyframes entrada {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: none; }
}
</style>
