import psycopg2
import secret_config

from src.model import logica_sensores


class FacturasController:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
         database=secret_config.database,
         user=secret_config.user,
         password=secret_config.password,
         host=secret_config.host,
         port=secret_config.port,
         sslmode="require"
        )

    @staticmethod
    def insertar(numero_factura: str, nit: str, cliente: str,
                 n_servicios: int, precio_unitario: float):

        subtotal = n_servicios * precio_unitario
        iva = subtotal * 0.19
        valor_total = subtotal + iva
    

        conexion = FacturasController.obtener_conexion()
        cursor = conexion.cursor()

        try:
            consulta = """
                INSERT INTO public.facturas
                (numero_factura, nit, cliente, n_servicios,
                 precio_unitario, iva, valor_total)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            datos = (
                numero_factura,
                nit,
                cliente,
                n_servicios,
                precio_unitario,
                iva,
                valor_total
            )

            cursor.execute(consulta, datos)
            conexion.commit()

            return True

        except Exception as error:
            conexion.rollback()
            print("Error al insertar la factura:", error)
            raise

        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def buscar_factura(numero_factura: str):
     conexion = FacturasController.obtener_conexion()
     cursor = conexion.cursor()

     try:
        consulta = """
            SELECT id_factura, numero_factura, nit, cliente,
                   n_servicios, precio_unitario, iva, valor_total, fecha
            FROM public.facturas
            WHERE numero_factura = %s
        """

        cursor.execute(consulta, (numero_factura,))
        factura = cursor.fetchone()

        if factura:
            print("Factura encontrada:", factura)
            return factura
        else:
            print("No se encontró la factura.")
            return None

     except Exception as error:
        print("Error al buscar la factura:", error)
        return None

     finally:
        cursor.close()
        conexion.close()

    @staticmethod
    def crear_tabla():
     conexion = FacturasController.obtener_conexion()
     cursor = conexion.cursor()

     try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS public.facturas (
                id_factura SERIAL PRIMARY KEY,
                numero_factura VARCHAR(50) UNIQUE NOT NULL,
                nit VARCHAR(30) NOT NULL,
                cliente VARCHAR(100) NOT NULL,
                n_servicios INTEGER NOT NULL,
                precio_unitario NUMERIC(12, 2) NOT NULL,
                iva NUMERIC(12, 2) NOT NULL,
                valor_total NUMERIC(12, 2) NOT NULL,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conexion.commit()
        print("Tabla facturas creada correctamente.")

     except Exception as error:
        conexion.rollback()
        print(f"Error al crear la tabla: {error}")

     finally:
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_tabla():
     conexion = FacturasController.obtener_conexion()
     cursor = conexion.cursor()

     try:
        cursor.execute("DROP TABLE IF EXISTS public.facturas")
        conexion.commit()
        print("Tabla facturas eliminada correctamente.")

     except Exception as error:
        conexion.rollback()
        print("Error al eliminar la tabla:", error)

     finally:
        cursor.close()
        conexion.close()