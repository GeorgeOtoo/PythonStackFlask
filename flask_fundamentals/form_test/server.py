from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes

#the index.html route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


#This is the route that will be called when the client submits the form
# We also define which HTTP methods are allowed by the route
""" @app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form['name'])

    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']
    name = request.form['name']
    email = request.form['email']

    #this redirects the client back to the '/' route
    return redirect('/') """


@app.route('/users', methods=['POST'])
def create_user():

    print("Got Post Info")

    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # Here's the line that changed. We're rendering a template from a post route now.
    return redirect('/show') # redirects back to the '/show' route


@app.route('/show')
def show_user():
    return render_template('user.html')


if __name__ == "__main__":
    # run our server
    app.run(debug=True)