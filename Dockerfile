# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /

# Copy all files from the current directory to /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir grpcio grpcio-tools protobuf

# Expose gRPC port
EXPOSE 50051

# Run the gRPC server
CMD ["python", "server1.py"]
