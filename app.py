from flask import Flask, jsonify

app = Flask(__name__)


address = [
    {
        "id": 1,
        "name": "John Doe",
        "address": "123 Main St",
        "city": "Anytown",
        "state": "CA",
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "address": "456 Main St",
        "city": "Anytown",
        "state": "CA",
    },
]


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({"data": address}), 200


if __name__ == "__main__":
    app.run(debug=True)
