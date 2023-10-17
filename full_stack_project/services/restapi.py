from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app,origins='*')
with open("configfile.json", "r") as config_file:
    config = json.load(config_file)
    employee_api_url = config.get("employee_api_url")

 # Route to fetch all employees from the employee management application
@app.route('/employeesinfo', methods=['GET'])
def fetch_employees():
    response = requests.get(f"{employee_api_url}/employees")
    if response.status_code == 200:
        employees = response.json()
        return jsonify(employees)
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

 
# Route to fetch a single employee by ID from the employee management application
@app.route('/employeesinfo/<int:employee_id>', methods=['GET'])
def fetch_employee(employee_id):
    response = requests.get(f"{employee_api_url}/employees/{employee_id}")
    if response.status_code == 200:
        employee = response.json()
        return jsonify(employee)
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

# Route to add a new employee to the employee management application
@app.route('/employeesinfo', methods=['POST'])
def add_employee():
    data = request.json
    response = requests.post(f"{employee_api_url}/employees", json=data)
    if response.status_code == 201:
        return jsonify({"message": "Employee added successfully"})
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

# Route to update an employee by ID in the employee management application
@app.route('/employeesinfo/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    response = requests.put(f"{employee_api_url}/employees/{employee_id}", json=data)
    if response.status_code == 200:
        return jsonify({"message": "Employee updated successfully"})
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

 
# Route to delete an employee by ID in the employee management application
@app.route('/employeesinfo/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    response = requests.delete(f"{employee_api_url}/employees/{employee_id}")
    if response.status_code == 200:
        return jsonify({"message": "Employee deleted successfully"})
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
