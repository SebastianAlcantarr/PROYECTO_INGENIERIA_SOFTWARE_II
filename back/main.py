import base64
import os
from contextlib import contextmanager
from typing import List, Optional

import bcrypt
import psycopg2
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import errors as pg_errors
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool
from pydantic import BaseModel

try:  # En local se lee back/.env; en Render se usan sus variables de entorno.
    from dotenv import load_dotenv

    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
except ImportError:
    pass

app = FastAPI()

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CORREO_PROFESOR = "admin@gmail.com"

# ==========================================
#            MODELOS DE DATOS
# ==========================================

# 1. Usuarios
class UsuarioRegistro(BaseModel):
    email: str
    password: str
    nombre: Optional[str] = None
    apellidos: Optional[str] = None

class UsuarioDatos(BaseModel):
    email: str
    nombre: str
    apellidos: str

# 2. Modelo Genérico para Foros (Sirve para 1, 2, 4, 6)
class RespuestasForo(BaseModel):
    email: str
    r1: str = ""
    r2: str = ""
    r3: str = ""
    r4: str = ""
    r5: str = ""
    r6: str = ""
    r7: str = ""
    r8: str = ""

# 3. Modelo Exclusivo Foro 3 (Tabla compleja)
class RespuestaForo_3(BaseModel):
    email: str
    r1: str = ""; r2: str = ""; r3: str = ""; r4: str = ""; r5: str = ""
    t6_r1_c1: str = ""; t6_r1_c2: str = ""; t6_r1_c3: str = ""
    t6_r2_c1: str = ""; t6_r2_c2: str = ""; t6_r2_c3: str = ""
    t6_r3_c1: str = ""; t6_r3_c2: str = ""; t6_r3_c3: str = ""
    t6_r4_c1: str = ""; t6_r4_c2: str = ""; t6_r4_c3: str = ""
    t6_r5_c1: str = ""; t6_r5_c2: str = ""; t6_r5_c3: str = ""
    t6_r6_c1: str = ""; t6_r6_c2: str = ""; t6_r6_c3: str = ""
    t6_r7_c1: str = ""; t6_r7_c2: str = ""; t6_r7_c3: str = ""
    r7: str = ""; r8: str = ""

# 4. Modelos de exámenes
class Examen1(BaseModel):
    email: str
    r1: str = ""; r2: str = ""; r3: str = ""; r4: str = ""; r5: str = ""; r6: str = ""

class Examen2(BaseModel):
    email: str
    r1: str = ""; r2: str = ""; r3: str = ""; r4: str = ""; r5: str = ""; r6: str = ""; r7: str = ""

class FeedbackData(BaseModel):
    email_alumno: str
    actividad: str
    comentario: str

# ==========================================
#            CONFIGURACIÓN BD
# ==========================================

# Foros que comparten la ruta dinámica /guardar_foro{id}
FOROS = {
    1: {"tabla": "respuestas_foro1", "preguntas": 6},
    2: {"tabla": "respuestas_foro2", "preguntas": 6},
    4: {"tabla": "respuestas_foro4", "preguntas": 7},
    6: {"tabla": "respuestas_foro6", "preguntas": 8},
}

# Actividad -> tabla (expedientes y retroalimentación)
ACTIVIDADES = {
    "foro1": "respuestas_foro1",
    "foro2": "respuestas_foro2",
    "foro3": "respuestas_foro3",
    "foro4": "respuestas_foro4",
    "foro5": "respuestas_foro5",
    "foro6": "respuestas_foro6",
    "examen1": "examen1",
    "examen2": "examen2",
}

CAMPOS_FORO3 = (
    ["r1", "r2", "r3", "r4", "r5"]
    + [f"t6_r{f}_c{c}" for f in range(1, 8) for c in range(1, 4)]
    + ["r7", "r8"]
)

_pool: Optional[ThreadedConnectionPool] = None


def _obtener_pool() -> ThreadedConnectionPool:
    """Crea el pool la primera vez. La conexión viene de DATABASE_URL (Supabase, Session pooler)."""
    global _pool
    if _pool is None:
        dsn = os.environ.get("DATABASE_URL")
        if not dsn:
            raise HTTPException(500, "Falta la variable de entorno DATABASE_URL")
        _pool = ThreadedConnectionPool(
            1, 8, dsn,
            sslmode="require",
            connect_timeout=10,
            keepalives=1, keepalives_idle=30, keepalives_interval=10, keepalives_count=3,
        )
    return _pool


