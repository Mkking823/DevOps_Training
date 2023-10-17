import unittest

from unittest.mock import patch, MagicMock

from database import (

    load_config,

    get_database_connection,

    get_employees,

    add_employee,

    get_employee,

    update_employee,

    delete_employee,

)


class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        self.mock_config_data = '{"DATABASE_CONFIG": {"host": "localhost", "user": "testuser", "password": "testpass", "database": "testdb"}}'

        self.mock_records = [

            {'Employee_ID': 1, 'Employee_Name': 'John', 'Employee_DateOfJoining': '2023-01-01',
             'Employee_Location': 'New York', 'Employee_Project': 'Project A'},

            {'Employee_ID': 2, 'Employee_Name': 'Jane', 'Employee_DateOfJoining': '2023-02-01',
             'Employee_Location': 'San Francisco', 'Employee_Project': 'Project B'},

        ]

    def test_load_config(self):
        with patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=self.mock_config_data):
            config = load_config()

            self.assertEqual(config, {
                "DATABASE_CONFIG": {"host": "localhost", "user": "testuser", "password": "testpass",
                                    "database": "testdb"}})

    @patch('mysql.connector.connect')
    def test_get_database_connection(self, mock_connect):
        mock_connection = MagicMock()

        mock_connect.return_value = mock_connection

        connection = get_database_connection()

        self.assertEqual(connection, mock_connection)

    @patch('database.get_database_connection')
    def test_get_employees(self, mock_get_database_connection):
        mock_cursor = MagicMock()

        mock_cursor.fetchall.return_value = self.mock_records

        mock_get_database_connection.return_value.cursor.return_value = mock_cursor

        employees = get_employees()

        self.assertEqual(employees, self.mock_records)

    @patch('database.get_database_connection')
    def test_add_employee(self, mock_get_database_connection):
        mock_connection = MagicMock()

        mock_cursor = MagicMock()

        mock_get_database_connection.return_value = mock_connection

        mock_connection.cursor.return_value = mock_cursor

        employee_data = {

            'Employee_Name': 'Alice',

            'Employee_DateOfJoining': '2023-03-01',

            'Employee_Location': 'Los Angeles',

            'Employee_Project': 'Project C',

        }

        add_employee(**employee_data)

        mock_cursor.execute.assert_called_once()

        mock_connection.commit.assert_called_once()

    @patch('database.get_database_connection')
    def test_get_employee_by_id(self, mock_get_database_connection):
        employee_id = 1

        mock_cursor = MagicMock()

        mock_record = self.mock_records[0]

        mock_cursor.fetchone.return_value = mock_record

        mock_get_database_connection.return_value.cursor.return_value = mock_cursor

        employee = get_employee(employee_id)

        self.assertEqual(employee, mock_record)

    @patch('database.get_database_connection')
    def test_update_employee(self, mock_get_database_connection):
        employee_data = {

            'Employee_ID': 1,

            'Employee_Name': 'Updated John',

            'Employee_DateOfJoining': '2023-02-01',

            'Employee_Location': 'Updated Location',

            'Employee_Project': 'Updated Project',

        }

        mock_cursor = MagicMock()

        mock_get_database_connection.return_value.cursor.return_value = mock_cursor


        mock_cursor.fetchone.return_value = employee_data

        update_employee(**employee_data)

        updated_employee = get_employee(1)

       
        self.assertEqual(updated_employee['Employee_Name'], 'Updated John')

        self.assertEqual(updated_employee['Employee_Location'], 'Updated Location')

        self.assertEqual(updated_employee['Employee_Project'], 'Updated Project')

    @patch('database.get_database_connection')
    def test_delete_employee(self, mock_get_database_connection):
        employee_id = 1

        mock_cursor = MagicMock()

        mock_get_database_connection.return_value.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = None

        delete_employee(employee_id)

        deleted_employee = get_employee(employee_id)

        self.assertIsNone(deleted_employee)


if __name__ == '__main__':
    unittest.main()
