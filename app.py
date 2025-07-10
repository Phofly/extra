from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

CSV_FILE = 'facturas.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extra1', methods=['POST'])
def guardar_datos():
    datos = {
        'nombre': request.form['nombre'],
        'correo': request.form['correo'],
        'telefono': request.form['telefono'],
        'rfc': request.form['rfc'],
        'folio': request.form['folio'],
        'forma_pago': request.form['forma_pago'],
        'fecha_consumo': request.form['fecha_consumo'],
        'importe_consumo': request.form['importe_consumo'],
        'calle': request.form['calle'],
        'colonia': request.form['colonia'],
        'localidad': request.form['localidad'],
        'municipio': request.form['municipio'],
        'estado': request.form['estado'],
        'codigo_postal': request.form['codigo_postal'],
        'regimen_fiscal': request.form['regimen_fiscal'],
        'uso_cfdi': request.form['uso_cfdi']
    }

    archivo_existe = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as archivo:
        campos = list(datos.keys())
        writer = csv.DictWriter(archivo, fieldnames=campos)
        if not archivo_existe:
            writer.writeheader()
        writer.writerow(datos)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)