from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a + b)


@app.route("/multiply")
def multiply():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify(result=a * b)
    except (TypeError, ValueError):
        return jsonify(error="invalid input"), 400


@app.route("/divide")
def divide():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        if b == 0:
            return jsonify(error="Cannot divide by zero"), 400
        return jsonify(result=a / b)
    except (TypeError, ValueError):
        return jsonify(error="Invalid input"), 400


@app.route("/subtract")
def subtract():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify(result=a - b)
    except (TypeError, ValueError):
        return jsonify(error="Invalid input"), 400


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True)
