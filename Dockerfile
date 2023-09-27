# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

COPY one_server.py one_clients.py /app/
# Copy the Python scripts and configuration files into the container
COPY one_server.py one_clients.py config.json /app/

# Install any needed packages specified in requirements.txt
# (if your script has dependencies)
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt
#hello
# Expose the ports for both the server and client
EXPOSE 9999

# Define the default command to run (server by default)
CMD [ "python", "one_server.py" ]
