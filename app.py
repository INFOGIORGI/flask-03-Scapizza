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
    print("scaffa:",scaffale)
    for o in prodotti:
        print(o[1])
        if o[1]==scaffale:
            p.append(o)
    
    print("lista:",p)
    
    return render_template("dettagliProdotto.html", prodotti=p)




app.run(debug=True)
