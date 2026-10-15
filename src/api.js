// URL del backend. Para usar otro (p. ej. local), define VITE_API_URL en un archivo .env:
//   VITE_API_URL=http://127.0.0.1:8000
export const API_URL = (
  import.meta.env.VITE_API_URL || "https://proyecto-ingenieria-software-iii.onrender.com"
).replace(/\/$/, "");
