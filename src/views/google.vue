<script>
export default {
  name: "GoogleLogin",

  mounted() {
    // Esperamos a que Google cargue
    if (window.google) {
      this.initGoogle();
    } else {
      // Por si el script tarda en cargar
      const check = setInterval(() => {
        if (window.google) {
          clearInterval(check);
          this.initGoogle();
        }
      }, 100);
    }
  },

  methods: {
    initGoogle() {
      google.accounts.id.initialize({
        client_id: "98898760407-st39p9tb5ldfcb4g6t4jtg86g8dl91an.apps.googleusercontent.com",
        callback: this.handleCredentialResponse,
      });
      google.accounts.id.renderButton(document.getElementById("googleBtn"), { theme: "filled_blue", size: "large" });

    },

    handleCredentialResponse(response) {
      console.log("TOKEN DE GOOGLE:", response.credential);

      // Este token (JWT) es lo que envías a tu backend
      // Backend verifica el token con Google
      // Luego tu backend crea la sesión del usuario
    },
  },
};
</script>
