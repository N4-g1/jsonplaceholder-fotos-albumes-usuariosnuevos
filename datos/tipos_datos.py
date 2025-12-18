from datos.conexion import sesion



def obtener_listado_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos

def insertar_objeto(objeto):
    try:
        sesion.add(objeto)
        sesion.flush()
        sesion.refresh(objeto)
        id_objeto = objeto.id
        sesion.commit()
        print("El objeto se ha guardado correctamente.")
        return id_objeto
    except Exception as error:
        sesion.rollback()
        print(f"Error al guardar el objeto: {error}")
        return None
    
def listar_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos

def eliminar_objeto(objeto):
    try:
        sesion.delete(objeto)
        sesion.commit()
        print("El objeto se ha eliminado correctamente.")
    except Exception as error:
        sesion.rollback()
        print(f"Error al eliminar el objeto: {error}")
    finally:
        sesion.close()

def actualizar_objeto():
    try:
        sesion.commit()
        print("El objeto se ha actualizado correctamente.")
    except Exception as error:
        sesion.rollback()
        print(f"Error al actualizar el objeto: {error}")
    finally:
        sesion.close()
