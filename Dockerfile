# Dockerfile
FROM python:3.13

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
