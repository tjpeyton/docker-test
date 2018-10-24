FROM python:3.6

# Set the working directory to /app
WORKDIR /test

# Copy the current directory contents into the container at /app
COPY . /test

# Install any needed packages specified in requirements.txt

# Make port 80 available to the world outside this container

# Define environment varia

# Run app.py when the container launches
CMD ["python", "hello.py"]
