from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL


app= Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'tienda'
mysql.init_app(app)

@app.route("/")
def index():
    """sql =""
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql)
    conn.commit()"""
    return render_template("clientes/index.html")

@app.route('/create')
def create():
    return render_template('clientes/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form["txtNombre"]
    _apellido=request.form["txtApellido"]
    _correo=request.form["txtCorreo"]
    _telefono=request.form["txtTelefono"]

    sql ="INSERT into clientes (nombre, apellido, telefono, correo) VALUES (%s, %s, %s, %s);"

    datos=(_nombre,_apellido,_telefono,_correo)
    conn = mysql.connect()
    cursor = conn.cursor() 
    cursor.execute(sql, datos)
    conn.commit()
    return render_template("clientes/index.html")


if __name__ == '__main__':
    app.run(debug=True)