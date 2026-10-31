from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple in-memory storage for learning.
# Data is reset whenever the application restarts.
employees = []


@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    role = data.get("role")

    if not name or not role:
        return jsonify({"message": "Both name and role are required"}), 400

    employee = {
        "id": len(employees) + 1,
        "name": name,
        "role": role,
    }

    employees.append(employee)
    return jsonify(employee), 201


@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees), 200


@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return jsonify(employee), 200

    return jsonify({"message": "Employee not found"}), 404


@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            return jsonify({"message": "Employee deleted"}), 200

    return jsonify({"message": "Employee not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
