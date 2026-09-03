from flask import Flask, render_template, request

app = Flask(__name__)

USUARIOS = {
    "admin": "1234",
    "daniel": "flask2026"
}

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nit = request.form['nit']
        correo = request.form['correo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        return render_template('clientes_confirmacion.html',
                                nombre=nombre, nit=nit, correo=correo,
                                telefono=telefono, direccion=direccion)
    else:
        return render_template('clientes.html')

if __name__ == '__main__':
    app.run(debug=True)