import unittest
from unittest.mock import MagicMock, patch
from database import get_books, add_book, get_book, update_book, delete_book
from unittest.mock import patch

# class TestBookFunctions(unittest.TestCase):
#     @patch('database.open', create=True)
#     def test_get_books(self, mock_open):
#         # Mock the file content to return the desired configuration
#         mock_open.return_value.__enter__.return_value.read.return_value = '{"DATABASE_CONFIG": {"user": "test_user", "password": "test_password", "host": "localhost", "database": "test_database"}}'

#         # Rest of your test code
#         result = get_books()
#         # Assertions

class TestBookFunctions(unittest.TestCase):
    @patch('database.mysql.connector.connect')
    def test_get_books(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'title': 'Book 1', 'author': 'Author 1', 'year': 2022}]
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Call the function to be tested
        result = get_books()

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[0]['title'], 'Book 1')
        self.assertEqual(result[0]['author'], 'Author 1')
        self.assertEqual(result[0]['year'], 2022)

    @patch('database.mysql.connector.connect')
    def test_add_book(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Call the function to be tested
        add_book('New Book', 'New Author', 2023)

        # Assertions
        mock_cursor.execute.assert_called_once_with('INSERT INTO Books (title, author, year) VALUES (%s, %s, %s)', ('New Book', 'New Author', 2023))

    @patch('database.mysql.connector.connect')
    def test_get_book(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'id': 1, 'title': 'Book 1', 'author': 'Author 1', 'year': 2022}
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Call the function to be tested
        result = get_book(1)

        # Assertions
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['title'], 'Book 1')
        self.assertEqual(result['author'], 'Author 1')
        self.assertEqual(result['year'], 2022)

    # Similarly, you can write tests for update_book and delete_book functions

if __name__ == '__main__':
    unittest.main()
