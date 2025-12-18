class CodigoRespuesta:
    OK = 200
    CREADO = 201
    NO_CONTENIDO = 204
    
    SOLICITUD_INCORRECTA = 400
    NO_AUTORIZADO = 401
    NO_ENCONTRADO = 404
    CONFLICTO = 409
    
    ERROR_INTERNO = 500

MENSAJES = {
    200: "OK",
    201: "Creado",
    204: "Sin contenido",
    400: "Solicitud incorrecta",
    401: "No autorizado",
    404: "No encontrado",
    409: "Conflicto - Ya existe",
    500: "Error interno del servidor"
}

def obtener_mensaje(codigo):
    return MENSAJES.get(codigo, "Desconocido")
