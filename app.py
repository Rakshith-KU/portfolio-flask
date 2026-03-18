from flask import Flask, render_template
from data import portfolio_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)