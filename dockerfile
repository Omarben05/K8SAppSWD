# Use Python 3.11 slim image as the base image (lightweight version without unnecessary packages)
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from the host to the container's current directory
# This file contains all Python package dependencies with their versions
# Copying it separately before copying the entire app allows Docker to cache the dependency installation layer
# This means if only app code changes (not dependencies), Docker can reuse the cached layer with installed packages
COPY requirements.txt ./

# Install Python dependencies from requirements.txt without caching to reduce image size
# requirements.txt ensures reproducible builds by specifying exact package versions
# --no-cache-dir prevents pip from storing cache files, keeping the image smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory on the host to the container's working directory
COPY . .

# Expose port 5000 to document that the application listens on this port
EXPOSE 5000

# Define the default command to run when the container starts (execute the Flask app)
CMD ["python", "app.py"]