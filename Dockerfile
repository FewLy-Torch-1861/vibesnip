# Use official lightweight Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Set environment variables to prevent bytecode and buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (needed for some python packages or sqlite)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the application
# We use 'exec' to ensure signals are passed correctly
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
