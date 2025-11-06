import { createApp } from 'vue'
import App from './App.vue'
import './styles.css'
import router from './router'  // importar router

createApp(App)
    .use(router)                 // usar router
    .mount('#app')
