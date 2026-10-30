# 🧾 Sistema de Facturación de Sensores

## 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema para calcular y gestionar la facturación de servicios de sensores de una empresa.

El proyecto fue desarrollado tomando como base **facturas reales proporcionadas por la empresa**, utilizando principalmente el número de servicios y el valor unitario registrados en ellas para comprobar que los resultados obtenidos por el programa fueran correctos.

Además, el sistema permite registrar y consultar la información de los clientes mediante una base de datos PostgreSQL.

La aplicación está desarrollada en Python siguiendo el patrón **MVC (Modelo-Vista-Controlador)**, separando la lógica de facturación, las operaciones con la base de datos y la interacción con el usuario.

En el repositorio también se encuentra un **audio en el que se explica el proceso de facturación por sensores de la empresa**, permitiendo conocer el contexto del proceso que se está representando mediante el programa.

---

## 🎯 Objetivo

El objetivo principal es desarrollar un sistema que permita calcular correctamente el valor total a pagar por los servicios de sensores, teniendo en cuenta la cantidad de servicios, el valor unitario y el IVA correspondiente.

También se busca almacenar la información de los clientes en una base de datos PostgreSQL, permitiendo registrar nuevos clientes y consultar su información mediante el NIT.

El funcionamiento del programa se comprueba mediante **pruebas unitarias**, incluyendo pruebas basadas en facturas reales, casos de error y casos extraordinarios.

---

## ⚙️ Funcionamiento

El programa recibe los siguientes datos de entrada:

* 🪪 **NIT:** identificación del cliente.
* 👤 **Nombre del cliente:** nombre o razón social.
* 🔢 **Número de servicios:** cantidad de servicios o sensores que se deben facturar.
* 💰 **Precio unitario:** valor correspondiente a cada servicio.

El sistema calcula automáticamente el IVA del **19 %** y lo agrega al valor de los servicios.

### 🧮 Operación

**Subtotal = Número de servicios × Precio unitario**

**IVA = Subtotal × 19 %**

**Valor a pagar = Subtotal + IVA**

---

## 📥 Valores de entrada

| Entrada | Descripción |
|---|---|
| 🪪 **NIT** | Identificación del cliente. |
| 👤 **Nombre del cliente** | Nombre o razón social del cliente. |
| 🔢 **Número de servicios** | Cantidad de servicios de sensores que se deben facturar. |
| 💰 **Valor unitario** | Valor correspondiente a cada servicio. |

---

## 📤 Valor de salida

| Salida | Descripción |
|---|---|
| 💵 **Subtotal** | Valor de los servicios antes de IVA. |
| 🧾 **IVA** | Impuesto calculado sobre el subtotal, correspondiente al 19 %. |
| 💰 **Valor a pagar** | Valor total de los servicios incluyendo el IVA. |

---

## 🧾 IVA

Para el proceso de facturación analizado en este proyecto se utiliza un **IVA fijo del 19 %**.

El IVA es calculado automáticamente por el programa a partir del valor obtenido de multiplicar el número de servicios por el valor unitario.

---

## 🧪 Pruebas unitarias de la lógica de facturación

Las pruebas fueron desarrolladas utilizando **Python y la librería `unittest`**.

Una parte importante de las pruebas se realizó utilizando información obtenida de **facturas reales de la empresa**. Estas contienen diferentes cantidades de servicios y valores unitarios, permitiendo comprobar que el programa genere los valores esperados.

Entre las facturas utilizadas para las pruebas se encuentran registros de diferentes clientes como:

* Gamma
* Corlanc
* Locería
* Enka
* Cryogas
* Suministros de Colombia S.A.S.
* Materiales y Pinturas Sabaneta
* Moldes Itagüí
* Calcinación

El objetivo es verificar que los resultados calculados por el programa coincidan con los valores esperados de las facturas.

---

## ❌ Casos de error de la lógica de facturación

Además de las pruebas realizadas con las facturas, se desarrollaron **4 casos de error** para comprobar el comportamiento del sistema cuando se ingresan datos inválidos.

Los casos son:

### 🔴 Error 1 — Número de servicios igual a 0

Se comprueba que el sistema no permita realizar una facturación cuando la cantidad de servicios es igual a `0`.

### 🔴 Error 2 — Valor unitario igual a 0