@contextmanager
def bd(dict_cursor: bool = False):
    """Entrega un cursor dentro de una transacción: commit si todo sale bien, rollback si falla."""
    try:
        pool = _obtener_pool()
        conexion = pool.getconn()
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error conectando a la BD: {e}")
        raise HTTPException(500, "Error BD")

    if conexion.closed:  # la conexión del pool se cayó (p. ej. por inactividad)
        pool.putconn(conexion, close=True)
        conexion = pool.getconn()

    try:
        with conexion:
            with conexion.cursor(cursor_factory=RealDictCursor if dict_cursor else None) as cursor:
                yield cursor
    finally:
        pool.putconn(conexion, close=bool(conexion.closed))


def hashear(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def password_correcta(password: str, guardada: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), guardada.encode("utf-8"))
    except ValueError:
        return False


def a_data_url(valor) -> Optional[str]:
    if valor is None:
        return None
    if isinstance(valor, memoryview):
        valor = bytes(valor)
    return f"data:image/jpeg;base64,{base64.b64encode(valor).decode('utf-8')}"


def convertir_bytes(registro):
    """Convierte columnas binarias (imágenes) a texto para poder enviarlas como JSON."""
    if not registro:
        return
    for clave, valor in list(registro.items()):
        if isinstance(valor, memoryview):
            valor = bytes(valor)
        if isinstance(valor, (bytes, bytearray)):
            if "imagen" in clave.lower():
                registro[clave] = a_data_url(valor)
            else:
                registro[clave] = base64.b64encode(valor).decode("utf-8")


def insertar_una_vez(tabla: str, email: str, campos: List[str], valores: list) -> bool:
    """Inserta la respuesta solo si el alumno no había participado. Devuelve False si ya existía."""
    columnas = ", ".join(["email", *campos])
    marcadores = ", ".join(["%s"] * (len(campos) + 1))
    try:
        with bd() as cursor:
            cursor.execute(
                f"INSERT INTO {tabla} ({columnas}) VALUES ({marcadores}) ON CONFLICT (email) DO NOTHING",
                (email, *valores),
            )
            return cursor.rowcount == 1
    except pg_errors.ForeignKeyViolation:
        raise HTTPException(400, "El usuario no existe. Inicia sesión de nuevo.")


def ya_participo(tabla: str, email: str) -> bool:
    with bd() as cursor:
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {tabla} WHERE email = %s)", (email,))
        return cursor.fetchone()[0]


def muro(tabla: str) -> list:
    with bd(dict_cursor=True) as cursor:
        cursor.execute(
            f"""
            SELECT r.*, u.nombre, u.apellidos
            FROM {tabla} r
            LEFT JOIN usuarios u ON u.email = r.email
            ORDER BY r.fecha DESC
            """
        )
        return cursor.fetchall()

# ==========================================
#            RUTAS DE USUARIOS
# ==========================================

@app.post("/registrar")
def registrar(datos: UsuarioRegistro):
    email = datos.email.strip().lower()
    try:
        with bd() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (email, password, nombre, apellidos) VALUES (%s, %s, %s, %s)",
                (email, hashear(datos.password), datos.nombre, datos.apellidos),
            )
        return {"mensaje": "Usuario creado", "exito": True}
    except pg_errors.UniqueViolation:
        return {"mensaje": "El usuario ya existe", "exito": False}
    except pg_errors.CheckViolation:
        return {"mensaje": "El correo electrónico no es válido", "exito": False}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error registrando: {e}")
        return {"mensaje": "No se pudo crear la cuenta", "exito": False}


@app.post("/login")
def login(datos: UsuarioRegistro):
    with bd(dict_cursor=True) as cursor:
        cursor.execute(
            "SELECT email, password, nombre, apellidos FROM usuarios WHERE lower(email) = lower(%s)",
            (datos.email.strip(),),
        )
        usuario = cursor.fetchone()

    if usuario and password_correcta(datos.password, usuario["password"]):
        return {
            "mensaje": "Login correcto",
            "exito": True,
            "usuario": usuario["email"],
            "nombre": usuario["nombre"],
            "apellidos": usuario["apellidos"],
        }
    return {"mensaje": "Credenciales incorrectas", "exito": False}


@app.post("/actualizar_perfil")
def actualizar_perfil(datos: UsuarioDatos):
    with bd() as cursor:
        cursor.execute(
            "UPDATE usuarios SET nombre = %s, apellidos = %s WHERE email = %s",
            (datos.nombre, datos.apellidos, datos.email),
        )
    return {"mensaje": "Datos guardados", "exito": True}


@app.get("/conseguir_usuario/{email}")
def sacar_usuario(email: str):
    with bd(dict_cursor=True) as cursor:
        cursor.execute(
            "SELECT nombre, apellidos, email FROM usuarios WHERE lower(email) = lower(%s)", (email,)
        )
        resultado = cursor.fetchone()
    if not resultado:
        raise HTTPException(404, "Usuario no encontrado")
    return resultado

