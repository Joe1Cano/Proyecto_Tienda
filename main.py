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
def destroyC(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM clientes WHERE noClientes = %s",(id))
    conn.commit()
    return redirect('/clientes')

@app.route('/productos/destroy/<int:id>')
def destroyP(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM productos WHERE noProductos = %s",(id))
    conn.commit()
    return redirect('/productos')

@app.route('/clientes/create')
def createC():
    return render_template('clientes/create.html')



@app.route('/clientes/update', methods=['POST'])
def updateC():
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

@app.route('/productos/update', methods=['POST'])
def updateP():
    _Nombre = request.form["txtNombre"]
    _Precio = request.form["txtPrecio"]
    _Cantidad = request.form["txtCantidad"]
    _noProveedor = request.form["txtProveedor"]
    _Costo = request.form["txtCosto"]
    id=request.form["txtID"]

    sql ="UPDATE productos set nombre=%s, precio=%s, cantidad=%s, noProveedor=%s, costo=%s where noProductos =%s;"
    datos=(_Nombre,_Precio,_Cantidad,_noProveedor,_Costo, id)
    
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/productos')

@app.route('/productos/create')
def createP():
    return render_template('productos/create.html')

@app.route('/clientes/edit/<int:id>')
def editC(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM clientes WHERE noClientes =%s", (id))

    clientes = cursor.fetchall()
    print(clientes)

    conn.commit()
    return render_template('clientes/edit.html', clientes=clientes)

@app.route('/productos/edit/<int:id>')
def editP(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM productos WHERE noProductos =%s", (id))

    productos = cursor.fetchall()
    print(productos)

    conn.commit()
    return render_template('productos/edit.html', productos=productos)

@app.route('/clientes/store', methods=['POST'])
def storageC():
    _nombre=request.form["txtNombre"]
    _apellido=request.form["txtApellido"]
    _correo=request.form["txtCorreo"]
    _telefono=request.form["txtTelefono"]

    if _nombre=="" or _apellido=="" or _correo =="" or _telefono =="":
        flash('Tienes que llenar todos los campos')
        return redirect(url_for("clientes/create"))

    sql ="call altaClientes(%s, %s, %s, %s);"

    datos=(_nombre,_apellido,_correo,_telefono)
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/clientes')

@app.route('/productos/store', methods=['POST'])
def storageP():
    _Nombre = request.form["txtNombre"]
    _Precio = request.form["txtPrecio"]
    _Cantidad = request.form["txtCantidad"]
    _noProveedor = request.form["txtProveedor"]
    _Costo = request.form["txtCosto"]

    if _Nombre=="" or _Precio=="" or _Cantidad =="" or _noProveedor =="" or _Costo=="":
        flash('Tienes que llenar todos los campos')
        return redirect(url_for("create"))

    sql ="INSERT INTO productos (nombre, precio, cantidad, noProveedor, costo) VALUES (%s,%s,%s,%s,%s);"

    datos=(_Nombre,_Precio,_Cantidad,_noProveedor,_Costo)
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/productos')


if __name__ == '__main__':
    app.run(debug=True)