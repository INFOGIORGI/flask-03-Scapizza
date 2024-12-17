from flask import Flask,render_template

app = Flask(__name__)

prodotti = (("pennette", 1, 2),("prosciutto", 1, 1.5), ("armadio", 3, 120), ("Monopoli", 2, 8))

@app.route("/")
def index():
    return render_template("index.html", titolo="Homepage")

@app.route("/details")
def details():
    return render_template("details.html", titolo="Details", prodotti=prodotti)

@app.route("/dettagliProdotto/<int:scaffale>")
def dettagliProdotto(scaffale):
    p =[]
    for o in prodotti:
        if o[1]==scaffale:
            p.append(o)
    
    return render_template("dettagliProdotto.html", prodotti=p)




app.run(debug=True)
