<template>
  <div class="mt-6">
    <label class="block text-sm font-medium text-gray-300 mb-3">
      Subir fotos de la tabla (max 3 imagenes)
    </label>
    <div
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      @click="fileInput && fileInput.click()"
      :class="[
        'border-2 border-dashed rounded-lg p-6 text-center transition-colors cursor-pointer',
        isDragging
          ? 'border-blue-500 bg-blue-500/10'
          : 'border-gray-600 hover:border-blue-400',
      ]"
    >
      <!-- Estado vacío -->
      <div v-if="previews.length === 0" class="space-y-2">
        <div class="flex justify-center">
          <svg
            class="w-12 h-12 text-blue-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
            />
          </svg>
        </div>
        <p class="text-sm text-gray-300">
          <span class="text-blue-400 font-medium">
            Subir imágenes (máx. 3)
          </span>
        </p>
      </div>
      <!-- Vista previa -->
      <div v-else class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div v-for="(img, index) in previews" :key="index" class="relative">
          <img
            :src="img"
            class="h-40 w-full object-cover rounded-lg border border-gray-600 shadow"
          />
          <button
            @click.stop="removePhoto(index)"
            class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full p-1 shadow hover:bg-red-600"
            title="Eliminar imagen"
          >
            ✕
          </button>
        </div>
      </div>
    </div>
    <input
      type="file"
      ref="fileInput"
      class="hidden"
      accept="image/jpeg,image/png"
      multiple
      @change="onFileChange"
    />
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

  // 🔴 CLAVE
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

  // 🔴 CLAVE
  emit("updateFotos", files.value);
}
</script>
