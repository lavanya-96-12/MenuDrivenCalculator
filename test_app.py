from flask import Flask, jsonify, request

app = Flask(__name__)

# Core calculator logic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

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



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
