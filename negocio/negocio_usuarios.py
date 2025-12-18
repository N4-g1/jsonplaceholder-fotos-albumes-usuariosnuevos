from prettytable import PrettyTable
import bcrypt
from modelos.modelos import Usuario
from datos.tipos_datos import insertar_objeto, obtener_listado_objetos, actualizar_objeto, eliminar_objeto
from datos.conexion import sesion
from auxiliares.codigos_estado import CodigoRespuesta, obtener_mensaje

def hashear_contrasena(contrasena):
#Hashea la contraseña usando bcrypt
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(contrasena.encode(), salt).decode()

def verificar_contrasena(contrasena, contrasena_hash):
#Verifica si la contraseña coincide con el hash
    return bcrypt.checkpw(contrasena.encode(), contrasena_hash.encode())

def crear_usuario_db(nombre, correo, contrasena):
    contrasena_hash = hashear_contrasena(contrasena)
    nuevo_usuario = Usuario(
        nombre=nombre,
        correo=correo,
        contrasena_hash=contrasena_hash
    )
    try:
        resultado = insertar_objeto(nuevo_usuario)
        if resultado:
            print(f'[{CodigoRespuesta.CREADO}] {obtener_mensaje(CodigoRespuesta.CREADO)}')
            return resultado
        else:
            print(f'[{CodigoRespuesta.CONFLICTO}] {obtener_mensaje(CodigoRespuesta.CONFLICTO)}')
            return None
    except Exception as error:
        print(f'[{CodigoRespuesta.ERROR_INTERNO}] {obtener_mensaje(CodigoRespuesta.ERROR_INTERNO)}: {error}')
        return None

def listar_usuarios_db():
    usuarios = obtener_listado_objetos(Usuario)
    if usuarios:
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Correo"]
        for usuario in usuarios:
            tabla.add_row([usuario.id, usuario.nombre, usuario.correo])
        print(tabla)
    else:
        print("No hay usuarios registrados.")

def actualizar_usuario_db(id_usuario, nuevo_nombre=None, nuevo_correo=None, nueva_contrasena=None):
    usuario = sesion.query(Usuario).filter_by(id=id_usuario).first()
    if usuario:
        if nuevo_nombre:
            usuario.nombre = nuevo_nombre
        if nuevo_correo:
            usuario.correo = nuevo_correo
        if nueva_contrasena:
            usuario.contrasena_hash = hashear_contrasena(nueva_contrasena)
        actualizar_objeto()
        print(f"[{CodigoRespuesta.OK}] {obtener_mensaje(CodigoRespuesta.OK)} - Usuario {id_usuario} actualizado")
    else:
        print(f"[{CodigoRespuesta.NO_ENCONTRADO}] {obtener_mensaje(CodigoRespuesta.NO_ENCONTRADO)} - Usuario ID {id_usuario}")

def eliminar_usuario_db(id_usuario):
    usuario = sesion.query(Usuario).filter_by(id=id_usuario).first()
    if usuario:
        eliminar_objeto(usuario)
        print(f"[{CodigoRespuesta.NO_CONTENIDO}] {obtener_mensaje(CodigoRespuesta.NO_CONTENIDO)} - Usuario {id_usuario} eliminado")
    else:
        print(f"[{CodigoRespuesta.NO_ENCONTRADO}] {obtener_mensaje(CodigoRespuesta.NO_ENCONTRADO)} - Usuario ID {id_usuario}")

def iniciar_sesion(correo, contrasena):
    usuario = sesion.query(Usuario).filter_by(correo=correo).first()
    if usuario and verificar_contrasena(contrasena, usuario.contrasena_hash):
        print(f"[{CodigoRespuesta.OK}] {obtener_mensaje(CodigoRespuesta.OK)} - Inicio de sesión exitoso para {usuario.nombre}")
        return usuario
    else:
        print(f"[{CodigoRespuesta.NO_AUTORIZADO}] {obtener_mensaje(CodigoRespuesta.NO_AUTORIZADO)} - Credenciales inválidas")
        return None    