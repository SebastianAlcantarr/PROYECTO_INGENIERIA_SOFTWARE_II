from fastapi import FastAPI, HTTPException
import base64
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse

app = FastAPI()

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
#            MODELOS DE DATOS
# ==========================================

# 1. Usuarios
class UsuarioRegistro(BaseModel):
    email: str
    password: str
    nombre: str = None
    apellidos: str = None

class UsuarioDatos(BaseModel):
    email: str
    nombre: str
    apellidos: str

# 2. Modelo Genérico para Foros (Sirve para 1, 2, 4, 5, 6)
# Incluye hasta r7 y r8 por si acaso
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

# 4. Modelo Examen
class Examen1(BaseModel):
    email: str
    r1: str = ""; r2: str = ""; r3: str = ""; r4: str = ""; r5: str = ""; r6: str = ""

class Examen2(BaseModel):
        email: str
        r1: str = ""
        r2: str = ""
        r3: str = ""
        r4: str = ""
        r5: str = ""
        r6: str = ""
        r7: str = ""

class FeedbackData(BaseModel):
    email_alumno: str
    actividad: str
    comentario: str

# ==========================================
#            CONFIGURACIÓN BD
# ==========================================

# Configuración de tus foros dinámicos
FOROS = [
    {"id": 1, "nombre": "respuestas_foro1", "preguntas": 6, "ruta": "foro1"},
    {"id": 2, "nombre": "respuestas_foro2", "preguntas": 6, "ruta": "foro2"},
    {"id": 4, "nombre": "respuestas_foro4", "preguntas": 7, "ruta": "foro4"},
    {"id": 6, "nombre": "respuestas_foro6", "preguntas": 8, "ruta": "foro6"}
]

def get_foro_config(foro_id: int):
    for foro in FOROS:
        if foro["id"] == foro_id:
            return foro
    return None

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

# ==========================================
#            RUTAS DE USUARIOS
# ==========================================

@app.post("/registrar")
async def registrar(datos: UsuarioRegistro):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO usuarios (email, password, nombre, apellidos) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (datos.email, datos.password, datos.nombre, datos.apellidos))
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
    finally:
        conexion.close()

