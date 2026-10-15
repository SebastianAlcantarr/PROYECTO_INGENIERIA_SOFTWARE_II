import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  // En GitHub Pages el sitio vive en /PROYECTO_INGENIERIA_SOFTWARE_II/ (lo define el workflow).
  base: process.env.BASE_PATH || '/',
    plugins: [
    vue(),tailwindcss()
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})

