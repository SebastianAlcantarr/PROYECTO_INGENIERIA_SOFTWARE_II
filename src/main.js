import { createApp } from 'vue'
import App from './App.vue'
import './styles.css'
import router from '/index.js'


createApp(App)
    .use(router)
    .mount('#app')
