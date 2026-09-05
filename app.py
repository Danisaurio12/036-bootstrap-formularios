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

@app.route('/proveedores', methods=['GET', 'POST'])
def proveedores():
    if request.method == 'POST':
        empresa = request.form['empresa']
        contacto = request.form['contacto']
        nit = request.form['nit']
        tipo_producto = request.form['tipo_producto']
        condicion_pago = request.form['condicion_pago']
        activo = 'Si' if request.form.get('activo') else 'No'
        return render_template('proveedores_confirmacion.html',
                                empresa=empresa, contacto=contacto, nit=nit,
                                tipo_producto=tipo_producto, condicion_pago=condicion_pago,
                                activo=activo)
    else:
        return render_template('proveedores.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        exito = usuario in USUARIOS and USUARIOS[usuario] == password
        return render_template('login_resultado.html', exito=exito, usuario=usuario)
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)