Se comprueba que el sistema no permita utilizar un valor unitario igual a `0`.

### 🔴 Error 3 — Número de servicios negativo

Se comprueba que el sistema rechace una cantidad negativa de servicios, ya que no es posible facturar una cantidad negativa.

### 🔴 Error 4 — Valor unitario negativo

Se comprueba que el sistema rechace un valor unitario negativo, ya que un servicio no puede tener un precio negativo.

Estos casos permiten comprobar que el programa no solamente realice operaciones matemáticas, sino que también tenga en cuenta la **validación de los datos de entrada**.

---

## 🟣 Casos de prueba extraordinarios

También se realizaron **3 casos de prueba extraordinarios**. Estos casos no representan errores, sino situaciones diferentes a los valores utilizados normalmente en las facturas.

### 🟣 Extraordinario 1 — Gran cantidad de servicios

Se prueba el funcionamiento del programa utilizando **100 servicios** con un valor unitario de **$1.000**.

El objetivo es comprobar que el sistema pueda trabajar correctamente con una cantidad de servicios mucho mayor a las utilizadas en las facturas de referencia.

### 🟣 Extraordinario 2 — Valor unitario con decimales

Se prueba el sistema utilizando **2 servicios** con un valor unitario de **$1.250,50**.

Este caso permite comprobar que el programa pueda trabajar correctamente con valores unitarios que contienen decimales.

### 🟣 Extraordinario 3 — Valor unitario muy alto

Se prueba el sistema utilizando **1 servicio** con un valor unitario de **$10.000.000**.

El objetivo es comprobar que la función pueda manejar correctamente valores unitarios considerablemente superiores a los utilizados en las facturas de referencia.

### 📊 Resumen de pruebas especiales

| Tipo | Caso | Objetivo |
|---|---|---|
| 🔴 Error | Servicios = `0` | Validar cantidad de servicios. |
| 🔴 Error | Precio = `0` | Validar valor unitario. |
| 🔴 Error | Servicios negativos | Rechazar cantidades inválidas. |
| 🔴 Error | Precio negativo | Rechazar valores inválidos. |
| 🟣 Extraordinario | 100 servicios | Probar una cantidad elevada. |
| 🟣 Extraordinario | Precio decimal | Probar valores con decimales. |
| 🟣 Extraordinario | Precio de $10.000.000 | Probar un valor unitario elevado. |

---

## 🗄️ Base de datos PostgreSQL

El proyecto incorpora una base de datos PostgreSQL para almacenar la información de los clientes y permitir su consulta.

La conexión entre Python y PostgreSQL se realiza mediante la librería **`psycopg2`**.

Los datos de conexión se configuran en el archivo `secret_config.py`, que contiene la información necesaria para establecer la conexión con la base de datos.

### 📋 Tabla clientes

El sistema utiliza una tabla llamada `clientes`, encargada de almacenar la información de los clientes registrados.

La tabla contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| `id_cliente` | Identificador único del registro. |
| `nit` | Identificación del cliente. |
| `nombre_cliente` | Nombre del cliente. |
| `numero_servicios` | Cantidad de servicios contratados. |
| `precio_sensor` | Precio unitario de cada sensor. |
| `iva` | Valor del IVA calculado. |
| `valor_total` | Valor total incluyendo IVA. |
| `fecha` | Fecha de registro del cliente. |

El campo `nit` tiene una restricción de valor único para evitar registrar dos clientes con el mismo NIT.

### ⚙️ Operaciones de la base de datos

El controlador permite realizar las siguientes operaciones:

* **CREATE TABLE:** crear la tabla `clientes`.
* **DROP TABLE:** eliminar la tabla `clientes`.
* **INSERT INTO:** insertar los datos de un cliente.
* **SELECT:** consultar la información de un cliente mediante su NIT.

---

## 🧠 Modelo

El modelo contiene la clase `Cliente`, encargada de representar la información de cada cliente.

La clase se encuentra en:

`src/model/logica_sensores.py`

Sus atributos son:

* `nit`
* `nombre_cliente`
* `numero_servicios`
* `precio_sensor`

También contiene la lógica principal encargada de calcular el valor de la factura y realizar las validaciones de los datos de entrada.

La separación de esta lógica permite reutilizar los cálculos y mantener organizado el proyecto.

