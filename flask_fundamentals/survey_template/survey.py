from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/')
def enterInfo():
    return render_template('index.html')

@app.route('/result' , methods=['POST'])
def confirmation():

    session['yourName'] = request.form['name']
    yourLocation = request.form['location']
    yourFavLanguage = request.form['language']
    yourComment = request.form['message']

    return render_template('result.html')

@app.route('/danger')
def redirectRoute():
    print("a user tried to visit /danger.  we have redirected the user to /")

    return redirect('/')

@app.route('/show')
def show_user():
    return render_template('user.html', name='Jay' , email='gpractice@tuski.com')


if __name__ == "__main__":
    # run our server
    app.run(debug=True)
