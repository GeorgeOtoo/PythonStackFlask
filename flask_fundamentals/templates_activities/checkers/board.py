from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def defaultChecker():
    return render_template('index.html', x=8, y=8)

@app.route('/<row>/<columne>')
def sizeChecker(row,column):
    return render_template('index.html', x=int(row), y=int(column))

if __name__ == "__main__":
    app.run(debug=True)