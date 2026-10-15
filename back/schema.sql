-- =====================================================================
--  Portal de Derivadas · Universidad de Sonora
--  Esquema de la base de datos (PostgreSQL 13+)
--
--  Uso en una base NUEVA (vacía):
--      psql "$DATABASE_URL" -f back/schema.sql
--
--  Para la base que YA está en Render, usa back/migracion.sql
--  (no borra datos; solo agrega lo que falta).
--
--  Convenciones:
--  * Cada alumno se identifica por su correo (usuarios.email).
--  * Cada tabla de respuestas guarda UNA fila por alumno (UNIQUE email).
--  * fecha es TIMESTAMP sin zona horaria en UTC: el frontend le agrega
--    la «Z» al mostrarla, así que NO debe ser TIMESTAMPTZ.
-- =====================================================================

BEGIN;

-- ---------------------------------------------------------------------
--  Usuarios (alumnos y profesor)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
    email       VARCHAR(255) PRIMARY KEY,
    password    TEXT         NOT NULL,          -- hash bcrypt ($2b$...)
    nombre      VARCHAR(120),
    apellidos   VARCHAR(160),
    fecha       TIMESTAMP    NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT usuarios_email_formato CHECK (email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$')
);

-- Búsqueda de correo sin importar mayúsculas (login, registro)
CREATE UNIQUE INDEX IF NOT EXISTS usuarios_email_lower_uq ON usuarios (lower(email));

-- Lista de estudiantes del profesor (ORDER BY apellidos)
CREATE INDEX IF NOT EXISTS usuarios_apellidos_idx ON usuarios (apellidos);

-- ---------------------------------------------------------------------
--  Foro 1 · La densidad mineral ósea (6 preguntas)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS respuestas_foro1 (
    id      SERIAL PRIMARY KEY,
    email   VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r1 TEXT NOT NULL DEFAULT '', r2 TEXT NOT NULL DEFAULT '', r3 TEXT NOT NULL DEFAULT '',
    r4 TEXT NOT NULL DEFAULT '', r5 TEXT NOT NULL DEFAULT '', r6 TEXT NOT NULL DEFAULT '',
    fecha   TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT respuestas_foro1_email_uq UNIQUE (email)
);

-- ---------------------------------------------------------------------
--  Foro 2 · Gráfico comparativo (6 preguntas)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS respuestas_foro2 (
    id      SERIAL PRIMARY KEY,
    email   VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r1 TEXT NOT NULL DEFAULT '', r2 TEXT NOT NULL DEFAULT '', r3 TEXT NOT NULL DEFAULT '',
    r4 TEXT NOT NULL DEFAULT '', r5 TEXT NOT NULL DEFAULT '', r6 TEXT NOT NULL DEFAULT '',
    fecha   TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT respuestas_foro2_email_uq UNIQUE (email)
);

-- ---------------------------------------------------------------------
--  Foro 3 · Relación entre edad y DMO (8 preguntas + tabla de 7x3)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS respuestas_foro3 (
    id      SERIAL PRIMARY KEY,
    email   VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r1 TEXT NOT NULL DEFAULT '', r2 TEXT NOT NULL DEFAULT '', r3 TEXT NOT NULL DEFAULT '',
    r4 TEXT NOT NULL DEFAULT '', r5 TEXT NOT NULL DEFAULT '',
    -- Pregunta 6: tabla de intervalos (fila = intervalo, columna = razón / comportamiento / DMO)
    t6_r1_c1 TEXT NOT NULL DEFAULT '', t6_r1_c2 TEXT NOT NULL DEFAULT '', t6_r1_c3 TEXT NOT NULL DEFAULT '',
    t6_r2_c1 TEXT NOT NULL DEFAULT '', t6_r2_c2 TEXT NOT NULL DEFAULT '', t6_r2_c3 TEXT NOT NULL DEFAULT '',
    t6_r3_c1 TEXT NOT NULL DEFAULT '', t6_r3_c2 TEXT NOT NULL DEFAULT '', t6_r3_c3 TEXT NOT NULL DEFAULT '',
    t6_r4_c1 TEXT NOT NULL DEFAULT '', t6_r4_c2 TEXT NOT NULL DEFAULT '', t6_r4_c3 TEXT NOT NULL DEFAULT '',
    t6_r5_c1 TEXT NOT NULL DEFAULT '', t6_r5_c2 TEXT NOT NULL DEFAULT '', t6_r5_c3 TEXT NOT NULL DEFAULT '',
    t6_r6_c1 TEXT NOT NULL DEFAULT '', t6_r6_c2 TEXT NOT NULL DEFAULT '', t6_r6_c3 TEXT NOT NULL DEFAULT '',
    t6_r7_c1 TEXT NOT NULL DEFAULT '', t6_r7_c2 TEXT NOT NULL DEFAULT '', t6_r7_c3 TEXT NOT NULL DEFAULT '',
    r7 TEXT NOT NULL DEFAULT '', r8 TEXT NOT NULL DEFAULT '',
    fecha   TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT respuestas_foro3_email_uq UNIQUE (email)
);

