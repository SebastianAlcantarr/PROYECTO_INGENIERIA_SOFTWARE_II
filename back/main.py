from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE DATOS ---
class UsuarioRegistro(BaseModel):
    email: str
    password: str

class RespuestasForo1(BaseModel):
    email: str
    r1: str
    r2: str
    r3: str
    r4: str
    r5: str
    r6: str

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

# --- RUTAS DE USUARIOS (LOGIN/REGISTRO) ---

@app.post("/registrar")
async def registrar(datos: UsuarioRegistro):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
        cursor.execute(query, (datos.email, datos.password))
        conexion.commit()
        return {"mensaje": "Usuario creado", "exito": True}
    except psycopg2.IntegrityError:
        conexion.rollback()
        return {"mensaje": "El usuario ya existe", "exito": False}
    except Exception as e:
        conexion.rollback()
        return {"mensaje": f"Error: {str(e)}", "exito": False}
    finally:
        conexion.close()

@app.post("/login")
async def login(datos: UsuarioRegistro):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cursor.execute(query, (datos.email, datos.password))
        usuario = cursor.fetchone()
        if usuario:
            return {"mensaje": "Login correcto", "exito": True, "usuario": usuario['email']}
        else:
            return {"mensaje": "Credenciales incorrectas", "exito": False}
    finally:
        conexion.close()

@app.post("/guardar_foro1")
async def guardar_respuestas(datos: RespuestasForo1):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = """
                INSERT INTO respuestas_foro1 (email, r1, r2, r3, r4, r5, r6)
                VALUES (%s, %s, %s, %s, %s, %s, %s) \
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
        # Traemos las respuestas ordenadas por fecha (las más nuevas primero)
        query = "SELECT * FROM respuestas_foro1 ORDER BY fecha DESC"
        cursor.execute(query)
        lista = cursor.fetchall()
        return lista
    finally:
        conexion.close()