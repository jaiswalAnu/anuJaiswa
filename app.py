from flask import Flask
app = Flask(__name__)

# Home route
@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to Home pages and how</h1>"

@app.route('/about')
def about():
    return "<h1>Welcome to About pages pages</h1>"

# # Dynamic route example
# @app.route('/hello/<name>')
# def hello_name(name):
#     return f"Hello, {name}!"

# # API route with GET and POST
# @app.route('/api/data', methods=['GET', 'POST'])
# def data_api():
#     if request.method == 'POST':
#         data = request.get_json()
#         return jsonify({"you_sent": data}), 201
#     else:
#         return jsonify({"message": "Send a POST request with JSON data."})

if __name__ == '__main__':
    app.run(debug=True)
