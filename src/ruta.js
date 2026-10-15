// La secuencia didáctica en orden: la «playlist» del curso.
// Única fuente de verdad para la ruta guiada (encabezado, barra «En curso»,
// bienvenida, login y panel del alumno).

export const actividades = [
  { numero: 1, nombre: "Actividad 1", color: "var(--c-a1)", texto: "var(--c-a1)" },
  { numero: 2, nombre: "Actividad 2", color: "var(--c-a2)", texto: "var(--c-a2-texto)" },
  { numero: 3, nombre: "Actividad 3", color: "var(--c-a3)", texto: "var(--c-a3)" },
];

export const pasos = [
  { ruta: "/foro1", codigo: "foro1", tipo: "Foro 1", titulo: "La densidad mineral ósea", corto: "Densidad mineral", actividad: 1, icono: "bar_chart" },
  { ruta: "/foro2", codigo: "foro2", tipo: "Foro 2", titulo: "Densidad mineral ósea entre hombres y mujeres", corto: "Gráfico comparativo", actividad: 2, icono: "stacked_line_chart" },
  { ruta: "/foro2/examen1", codigo: "examen1", tipo: "Examen 1", titulo: "Evalúa tu comprensión: Densidad Mineral Ósea y Edad", corto: "DMO y edad", actividad: 2, icono: "assignment" },
  { ruta: "/foro3", codigo: "foro3", tipo: "Foro 3", titulo: "Relación entre edad y DMO", corto: "DMO cadera", actividad: 3, icono: "accessibility_new" },
  { ruta: "/foro4", codigo: "foro4", tipo: "Foro 4", titulo: "Análisis DMO", corto: "Análisis DMO", actividad: 3, icono: "query_stats" },
  { ruta: "/foro5", codigo: "foro5", tipo: "Foro 5", titulo: "Razón promedio de cambio", corto: "Razón de cambio", actividad: 3, icono: "trending_up" },
  { ruta: "/foro6", codigo: "foro6", tipo: "Foro 6", titulo: "Covariación de las magnitudes", corto: "Covariación", actividad: 3, icono: "swap_horiz" },
  { ruta: "/foro6/examen2", codigo: "examen2", tipo: "Examen 2", titulo: "Evalúa tu comprensión sobre el modelo", corto: "El modelo", actividad: 3, icono: "assignment_turned_in" },
];

export function indiceDe(ruta) {
  return pasos.findIndex((p) => p.ruta === ruta);
}

export function pista(indice) {
  return String(indice + 1).padStart(2, "0");
}

export function colorDeActividad(numero) {
  return actividades.find((a) => a.numero === numero)?.color ?? "var(--c-a1)";
}

// Variante legible como texto sobre el fondo (el dorado se oscurece en tema claro).
export function colorTextoDeActividad(numero) {
  return actividades.find((a) => a.numero === numero)?.texto ?? "var(--c-a1)";
}
