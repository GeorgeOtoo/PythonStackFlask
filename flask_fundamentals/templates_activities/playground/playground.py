from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def boxes():
    return render_template('index.html', times=3)

@app.route('/play/<num>')
def specifyNum(num):
    return render_template('index.html', times=int(num))

@app.route('/play/<num>/<color>')
def specifyColor(num, color='red'):
    return render_template('index.html', times=int(num), yourColor="color") 



if __name__ == "__main__":
    app.run(debug=True)