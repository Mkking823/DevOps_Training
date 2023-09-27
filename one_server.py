import socket
import json

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

host = config["server"]["host"]
port = config["server"]["port"]
buffer_size=config["server"]["buffer_size"]

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on {}:{}".format(host, port))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

try:
    while True:
        # Receive data from the client
        data = client_socket.recv(buffer_size).decode()
        print("Client:", data)

        # Check if the client wants to exit
        if data.lower() == 'bye':
            print("client sent bye so connection closed")
            break

        # Send a response to the client
        message = input("Server: ")
        client_socket.send(message.encode())

        # Check if the server wants to exit
        if message.lower() == 'bye':
            break

except Exception as e:
    print("Error:", e)

finally:
    # Close the client socket
    client_socket.close()

# Close the server socket
