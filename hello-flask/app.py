from flask import Flask

app = Flask(__name__)


# If the website domain is www.xyz.com, http://www.xyz.com/ will trigger the function below
@app.route("/")
def index():
    return "<p>Hello, World!</p>"


# If the website domain is www.xyz.com, http://www.xyz.com/hello and http://www.xyz.com/hello/<name> will trigger the function below
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'<h1>Hello, {name}!</h1> <p style="color:red">I am very excited to learn flask.</p>'
    return "<h1>Hello, guest!</h1>"


# Create another route like '/square/<num>', so the web app will display the square of the number
@app.route('/square/<num>')
def square(num=None):
    if num:
        result = float(num) ** 2
        return f'The square of {num} is {result}.'
    return 'You need to provide a number.'


if __name__ == "__main__":
    app.run(debug=True)