---

## 🎮 Controlador

El controlador se encuentra en:

`src/controller/__init__.py`

Contiene la clase `ClienteController`, encargada de conectar el programa con PostgreSQL y ejecutar las operaciones sobre la tabla de clientes.

Sus principales métodos son:

| Método | Función |
|---|---|
| `obtener_conexion()` | Establece la conexión con PostgreSQL. |
| `crear_tabla()` | Crea la tabla `clientes` si no existe. |
| `eliminar_tabla()` | Elimina la tabla `clientes`. |
| `insertar(cliente)` | Registra un cliente en la base de datos. |
| `buscar_cliente(nit)` | Busca un cliente mediante su NIT. |

### 📝 Inserción de clientes

El método `insertar()` recibe un objeto de la clase `Cliente`.

A partir de sus atributos calcula el subtotal, el IVA del 19 % y el valor total.

Posteriormente, ejecuta una consulta SQL `INSERT INTO` para almacenar la información del cliente en PostgreSQL.

### 🔎 Búsqueda de clientes

El método `buscar_cliente()` recibe el NIT como parámetro y ejecuta una consulta SQL `SELECT` para encontrar el registro correspondiente.

Si el cliente existe, devuelve su información. Si no se encuentra, devuelve `None`.

---

## 🧪 Pruebas unitarias del controlador y la base de datos

Además de las pruebas de la lógica de facturación, el proyecto cuenta con pruebas unitarias para verificar las operaciones realizadas por el controlador sobre PostgreSQL.

Estas pruebas utilizan **`unittest`** y se encuentran en:

`test/test_cliente.py`

Se utiliza un fixture para preparar la tabla de clientes antes de ejecutar las pruebas.

Las pruebas permiten comprobar:

* La creación de la tabla.
* La eliminación de la tabla.
* La inserción de clientes.
* La búsqueda de clientes por NIT.
* El manejo de errores durante las operaciones de la base de datos.

### 📊 Casos de prueba del controlador

| Operación | Caso | Resultado esperado |
|---|---|---|
| Crear tabla | La tabla no existe | La tabla se crea correctamente. |
| Crear tabla | La tabla ya existe | La operación no genera error. |
| Eliminar tabla | La tabla existe | La tabla se elimina correctamente. |
| Insertar | Datos correctos | El cliente se registra. |
| Insertar | NIT duplicado | Se genera un error por la restricción de unicidad. |
| Buscar | NIT existente | Se devuelve la información del cliente. |
| Buscar | NIT inexistente | Se devuelve `None`. |

También se incluyen cinco casos exitosos de inserción y cinco búsquedas exitosas para comprobar el funcionamiento de estas operaciones con diferentes clientes.

Las pruebas de la base de datos deben ejecutarse utilizando una base de datos destinada a pruebas, ya que algunas operaciones eliminan y vuelven a crear la tabla.

---

## 🎧 Explicación del proceso

Dentro del repositorio se encuentra un **audio relacionado con el proyecto**.

En este audio se explica el **proceso de facturación por sensores de la empresa**, proporcionando el contexto necesario para comprender cómo funciona el servicio y de dónde provienen los datos utilizados para realizar las pruebas.

El audio complementa la información presentada en el código, las facturas y las pruebas unitarias.

---

# 📂 Estructura del repositorio

El proyecto está organizado dentro de la carpeta principal `FACTURACION_S`, donde se encuentran los archivos de documentación, la información utilizada como referencia y el código fuente del sistema.

```text
FACTURACION_S/
│
├── README.md
├── requirements.txt
├── secret_config_sample.py
├── secret_config.py
├── probar_conexion.py
│
├── Audio
│   └── Explicación del proceso de facturación por sensores
│
├── Archivo de Excel
│   └── Información de facturas, casos de error y pruebas
│
├── src/
│   │
│   ├── controller/
│   │   └── __init__.py
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   └── logica_sensores.py
│   │
│   └── view_console/
│       └── crear_cliente.py
│
└── test/
    ├── __init__.py
    └── test_cliente.py
```

## 📄 README.md

Contiene la documentación general del proyecto, incluyendo:

