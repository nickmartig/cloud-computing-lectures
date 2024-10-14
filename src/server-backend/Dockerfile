# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 6789

# Run the Python web server
CMD ["python", "server.py"]