@app.get("/conseguir_usuario/{email}")
async def sacar_usuario(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, apellidos, email FROM usuarios WHERE email = %s", (email,))
        resultado = cursor.fetchone()
        if not resultado: raise HTTPException(404, "Usuario no encontrado")
        return {"nombre": resultado[0], "apellidos": resultado[1], "email": resultado[2]}
    finally:
        conexion.close()

# ==========================================
#            RUTAS DINÁMICAS (Foros 1,2,4,5,6)
# ==========================================

@app.post("/guardar_foro{foro_id}")
async def guardar_respuestas_dinamico(foro_id: int, datos: RespuestasForo):
    foro = get_foro_config(foro_id)
    if not foro: raise HTTPException(404, "Foro no encontrado")

    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")

    try:
        cursor = conexion.cursor()
        # Verificar si ya existe
        cursor.execute(f"SELECT COUNT(*) FROM {foro['nombre']} WHERE email = %s", (datos.email,))
        if cursor.fetchone()[0] > 0:
            return {"mensaje": "Ya has participado", "exito": True}

        # Construir Query Dinámica
        campos = ["email"]
        valores = [datos.email]
        for i in range(1, foro['preguntas'] + 1):
            campo = f"r{i}"
            campos.append(campo)
            valores.append(getattr(datos, campo, ""))

        placeholders = ", ".join(["%s"] * len(campos))
        campos_str = ", ".join(campos)

        query = f"INSERT INTO {foro['nombre']} ({campos_str}) VALUES ({placeholders})"
        cursor.execute(query, tuple(valores))
        conexion.commit()
        return {"mensaje": "Guardado", "exito": True}
    except Exception as e:
        conexion.rollback()
        print(f"Error foro {foro_id}: {str(e)}")
        return {"mensaje": str(e), "exito": False}
    finally:
        conexion.close()

@app.get("/respuestas_foro{foro_id}")
async def obtener_respuestas_dinamico(foro_id: int):
    foro = get_foro_config(foro_id)
    if not foro: raise HTTPException(404, "Foro no encontrado")
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        # Intentamos JOIN con usuarios
        try:
            query = f"""
                SELECT r.*, u.nombre, u.apellidos
                FROM {foro['nombre']} r
                LEFT JOIN usuarios u ON r.email = u.email
                ORDER BY r.fecha DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except:
            conexion.rollback()
            # Si falla el join, traemos solo respuestas
            cursor.execute(f"SELECT * FROM {foro['nombre']} ORDER BY fecha DESC")
            return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/verificar_foro{foro_id}/{email}")
async def verificar_participacion_dinamico(foro_id: int, email: str):
    foro = get_foro_config(foro_id)
    if not foro: return {"participo": False}
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {foro['nombre']} WHERE email = %s", (email,))
        return {"participo": cursor.fetchone()[0] > 0}
    except:
        return {"participo": False}
    finally:
        conexion.close()

# ==========================================
#            FORO 3 (ESPECIAL)
# ==========================================

@app.post("/guardar_en_foro_3")
async def guardar_foro3(datos: RespuestaForo_3):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM respuestas_foro3 WHERE email = %s", (datos.email,))
        if cursor.fetchone()[0] > 0: return {"mensaje": "Ya participaste", "exito": True}

        query = """
                INSERT INTO respuestas_foro3
                (email, r1, r2, r3, r4, r5, t6_r1_c1, t6_r1_c2, t6_r1_c3, t6_r2_c1, t6_r2_c2, t6_r2_c3,
                 t6_r3_c1, t6_r3_c2, t6_r3_c3, t6_r4_c1, t6_r4_c2, t6_r4_c3, t6_r5_c1, t6_r5_c2, t6_r5_c3,
                 t6_r6_c1, t6_r6_c2, t6_r6_c3, t6_r7_c1, t6_r7_c2, t6_r7_c3, r7, r8)
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) \
                """
        valores = (datos.email, datos.r1, datos.r2, datos.r3, datos.r4, datos.r5,
                   datos.t6_r1_c1, datos.t6_r1_c2, datos.t6_r1_c3, datos.t6_r2_c1, datos.t6_r2_c2, datos.t6_r2_c3,
                   datos.t6_r3_c1, datos.t6_r3_c2, datos.t6_r3_c3, datos.t6_r4_c1, datos.t6_r4_c2, datos.t6_r4_c3,
                   datos.t6_r5_c1, datos.t6_r5_c2, datos.t6_r5_c3, datos.t6_r6_c1, datos.t6_r6_c2, datos.t6_r6_c3,
                   datos.t6_r7_c1, datos.t6_r7_c2, datos.t6_r7_c3, datos.r7, datos.r8)
        cursor.execute(query, valores)
        conexion.commit()
        return {"mensaje": "Guardado", "exito": True}
    except Exception as e:
        print(e)
        return {"mensaje": str(e), "exito": False}
    finally:
        conexion.close()

@app.get("/respuestas_en_foro_3")
async def leer_foro3():
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT r.*, u.nombre, u.apellidos FROM respuestas_foro3 r LEFT JOIN usuarios u ON r.email = u.email ORDER BY r.fecha DESC")
        return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/verificar_en_foro_3/{email}")
async def verificar_foro3(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM respuestas_foro3 WHERE email = %s", (email,))
        return {"participo": cursor.fetchone()[0] > 0}
    except:
        return {"participo": False}
    finally:
        conexion.close()

# ==========================================
#            EXAMEN 1
# ==========================================

@app.post("/guardar_examen1")
async def guardar_examen1(datos: Examen1):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO examen1 (email,r1,r2,r3,r4,r5,r6) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        cursor.execute(query, (datos.email, datos.r1, datos.r2, datos.r3, datos.r4, datos.r5, datos.r6))
        conexion.commit()
        return {"mensaje": "Guardado", "exito": True}
    finally:
        conexion.close()

@app.get("/respuestas_examen1")
async def leer_examen1():
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT r.*, u.nombre, u.apellidos FROM examen1 r LEFT JOIN usuarios u ON r.email = u.email ORDER BY r.fecha DESC")
        return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/verificar_examen1/{email}")
async def verificar_examen1(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM examen1 WHERE email = %s AND email != 'admin@gmail.com'", (email,))
        return {"participo": cursor.fetchone()[0] > 0}
    finally:
        conexion.close()

# ==========================================
#            PANEL PROFESOR
# ==========================================

@app.get("/lista_estudiantes")
async def lista_estudiantes():
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT email, nombre, apellidos 
            FROM usuarios 
            WHERE email != 'admin@gmail.com'
            ORDER BY apellidos ASC
        """)
        return cursor.fetchall()
    finally:
        conexion.close()