* Descripción del sistema.
* Objetivo.
* Funcionamiento.
* Valores de entrada y salida.
* Cálculo del IVA.
* Información de la base de datos.
* Modelo y controlador.
* Pruebas realizadas.
* Casos de error.
* Casos extraordinarios.
* Estructura del proyecto.
* Instrucciones de instalación y ejecución.
* Información de los autores.

## 🎧 Audio

Contiene la explicación del proceso de facturación por sensores de la empresa.

El audio permite comprender el proceso real que sirvió como base para desarrollar el sistema y realizar las diferentes pruebas.

## 📊 Archivo de Excel

Contiene la información utilizada como referencia para el desarrollo del proyecto, incluyendo los datos obtenidos de las facturas de la empresa, así como la información de los casos de error y casos de prueba.

## 🧠 model

Contiene la lógica principal del sistema.

* `__init__.py` → Permite identificar la carpeta como un paquete de Python.
* `logica_sensores.py` → Contiene la clase `Cliente`, la función encargada de realizar el cálculo de la facturación y las validaciones de los datos de entrada.

## 🎮 controller

Contiene el controlador encargado de gestionar las operaciones con la base de datos PostgreSQL.

* `__init__.py` → Contiene la clase `ClienteController`, encargada de establecer la conexión con PostgreSQL, crear y eliminar la tabla, insertar clientes y buscar información mediante el NIT.

## 🧪 test

Contiene las pruebas unitarias del proyecto.

* `__init__.py` → Permite identificar la carpeta como un paquete de Python.
* `test_cliente.py` → Contiene las pruebas de las operaciones del controlador, incluyendo creación y eliminación de la tabla, inserción de clientes, búsqueda de clientes y casos de error.
* Las pruebas de la lógica de facturación también comprueban las facturas reales, los 4 casos de error y los 3 casos extraordinarios.

## 🖥️ view_console

Contiene la parte encargada de la interacción con el usuario mediante la terminal.

* `crear_cliente.py` → Permite registrar clientes, buscar clientes mediante el NIT, crear la tabla y ejecutar las opciones disponibles en el menú.

## ⚙️ Configuración

* `requirements.txt` → Contiene las dependencias necesarias para ejecutar el proyecto.
* `secret_config_sample.py` → Archivo de ejemplo que muestra los datos de conexión que se deben configurar.
* `secret_config.py` → Contiene los datos reales de conexión a PostgreSQL. Este archivo es privado y no debe subirse al repositorio.
* `probar_conexion.py` → Archivo utilizado para comprobar la conexión y el funcionamiento de las operaciones de la base de datos.

---

## 🔗 Organización general

La estructura del proyecto permite separar claramente cada responsabilidad:

**📊 Información → 🧠 Model → 🎮 Controller → 🖥️ View → 🧪 Test**

De esta manera:

* 📊 **Excel:** proporciona la información de referencia.
* 🧠 **Model:** representa los clientes y realiza los cálculos y validaciones.
* 🎮 **Controller:** conecta el programa con PostgreSQL y administra los datos.
* 🖥️ **View:** permite la interacción mediante consola.
* 🧪 **Test:** comprueba que el sistema funcione correctamente.
* 🎧 **Audio:** explica el proceso real de facturación.
* 📄 **README:** documenta todo el proyecto.

---

## 🚀 Futuras implementaciones

Como futura mejora del proyecto, se busca implementar los **meses del servicio como una variable de entrada**.

Actualmente, los datos utilizados fueron establecidos principalmente con base en las **facturas reales proporcionadas por la empresa**. Por esta razón, el número de meses no se maneja actualmente como una entrada independiente y el sistema está limitado a las situaciones representadas en las facturas utilizadas.

Al implementar los meses como una variable de entrada, el programa podría adaptarse de una manera más flexible a diferentes periodos de facturación.

### 🔮 Posibles mejoras

* 📅 Permitir ingresar la cantidad de meses del servicio.
* 🔄 Adaptar el cálculo a diferentes periodos de facturación.
* 🧮 Realizar cálculos más dinámicos.
* 📈 Aumentar la variedad de casos de prueba.
* ⚙️ Representar de una manera más completa el proceso real de facturación de la empresa.

---

