from flask import Flask

app = Flask(__name__)

@app.route('/')
def intro():
    print("Hello World")
    return "Hello World"

@app.route('/dojo')
def dojoIntro():
    print("Dojo")
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    print("Hi " + name)
    return "Hi " + name

@app.route('/repeat/<num>/<message>')
def repeatNum(num, message):
    print("Hello")
    return message * int(num)

if __name__ == "__main__":
    app.run(debug=True)