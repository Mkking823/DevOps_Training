import socket
import json

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

host = config["server"]["host"]
port = config["server"]["port"]
buffer_size=config['server']['buffer_size']

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))
print("Connected to server")

try:
    while True:
        # Send a message to the server
        message = input("Client: ")
        client_socket.send(message.encode())

        # Check if the client wants to exit
        if message.lower() == 'bye':
            break

        # Receive data from the server
        data = client_socket.recv(buffer_size).decode()
        print("Server:", data)

        # Check if the server wants to exit
        if data.lower() == 'bye':
            print("server sent bye so connection closed")
            break

except Exception as e:
    print("Error:", e)

finally:
    # Close the client socket
    client_socket.close()
