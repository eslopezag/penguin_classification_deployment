# Base image:
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Set working directory:
WORKDIR /app

# Expose port 80:
EXPOSE 80

# Copy the requirements file:
COPY ./requirements.txt .

# Install dependecies:
RUN ["pip", "install", "-r", "requirements.txt"]

# Copy the current local directory to the image's woking directory:
COPY . .

# Run the app script:
CMD ["python3", "main.py"]
