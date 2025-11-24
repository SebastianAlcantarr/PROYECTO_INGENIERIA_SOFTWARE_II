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

class UsuarioRegistro(BaseModel):
    email: str
    password: str


def conectar_bd():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="derivadas_db",
            user="postgres",
            password="admin123",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la BD: {e}")
        return None

@app.post("/registrar")
async def registrar(datos: UsuarioRegistro):
    conexion = conectar_bd()
    if not conexion:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la Base de Datos")

    try:
        cursor = conexion.cursor()
        # Tu lógica clásica de SQL:
        query = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
        cursor.execute(query, (datos.email, datos.password))
        conexion.commit()

        return {"mensaje": "Usuario creado correctamente", "exito": True}

    except psycopg2.IntegrityError:
        conexion.rollback()
        return {"mensaje": "El usuario ya existe", "exito": False}
    except Exception as e:
        conexion.rollback()
        return {"mensaje": f"Error: {str(e)}", "exito": False}
    finally:
        cursor.close()
        conexion.close()

@app.post("/login")
async def login(datos: UsuarioRegistro):
    conexion = conectar_bd()
    if not conexion:
        raise HTTPException(status_code=500, detail="Error de conexión")

    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)

        query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cursor.execute(query, (datos.email, datos.password))
        usuario = cursor.fetchone()

        if usuario:
            return {"mensaje": "Login correcto", "exito": True, "usuario": usuario['email']}
        else:
            return {"mensaje": "Correo o contraseña incorrectos", "exito": False}
    finally:
        cursor.close()
        conexion.close()