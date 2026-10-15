<template>
  <div class="mt-4">
    <p class="mb-2 text-sm font-semibold text-tinta">Subir fotos de la tabla (max 3 imagenes)</p>
    <div
      role="button"
      tabindex="0"
      aria-label="Subir fotos de la tabla, máximo 3 imágenes"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      @click="fileInput && fileInput.click()"
      @keydown.enter.prevent="fileInput && fileInput.click()"
      @keydown.space.prevent="fileInput && fileInput.click()"
      class="cursor-pointer rounded-2xl border-2 border-dashed p-6 text-center transition-colors"
      :class="isDragging ? 'border-a1 bg-[color-mix(in_srgb,var(--c-a1)_10%,transparent)]' : 'border-linea-fuerte bg-superficie hover:border-a1'"
    >
      <div v-if="previews.length === 0" class="flex flex-col items-center gap-2 py-2">
        <span class="material-symbols-outlined text-4xl text-a1" aria-hidden="true">add_photo_alternate</span>
        <p class="font-semibold">Subir imágenes (máx. 3)</p>
        <p class="text-sm text-tenue">Arrastra aquí o haz clic · JPG o PNG</p>
      </div>
      <div v-else class="grid grid-cols-1 gap-4 sm:grid-cols-3">
        <div v-for="(img, index) in previews" :key="index" class="relative">
          <img :src="img" :alt="`Foto ${index + 1} de la tabla`" class="h-40 w-full rounded-xl border border-linea object-cover" />
          <button
            type="button"
            class="absolute -right-2 -top-2 grid h-8 w-8 place-items-center rounded-full bg-tinta text-fondo shadow"
            :aria-label="`Eliminar foto ${index + 1}`"
            @click.stop="removePhoto(index)"
          ><span class="material-symbols-outlined text-[18px]" aria-hidden="true">close</span></button>
        </div>
      </div>
    </div>
    <input type="file" ref="fileInput" class="hidden" accept="image/jpeg,image/png" multiple @change="onFileChange" />
  </div>
</template>

<script setup>
import { ref } from "vue";

const emit = defineEmits(["updateFotos"]);

const MAX_FILES = 3;

const previews = ref([]);
const files = ref([]);
const fileInput = ref(null);
const isDragging = ref(false);

function addFiles(fileList) {
  for (const file of fileList) {
    if (files.value.length >= MAX_FILES) break;
    if (!file.type.startsWith("image/")) continue;

    files.value.push(file);
    previews.value.push(URL.createObjectURL(file));
  }
  emit("updateFotos", files.value);
}

function onFileChange(e) {
  addFiles(e.target.files);
  e.target.value = "";
}

function handleDrop(e) {
  isDragging.value = false;
  addFiles(e.dataTransfer.files);
}

function removePhoto(index) {
  URL.revokeObjectURL(previews.value[index]);
  previews.value.splice(index, 1);
  files.value.splice(index, 1);
  emit("updateFotos", files.value);
}
</script>
