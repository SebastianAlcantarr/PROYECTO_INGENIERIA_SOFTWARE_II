<template>
  <div class="mt-4">
    <p class="mb-2 text-sm font-semibold text-tinta">Sube una foto de tu bosquejo</p>
    <div
      role="button"
      tabindex="0"
      aria-label="Subir imagen del bosquejo"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      @click="fileInput && fileInput.click()"
      @keydown.enter.prevent="fileInput && fileInput.click()"
      @keydown.space.prevent="fileInput && fileInput.click()"
      class="cursor-pointer rounded-2xl border-2 border-dashed text-center transition-colors"
      :class="[
        isDragging ? 'border-a1 bg-[color-mix(in_srgb,var(--c-a1)_10%,transparent)]' : 'border-linea-fuerte bg-superficie hover:border-a1',
        preview ? 'p-4' : 'px-6 py-8',
      ]"
    >
      <div v-if="!preview" class="flex flex-col items-center gap-2">
        <span class="material-symbols-outlined text-4xl text-a1" aria-hidden="true">upload</span>
        <p class="font-semibold">Subir Imagen del Bosquejo</p>
        <p class="text-sm text-tenue">Arrastra aquí o haz clic · JPG o PNG</p>
      </div>
      <div v-else class="space-y-3">
        <div class="relative mx-auto max-w-xs">
          <img :src="preview" alt="Vista previa del bosquejo" class="mx-auto max-h-64 w-auto rounded-xl border border-linea" />
          <button
            type="button"
            class="absolute -right-3 -top-2 grid h-8 w-8 place-items-center rounded-full bg-tinta text-fondo shadow"
            aria-label="Eliminar imagen"
            @click.stop="removePhoto"
          ><span class="material-symbols-outlined text-[18px]" aria-hidden="true">close</span></button>
        </div>
        <p class="text-sm font-semibold text-ok">Imagen cargada</p>
      </div>
    </div>
    <input type="file" ref="fileInput" class="hidden" accept="image/jpeg,image/png" @change="onFileChange" />
  </div>
</template>

<script setup>
import { ref } from "vue";

const emit = defineEmits(["updateFoto"]);

const preview = ref(null);
const fileInput = ref(null);
const isDragging = ref(false);
const file = ref(null);

function onFileChange(e) {
  const f = e.target.files[0];
  if (!f) return;

  file.value = f;
  preview.value = URL.createObjectURL(f);
  emit("updateFoto", f);

  e.target.value = "";
}

function handleDrop(e) {
  isDragging.value = false;
  const f = e.dataTransfer.files[0];
  if (!f) return;

  file.value = f;
  preview.value = URL.createObjectURL(f);
  emit("updateFoto", f);
}

function removePhoto() {
  if (preview.value) URL.revokeObjectURL(preview.value);

  preview.value = null;
  file.value = null;
  emit("updateFoto", null);
}
</script>
