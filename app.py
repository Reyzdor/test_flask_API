from flask import Flask, jsonify, request
import json

app = Flask(__name__)


with open("data.json", "r") as f:
    data = json.load(f)

@app.route("/api/data", methods=["GET"])
def get_all_data():
    return jsonify(data)


@app.route("/api/data/<int:id>", methods=["GET"])
def get_item(id):
    item = next((item for item in data if item["id"] == id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)