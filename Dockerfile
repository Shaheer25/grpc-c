# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir grpcio grpcio-tools protobuf

# Expose gRPC port
EXPOSE 50051

# Run the gRPC server
ENTRYPOINT ["python3", "server1.py"]
