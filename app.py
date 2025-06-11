from flask import Flask, jsonify, request
import json

app = Flask(__name__)


with open("data.json", "r") as f:
    data = json.load(f)

@app.route("/api/data", methods=["GET"])
def get_all_data():
    return jsonify(data)


@app.route("/api/data/<string:brand>", methods=["GET"])
def get_item(brand):
    item = next((item for item in data if item["Brand"].lower() == brand.lower()), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Not found"}), 404


@app.route('/api/data/<string:brand>', methods=['DELETE'])
def delete_item(brand):
    global data
    initial_length = len(data)
    data = [item for item in data if item["Brand"].lower() != brand.lower()]

    if len(data) < initial_length:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        return jsonify({f"message: {brand} deleted"}), 200
    return jsonify({"error": "Brand not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)