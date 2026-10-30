
from src.controller import ClienteController
from src.model.logica_sensores import Cliente


def crear_cliente():
    print("\n--- REGISTRAR CLIENTE ---")

    try:
        nit = input("Ingrese el NIT del cliente: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        numero_servicios = int(input("Ingrese el número de servicios: "))
        precio_sensor = float(input("Ingrese el precio de cada sensor: "))

        cliente = Cliente(
            nit,
            nombre_cliente,
            numero_servicios,
            precio_sensor
        )

        ClienteController.insertar(cliente)

        print("\nCliente registrado correctamente.")

    except ValueError:
        print("Error: ingrese números válidos para los servicios y el precio.")

    except Exception as error:
        print(f"No fue posible registrar el cliente: {error}")


def buscar_cliente():
    print("\n--- BUSCAR CLIENTE ---")

    nit = input("Ingrese el NIT del cliente que desea buscar: ")

    try:
        resultado = ClienteController.buscar_cliente(nit)

        if resultado is not None:
            print("\n--- DATOS DEL CLIENTE ---")
            print(f"NIT: {resultado[0]}")
            print(f"Nombre: {resultado[1]}")
            print(f"Número de servicios: {resultado[2]}")
            print(f"Precio por sensor: ${resultado[3]}")
            print(f"IVA: ${resultado[4]}")
            print(f"Valor total: ${resultado[5]}")
            print(f"Fecha de registro: {resultado[6]}")

    except Exception as error:
        print(f"No fue posible buscar el cliente: {error}")


def menu():
    while True:
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1. Crear tabla")
        print("2. Registrar cliente")
        print("3. Buscar cliente")
        print("4. Eliminar tabla")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ClienteController.crear_tabla()

        elif opcion == "2":
            crear_cliente()

        elif opcion == "3":
            buscar_cliente()

        elif opcion == "4":
            confirmar = input(
                "¿Seguro que desea eliminar TODA la tabla? (s/n): "
            )

            if confirmar.lower() == "s":
                ClienteController.eliminar_tabla()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
