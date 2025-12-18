from prettytable import PrettyTable
import requests
from modelos.modelos import Foto as Photo
from datos.tipos_datos import insertar_objeto, obtener_listado_objetos, actualizar_objeto, eliminar_objeto
from datos.conexion import sesion
from requests.exceptions import RequestException
from auxiliares.codigos_estado import CodigoRespuesta, obtener_mensaje

def obtener_data_photos(url):
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        fotos = respuesta.json()[:20]  # Limitar a 20 fotos
        
        for foto in fotos:
            crear_foto_db(
                id_manual=foto['id'],
                id_album=foto['albumId'],
                titulo=foto['title'],
                url_img=foto['url'],
                url_thumb=foto['thumbnailUrl']
            )
        print(f"Fotos sincronizadas con éxito. Total: {len(fotos)}")
    except RequestException as e:
        print(f"Error al obtener fotos: {e}")

def crear_foto_db(id_manual, id_album, titulo, url_img, url_thumb):
    nueva_foto = Photo(
        id=id_manual,
        albumId=id_album,
        title=titulo,
        url=url_img,
        thumbnailUrl=url_thumb
    )
    try:
        resultado = insertar_objeto(nueva_foto)
        if resultado:
            print(f'[{CodigoRespuesta.CREADO}] {obtener_mensaje(CodigoRespuesta.CREADO)}')
            return resultado
        else:
            print(f'[{CodigoRespuesta.CONFLICTO}] {obtener_mensaje(CodigoRespuesta.CONFLICTO)} - ID {id_manual}')
            return None
    except Exception as error:
        print(f'[{CodigoRespuesta.ERROR_INTERNO}] {obtener_mensaje(CodigoRespuesta.ERROR_INTERNO)}: {error}')
        return None

def actualizar_foto_db(id_foto, nuevo_titulo):
    foto = sesion.query(Photo).filter_by(id=id_foto).first()
    if foto:
        foto.title = nuevo_titulo
        actualizar_objeto()
        print(f"Foto {id_foto} actualizada correctamente.")
    else:
        print(f"Foto con ID {id_foto} no encontrada.")

def eliminar_foto_db(id_foto):
    foto = sesion.query(Photo).filter_by(id=id_foto).first()
    if foto:
        eliminar_objeto(foto)
        print(f"Foto {id_foto} eliminada correctamente.")
    else:
        print(f"Foto con ID {id_foto} no encontrada.")

def listado_photos_db():
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Album ID', 'Título', 'URL']

    listado = obtener_listado_objetos(Photo)
    
    if listado:
        for p in listado[:20]: 
            tabla.add_row([p.id, p.albumId, p.title[:30], p.url])
        print('\nListado de Fotos (Primeras 20)')
        print(tabla)