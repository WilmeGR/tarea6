from flask import Flask, render_template

from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("base.html")

@app.route("/mision")
def mision():
    return render_template ("mision.html")

@app.route("/servicios")
def servicios():
    return render_template ("servicios.html")

@app.route("/valores")
def valores():
    return render_template ("valores.html")

@app.route("/contactos")
def contactos():
    return render_template ("contactos.html")


if __name__=="__main__":
    app.run(debug=True)
