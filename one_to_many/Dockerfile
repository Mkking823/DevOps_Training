# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

#COPY server1.py server2.py client.py /app/
# Copy the Python scripts and configuration files into the container
COPY server1.py server2.py client.py config_file.json /app/

# Install any needed packages specified in requirements.txt
# (if your script has dependencies)
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt
#hello
# Expose the ports for both the server and client
EXPOSE 3333

EXPOSE 8888

# Define the default command to run (server by default)
#CMD [ "python" ]


