
from src.controller import FacturasController

try:
    # 1. Probar la conexión
    conexion = FacturasController.obtener_conexion()
    conexion.close()
    print("Conexión exitosa a PostgreSQL")

    # 2. Crear la tabla si no existe
    FacturasController.crear_tabla()

    FacturasController.eliminar_tabla("FAC-001")

except Exception as error:
    print("Error durante la prueba:", error)