import base64



@app.get("/expediente_completo/{email}")
async def expediente_completo(email: str):
    if email == "admin@gmail.com":
        return {
            "foro1": None,
            "foro2": None,
            "foro3": None,
            "foro4": None,
            "foro5": None,
            "foro6": None,
            "examen1": None,
            "examen2": None
        }

    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)

        cursor.execute("SELECT * FROM respuestas_foro1 WHERE email = %s", (email,))
        foro1 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro2 WHERE email = %s", (email,))
        foro2 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro4 WHERE email = %s", (email,))
        foro4 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro3 WHERE email = %s", (email,))
        foro3 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro5 WHERE email = %s", (email,))
        foro5 = cursor.fetchone()

        cursor.execute("SELECT * FROM examen1 WHERE email = %s", (email,))
        examen1 = cursor.fetchone()

        cursor.execute("SELECT * FROM examen2 WHERE email = %s", (email,))
        examen2 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro6 WHERE email = %s", (email,))
        foro6 = cursor.fetchone()

        if foro5 and "imagen" in foro5 and foro5["imagen"]:
            foro5["imagen"] = base64.b64encode(foro5["imagen"]).decode("utf-8")

        return {
            "foro1": foro1,
            "foro2": foro2,
            "foro3": foro3,
            "foro4": foro4,
            "foro5": foro5,
            "foro6": foro6,
            "examen1": examen1,
            "examen2":examen2
        }
    finally:
        conexion.close()


@app.get("/expediente_completo_alumno/{email}")
async def expediente_completo(email: str):
    if email == "admin@gmail.com":
        return {
            "foro1": None,
            "foro2": None,
            "foro3": None,
            "foro4": None,
            "foro5": None,
            "foro6": None,
            "examen1": None,
            "examen2": None
        }

    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)

        cursor.execute("SELECT * FROM respuestas_foro1 WHERE email = %s", (email,))
        foro1 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro2 WHERE email = %s", (email,))
        foro2 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro4 WHERE email = %s", (email,))
        foro4 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro3 WHERE email = %s", (email,))
        foro3 = cursor.fetchone()

        cursor.execute("SELECT r3 FROM respuestas_foro5 WHERE email = %s", (email,))
        foro5 = cursor.fetchone()

        cursor.execute("SELECT * FROM examen1 WHERE email = %s", (email,))
        examen1 = cursor.fetchone()

        cursor.execute("SELECT * FROM examen2 WHERE email = %s", (email,))
        examen2 = cursor.fetchone()

        cursor.execute("SELECT * FROM respuestas_foro6 WHERE email = %s", (email,))
        foro6 = cursor.fetchone()

        if foro5 and "imagen" in foro5 and foro5["imagen"]:
            foro5["imagen"] = base64.b64encode(foro5["imagen"]).decode("utf-8")

        return {
            "foro1": foro1,
            "foro2": foro2,
            "foro3": foro3,
            "foro4": foro4,
            "foro5": foro5,
            "foro6": foro6,
            "examen1": examen1,
            "examen2":examen2
        }
    finally:
        conexion.close()



