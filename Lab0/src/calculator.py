
from flask import Flask, request, jsonify
import re
"""
MOCK calculator implementation.

Purpose: unblock the sub-group building the API and its tests while the
real calculator implementation is still being developed on another branch.
This is a stand-in that satisfies the same interface (a `calc` method
taking a string and returning a string) -- swap it out once the real
implementation is merged.

WARNING -- do not use this pattern for anything beyond this lab exercise:
this calls eval() directly on its input with NO sanitisation whatsoever.
That means any Python expression -- not just arithmetic -- will be
executed, including code with side effects. This is intentionally unsafe
and is meant only as a temporary stub while you build against a stable
interface.
"""


class Calculator:
    def calc(self, expression: str) -> str:
        if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
            raise ValueError("Invalid expression")


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
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid expression"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)