from flask import Flask, request, jsonify
import re


class Calculator:
    def calc(self, expression: str) -> str:
        if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
            raise ValueError("Invalid expression")

        return str(eval(expression))


app = Flask(__name__)
calculator = Calculator()


@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/calc", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        result = calculator.calc(expression)

        return jsonify({
            "expression": expression,
            "result": result
        })

    except ValueError:
        return jsonify({"error": "Invalid expression"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)