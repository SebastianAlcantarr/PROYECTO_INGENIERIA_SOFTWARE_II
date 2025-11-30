from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE DATOS ---

# 1. Modelo de Registro/Login actualizado
class UsuarioRegistro(BaseModel):
    email: str
    password: str
    nombre: str = None
    apellidos: str = None

# 2. Modelo para actualizar datos (por si acaso)
class UsuarioDatos(BaseModel):
    email: str
    nombre: str
    apellidos: str

# 3. Modelo para las respuestas del Foro
class RespuestasForo1(BaseModel):
    email: str
    r1: str
    r2: str
    r3: str
    r4: str
    r5: str
    r6: str

# --- CONEXIÓN A BASE DE DATOS ---
def conectar_bd():
    try:
        conn = psycopg2.connect(
            host="dpg-d4f80d7pm1nc73eop5h0-a.oregon-postgres.render.com",
            database="database_7vyi",
            user="database_7vyi_user",
            password="EqKTvvDaJK6Ml5YoVYjnt4rLQmrxYIzo",
            port=5432,
            sslmode="require"
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la BD: {e}")
        return None

# --- RUTAS DE USUARIOS ---

@app.post("/registrar")
async def registrar(datos: UsuarioRegistro):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = """
                INSERT INTO usuarios (email, password, nombre, apellidos)
                VALUES (%s, %s, %s, %s) \
                """
        cursor.execute(query, (datos.email, datos.password, datos.nombre, datos.apellidos))

        conexion.commit()
        return {"mensaje": "Usuario creado correctamente", "exito": True}

    except psycopg2.IntegrityError:
        conexion.rollback()
        return {"mensaje": "El usuario ya existe", "exito": False}
    except Exception as e:
        conexion.rollback()
        print(f"Error en registro: {e}")
        return {"mensaje": f"Error interno: {str(e)}", "exito": False}
    finally:
        conexion.close()

@app.post("/login")
async def login(datos: UsuarioRegistro):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        query = "SELECT email, nombre, apellidos FROM usuarios WHERE email = %s AND password = %s"
        cursor.execute(query, (datos.email, datos.password))
        usuario = cursor.fetchone()

        if usuario:
            return {
                "mensaje": "Login correcto",
                "exito": True,
                "usuario": usuario['email'],
                "nombre": usuario['nombre'],
                "apellidos": usuario['apellidos']
            }
        else:
            return {"mensaje": "Credenciales incorrectas", "exito": False}
    finally:
        conexion.close()

@app.post("/actualizar_perfil")
async def actualizar_perfil(datos: UsuarioDatos):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = "UPDATE usuarios SET nombre = %s, apellidos = %s WHERE email = %s"
        cursor.execute(query, (datos.nombre, datos.apellidos, datos.email))
        conexion.commit()
        return {"mensaje": "Datos guardados", "exito": True}
    except Exception as e:
        conexion.rollback()
        print(e)
        return {"mensaje": "Error al actualizar", "exito": False}
    finally:
        conexion.close()

# --- RUTAS DEL FORO 1 ---

@app.post("/guardar_foro1")
async def guardar_respuestas(datos: RespuestasForo1):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = """
                INSERT INTO respuestas_foro1 (email, r1, r2, r3, r4, r5, r6)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(query, (datos.email, datos.r1, datos.r2, datos.r3, datos.r4, datos.r5, datos.r6))
        conexion.commit()
        return {"mensaje": "Respuestas guardadas", "exito": True}
    except Exception as e:
        print(e)
        return {"mensaje": "Error al guardar respuestas", "exito": False}
    finally:
        conexion.close()

@app.get("/respuestas_foro1")
async def obtener_respuestas():
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        query = """
                SELECT r.*, u.nombre, u.apellidos
                FROM respuestas_foro1 r
                         LEFT JOIN usuarios u ON r.email = u.email
                ORDER BY r.fecha DESC \
                """
        cursor.execute(query)
        lista = cursor.fetchall()
        return lista
    except Exception as e:
        print(f"Error obteniendo respuestas: {e}")
        conexion.rollback()
        cursor.execute("SELECT * FROM respuestas_foro1 ORDER BY fecha DESC")
        return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/verificar_foro1/{email}")
async def verificar_participacion(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        # Contamos cuántas respuestas tiene este email en la tabla
        query = "SELECT COUNT(*) FROM respuestas_foro1 WHERE email = %s"
        cursor.execute(query, (email,))
        resultado = cursor.fetchone()

        # Si el conteo es mayor a 0, es que YA respondió
        ya_respondio = resultado[0] > 0

        return {"participo": ya_respondio}
    finally:
        conexion.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)