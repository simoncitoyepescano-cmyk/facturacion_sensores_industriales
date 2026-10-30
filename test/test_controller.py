
import unittest
import psycopg2

from src.controller.cliente_controller import ClienteController


class TestClienteController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Fixture: preparar la tabla antes de las pruebas.
        ClienteController.crear_tabla()

    def setUp(self):
        # Cada prueba empieza con una tabla limpia.
        conexion = ClienteController.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM clientes;")
        conexion.commit()

        cursor.close()
        conexion.close()

    def test_crear_tabla(self):
        # Caso normal: crear una tabla que ya existe no debe fallar.
        ClienteController.crear_tabla()

        conexion = ClienteController.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT to_regclass('public.clientes');")

        resultado = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        self.assertEqual(resultado, "clientes")

    def test_eliminar_tabla(self):
        # Caso normal: eliminar la tabla.
        ClienteController.eliminar_tabla()

        conexion = ClienteController.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT to_regclass('public.clientes');")

        resultado = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        self.assertIsNone(resultado)

        # Restaurar la tabla para las demás pruebas.
        ClienteController.crear_tabla()

    def test_insertar_cliente(self):
        # Caso normal: insertar un cliente.
        cliente = Cliente(
            "TEST1001",
            "Cliente Uno",
            10,
            5000
        )

        resultado = ClienteController.insertar(cliente)

        self.assertTrue(resultado)

    def test_insertar_cinco_clientes(self):
        # Cinco casos exitosos de inserción.
        clientes = [
            Cliente("TEST2001", "Cliente Dos", 2, 1000),
            Cliente("TEST2002", "Cliente Tres", 3, 2000),
            Cliente("TEST2003", "Cliente Cuatro", 4, 3000),
            Cliente("TEST2004", "Cliente Cinco", 5, 4000),
            Cliente("TEST2005", "Cliente Seis", 6, 5000)
        ]

        for cliente in clientes:
            with self.subTest(nit=cliente.nit):
                self.assertTrue(ClienteController.insertar(cliente))

    def test_insertar_nit_duplicado(self):
        # Caso de error: no se puede repetir el NIT.
        cliente1 = Cliente(
            "TEST3001", "Cliente A", 2, 1000
        )
        cliente2 = Cliente(
            "TEST3001", "Cliente B", 3, 2000
        )

        ClienteController.insertar(cliente1)

        with self.assertRaises(psycopg2.errors.UniqueViolation):
            ClienteController.insertar(cliente2)

    def test_buscar_cliente_existente(self):
        # Caso normal: buscar un cliente registrado.
        cliente = Cliente(
            "TEST4001", "Cliente Buscado", 4, 2500
        )

        ClienteController.insertar(cliente)
        resultado = ClienteController.buscar_cliente("TEST4001")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], "TEST4001")
        self.assertEqual(resultado[1], "Cliente Buscado")

    def test_buscar_cinco_clientes(self):
        # Cinco casos exitosos de búsqueda.
        clientes = [
            Cliente("TEST5001", "Cliente Siete", 1, 1000),
            Cliente("TEST5002", "Cliente Ocho", 2, 2000),
            Cliente("TEST5003", "Cliente Nueve", 3, 3000),
            Cliente("TEST5004", "Cliente Diez", 4, 4000),
            Cliente("TEST5005", "Cliente Once", 5, 5000)
        ]

        for cliente in clientes:
            ClienteController.insertar(cliente)

        for cliente in clientes:
            with self.subTest(nit=cliente.nit):
                resultado = ClienteController.buscar_cliente(cliente.nit)
                self.assertIsNotNone(resultado)
                self.assertEqual(resultado[0], cliente.nit)

    def test_buscar_cliente_inexistente(self):
        # Caso de error funcional: el NIT no está registrado.
        resultado = ClienteController.buscar_cliente("NO_EXISTE")
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
