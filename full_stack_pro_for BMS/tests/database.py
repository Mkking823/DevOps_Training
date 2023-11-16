
import mysql.connector
import json

def load_config():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

def get_database_connection():
    config = load_config()
    return mysql.connector.connect(**config['DATABASE_CONFIG'])

def get_books():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

def add_book(title, author, year):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Books (title, author, year) VALUES (%s, %s, %s)', (title, author, year))
    connection.commit()
    cursor.close()
    connection.close()

def get_book(book_id):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Books WHERE id=%s', (book_id,))
    book = cursor.fetchone()
    cursor.close()
    connection.close()
    return book

def update_book(book_id, title, author, year):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE Books SET title=%s, author=%s, year=%s WHERE id=%s', (title, author, year, book_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_book(book_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Books WHERE id=%s', (book_id,))
    connection.commit()
    cursor.close()
    connection.close()