## 💻 Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| 🐍 **Python** | Desarrollo del programa. |
| 🐘 **PostgreSQL** | Almacenamiento de información de clientes. |
| 🔌 **psycopg2** | Conexión entre Python y PostgreSQL. |
| 🧪 **unittest** | Creación y ejecución de pruebas unitarias. |
| 🐙 **GitHub** | Almacenamiento y gestión del proyecto. |

---

## 📚 Metodología

El proyecto se desarrolló siguiendo el siguiente proceso:

**Facturas reales → Identificación de datos → Desarrollo de la función → Pruebas con facturas → Casos de error → Casos extraordinarios → Diseño del modelo → Conexión a PostgreSQL → Desarrollo del controlador → Interfaz de usuario → Pruebas unitarias**

De esta manera, el proyecto combina información real de la empresa con pruebas diseñadas para comprobar diferentes comportamientos del sistema.

---

# ▶️ Ejecución del proyecto y pruebas

Para ejecutar el proyecto y comprobar el funcionamiento de las pruebas, otra persona puede descargar o clonar el repositorio y seguir los siguientes pasos.

## 1️⃣ Clonar el repositorio

Desde una terminal se debe ejecutar:

```bash
git clone URL_DEL_REPOSITORIO
```

Luego ingresar a la carpeta del proyecto:

```bash
cd FACTURACION_S
```

## 2️⃣ Instalar dependencias

El proyecto utiliza **Python 3**, PostgreSQL y la librería `psycopg2`.

Desde la carpeta `FACTURACION_S` se debe ejecutar:

```bash
pip install -r requirements.txt
```

Si no se cuenta con el archivo de dependencias configurado, se puede instalar `psycopg2` mediante:

```bash
pip install psycopg2
```

## 3️⃣ Configurar la conexión a PostgreSQL

Asegúrese de tener una base de datos PostgreSQL creada y sus respectivos datos de acceso.

Copie el archivo `secret_config_sample.py` como `secret_config.py` y establezca en este archivo los datos de conexión a su base de datos.

El archivo debe contener los siguientes datos:

```python
database = "nombre_base_datos"
user = "usuario"
password = "contraseña"
host = "host"
port = "puerto"
```

Los valores anteriores son ejemplos de configuración. Deben reemplazarse por los datos reales de conexión.

El archivo `secret_config.py` contiene información privada y no debe subirse al repositorio público.

## 4️⃣ Verificar la estructura del proyecto

Dentro de `FACTURACION_S` se encontrará la carpeta `src`, que contiene el modelo, el controlador y la interfaz de consola.

También se encuentra la carpeta `test`, que contiene las pruebas unitarias.

## 5️⃣ Ejecutar las pruebas unitarias

Las pruebas del controlador se encuentran dentro de:

`test/test_cliente.py`

Para ejecutarlas desde la terminal, ubicándose en la carpeta `FACTURACION_S`, se debe utilizar:

```bash
python -m unittest discover -s test -v
```

Este comando busca automáticamente las pruebas dentro de la carpeta `test` y las ejecuta.

Las pruebas incluyen:

* Creación de la tabla.
* Eliminación de la tabla.
* Inserción de clientes.
* Búsqueda de clientes.
* Casos de error.
* Cinco casos exitosos de inserción.
* Cinco casos exitosos de búsqueda.

**Importante:** las pruebas de base de datos deben ejecutarse sobre una base de datos destinada a pruebas, ya que el fixture prepara y limpia la tabla `clientes` antes de cada prueba.

## 6️⃣ Resultado esperado

Al ejecutar las pruebas, el programa mostrará en la terminal el resultado de las pruebas realizadas.

Si todas las pruebas funcionan correctamente, se mostrará un resultado indicando que las pruebas fueron ejecutadas satisfactoriamente.

---

## 🖥️ Ejecución de la interfaz de consola

El proyecto cuenta con una interfaz de usuario por consola que permite registrar clientes y consultar su información almacenada en PostgreSQL.

La interfaz se encuentra en:

```text
FACTURACION_S/
└── src/
    └── view_console/
        └── crear_cliente.py
```

### ▶️ Pasos para ejecutar la interfaz de consola

#### 1. Abrir una terminal

Ubícate en la carpeta principal del proyecto:

```bash
cd FACTURACION_S
```

#### 2. Ejecutar la consola

Ejecuta el siguiente comando:

```bash
python -m src.view_console.crear_cliente
```

#### 3. Seleccionar una opción

