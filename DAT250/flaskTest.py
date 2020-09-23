from flask import Flask, render_template, url_for

app = Flask(__name__)

kontoer = [
    {
        'type': 'brukskonto',
        'kontonummer': '1234 01 00001',
        'saldo': '0'
    },
    {
        'type': 'sparekonto',
        'kontonummer': '1234 01 00002',
        'saldo': '0'
    },
    {
        'type': 'BSU',
        'kontonummer': '1234 01 00003',
        'saldo': '0'
    }
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