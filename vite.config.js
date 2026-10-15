import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig(({ command, isPreview }) => ({
  // En GitHub Pages el sitio vive en /PROYECTO_INGENIERIA_SOFTWARE_II/; en desarrollo, en /.
  base: command === 'build' || isPreview ? '/PROYECTO_INGENIERIA_SOFTWARE_II/' : '/',
    plugins: [
    vue(),tailwindcss()
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
}))
