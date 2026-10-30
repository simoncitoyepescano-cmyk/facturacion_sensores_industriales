from flask import Flask, render_template, request

from src.model import logica_sensores
from src.controller.cliente_controller import ClienteController

app = Flask(__name__)


# Mostrar el formulario HTML
@app.route('/')
def inicio():
    return render_template("nuevo_cliente.html")


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


if __name__ == '__main__':
    app.run(debug=True)
