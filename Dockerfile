# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install any required dependencies (none needed here, but keeping it ready for future)
# RUN pip install -r requirements.txt

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run the main script
CMD ["python", "src/main.py"]