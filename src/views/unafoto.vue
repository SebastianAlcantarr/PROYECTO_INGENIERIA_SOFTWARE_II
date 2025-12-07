<template> <div class="mt-6"> <label class="block text-sm font-medium text-gray-300 mb-3"> Sube una foto de tu bosquejo </label> <div @dragover.prevent="isDragging = true" @dragleave.prevent="isDragging = false" @drop.prevent="handleDrop" @click="fileInput && fileInput.click()" :class="[ 'border-2 border-dashed rounded-lg p-6 text-center transition-colors cursor-pointer', isDragging ? 'border-blue-500 bg-blue-500/10' : 'border-gray-600 hover:border-blue-400', preview ? 'p-4' : 'py-8' ]" > <!-- Estado vacío --> <div v-if="!preview" class="space-y-2"> <div class="flex justify-center"> <svg class="w-12 h-12 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" > <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" /> </svg> </div> <p class="text-sm text-gray-300"> <span class="text-blue-400 font-medium"> Subir Imagen del Bosquejo </span> </p> </div> <!-- Vista previa --> <div v-else class="space-y-4"> <div class="relative mx-auto max-w-xs"> <img :src="preview" alt="Vista previa del bosquejo" class="max-h-64 w-auto mx-auto rounded-lg shadow-md border border-gray-600" /> <button @click.stop="removePhoto" class="absolute -top-3 -right-3 bg-red-500 text-white rounded-full p-1.5 shadow-lg hover:bg-red-600 transition-colors" title="Eliminar imagen" > <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" > <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /> </svg> </button> </div> <p class="text-xs text-green-400 text-center"> Imagen cargada </p> </div> </div> <input type="file" ref="fileInput" class="hidden" accept="image/jpeg,image/png" @change="onFileChange" /> </div> </template>


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
