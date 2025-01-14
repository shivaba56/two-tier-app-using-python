# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install required dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt


# Copy the app files into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000


# Run the Flask app
CMD ["python", "app.py"]
