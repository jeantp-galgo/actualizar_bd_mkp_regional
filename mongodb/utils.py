import mongodb.conexion_mongodb as conexion
from mongodb.pipeline import *

class mongodb_funciones:
    def __init__(self):
        self.cliente = conexion.conectar_mongo()

    def listar_colecciones(self):
        db = self.cliente.db_marketplace
        return db.list_collection_names()
    
    def seleccionar_coleccion(self, nombre_coleccion):
        db = self.cliente.db_marketplace
        nombre_coleccion = db.list_collection_names()[5]
        coleccion = db[nombre_coleccion]
        return coleccion

    def mostrar_primeros_registros_coleccion(self, nombre_coleccion):
        coleccion = self.seleccionar_coleccion(nombre_coleccion)
        print(f"\nPrimeros 5 documentos de {nombre_coleccion}:")
        for doc in coleccion.find().limit(5):
            print(doc)

    def datos_con_aggregation_personalizado(self, nombre_coleccion):
        pipeline = aggregation_personalizado()
        coleccion = self.seleccionar_coleccion(nombre_coleccion)
        return list(coleccion.aggregate(pipeline))
