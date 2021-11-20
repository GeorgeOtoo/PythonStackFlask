from flask import Flask, session, render_template, request, redirect
import random 

app = Flask(__name__)
app.secret_key = "guessNuMber"

@app.route('/')
def show():
    # x = random.randrange(0, 101)
    # print(x)
    return render_template("index.html")

@app.route('/enternumber', methods=['POST'])
def yourNumber():
    #session['x']
    x = random.randrange(0, 101)

    #session['clientNumber'] 
    y = request.form['yournumber']

    #if session['x'] > int(session['clientNumber']):
    if x > int(y):
        #return render_template('greater.html', y=session['clientNumber'], z=session['x'])
        return render_template('greater.html', clientNumber=y, z=x)
    else :
        return render_template('less.html', clientNumber=y, randomNum=x)


if __name__ == "__main__":
    app.run(debug=True)