-- ---------------------------------------------------------------------
--  Foro 4 · Análisis DMO (7 preguntas)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS respuestas_foro4 (
    id      SERIAL PRIMARY KEY,
    email   VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r1 TEXT NOT NULL DEFAULT '', r2 TEXT NOT NULL DEFAULT '', r3 TEXT NOT NULL DEFAULT '',
    r4 TEXT NOT NULL DEFAULT '', r5 TEXT NOT NULL DEFAULT '', r6 TEXT NOT NULL DEFAULT '',
    r7 TEXT NOT NULL DEFAULT '',
    fecha   TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT respuestas_foro4_email_uq UNIQUE (email)
);

-- ---------------------------------------------------------------------
--  Foro 5 · Razón promedio de cambio (texto + fotos)
--  La pregunta 1 son hasta 3 fotos de la tabla; la 3 es la foto del bosquejo
--  más su argumentación (r3).
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS respuestas_foro5 (
    id                 SERIAL PRIMARY KEY,
    email              VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r2                 TEXT NOT NULL DEFAULT '',
    r3                 TEXT NOT NULL DEFAULT '',
    r4                 TEXT NOT NULL DEFAULT '',
    r5                 TEXT NOT NULL DEFAULT '',
    r6                 TEXT NOT NULL DEFAULT '',
    imagen_pregunta_3  BYTEA,
    imagen_1           BYTEA,
    imagen_2           BYTEA,
    imagen_3           BYTEA,
    fecha              TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT respuestas_foro5_email_uq UNIQUE (email),
    -- Límite de 8 MB por imagen para no saturar la base del plan gratuito
    CONSTRAINT respuestas_foro5_imagenes_tamano CHECK (
        coalesce(octet_length(imagen_pregunta_3), 0) <= 8388608 AND
        coalesce(octet_length(imagen_1), 0) <= 8388608 AND
        coalesce(octet_length(imagen_2), 0) <= 8388608 AND
        coalesce(octet_length(imagen_3), 0) <= 8388608
    )
);

-- ---------------------------------------------------------------------
--  Foro 6 · Covariación de las magnitudes (8 preguntas)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS respuestas_foro6 (
    id      SERIAL PRIMARY KEY,
    email   VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r1 TEXT NOT NULL DEFAULT '', r2 TEXT NOT NULL DEFAULT '', r3 TEXT NOT NULL DEFAULT '',
    r4 TEXT NOT NULL DEFAULT '', r5 TEXT NOT NULL DEFAULT '', r6 TEXT NOT NULL DEFAULT '',
    r7 TEXT NOT NULL DEFAULT '', r8 TEXT NOT NULL DEFAULT '',
    fecha   TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT respuestas_foro6_email_uq UNIQUE (email)
);

-- ---------------------------------------------------------------------
--  Examen 1 · cuestionario + 2 juegos. r6 = puntaje total
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS examen1 (
    id      SERIAL PRIMARY KEY,
    email   VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r1 TEXT NOT NULL DEFAULT '', r2 TEXT NOT NULL DEFAULT '', r3 TEXT NOT NULL DEFAULT '',
    r4 TEXT NOT NULL DEFAULT '', r5 TEXT NOT NULL DEFAULT '', r6 TEXT NOT NULL DEFAULT '',
    fecha   TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT examen1_email_uq UNIQUE (email)
);

