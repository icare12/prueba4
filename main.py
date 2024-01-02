from flask import Flask, request, render_template
import os

def crear_app():
    app = Flask(__name__)

    # Lista de tasas de comisión porcentuales adicionales
    tasas_porcentuales_adicionales = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50,
                                      0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

    # Ruta principal para mostrar el formulario de la calculadora y calcular comisiones
    @app.route('/', methods=['GET', 'POST'])
    def index():
        nombre = ''
        comisiones = {}

        if request.method == 'POST':
            nombre = request.form['nombre']
            ventas_str = request.form['ventas']

            # Verificar si el campo de ventas no está vacío
            if ventas_str:
                try:
                    ventas = int(ventas_str)

                    # Calcula la comisión para cada tasa y almacena los resultados en un diccionario
                    for tasa in tasas_porcentuales_adicionales:
                        comisiones[f"{int(tasa * 100)}%"] = round(ventas * tasa, 2)
                except ValueError:
                    # Manejar la excepción si la conversión a entero no es exitosa
                    return render_template('index.html', nombre=nombre, error="Ingrese un valor válido para las ventas.")

        return render_template('index.html', nombre=nombre, comisiones=comisiones)

    # Ruta para mostrar el formulario de la calculadora
    @app.route('/calculadora', methods=['GET', 'POST'])
    def calculadora():
        return render_template('calculadora.html')

    # Ruta para mostrar el formulario del conversor
    @app.route('/conversor', methods=['GET'])
    def conversor():
        return render_template('conversor.html')

    # Ruta para mostrar el contenido de "Empresas para Datos"
    @app.route('/empresas_para_datos', methods=['GET'])
    def empresas_para_datos():
        return render_template('empresas_para_datos.html')

    # Ruta para mostrar el contenido de la tabla
    @app.route('/tabla', methods=['GET'])
    def tabla():
        return render_template('tabla.html')

    return app

if __name__ == '__main__':
    app = crear_app()
    app.run()










