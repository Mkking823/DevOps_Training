Nallamothu Sri Sindhu 27/09/23 11:14 AM • # Use an official Python runtime as a parent image
FROM python:3.8-slim

RUN pip install xmltodict

# Set the working directory in the container
WORKDIR /app


# Copy the Python script to the container
COPY xmltodict.py /app/



# Run the Python script when the container launches
ENTRYPOINT ["python","/app/xmltodict.py"]