-- ---------------------------------------------------------------------
--  Examen 2 · 7 preguntas
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS examen2 (
    id      SERIAL PRIMARY KEY,
    email   VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    r1 TEXT NOT NULL DEFAULT '', r2 TEXT NOT NULL DEFAULT '', r3 TEXT NOT NULL DEFAULT '',
    r4 TEXT NOT NULL DEFAULT '', r5 TEXT NOT NULL DEFAULT '', r6 TEXT NOT NULL DEFAULT '',
    r7 TEXT NOT NULL DEFAULT '',
    fecha   TIMESTAMP NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT examen2_email_uq UNIQUE (email)
);

-- ---------------------------------------------------------------------
--  Retroalimentación del profesor
--  Se guarda el historial; el alumno ve el comentario más reciente
--  de cada actividad.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS feedback (
    id            SERIAL PRIMARY KEY,
    email_alumno  VARCHAR(255) NOT NULL REFERENCES usuarios (email) ON UPDATE CASCADE ON DELETE CASCADE,
    actividad     VARCHAR(20)  NOT NULL,
    comentario    TEXT         NOT NULL,
    fecha         TIMESTAMP    NOT NULL DEFAULT (now() AT TIME ZONE 'utc'),
    CONSTRAINT feedback_actividad_valida CHECK (
        actividad IN ('foro1', 'foro2', 'foro3', 'foro4', 'foro5', 'foro6', 'examen1', 'examen2')
    ),
    CONSTRAINT feedback_comentario_no_vacio CHECK (length(btrim(comentario)) > 0)
);

-- «Último comentario por actividad de un alumno»
CREATE INDEX IF NOT EXISTS feedback_alumno_actividad_fecha_idx
    ON feedback (email_alumno, actividad, fecha DESC);

-- Muros de respuestas: se listan del más reciente al más antiguo
CREATE INDEX IF NOT EXISTS respuestas_foro1_fecha_idx ON respuestas_foro1 (fecha DESC);
CREATE INDEX IF NOT EXISTS respuestas_foro2_fecha_idx ON respuestas_foro2 (fecha DESC);
CREATE INDEX IF NOT EXISTS respuestas_foro3_fecha_idx ON respuestas_foro3 (fecha DESC);
CREATE INDEX IF NOT EXISTS respuestas_foro4_fecha_idx ON respuestas_foro4 (fecha DESC);
CREATE INDEX IF NOT EXISTS respuestas_foro5_fecha_idx ON respuestas_foro5 (fecha DESC);
CREATE INDEX IF NOT EXISTS respuestas_foro6_fecha_idx ON respuestas_foro6 (fecha DESC);
CREATE INDEX IF NOT EXISTS examen1_fecha_idx          ON examen1 (fecha DESC);
CREATE INDEX IF NOT EXISTS examen2_fecha_idx          ON examen2 (fecha DESC);

COMMIT;

-- ---------------------------------------------------------------------
--  Supabase: protege las tablas de su API pública (REST/anon key).
--  El backend se conecta como «postgres», que no está sujeto a RLS,
--  así que esto no afecta a la aplicación.
-- ---------------------------------------------------------------------
ALTER TABLE usuarios          ENABLE ROW LEVEL SECURITY;
ALTER TABLE respuestas_foro1  ENABLE ROW LEVEL SECURITY;
ALTER TABLE respuestas_foro2  ENABLE ROW LEVEL SECURITY;
ALTER TABLE respuestas_foro3  ENABLE ROW LEVEL SECURITY;
ALTER TABLE respuestas_foro4  ENABLE ROW LEVEL SECURITY;
ALTER TABLE respuestas_foro5  ENABLE ROW LEVEL SECURITY;
ALTER TABLE respuestas_foro6  ENABLE ROW LEVEL SECURITY;
ALTER TABLE examen1           ENABLE ROW LEVEL SECURITY;
ALTER TABLE examen2           ENABLE ROW LEVEL SECURITY;
ALTER TABLE feedback          ENABLE ROW LEVEL SECURITY;
