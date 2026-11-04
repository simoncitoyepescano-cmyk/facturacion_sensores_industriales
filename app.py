from flask import Flask, render_template, request

from src.model import logica_sensores
from src.controller.cliente_controller import ClienteController

app = Flask(__name__)


# Mostrar el formulario HTML
@app.route('/')
def inicio():
    return render_template("crear_cliente.html")

@app.route('/crear_tablas')
def crear_tablas():
    ClienteController.crear_tabla()
    return "Tablas creadas exitosamente"


# Recibir los datos y guardar el cliente
@app.route('/guardar_cliente', methods=['POST'])
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
@app.route('/buscarcliente')

# Calcular el valor de la factura
@app.route('/valorfactura')
def calcular_valor_factura():

    numero_servicios = int(request.args["numero_servicios"])
    precio_sensor = float(request.args["precio_sensor"])
    nombre = request.args["nombre_cliente"]

    valor_factura = logica_sensores.calcular_valor_factura(
        numero_servicios,
        precio_sensor
    )

    return f"El valor de la factura de {nombre} fue de {valor_factura}"

@app.route('/formulario_buscar_cliente')
def formulario_buscar_cliente():
    return render_template("buscar_cliente.html")

# Buscar un cliente por su NIT
@app.route('/buscar_cliente', methods=['GET'])
def buscar_cliente():

    nit = request.args["nit"]

    cliente = ClienteController.buscar_cliente(nit)

    return render_template("buscar_cliente.html", cliente=cliente)

@app.route('/crear_tablas', methods=['POST'])
def crear_tablas():
    ClienteController.crear_tabla()
    return redirect('/')


@app.route('/eliminar_cliente', methods=['POST'])
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
    app.run(debug=True)




