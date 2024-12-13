from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", titolo="Homepage")

@app.route("/details")
def details():
    prodotti = (("pennette", "pasta", 2),("prosciutto", "affettati", 1.5), ("armadio", "mobili", 120), ("Monopoli", "giochi", 8))
    return render_template("details.html", titolo="Details", prodotti=prodotti)

@app.route("/dettagliProdotto/<prodotto>")
def dettagliProdotto(prodotto):




app.run(debug=True)
