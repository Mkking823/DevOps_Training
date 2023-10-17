import mysql.connector
import json

def load_config():
    with open('tests/config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

def get_database_connection():
    config = load_config()
    return mysql.connector.connect(**config['DATABASE_CONFIG'])

def get_employees():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()    
    cursor.close()
    connection.close()
    return employees

def add_employee(Employee_Name, Employee_DateOfJoining,Employee_Location,Employee_Project):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Employees (Employee_Name, Employee_DateOfJoining,Employee_Location,Employee_Project) VALUES (%s, %s,%s,%s)', (Employee_Name, Employee_DateOfJoining,Employee_Location,Employee_Project))
    connection.commit()
    cursor.close()
    connection.close()

def get_employee(Employee_ID):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Employees WHERE Employee_ID=%s', (Employee_ID,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee
def update_employee(Employee_ID, Employee_Name, Employee_DateOfJoining,Employee_Location,Employee_Project):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE Employees SET  Employee_Name=%s, Employee_DateOfJoining=%s,Employee_Location=%s,Employee_Project=%s WHERE Employee_ID=%s', (Employee_Name, Employee_DateOfJoining,Employee_Location,Employee_Project,Employee_ID))
    connection.commit()
    cursor.close()
    connection.close()
def delete_employee(Employee_ID):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Employees WHERE Employee_ID=%s', (Employee_ID,))
    connection.commit()
    cursor.close()
    connection.close()
