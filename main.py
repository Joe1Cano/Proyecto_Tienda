from flask import Flask
from flask import render_template


app= Flask(_name_)

@app.route("/")
def index():
    return render_template("empleados/index.html")