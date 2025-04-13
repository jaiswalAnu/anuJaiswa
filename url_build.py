
import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the home page</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Congratulations! {sname.title()}You passed.{marks}</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry, you failed{sname.title()}. Try again{marks} next time.</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    time.sleep(1)  # Simulate delay
    if num < 30:
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        return redirect(url_for("passed",sname=name,marks=num))

if __name__ == '__main__':
    app.run(debug=True)
