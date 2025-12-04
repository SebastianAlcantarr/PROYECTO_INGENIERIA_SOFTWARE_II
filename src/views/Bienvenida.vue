<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#244a76] dark:bg-[rgb(16,22,34)] p-6 font-display relative overflow-hidden">

    <!-- Fondo decorativo -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
      <div class="absolute -top-24 -left-24 w-96 h-96 rounded-full bg-blue-500/10 blur-3xl"></div>
      <div class="absolute top-1/2 right-0 w-64 h-64 rounded-full bg-purple-500/10 blur-3xl"></div>
    </div>

    <!-- Tarjeta Principal -->
    <div class="relative z-10 max-w-4xl w-full bg-[#161d2b]/90 backdrop-blur-md border border-gray-700 rounded-2xl shadow-2xl overflow-hidden flex flex-col md:flex-row animate-fade-in-up">

      <!-- Izquierda -->
      <div class="w-full md:w-1/3 bg-linear-to-br from-blue-600 to-indigo-700 p-8 flex flex-col items-center justify-center text-white text-center">
        <span class="material-symbols-outlined text-8xl mb-4 text-white/90">school</span>
        <h2 class="text-2xl font-bold">Cálculo Diferencial</h2>
        <div class="w-16 h-1 bg-white/30 rounded-full my-4"></div>
        <p class="text-blue-100 text-sm font-medium">Secuencia Didáctica</p>
      </div>

      <!-- Derecha -->
      <div class="w-full md:w-2/3 p-8 md:p-12 flex flex-col justify-center">
        <h1 class="text-3xl md:text-4xl font-black text-white mb-6">
          ¡Bienvenido/a!
        </h1>

        <div class="space-y-4 text-gray-300 text-lg leading-relaxed mb-8">
          <p>
            Hola, <span class="text-blue-400 font-bold text-xl">{{ nombreUsuario }}</span>.
          </p>
          <p>
            Esta plataforma está diseñada para guiarte en el aprendizaje de las
            <strong class="text-white">derivadas</strong> y su aplicación en la vida real,
            analizando casos como la densidad mineral ósea.
          </p>
          <p>
            Estás a punto de iniciar. Sigue las instrucciones de cada foro y actividad.
          </p>
        </div>

        <div class="flex justify-end">
          <button
              @click="comenzar"
              class="group flex items-center gap-3 bg-blue-600 hover:bg-blue-500 text-white text-lg font-bold py-4 px-8 rounded-xl transition-all shadow-lg   active:scale-95"
          >
            <span>Comenzar</span>
            <span class="material-symbols-outlined group-hover:translate-x-1 transition-transform">arrow_forward</span>
          </button>
        </div>
      </div>

    </div>

    <p class="text-gray-500 text-sm mt-8 relative z-10">Ingeniería de Software II &copy; 2024</p>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

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
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fadeInUp 0.6s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
</style>