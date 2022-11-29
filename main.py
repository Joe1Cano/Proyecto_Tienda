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

@app.route("/movimientos")
def indexM():
    sql ="call mostrarmovProductos();"
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql)

    movimientos = cursor.fetchall()
    print(movimientos)

    conn.commit()
    return render_template("movimientos/index.html", movimientos=movimientos )

@app.route("/ventas")
def indexV():
    sql ="call mostrarvenProductos;"
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql)

    ventas = cursor.fetchall()
    print(ventas)

    conn.commit()
    return render_template("ventas/index.html", ventas=ventas )

@app.route('/movimientos/create')
def createM():
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()
    print(productos)

    conn.commit()
    return render_template('movimientos/create.html', productos=productos)

@app.route('/movimientos/store', methods=['POST'])
def storageM():
    _Idproducto = request.form["txtIDProducto"]
    _Tipo = request.form["Tipo"]
    _Fecha = request.form["txtFecha"]
    _Cantidad = request.form["txtCantidad"]

    if _Idproducto=="" or _Tipo =="" or _Fecha=="" or _Cantidad=="":
        flash('Tienes que llenar todos los campos')
        return redirect(url_for("create"))

    sql ="INSERT INTO movimientos (noProductos, tipo, fecha, cantidad) VALUES (%s,%s,%s,%s);"

    datos=(_Idproducto,_Tipo,_Fecha,_Cantidad)
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/movimientos')

@app.route('/ventas/create')
def createV():
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()
    print(productos)

    conn.commit()
    return render_template('ventas/create.html', productos=productos)

@app.route('/ventas/store', methods=['POST'])
def storageV():
    _Idproducto = request.form["txtIDProducto"]
    _Fecha = request.form["txtFecha"]
    _Cantidad = request.form["txtCantidad"]
    _Precio = request.form["txtPrecio"]

    if _Idproducto=="" or _Fecha=="" or _Cantidad=="" or _Precio=="":
        flash('Tienes que llenar todos los campos')
        return redirect(url_for("create"))

    sql ="INSERT INTO ventas (noProductos, fecha, cantidad, precio) VALUES (%s,%s,%s,%s);"

    datos=(_Idproducto,_Fecha,_Cantidad,_Precio)
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/ventas')

@app.route("/proveedores")
def indexPr():
    sql ="Select * from proveedores;"
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql)

    proveedores = cursor.fetchall()
    print(proveedores)

    conn.commit()
    return render_template("proveedores/index.html", proveedores=proveedores )

@app.route('/proveedores/destroy/<int:id>')
def destroyPr(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM proveedores WHERE noProveedores = %s",(id))
    conn.commit()
    return redirect('/proveedores')

@app.route('/proveedores/create')
def createPr():
    return render_template('proveedores/create.html')

@app.route('/proveedores/store', methods=['POST'])
def storagePr():
    _Nombre = request.form["txtNombre"]
    _Apellido = request.form["txtApellido"]
    _Correo = request.form["txtCorreo"]
    _Telefono = request.form["txtTelefono"]

    if _Nombre=="" or _Apellido=="" or _Correo =="" or _Telefono =="":
        flash('Tienes que llenar todos los campos')
        return redirect(url_for("create"))

    sql ="INSERT INTO proveedores (nombre, apellido, correo, telefono) VALUES (%s,%s,%s,%s);"

    datos=(_Nombre,_Apellido,_Correo,_Telefono)
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/proveedores')

@app.route('/proveedores/update', methods=['POST'])
def updatePr():
    _nombre=request.form["txtNombre"]
    _apellido=request.form["txtApellido"]
    _correo=request.form["txtCorreo"]
    _telefono=request.form["txtTelefono"]
    id=request.form["txtID"]

    sql ="UPDATE proveedores set nombre=%s, apellido=%s, telefono=%s, correo=%s WHERE noProveedores=%s;"
    datos=(_nombre, _apellido, _telefono, _correo, id)
    
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/proveedores')

@app.route('/proveedores/edit/<int:id>')
def editPr(id):
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM proveedores WHERE noProveedores =%s", (id))

    proveedores = cursor.fetchall()
    print(proveedores)

    conn.commit()
    return render_template('proveedores/edit.html', proveedores=proveedores)

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