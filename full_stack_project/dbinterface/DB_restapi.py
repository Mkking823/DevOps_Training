from flask import Flask, request, jsonify
from database import get_employees, add_employee, get_employee, update_employee, delete_employee
import json
from flask_cors import CORS
def load_config():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
        ip_config = config_data.get('IP_CONFIG', {})
        ip = ip_config.get('ip')
        port = ip_config.get('port')
    return config_data, ip, port


app = Flask(__name__)
# Load config and get IP and port
config_data, ip, port = load_config()
CORS(app, origins='*')


# Get all employees
@app.route('/employees', methods=['GET'])
def get_all_employees():
    employees = get_employees()
    return jsonify(employees)

# Get an employee by ID
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_single_employee(employee_id):
    employee = get_employee(employee_id)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

# Add a new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    Employee_Name = data.get('Employee_Name')
    Employee_DateOfJoining = data.get('Employee_DateOfJoining')
    Employee_Location = data.get('Employee_Location')
    Employee_Project = data.get('Employee_Project')

    add_employee(Employee_Name, Employee_DateOfJoining, Employee_Location, Employee_Project)
    return jsonify({"message": "Employee added successfully"}), 201

# Update an employee by ID
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_single_employee(employee_id):
    data = request.json
    Employee_Name = data.get('Employee_Name')
    Employee_DateOfJoining = data.get('Employee_DateOfJoining')
    Employee_Location = data.get('Employee_Location')
    Employee_Project = data.get('Employee_Project')

    update_employee(employee_id, Employee_Name, Employee_DateOfJoining, Employee_Location, Employee_Project)
    return jsonify({"message": "Employee updated successfully"})

# Delete an employee by ID
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_single_employee(employee_id):
    delete_employee(employee_id)
    return jsonify({"message": "Employee deleted successfully"})

if __name__ == '__main__':
    app.run(host=ip, port=port, debug=True)
