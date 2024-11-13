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
        coleccion = db[nombre_coleccion]
        return coleccion

    def mostrar_primeros_registros_coleccion(self, nombre_coleccion):
        coleccion = self.seleccionar_coleccion(nombre_coleccion)
        print(f"\nPrimeros 5 documentos de {nombre_coleccion}:")
        for doc in coleccion.find().limit(5):
            print(doc)

    def datos_con_aggregation_personalizado(self, nombre_coleccion):
        pipeline = aggregation_personalizado()
        print(f"Pipeline utilizado: {pipeline}")
        coleccion = self.seleccionar_coleccion(nombre_coleccion)
        print(f"Colección seleccionada: {coleccion.name}")
        resultados = list(coleccion.aggregate(pipeline))
        print(f"Resultados de la agregación: {resultados}")
        return resultados
