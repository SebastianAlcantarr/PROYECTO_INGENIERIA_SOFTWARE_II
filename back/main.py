from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor



class examen1(BaseModel):
    email: str
    r1: str = ""
    r2: str = ""
    r3: str = ""
    r4: str = ""
    r5: str = ""
    r6: str = ""


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

# 3. Modelo genérico para las respuestas del Foro
class RespuestasForo(BaseModel):
    email: str
    r1: str = ""
    r2: str = ""
    r3: str = ""
    r4: str = ""
    r5: str = ""
    r6: str = ""
    r7: str = ""


class RespuestaForo_3(BaseModel):
    email: str
    r1: str = ""
    r2: str = ""
    r3: str = ""
    r4: str = ""
    r5: str = ""
    t6_r1_c1: str = ""
    t6_r1_c2: str = ""
    t6_r1_c3: str = ""
    t6_r2_c1: str = ""
    t6_r2_c2: str = ""
    t6_r2_c3: str = ""
    t6_r3_c1: str = ""
    t6_r3_c2: str = ""
    t6_r3_c3: str = ""
    t6_r4_c1: str = ""
    t6_r4_c2: str = ""
    t6_r4_c3: str = ""
    t6_r5_c1: str = ""
    t6_r5_c2: str = ""
    t6_r5_c3: str = ""
    t6_r6_c1: str = ""
    t6_r6_c2: str = ""
    t6_r6_c3: str = ""
    t6_r7_c1: str = ""
    t6_r7_c2: str = ""
    t6_r7_c3: str = ""
    r7: str=""
    r8: str = ""



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
                VALUES (%s, %s, %s, %s) 
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

#FOROS
FOROS = [
    {"id": 1, "nombre": "respuestas_foro1", "preguntas": 6, "ruta": "foro1"},
    {"id": 2, "nombre": "respuestas_foro2", "preguntas": 6, "ruta": "foro2"},
    {"id": 4, "nombre": "respuestas_foro4", "preguntas": 7, "ruta": "foro4"},
    {"id": 5, "nombre": "respuestas_foro5", "preguntas": 7, "ruta": "foro5"},
    {"id": 6, "nombre": "respuestas_foro6", "preguntas": 7, "ruta": "foro6"}
]

def get_foro_config(foro_id: int):
    for foro in FOROS:
        if foro["id"] == foro_id:
            return foro
    return None

# --- RUTAS DINÁMICAS PARA FOROS ---
@app.post("/guardar_foro{foro_id}")
async def guardar_respuestas(foro_id: int, datos: RespuestasForo):
    foro = get_foro_config(foro_id)
    if not foro:
        raise HTTPException(404, "Foro no encontrado")

    conexion = conectar_bd()
    if not conexion:
        raise HTTPException(500, "Error de conexion a la base de datos")

    try:
        cursor = conexion.cursor()

        # Ver s ya hay usuario
        query_check = f"SELECT COUNT(*) FROM {foro['nombre']} WHERE email = %s"
        cursor.execute(query_check, (datos.email,))
        existe = cursor.fetchone()[0] > 0

        if existe:
            return {"mensaje": "Ya has participado en este foro", "exito": False}

        campos = ["email"]
        valores = [datos.email]

        for i in range(1, foro['preguntas'] + 1):
            campo = f"r{i}"
            campos.append(campo)
            valor = getattr(datos, campo, "")
            valores.append(valor)

        placeholders = ", ".join(["%s"] * len(campos))
        campos_str = ", ".join(campos)

        query = f"""
                INSERT INTO {foro['nombre']} ({campos_str})
                VALUES ({placeholders})
                """

        cursor.execute(query, tuple(valores))
        conexion.commit()
        return {"mensaje": "Respuestas guardadas exitosamente", "exito": True}

    except Exception as e:
        conexion.rollback()
        print(f"Error al guardar respuestas para foro {foro_id}: {str(e)}")
        return {"mensaje": f"Error al guardar respuestas: {str(e)}", "exito": False}
    finally:
        conexion.close()

@app.get("/respuestas_foro{foro_id}")
async def obtener_respuestas(foro_id: int):
    foro = get_foro_config(foro_id)
    if not foro:
        raise HTTPException(404, "Foro no encontrado")

    conexion = conectar_bd()
    if not conexion:
        raise HTTPException(500, "Error de conexión a la base de datos")

    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        query = f"""
                SELECT r.*, u.nombre, u.apellidos
                FROM {foro['nombre']} r
                LEFT JOIN usuarios u ON r.email = u.email
                ORDER BY r.fecha DESC
                """

        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print(f"Error obteniendo respuestas del foro {foro_id}: {str(e)}")
        conexion.rollback()

        # Intentar obtener solo los datos básicos si hay un error en la consulta compleja
        try:
            cursor.execute(f"SELECT * FROM {foro['nombre']} ORDER BY fecha DESC")
            return cursor.fetchall()
        except:
            return []
    finally:
        conexion.close()

@app.get("/verificar_foro{foro_id}/{email}")
async def verificar_participacion(foro_id: int, email: str):
    foro = get_foro_config(foro_id)
    if not foro:
        raise HTTPException(404, "Foro no encontrado")

    conexion = conectar_bd()
    if not conexion:
        raise HTTPException(500, "Error de conexión a la base de datos")

    try:
        cursor = conexion.cursor()

        # Verificar si el usuario ya ha participado en este foro
        query = f"SELECT COUNT(*) FROM {foro['nombre']} WHERE email = %s"
        cursor.execute(query, (email,))
        resultado = cursor.fetchone()

        return {"participo": resultado[0] > 0 if resultado else False}

    except Exception as e:
        print(f"Error verificando participación en foro {foro_id}: {str(e)}")
        return {"participo": False}
    finally:
        conexion.close()



