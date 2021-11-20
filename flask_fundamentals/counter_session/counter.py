from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "counterSessionkEY"

@app.route('/')
def trackSession():

    if 'visits' in session:
        session['visits'] +=  1
        # print(session['visits'])
    else:
        session['visits'] = 1
    return render_template('index.html' )

@app.route('/ammend', methods=['POST'])
def changeCount():
    if request.form['change'] == 'Add Two Visits':
        session['visits'] += 1

    elif request.form['change'] == 'Reset':
        session['visits'] = 0

    return redirect('/') 


@app.route('/destroy_session')
def clearSession():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
