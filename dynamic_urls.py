from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>welcome to the home pages</h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1> Hey {name.title()} ,welcome to our webpages! </h1>"

@app.route("/welcome/tony")
def welcome_tony():
    return f"<h1> Hey tony ,welcome to our webpages! </h1>"

if __name__=='__main__':
    app.run(debug=True)