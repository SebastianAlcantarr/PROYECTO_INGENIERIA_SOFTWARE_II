// Modo invitado: se puede recorrer todo el contenido sin cuenta,
// pero para enviar respuestas hay que iniciar sesión.
export function esInvitado() {
  return !localStorage.getItem("usuario");
}

export function entrarComoInvitado() {
  localStorage.removeItem("usuario");
  localStorage.removeItem("email");
  localStorage.removeItem("nombre");
}
