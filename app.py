from flask import Flask, render_template, request, flash
from DecifradoPlayfair import DecifradoPlayfair
from CifradoPlayfair import CifrarPlayfair

app = Flask(__name__)
app.secret_key = "Password"

@app.route("/")
def index():
    flash(" ")
    return render_template("index.html")

@app.route("/english")
def index_en():
    flash(" ")
    return render_template("index_en.html")

@app.route("/cifrar", methods = ["POST", "GET"])
def cifrar():
    Mensaje = request.form['Mensaje_Cifrar']
    Palabra = request.form["Palabra_Cifrar"]
    MC = CifrarPlayfair(Mensaje, Palabra)
    flash(MC)
    return render_template("index.html")

@app.route("/decifrar", methods = ["POST", "GET"])
def decifrar():
    Mensaje_D = request.form['Mensaje_Decifrar']
    Palabra_D = request.form["Palabra_Decifrar"]
    MD = DecifradoPlayfair(Mensaje_D, Palabra_D)
    flash(MD)
    return render_template("index.html")