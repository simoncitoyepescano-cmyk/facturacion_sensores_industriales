
import psycopg2
import secret_config
from src.model.logica_sensores import Cliente

class ClienteController:

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
    def crear_tabla():
        conexion = None
        cursor = None

        try:
            conexion = ClienteController.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id_cliente SERIAL PRIMARY KEY,
                    nit VARCHAR(30) UNIQUE NOT NULL,
                    nombre_cliente VARCHAR(100) NOT NULL,
                    numero_servicios INTEGER NOT NULL,
                    precio_sensor NUMERIC(12, 2) NOT NULL,
                    iva NUMERIC(12, 2) NOT NULL,
                    valor_total NUMERIC(12, 2) NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            conexion.commit()
            print("Tabla clientes creada correctamente.")

        except Exception as error:
            if conexion:
                conexion.rollback()
            print("Error al crear la tabla:", error)
            raise

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar_tabla():
        conexion = None
        cursor = None

        try:
            conexion = ClienteController.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute("DROP TABLE IF EXISTS clientes;")

            conexion.commit()
            print("Tabla clientes eliminada correctamente.")

        except Exception as error:
            if conexion:
                conexion.rollback()
            print("Error al eliminar la tabla:", error)
            raise

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    @staticmethod
    def insertar(cliente: Cliente):
        conexion = None
        cursor = None

        try:
            subtotal = cliente.numero_servicios * cliente.precio_sensor
            iva = subtotal * 0.19
            valor_total = subtotal + iva

            conexion = ClienteController.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute("""
                INSERT INTO clientes (
                    nit,
                    nombre_cliente,
                    numero_servicios,
                    precio_sensor,
                    iva,
                    valor_total
                )
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                cliente.nit,
                cliente.nombre_cliente,
                cliente.numero_servicios,
                cliente.precio_sensor,
                iva,
                valor_total
            ))

            conexion.commit()
            print("Cliente insertado correctamente.")
            return True

        except Exception as error:
            if conexion:
                conexion.rollback()
            print("Error al insertar el cliente:", error)
            raise

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_cliente(nit: str):
        conexion = None
        cursor = None

        try:
            conexion = ClienteController.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute("""
                SELECT
                    nit,
                    nombre_cliente,
                    numero_servicios,
                    precio_sensor,
                    iva,
                    valor_total,
                    fecha
                FROM clientes
                WHERE nit = %s;
            """, (nit,))

            resultado = cursor.fetchone()

            if resultado:
                print("Cliente encontrado:", resultado)
                return resultado

            print("No se encontró el cliente.")
            return None

        except Exception as error:
            print("Error al buscar el cliente:", error)
            raise

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
