
import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the home page</h1>"

@app.route("/pass")
def passed():
    return "<h1>Congratulations! You passed.</h1>"

@app.route("/fail")
def failed():
    return "<h1>Sorry, you failed. Try again next time.</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    time.sleep(1)  # Simulate delay
    if num < 30:
        return redirect(url_for("failed"))
    else:
        return redirect(url_for("passed"))

if __name__ == '__main__':
    app.run(debug=True)