#Exclusivo para el foro 3

@app.post("/guardar_en_foro_3")
async def guardar_respuestas(datos: RespuestaForo_3):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = """
                INSERT INTO respuestas_foro3 (email, r1, r2, r3, r4, r5, t6_r1_c1, t6_r1_c2, t6_r1_c3, t6_r2_c1, t6_r2_c2, t6_r2_c3, t6_r3_c1, t6_r3_c2, t6_r3_c3, t6_r4_c1, t6_r4_c2, t6_r4_c3, t6_r5_c1, t6_r5_c2, t6_r5_c3, t6_r6_c1, t6_r6_c2, t6_r6_c3, t6_r7_c1, t6_r7_c2, t6_r7_c3,r7,r8)
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
        cursor.execute(query, (datos.email, datos.r1, datos.r2, datos.r3, datos.r4, datos.r5,datos.t6_r1_c1, datos.t6_r1_c2, datos.t6_r1_c3, datos.t6_r2_c1, datos.t6_r2_c2, datos.t6_r2_c3, datos.t6_r3_c1, datos.t6_r3_c2, datos.t6_r3_c3, datos.t6_r4_c1, datos.t6_r4_c2, datos.t6_r4_c3, datos.t6_r5_c1, datos.t6_r5_c2, datos.t6_r5_c3, datos.t6_r6_c1, datos.t6_r6_c2, datos.t6_r6_c3, datos.t6_r7_c1, datos.t6_r7_c2, datos.t6_r7_c3,datos.r7,datos.r8))
        conexion.commit()
        return {"mensaje": "Respuestas guardadas", "exito": True}
    except Exception as e:
        print(e)
        return {"mensaje": "Error al guardar respuestas", "exito": False}
    finally:
        conexion.close()



@app.get("/respuestas_en_foro_3")
async def obtener_respuestas():
    global cursor
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        query = """
                SELECT r.*, u.nombre, u.apellidos
                FROM respuestas_foro3 r
                         LEFT JOIN usuarios u ON r.email = u.email
                ORDER BY r.fecha DESC 
                """
        cursor.execute(query)
        lista = cursor.fetchall()
        return lista
    except Exception as e:
        print(f"Error obteniendo respuestas: {e}")
        conexion.rollback()
        cursor.execute("SELECT * FROM respuestas_foro3 ORDER BY fecha DESC")
        return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/verificar_en_foro_3/{email}")
async def verificar_participacion(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        # Contamos cuántas respuestas tiene este email en la tabla
        query = "SELECT COUNT(*) FROM respuestas_foro3 WHERE email = %s"
        cursor.execute(query, (email,))
        resultado = cursor.fetchone()

        # Si el conteo es mayor a 0, es que YA respondió
        ya_respondio = resultado[0] > 0

        return {"participo": ya_respondio}
    finally:
        conexion.close()


















@app.get("/conseguir_usuario/{email}")
async def sacar_usuario(email: str):
    conexion = conectar_bd()
    if not conexion:
        raise HTTPException(500, "Error BD")

    try:
        cursor = conexion.cursor()
        query = "SELECT nombre, apellidos,email FROM usuarios WHERE email = %s"
        cursor.execute(query, (email,))
        resultado = cursor.fetchone()

        cursor.close()
        if not resultado:
            raise HTTPException(404, "Usuario no encontrado")

        nombre_usuario = resultado[0]
        apellido_usuario = resultado[1]
        email_usuario=resultado[2]


        return {
                "nombre": nombre_usuario,
                "apellidos":apellido_usuario,
                "email": email_usuario

        }


    finally:
        conexion.close()

@app.get("/lista_estudiantes")
async def lista_estudiantes():
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        # Traemos a todos los usuarios ordenados por apellido
        query = "SELECT email, nombre, apellidos FROM usuarios ORDER BY apellidos ASC"
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/expediente_completo/{email}")
async def expediente_completo(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)

        # respuestas del foro 1
        cursor.execute("SELECT * FROM respuestas_foro1 WHERE email = %s", (email,))
        foro1 = cursor.fetchone()

        # aqui van los demas

        return {
            "foro1": foro1
        }
    finally:
        conexion.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.post("/guardar_examen1")
async def guardar_respuestas(datos: examen1):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        query = """
                INSERT INTO examen1 (email,r1,r2,r3,r4,r5,r6)
                VALUES (%s, %s, %s, %s, %s, %s,%s)
                """
        cursor.execute(query, (datos.email, datos.r1, datos.r2, datos.r3, datos.r4,datos.r5,datos.r6))
        conexion.commit()
        return {"mensaje": "Respuestas guardadas", "exito": True}
    except Exception as e:
        print(e)
        return {"mensaje": "Error al guardar respuestas", "exito": False}
    finally:
        conexion.close()

@app.get("/respuestas_examen1")
async def obtener_respuestas():
    global cursor
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        query = """
                SELECT r.*, u.nombre, u.apellidos
                FROM examen1 r
                         LEFT JOIN usuarios u ON r.email = u.email
                ORDER BY r.fecha DESC 
                """
        cursor.execute(query)
        lista = cursor.fetchall()
        return lista
    except Exception as e:
        print(f"Error obteniendo respuestas: {e}")
        conexion.rollback()
        cursor.execute("SELECT * FROM respuestas_foro3 ORDER BY fecha DESC")
        return cursor.fetchall()
    finally:
        conexion.close()

@app.get("/verificar_examen1/{email}")
async def verificar_participacion(email: str):
    conexion = conectar_bd()
    if not conexion: raise HTTPException(500, "Error BD")
    try:
        cursor = conexion.cursor()
        # Contamos cuántas respuestas tiene este email en la tabla
        query = "SELECT COUNT(*) FROM examen1 WHERE email = %s"
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