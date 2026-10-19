import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
import secret_config

from model import facturacion_sensores


class FacturasController:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
            database="tarjetas_mgl4",
            user="cesar",
            password="f1I69LSQroX9NY7qQpufKIF48pkGwCRG",
            host="dpg-daps0sjtqb8s73djd10g-a.virginia-postgres.render.com",
            port=5432
        )

    @staticmethod
    def insertar(numero_factura: str, nit: str, cliente: str,
                 n_servicios: int, precio_unitario: float):

        # Calculamos el total utilizando el modelo del proyecto
        valor_total = facturacion_sensores.calcular_valor_factura(
            n_servicios, precio_unitario
        )

        # Calculamos el IVA del 19 %
        iva = n_servicios * precio_unitario * 0.19

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

        except Exception:
            conexion.rollback()
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
                       n_servicios, precio_unitario, iva,
                       valor_total, fecha
                FROM public.facturas
                WHERE numero_factura = %s
            """

            cursor.execute(consulta, (numero_factura,))
            factura = cursor.fetchone()

            return factura

        finally:
            cursor.close()
            conexion.close()