@app.post("/guardar_foro5/{email}")
async def guardar_foro5(
    email: str,                    # <-- viene del path
    r2: str = Form(""),
    r3: str = Form(""),
    r4: str = Form(""),
    r5: str = Form(""),
    r6: str = Form(""),
    imagen: UploadFile = File(None)
):

    conexion = conectar_bd()
    cursor = conexion.cursor()

    contenido = await imagen.read() if imagen else None

    query = """
        INSERT INTO respuestas_foro5 (email, r2, r3, r4, r5, r6, imagen)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (email, r2, r3, r4, r5, r6, contenido))

    conexion.commit()
    conexion.close()

    return {"exito": True}



@app.get("/verificar_en_foro_5/{email}")
async def verificar_foro3(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM respuestas_foro5 WHERE email = %s", (email,))
        return {"participo": cursor.fetchone()[0] > 0}
    except:
        return {"participo": False}
    finally:
        conexion.close()


@app.get("/respuestas_en_foro_5")
async def leer_foro3():
    conexion = conectar_bd()
    if not conexion:
        raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT r.*, u.nombre, u.apellidos 
            FROM respuestas_foro5 r
            LEFT JOIN usuarios u ON r.email = u.email
            ORDER BY r.id DESC;
        """)
        respuestas = cursor.fetchall()

        for resp in respuestas:
            try:
                if resp.get('imagen'):
                    encoded = base64.b64encode(resp['imagen']).decode('utf-8')
                    resp['imagen_url'] = f"data:image/jpeg;base64,{encoded}"
                    del resp['imagen']
                else:
                    resp['imagen_url'] = None
            except Exception as e:
                print("Error con imagen:", e)
                resp['imagen_url'] = None

        return respuestas
    except Exception as e:
        print("Error en endpoint:", e)
        raise HTTPException(500, str(e))
    finally:
        conexion.close()

        # ==========================================
        #            EXAMEN 2
        # ==========================================

        @app.post("/guardar_examen2")
        async def guardar_examen1(datos: Examen2):
            conexion = conectar_bd()
            if not conexion: raise HTTPException(500, "Error BD")
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO examen1 (email,r1,r2,r3,r4,r5,r6,r7) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"
                cursor.execute(query, (datos.email, datos.r1, datos.r2, datos.r3, datos.r4, datos.r5, datos.r6,datos.r7))
                conexion.commit()
                return {"mensaje": "Guardado", "exito": True}
            finally:
                conexion.close()

        @app.get("/respuestas_examen2")
        async def leer_examen1():
            conexion = conectar_bd()
            if not conexion: raise HTTPException(500, "Error BD")
            try:
                cursor = conexion.cursor(cursor_factory=RealDictCursor)
                cursor.execute(
                    "SELECT r.*, u.nombre, u.apellidos FROM examen2 r LEFT JOIN usuarios u ON r.email = u.email ORDER BY r.fecha DESC")
                return cursor.fetchall()
            finally:
                conexion.close()




@app.post("/guardar_examen2")
async def guardar_examen1(datos: Examen2):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO examen2 (email,r1,r2,r3,r4,r5,r6,r7) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"
        cursor.execute(query, (datos.email, datos.r1, datos.r2, datos.r3, datos.r4, datos.r5, datos.r6,datos.r7))
        conexion.commit()
        return {"mensaje": "Guardado", "exito": True}
    finally:
        conexion.close()

@app.get("/respuestas_examen2")
async def leer_examen1():
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT r.*, u.nombre, u.apellidos FROM examen2 r LEFT JOIN usuarios u ON r.email = u.email ORDER BY r.fecha DESC")
        return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/verificar_examen2/{email}")
async def verificar_examen1(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM examen2 WHERE email = %s AND email != 'admin@gmail.com'", (email,))
        return {"participo": cursor.fetchone()[0] > 0}
    finally:
        conexion.close()

@app.post("/guardar_feedback")
async def guardar_feedback(datos: FeedbackData):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO feedback (email_alumno, actividad, comentario) VALUES (%s, %s, %s)"
        cursor.execute(query, (datos.email_alumno, datos.actividad, datos.comentario))
        conexion.commit()
        return {"mensaje": "Feedback enviado", "exito": True}
    except Exception as e:
        print(e)
        return {"mensaje": str(e), "exito": False}
    finally:
        conexion.close()

@app.get("/obtener_feedback/{email}")
async def obtener_feedback(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM feedback WHERE email_alumno = %s ORDER BY fecha DESC", (email,))
        lista = cursor.fetchall()
        feedback_dict = {}
        for item in lista:
            feedback_dict[item['actividad']] = item['comentario']
        return feedback_dict
    finally:
        conexion.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)