from prettytable import PrettyTable
import requests
from modelos.modelos import Album
from datos.tipos_datos import insertar_objeto, obtener_listado_objetos, actualizar_objeto, eliminar_objeto
from datos.conexion import sesion
from requests.exceptions import RequestException
from auxiliares.codigos_estado import CodigoRespuesta, obtener_mensaje

def obtener_data_albums(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        albums = respuesta.json()[:20]  # Limitar a 20 álbumes
        for item in albums:
            crear_album_db(
                id_manual=item['id'], 
                user_id=item['userId'],
                titulo=item['title']
            )
        print(f"Álbumes sincronizados con éxito. Total: {len(albums)}.")
    except RequestException as e:
        print(f"Error al obtener álbumes: {e}")

def crear_album_db(id_manual, user_id, titulo):
    nuevo_album = Album(
        id=id_manual,
        userId=user_id,
        title=titulo
    )
    try:
        resultado = insertar_objeto(nuevo_album)
        if resultado:
            print(f'[{CodigoRespuesta.CREADO}] {obtener_mensaje(CodigoRespuesta.CREADO)}')
            return resultado
        else:
            print(f'[{CodigoRespuesta.CONFLICTO}] {obtener_mensaje(CodigoRespuesta.CONFLICTO)} - ID {id_manual}')
            return None
    except Exception as error:
        print(f'[{CodigoRespuesta.ERROR_INTERNO}] {obtener_mensaje(CodigoRespuesta.ERROR_INTERNO)}: {error}')
        return None

def actualizar_album_db(id_album, nuevo_titulo):
    album = sesion.query(Album).filter_by(id=id_album).first()
    if album:
        album.title = nuevo_titulo
        actualizar_objeto()
        print(f"[{CodigoRespuesta.OK}] {obtener_mensaje(CodigoRespuesta.OK)} - Álbum {id_album} actualizado")
    else:
        print(f"[{CodigoRespuesta.NO_ENCONTRADO}] {obtener_mensaje(CodigoRespuesta.NO_ENCONTRADO)} - Álbum ID {id_album}")

def eliminar_album_db(id_album):
    album = sesion.query(Album).filter_by(id=id_album).first()
    if album:
        eliminar_objeto(album)
        print(f"[{CodigoRespuesta.NO_CONTENIDO}] {obtener_mensaje(CodigoRespuesta.NO_CONTENIDO)} - Álbum {id_album} eliminado")
    else:
        print(f"[{CodigoRespuesta.NO_ENCONTRADO}] {obtener_mensaje(CodigoRespuesta.NO_ENCONTRADO)} - Álbum ID {id_album}")

def listado_albums_db():
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'User ID', 'Título']
    listado = obtener_listado_objetos(Album)
    
    if listado:
        for a in listado:
            tabla.add_row([a.id, a.userId, a.title])
        print('\nÁlbumes en Base de Datos')
        print(tabla)

