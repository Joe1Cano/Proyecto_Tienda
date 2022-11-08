from flask import Flask
from flask import render_template, request, redirect, flash, url_for
from flaskext.mysql import MySQL    


app= Flask(__name__)
app.secret_key="Develoteca  "

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'tienda'
mysql.init_app(app)

@app.route("/")
def index():
    return render_template("main/index.html")

@app.route("/productos")
def indexP():
    sql ="Select * from productos;"
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql)

    productos = cursor.fetchall()
    print(productos)

    conn.commit()
    return render_template("productos/index.html", productos=productos )


@app.route("/clientes")
def indexC():
    sql ="Select * from clientes;"
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql)

    clientes = cursor.fetchall()
    print(clientes)

    conn.commit()
    return render_template("clientes/index.html", clientes=clientes )

@app.route('/clientes/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM clientes WHERE noClientes = %s",(id))
    conn.commit()
    return redirect('/clientes')

@app.route('/clientes/create')
def create():
    return render_template('clientes/create.html')

@app.route('/clientes/update', methods=['POST'])
def update():
    _nombre=request.form["txtNombre"]
    _apellido=request.form["txtApellido"]
    _correo=request.form["txtCorreo"]
    _telefono=request.form["txtTelefono"]
    id=request.form["txtID"]

    sql ="UPDATE clientes set nombre=%s, apellido=%s, telefono=%s, correo=%s WHERE noClienteS=%s;"
    datos=(_nombre, _apellido, _telefono, _correo, id)
    
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/clientes')

@app.route('/clientes/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM clientes WHERE noClientes =%s", (id))

    clientes = cursor.fetchall()
    print(clientes)

    conn.commit()
    return render_template('clientes/edit.html', clientes=clientes)

@app.route('/clientes/store', methods=['POST'])
def storage():
    _nombre=request.form["txtNombre"]
    _apellido=request.form["txtApellido"]
    _correo=request.form["txtCorreo"]
    _telefono=request.form["txtTelefono"]

    if _nombre=="" or _apellido=="" or _correo =="" or _telefono =="":
        flash('Tienes que llenar todos los campos')
        return redirect(url_for("create"))

    sql ="call altaClientes(%s, %s, %s, %s);"

    datos=(_nombre,_apellido,_correo,_telefono)
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/clientes')


if __name__ == '__main__':
    app.run(debug=True)