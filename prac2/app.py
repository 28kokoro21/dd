
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "title": "Learn Flask", "completed": False}
]


# CREATE - POST
@app.route('/todos', methods=['POST'])
def create():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"message": "Title is required"}), 400

    todo = {
        "id": max([t["id"] for t in todos], default=0) + 1,
        "title": data["title"],
        "completed": False
    }

    todos.append(todo)
    return jsonify(todo), 201


# READ ALL - GET
@app.route('/todos', methods=['GET'])
def get_all():
    return jsonify(todos), 200


# READ ONE - GET
@app.route('/todos/<int:id>', methods=['GET'])
def get_one(id):
    for todo in todos:
        if todo["id"] == id:
            return jsonify(todo), 200

    return jsonify({"message": "Not found"}), 404


# UPDATE - PUT
@app.route('/todos/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()

    if not data or "title" not in data or "completed" not in data:
        return jsonify({
            "message": "Title and completed are required"
        }), 400

    for todo in todos:
        if todo["id"] == id:
            todo["title"] = data["title"]
            todo["completed"] = data["completed"]
            return jsonify(todo), 200

    return jsonify({"message": "Not found"}), 404


# DELETE - DELETE
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete(id):
    for todo in todos:
        if todo["id"] == id:
            todos.remove(todo)
            return jsonify({"message": "Deleted"}), 200

    return jsonify({"message": "Not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)