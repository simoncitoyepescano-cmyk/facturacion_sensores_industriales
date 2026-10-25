from flask import Flask
from src.model import logica_sensores

app = Flask(__name__)

nit = input("Ingrese el NIT del cliente: ")
nombre = input("Ingrese el nombre del cliente: ")
numero_servicios = int(input("Ingrese el número de servicios que posee el cliente: "))
precio_sensor = float(input("Ingrese el precio de cada sensor: "))

@app.route('/cliente')
def cliente():
    cliente = logica_sensores.Cliente(nit,nombre,numero_servicios,precio_sensor)

    return f"Cliente Creado: Nit: {cliente.nit} - Nombre: {cliente.nombre_cliente}"

@app.route('/valorfactura')
def calcular_valor_factura():
    valor_factura = logica_sensores.calcular_valor_factura(numero_servicios,precio_sensor)

    return f"El valor de la factura de {nombre} fue de {valor_factura}"

if __name__=='__main__':
    app.run(debug=True)