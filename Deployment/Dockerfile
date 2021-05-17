# Base image:
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Set working directory:
WORKDIR /app

# Expose port 80:
EXPOSE 80

# Copy the current local directory to the image's woking directory:
COPY . .

# Install dependecies:
RUN ["pip", "install", "-r", "requirements.txt"]

# Run the app script:
CMD ["python3", "main.py"]