Al iniciar el programa aparecerá el siguiente menú:

```text
===== SISTEMA DE CLIENTES =====

1. Crear tabla
2. Registrar cliente
3. Buscar cliente
4. Eliminar tabla
5. Salir

Seleccione una opción:
```

#### 4. Crear la tabla

Selecciona la opción:

```text
1
```

El programa ejecutará la operación de creación de la tabla `clientes` en PostgreSQL.

#### 5. Registrar un cliente

Selecciona la opción:

```text
2
```

La consola solicitará los siguientes datos:

* NIT del cliente.
* Nombre del cliente.
* Número de servicios.
* Precio de cada sensor.

Con estos datos se crea un objeto de la clase `Cliente` y se envía al controlador para almacenar la información en PostgreSQL.

#### 6. Buscar un cliente

Selecciona la opción:

```text
3
```

El programa solicitará el NIT del cliente que se desea consultar.

Si el cliente se encuentra registrado, se mostrará su información:

* NIT.
* Nombre del cliente.
* Número de servicios.
* Precio por sensor.
* IVA.
* Valor total.
* Fecha de registro.

Si el cliente no existe, el sistema mostrará un mensaje indicando que no se encontró el registro.

#### 7. Eliminar la tabla

Selecciona la opción:

```text
4
```

El sistema solicitará una confirmación antes de ejecutar la eliminación de la tabla.

**Advertencia:** esta opción elimina la tabla completa `clientes` y todos los registros almacenados en ella.

#### 8. Salir del programa

Selecciona:

```text
5
```

El programa finalizará su ejecución.

### 🔄 Flujo de interacción

El funcionamiento de la interfaz puede resumirse de la siguiente manera:

**👤 Datos del cliente → 🧠 Objeto Cliente → 🎮 Controlador → 🐘 PostgreSQL → 🔎 Consulta → 📋 Resultado**

La interfaz permite que el usuario interactúe directamente con el sistema mediante la consola y gestione la información de los clientes almacenada en la base de datos.

---

## 🖼️ Ejecución de la interfaz gráfica (GUI)

En la versión original del proyecto se contemplaba una interfaz gráfica de usuario (GUI) construida con la librería **Kivy**, que permite ingresar los datos del cliente y calcular la factura mediante campos de texto y botones.

La interfaz gráfica se encontraba en:

```text
FACTURACION_S/
└── src/
    └── view/
        └── gui/
            └── facturacion_sensores.py
```

Si este módulo continúa incluido en la versión actual del repositorio, se puede ejecutar desde la carpeta principal mediante:

```bash
python src/view/gui/facturacion_sensores.py
```

Para utilizar esta interfaz es necesario tener instalada la librería Kivy:

```bash
pip install kivy
```

La interfaz original permite:

1. Ingresar el nombre del cliente.
2. Ingresar el número de servicios o sensores.
3. Ingresar el precio unitario por sensor.
4. Presionar **Calcular factura** para visualizar el subtotal, el IVA (19 %) y el valor total a pagar.
5. Presionar **Limpiar** para reiniciar el formulario.

Si algún dato es inválido (vacío, no numérico, cero o negativo), la GUI muestra un mensaje de error amigable.

---

## 👥 Autores

**Simon Yepes Cano**

**Cesar Junior Ramirez**

---

## 📌 Conclusión

El proyecto permite representar de manera sencilla el proceso de **facturación de servicios de sensores de una empresa**, utilizando como referencia información obtenida de facturas reales.

Las pruebas unitarias permiten comprobar que los cálculos realizados por el programa sean correctos, mientras que los **4 casos de error** permiten validar el comportamiento del sistema frente a datos inválidos.

Por otra parte, los **3 casos extraordinarios** permiten comprobar que el programa también pueda trabajar correctamente con situaciones diferentes a las encontradas normalmente en las facturas.

La incorporación de PostgreSQL permite almacenar y consultar la información de los clientes, mientras que el patrón MVC facilita la separación de responsabilidades entre el modelo, el controlador y la interfaz.

Como futura mejora, se plantea incorporar los **meses del servicio como una variable de entrada**, haciendo que el sistema sea más flexible y pueda adaptarse a diferentes periodos de facturación.

https://facturacion-sensores-industriales.onrender.com/

