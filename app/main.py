"""Small Flask app used as the target of the CI/CD pipeline."""
import os

from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "1.0.0")


def add(a: int, b: int) -> int:
    """Return the sum of two numbers (kept simple for unit testing)."""
    return a + b


@app.route("/")
def home():
    return jsonify(message="Hello from the DevOps CI/CD lab!", version=VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify(result=add(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104 - container binding