# ==========================================
#            RUTAS DINÁMICAS (Foros 1, 2, 4, 6)
# ==========================================

@app.post("/guardar_foro{foro_id}")
def guardar_respuestas_dinamico(foro_id: int, datos: RespuestasForo):
    foro = FOROS.get(foro_id)
    if not foro:
        raise HTTPException(404, "Foro no encontrado")
    campos = [f"r{i}" for i in range(1, foro["preguntas"] + 1)]
    try:
        nuevo = insertar_una_vez(foro["tabla"], datos.email, campos, [getattr(datos, c) for c in campos])
    except HTTPException as e:
        return {"mensaje": e.detail, "exito": False}
    except Exception as e:
        print(f"Error foro {foro_id}: {e}")
        return {"mensaje": "No se pudieron guardar tus respuestas", "exito": False}
    return {"mensaje": "Guardado" if nuevo else "Ya has participado", "exito": True}


@app.get("/respuestas_foro{foro_id}")
def obtener_respuestas_dinamico(foro_id: int):
    foro = FOROS.get(foro_id)
    if not foro:
        raise HTTPException(404, "Foro no encontrado")
    return muro(foro["tabla"])


@app.get("/verificar_foro{foro_id}/{email}")
def verificar_participacion_dinamico(foro_id: int, email: str):
    foro = FOROS.get(foro_id)
    if not foro:
        return {"participo": False}
    return {"participo": ya_participo(foro["tabla"], email)}

# ==========================================
#            FORO 3 (ESPECIAL)
# ==========================================

@app.post("/guardar_en_foro_3")
def guardar_foro3(datos: RespuestaForo_3):
    try:
        nuevo = insertar_una_vez(
            "respuestas_foro3", datos.email, CAMPOS_FORO3, [getattr(datos, c) for c in CAMPOS_FORO3]
        )
    except HTTPException as e:
        return {"mensaje": e.detail, "exito": False}
    except Exception as e:
        print(f"Error foro 3: {e}")
        return {"mensaje": "No se pudieron guardar tus respuestas", "exito": False}
    return {"mensaje": "Guardado" if nuevo else "Ya participaste", "exito": True}


@app.get("/respuestas_en_foro_3")
def leer_foro3():
    return muro("respuestas_foro3")


@app.get("/verificar_en_foro_3/{email}")
def verificar_foro3(email: str):
    return {"participo": ya_participo("respuestas_foro3", email)}

# ==========================================
#            FORO 5 (TEXTO + IMÁGENES)
# ==========================================

@app.post("/guardar_foro5/{email}")
async def guardar_foro5(
    email: str,
    r2: str = Form(""),
    r3: str = Form(""),
    r4: str = Form(""),
    r5: str = Form(""),
    r6: str = Form(""),
    imagen_pregunta_3: UploadFile = File(None),
    imagenes: List[UploadFile] = File([]),
):
    # Imagen del bosquejo (pregunta 3) y hasta 3 fotos de la tabla (pregunta 1)
    bosquejo = await imagen_pregunta_3.read() if imagen_pregunta_3 else None
    fotos = [await f.read() for f in imagenes[:3]]
    fotos += [None] * (3 - len(fotos))

    campos = ["r2", "r3", "r4", "r5", "r6", "imagen_pregunta_3", "imagen_1", "imagen_2", "imagen_3"]
    valores = [
        r2, r3, r4, r5, r6,
        psycopg2.Binary(bosquejo) if bosquejo else None,
        *[psycopg2.Binary(f) if f else None for f in fotos],
    ]
    try:
        nuevo = await run_in_threadpool(insertar_una_vez, "respuestas_foro5", email, campos, valores)
    except HTTPException as e:
        return {"mensaje": e.detail, "exito": False}
    except pg_errors.CheckViolation:
        return {"mensaje": "Una de las imágenes pesa más de 8 MB", "exito": False}
    except Exception as e:
        print(f"Error foro 5: {e}")
        return {"mensaje": "No se pudieron guardar tus respuestas", "exito": False}
    return {"mensaje": "Guardado" if nuevo else "Ya participaste", "exito": True}


@app.get("/verificar_en_foro_5/{email}")
def verificar_foro5(email: str):
    return {"participo": ya_participo("respuestas_foro5", email)}


@app.get("/respuestas_en_foro_5")
def leer_foro5():
    respuestas = muro("respuestas_foro5")
    for resp in respuestas:
        resp["imagen_pregunta_3_url"] = a_data_url(resp.pop("imagen_pregunta_3", None))
        for i in range(1, 4):
            resp[f"imagen_{i}_url"] = a_data_url(resp.pop(f"imagen_{i}", None))
    return respuestas

# ==========================================
#            EXÁMENES
# ==========================================

