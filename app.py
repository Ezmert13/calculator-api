import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/add")
def add():
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        if a is None or b is None:
            logger.warning("/add missing input")
            return jsonify(error="Missing input"), 400
        a = float(a)
        b = float(b)
        result = a + b
        logger.info(f"/add called with a={a}, b={b}, result={result}")
        return jsonify(result=result)
    except (TypeError, ValueError):
        logger.warning("/add invalid input")
        return jsonify(error="Invalid input"), 400


@app.route("/multiply")
def multiply():
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        if a is None or b is None:
            logger.warning("/multiply missing input")
            return jsonify(error="Missing input"), 400
        a = float(a)
        b = float(b)
        result = a * b
        logger.info(f"/multiply called with a={a}, b={b}, result={result}")
        return jsonify(result=result)
    except (TypeError, ValueError):
        logger.warning("/multiply invalid input")
        return jsonify(error="invalid input"), 400


@app.route("/divide")
def divide():
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        if a is None or b is None:
            logger.warning("/divide missing input")
            return jsonify(error="Missing input"), 400
        a = float(a)
        b = float(b)
        if b == 0:
            logger.warning("/divide Cannot divide by zero")
            return jsonify(error="Cannot divide by zero"), 400
        result = a / b
        logger.info(f"/divide called with a={a}, b={b}, result={result}")
        return jsonify(result=result)
    except (TypeError, ValueError):
        logger.warning("/divide Invalid input")
        return jsonify(error="Invalid input"), 400


@app.route("/subtract")
def subtract():
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        if a is None or b is None:
            logger.warning("/subtract Missing input")
            return jsonify(error="Missing input"), 400
        a = float(a)
        b = float(b)
        result = a - b
        logger.info(f"/subtract called with a={a}, b={b}, result={result}")
        return jsonify(result=result)
    except (TypeError, ValueError):
        logger.warning("/subtract Invalid Input")
        return jsonify(error="Invalid input"), 400


@app.route("/sum-list")
def sum_list():
    try:
        numbers_raw = request.args.get("numbers")
        if not numbers_raw:
            return jsonify(error="Missing input"), 400

        numbers_list = numbers_raw.split(",")
        if len(numbers_list) < 2:
            return jsonify(error="Numbers with 1 element."), 400
        if not numbers_list:
            return jsonify(error="Empty list"), 400
        numbers = [float(n) for n in numbers_list]
        return jsonify(result=sum(numbers))
    except (TypeError, ValueError):
        logger.warning("/sum-list Invalid Input")
        return jsonify(error="Invalid Input"), 400


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
