from flask import Flask, render_template, request, redirect
import datetime  
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():

    print(request.form)
    apple1 = request.form['apple']
    raspberry1 = request.form['raspberry']
    strawberry1 = request.form['strawberry']

    # template = Template("{{ date.strftime('%Y-%m-%d') }}")
    date_now = datetime.datetime.now()

    sum = int(apple1) + int(raspberry1) + int(strawberry1)
    return render_template("checkout.html", total = sum, date = date_now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    