@app.post("/guardar_examen1")
def guardar_examen1(datos: Examen1):
    campos = ["r1", "r2", "r3", "r4", "r5", "r6"]
    try:
        nuevo = insertar_una_vez("examen1", datos.email, campos, [getattr(datos, c) for c in campos])
    except HTTPException as e:
        return {"mensaje": e.detail, "exito": False}
    return {"mensaje": "Guardado" if nuevo else "Ya habías enviado este examen", "exito": True}


@app.get("/respuestas_examen1")
def leer_examen1():
    return muro("examen1")


@app.get("/verificar_examen1/{email}")
def verificar_examen1(email: str):
    if email.lower() == CORREO_PROFESOR:
        return {"participo": False}
    return {"participo": ya_participo("examen1", email)}


@app.post("/guardar_examen2")
def guardar_examen2(datos: Examen2):
    campos = ["r1", "r2", "r3", "r4", "r5", "r6", "r7"]
    try:
        nuevo = insertar_una_vez("examen2", datos.email, campos, [getattr(datos, c) for c in campos])
    except HTTPException as e:
        return {"mensaje": e.detail, "exito": False}
    return {"mensaje": "Guardado" if nuevo else "Ya habías enviado este examen", "exito": True}


@app.get("/respuestas_examen2")
def leer_examen2():
    return muro("examen2")


@app.get("/verificar_examen2/{email}")
def verificar_examen2(email: str):
    if email.lower() == CORREO_PROFESOR:
        return {"participo": False}
    return {"participo": ya_participo("examen2", email)}

# ==========================================
#            PANEL PROFESOR
# ==========================================

@app.get("/lista_estudiantes")
def lista_estudiantes():
    with bd(dict_cursor=True) as cursor:
        cursor.execute(
            """
            SELECT email, nombre, apellidos
            FROM usuarios
            WHERE lower(email) <> %s
            ORDER BY apellidos ASC NULLS LAST, nombre ASC
            """,
            (CORREO_PROFESOR,),
        )
        return cursor.fetchall()


EXPEDIENTE_VACIO = {actividad: None for actividad in ACTIVIDADES}


@app.get("/expediente_completo/{email}")
def expediente_completo(email: str):
    """Todas las respuestas de un alumno (vista del profesor)."""
    if email.lower() == CORREO_PROFESOR:
        return dict(EXPEDIENTE_VACIO)

    expediente = {}
    with bd(dict_cursor=True) as cursor:
        for actividad, tabla in ACTIVIDADES.items():
            cursor.execute(f"SELECT * FROM {tabla} WHERE email = %s", (email,))
            registro = cursor.fetchone()
            convertir_bytes(registro)
            expediente[actividad] = registro
    return expediente


@app.get("/expediente_completo_alumno/{email}")
def expediente_completo_alumno(email: str):
    """Qué actividades ya entregó el alumno, en una sola consulta (true o null por actividad)."""
    if email.lower() == CORREO_PROFESOR:
        return dict(EXPEDIENTE_VACIO)

    columnas = ",\n".join(
        f"EXISTS (SELECT 1 FROM {tabla} WHERE email = %(email)s) AS {actividad}"
        for actividad, tabla in ACTIVIDADES.items()
    )
    with bd(dict_cursor=True) as cursor:
        cursor.execute(f"SELECT {columnas}", {"email": email})
        fila = cursor.fetchone()
    return {actividad: (True if fila[actividad] else None) for actividad in ACTIVIDADES}

# ==========================================
#            RETROALIMENTACIÓN
# ==========================================

@app.post("/guardar_feedback")
def guardar_feedback(datos: FeedbackData):
    if not datos.comentario.strip():
        return {"mensaje": "El comentario está vacío", "exito": False}
    try:
        with bd() as cursor:
            cursor.execute(
                "INSERT INTO feedback (email_alumno, actividad, comentario) VALUES (%s, %s, %s)",
                (datos.email_alumno, datos.actividad, datos.comentario.strip()),
            )
        return {"mensaje": "Feedback enviado", "exito": True}
    except (pg_errors.CheckViolation, pg_errors.ForeignKeyViolation):
        return {"mensaje": "Actividad o alumno no válido", "exito": False}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error guardando feedback: {e}")
        return {"mensaje": "No se pudo enviar el comentario", "exito": False}


@app.get("/obtener_feedback/{email}")
def obtener_feedback(email: str):
    """El comentario más reciente de cada actividad: {actividad: comentario}."""
    with bd(dict_cursor=True) as cursor:
        cursor.execute(
            """
            SELECT DISTINCT ON (actividad) actividad, comentario
            FROM feedback
            WHERE email_alumno = %s
            ORDER BY actividad, fecha DESC, id DESC
            """,
            (email,),
        )
        return {fila["actividad"]: fila["comentario"] for fila in cursor.fetchall()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
