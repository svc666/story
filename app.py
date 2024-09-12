from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Simple Flask App!'

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f'Hello, {name}!'

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    a = data.get('a', 0)
    b = data.get('b', 0)
    result = a + b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
