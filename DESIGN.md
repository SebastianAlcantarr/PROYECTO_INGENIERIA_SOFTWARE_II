# Design

Dirección: **Lista de reproducción** (elegida en la página de decisión, 2026-10-15). Reemplaza la dirección anterior («Libro de texto»).
Modo: operate (los foros y exámenes son tareas: leer, responder, enviar).

## Idea
La secuencia didáctica es la playlist del semestre. Cada foro y examen es una pista numerada (01–08), siempre sabes cuál «suena» y cuál sigue.

## Estructura (igual en todas las páginas)
- **Sin barra lateral.** Encabezado fijo (`EncabezadoPortal.vue`): marca, menús desplegables por actividad y menú de cuenta. En móvil, botón «Ruta» con hoja desplegable.
- **Cabecera de pista** (`PaginaPaso.vue`): número de pista enorme en el color de la actividad, título, actividad · tipo · estado, figura principal a la derecha.
- **Secciones plegables** (`Seccion.vue`): material de lectura, cuestionario, participaciones del grupo.
- **Preguntas** (`Pregunta.vue`): número grande a la izquierda, enunciado y campo.
- **Barra «En curso»** fija abajo (`BarraEnCurso.vue`): pista actual, avance por segmentos, anterior/siguiente.
- La ruta vive en `src/ruta.js` (única fuente de verdad).

## Tokens (`src/styles.css`)
- Claro y oscuro según la preferencia del sistema (`prefers-color-scheme`).
- Fondo `#f4f1ea` / `#0e1420`, tinta `#0e1420` / `#f1ede4`.
- Actividad 1 azul `#2f6fd6`, Actividad 2 dorado `#f2b33d` (texto `#8a5a00` en claro), Actividad 3 verde `#1f8a5c`.
- **Coral `#ff6b4a` reservado SOLO para lo que está «en curso»** (paso actual, botón Siguiente/Continuar/Comenzar). Nada más lo usa.
- Tipografía: Bricolage Grotesque (display, 700–800) + Figtree (texto). Lectura a 68ch.

## Reglas
- Lo completado se marca con trazo (número tachado) además de la etiqueta.
- La nota del profesor se lee en su propio margen junto a la pista, no en un modal.
- Sin bordes laterales gruesos, sin degradados, sin vidrio decorativo.
- Componentes compartidos: `.boton`, `.campo`, `.aviso`, `.ficha`, `.chip`, `.opcion`, `.recurso`, `.cita`, `.figura`, `.lectura`.

## Pendiente
Ninguno de identidad: el escudo oficial está en `src/imagenes/logo-unison.webp`.
