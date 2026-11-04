from flask import Blueprint, render_template, request

from src.model import logica_sensores
from src.controller.cliente_controller import ClienteController

blueprint = Blueprint( "vista_clientes", __name__, "templates" )


# Mostrar el formulario HTML
@blueprint.route('/')
def inicio():
    return render_template("crear_cliente.html")



# Recibir los datos y guardar el cliente
@blueprint.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():

    nit = request.form["nit"]
    nombre = request.form["nombre_cliente"]
    numero_servicios = int(request.form["numero_servicios"])
    precio_sensor = float(request.form["precio_sensor"])

    # Crear un cliente
    cliente = logica_sensores.Cliente(
        nit,
        nombre,
        numero_servicios,
        precio_sensor
    )

    # Guardar el cliente en PostgreSQL
    ClienteController.insertar(cliente)

    return f"Cliente guardado exitosamente: {cliente.nombre_cliente}"

# Buscar cliente
@blueprint.route('/buscarcliente')

# Calcular el valor de la factura
@blueprint.route('/valorfactura')
def calcular_valor_factura():

    numero_servicios = int(request.args["numero_servicios"])
    precio_sensor = float(request.args["precio_sensor"])
    nombre = request.args["nombre_cliente"]

    valor_factura = logica_sensores.calcular_valor_factura(
        numero_servicios,
        precio_sensor
    )

    return f"El valor de la factura de {nombre} fue de {valor_factura}"

@blueprint.route('/formulario_buscar_cliente')
def formulario_buscar_cliente():
    return render_template("buscar_cliente.html")

# Buscar un cliente por su NIT
@blueprint.route('/buscar_cliente', methods=['GET'])
def buscar_cliente():

    nit = request.args["nit"]

    cliente = ClienteController.buscar_cliente(nit)

    return render_template("buscar_cliente.html", cliente=cliente)

@blueprint.route('/crear_tablas', methods=['POST'])
def crear_tablas():

    try:
        clienteController.crear_tabla()

        mensaje = "Tabla de clientes creada exitosamente."

    except psycopg2.errors.DuplicateTable:
        mensaje = "La tabla de clientes ya existe."

    except Exception as e:
        mensaje = f"Error al crear la tabla: {e}"

    return render_template("crear_cliente.html", mensaje=mensaje)

@blueprint.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    nit = request.form["nit"]

    eliminado = ClienteController.eliminar_cliente(nit)

    if eliminado:
        mensaje = "Cliente eliminado correctamente."
    else:
        mensaje = "No existe un cliente con ese NIT."

    return render_template(
        "crear_cliente.html",
        mensaje=mensaje
    )


if __name__ == '__main__':
    blueprint.run(debug=True)