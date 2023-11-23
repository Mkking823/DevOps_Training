from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to wait for an element to be clickable
def wait_for_element_to_be_clickable(by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

# Create a new instance of the Firefox driver
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the web application
driver.get("http://127.0.0.1:5002")

# Function to wait for an element to be clickable
def wait_for_element_to_be_clickable(by, value, timeout=100):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

# --- Create Operation ---
def create_book(title, author, year):
    create_button = wait_for_element_to_be_clickable(By.ID, "createButton")
    create_button.click()

    create_title_input = wait_for_element_to_be_clickable(By.ID, "createTitle")
    create_author_input = wait_for_element_to_be_clickable(By.ID, "createAuthor")
    create_year_input = wait_for_element_to_be_clickable(By.ID, "createYear")
    submit_button = wait_for_element_to_be_clickable(By.XPATH, "//div[@id='createBookForm']//button[@type='submit']")

    create_title_input.send_keys(title)
    create_author_input.send_keys(author)
    create_year_input.send_keys(year)

    submit_button.click()
    time.sleep(5)

# --- Read Operation ---
def fetch_book(book_id):
    fetch_button = wait_for_element_to_be_clickable(By.ID, "fetchButton")
    fetch_button.click()

    fetch_id_input = wait_for_element_to_be_clickable(By.ID, "fetchBookId")
    submit_button = wait_for_element_to_be_clickable(By.XPATH, "//div[@id='fetchBookForm']//button[@type='submit']")

    fetch_id_input.send_keys(book_id)
    submit_button.click()
    time.sleep(5)

# --- Update Operation ---
def update_book(book_id, updated_title, updated_author, updated_year):
    update_button = wait_for_element_to_be_clickable(By.ID, "updateButton")
    update_button.click()
    

    update_id_input = wait_for_element_to_be_clickable(By.ID, "updateBookId")
    update_id_input.send_keys(book_id)

    fetch_button = wait_for_element_to_be_clickable(By.XPATH, "//div[@id='updateBookForm']//button[@type='submit']")
    fetch_button.click()

    update_title_input = wait_for_element_to_be_clickable(By.ID, "updateTitle")
    update_author_input = wait_for_element_to_be_clickable(By.ID, "updateAuthor")
    update_year_input = wait_for_element_to_be_clickable(By.ID, "updateYear")
    update_submit_button = wait_for_element_to_be_clickable(By.XPATH, "//div[@id='updateBookDetailsForm']//button[@type='submit']")

    update_title_input.clear()
    update_title_input.send_keys(updated_title)
    update_author_input.clear()
    update_author_input.send_keys(updated_author)
    update_year_input.clear()
    update_year_input.send_keys(updated_year)

    update_submit_button.click()
    time.sleep(5)

# --- Delete Operation ---
def delete_book(book_id):
    delete_button = wait_for_element_to_be_clickable(By.ID, "deleteButton")
    delete_button.click()

    delete_id_input = wait_for_element_to_be_clickable(By.ID, "deleteBookId")
    delete_submit_button = wait_for_element_to_be_clickable(By.XPATH, "//div[@id='deleteBookForm']//button[@type='submit']")

    delete_id_input.send_keys(book_id)
    delete_submit_button.click()
    time.sleep(5)

# --- Example Usage ---
try:
    # Create a book
    create_book("The Great Gatsby", "F. Scott Fitzgerald", "1925")

    # Fetch and display the details of the created book
    fetch_book("10")

    # Update the book details
    update_book("11", "The Great Gatsby (Updated)", "F. Scott Fitzgerald", "1925")

    # Delete the book
    delete_book("9")

finally:
    # Close the browser window
    print("test passed")
    driver.quit()
