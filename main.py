
from interfaz.menus import menú_principal, menú_fotos, menú_albums, menú_usuarios
from negocio.negocio_photos import obtener_data_photos, listado_photos_db, crear_foto_db, actualizar_foto_db, eliminar_foto_db
from negocio.negocio_albums import obtener_data_albums, listado_albums_db, crear_album_db, actualizar_album_db, eliminar_album_db
from negocio.negocio_usuarios import crear_usuario_db, listar_usuarios_db, actualizar_usuario_db, eliminar_usuario_db

print("Bienvenido a la aplicación de Gestión de Fotos y Álbumes")


while True:
    elección_principal = menú_principal()
    
    if elección_principal == '1':
        while True:
            elección_fotos = menú_fotos()
            if elección_fotos == '1':
                obtener_data_photos('https://jsonplaceholder.typicode.com/photos')
            elif elección_fotos == '2':
                listado_photos_db()
            elif elección_fotos == '3':
                id_foto = input("Ingrese el ID de la foto: ")
                id_album = input("Ingrese el ID del álbum: ")
                titulo = input("Ingrese el título: ")
                url_img = input("Ingrese la URL de la imagen: ")
                url_thumb = input("Ingrese la URL del thumbnail: ")
                resultado = crear_foto_db(int(id_foto), int(id_album), titulo, url_img, url_thumb)
                if resultado:
                    print("Foto creada correctamente.")
            elif elección_fotos == '4':
                id_foto = input("Ingrese el ID de la foto a actualizar: ")
                nuevo_titulo = input("Ingrese el nuevo título: ")
                actualizar_foto_db(int(id_foto), nuevo_titulo)
            elif elección_fotos == '5':
                id_foto = input("Ingrese el ID de la foto a eliminar: ")
                eliminar_foto_db(int(id_foto))
            elif elección_fotos == '6':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    
    elif elección_principal == '2':
        while True:
            elección_albums = menú_albums()
            if elección_albums == '1':
                obtener_data_albums('https://jsonplaceholder.typicode.com/albums')
            elif elección_albums == '2':
                listado_albums_db()
            elif elección_albums == '3':
                id_album = input("Ingrese el ID del álbum: ")
                user_id = input("Ingrese el ID del usuario: ")
                titulo = input("Ingrese el título: ")
                resultado = crear_album_db(int(id_album), int(user_id), titulo)
                if resultado:
                    print("Álbum creado correctamente.")
            elif elección_albums == '4':
                id_album = input("Ingrese el ID del álbum a actualizar: ")
                nuevo_titulo = input("Ingrese el nuevo título: ")
                actualizar_album_db(int(id_album), nuevo_titulo)
            elif elección_albums == '5':
                id_album = input("Ingrese el ID del álbum a eliminar: ")
                eliminar_album_db(int(id_album))
            elif elección_albums == '6':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    
    elif elección_principal == '3':
        while True:
            elección_usuarios = menú_usuarios()
            if elección_usuarios == '1':
                listar_usuarios_db()
            elif elección_usuarios == '2':
                nombre = input("Ingrese el nombre: ")
                correo = input("Ingrese el correo: ")
                contrasena = input("Ingrese la contraseña: ")
                resultado = crear_usuario_db(nombre, correo, contrasena)
                if resultado:
                    print("Usuario creado correctamente.")
            elif elección_usuarios == '3':
                id_usuario = input("Ingrese el ID del usuario a actualizar: ")
                nuevo_nombre = input("Ingrese el nuevo nombre (Enter para omitir): ")
                nuevo_correo = input("Ingrese el nuevo correo (Enter para omitir): ")
                nueva_contrasena = input("Ingrese la nueva contraseña (Enter para omitir): ")
                actualizar_usuario_db(int(id_usuario), nuevo_nombre or None, nuevo_correo or None, nueva_contrasena or None)
            elif elección_usuarios == '4':
                id_usuario = input("Ingrese el ID del usuario a eliminar: ")
                eliminar_usuario_db(int(id_usuario))
            elif elección_usuarios == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    
    elif elección_principal == '4':
        print("Saliendo de la aplicación. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
   