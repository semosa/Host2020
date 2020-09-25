from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

def kontonummer_generator():
    forste_tall = "1234 "
    andre_tall = "01 "
    tredje_tall_random = random.randint(1000, 9999)
    fjerde_tall_matte = abs(9 - (tredje_tall_random %11))
    #print(fjerde_tall_matte)
    fjerde_tall = str(fjerde_tall_matte)
    tredje_tall = str(tredje_tall_random)
    print(forste_tall + andre_tall + tredje_tall + fjerde_tall)
    return forste_tall + andre_tall + tredje_tall + fjerde_tall


kontonummer = kontonummer_generator()
kontoer = [
    dict(type="Brukskonto", nummer=kontonummer, saldo=0),
    dict(type="Sparekonto", nummer=kontonummer, saldo=0),
    dict(type="BSU", nummer=kontonummer, saldo=0) 
    ]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', kontoer=kontoer)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
    #kontonummer_generator()
