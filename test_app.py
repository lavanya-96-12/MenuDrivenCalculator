from flask import Flask, jsonify, request

app = Flask(__name__)

# Core calculator logic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def get_numbers():
    try:
        x = float(request.args.get('x'))
        y = float(request.args.get('y'))
        return x, y, None
    except (TypeError, ValueError):
        return None, None, "Invalid query parameters. Please provide numeric 'x' and 'y'."

@app.route("/add")
def api_add():
    x, y, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"result": add(x, y)})

@app.route("/subtract")
def api_subtract():
    x, y, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"result": subtract(x, y)})

@app.route("/multiply")
def api_multiply():
    x, y, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"result": multiply(x, y)})

@app.route("/divide")
def api_divide():
    x, y, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400
    try:
        return jsonify({"result": divide(x, y)})
    except ZeroDivisionError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
