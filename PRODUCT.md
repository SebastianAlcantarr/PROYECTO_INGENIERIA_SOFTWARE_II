# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Estudiantes de licenciatura (18 a 20 años) de la Universidad de Sonora que cursan Cálculo Diferencial y resuelven la secuencia didáctica (foros y exámenes) desde su computadora o celular. Un profesor (cuenta de administrador) revisa las respuestas de cada alumno y deja retroalimentación.

## Product Purpose
Que el alumno comprenda el concepto de derivada como razón de cambio, a partir de una situación contextualizada: la relación entre la edad de una persona y la densidad mineral ósea (DMO). Éxito: el alumno completa los foros y exámenes en orden y el profesor puede ver su avance y responder.

## Positioning
Es el sitio del curso de la Universidad de Sonora: una secuencia didáctica guiada por un solo contexto real (DMO y edad), no un banco genérico de ejercicios.

## Operating Context
Actividad 1 (Foro 1), Actividad 2 (Foro 2 y Examen 1), Actividad 3 (Foros 3 a 6 y Examen 2). Panel de alumno con progreso y notas del profesor; panel de profesor con lista de estudiantes. Las fórmulas se muestran con MathJax. Backend FastAPI + PostgreSQL desplegado en Render.

## Capabilities and Constraints
- Solo cambia la interfaz: la lógica, los endpoints y el backend se conservan tal cual.
- Los textos y consignas de foros y exámenes (contenido pedagógico) no se reescriben.
- Tema claro y oscuro según la preferencia del sistema del alumno.
- Recorrido: ruta guiada paso a paso (Actividad 1 → 2 → 3) con anterior/siguiente; la barra lateral puede eliminarse.
- Stack existente: Vue 3, Vue Router, Tailwind 4, Vite.
- Escudo oficial de la Universidad de Sonora en `src/imagenes/logo-unison.webp`.

## Brand Commitments
Se presenta como sitio oficial del curso de la Universidad de Sonora, con identidad institucional formal. Restricción declarada por el usuario: rediseño total, moderno y atractivo para alguien de 18 a 20 años; lo más importante es la experiencia de usuario. Debe evitar: verse como plantilla o hecho por IA, verse infantil, verse aburrido o serio de más, y paredes de texto (secciones colapsables). Cada cambio se aplica de forma consistente en todas las páginas.

## Evidence on Hand
Imágenes y gráficas del contenido en `src/imagenes/`. No hay logotipo oficial, testimonios ni datos de uso; no inventarlos.

## Product Principles
- El contexto de la derivada (DMO y edad) está siempre presente; la interfaz sirve a esa secuencia.
- Formal y claro como institución, pero pensado para estudiantes, no para administradores.
- El avance del alumno y la retroalimentación del profesor son siempre visibles y fáciles de encontrar.
- Cambiar la apariencia nunca cambia el contenido pedagógico ni el comportamiento.
