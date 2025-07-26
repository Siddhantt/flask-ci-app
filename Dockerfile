# Use a slim Python image
FROM python:3.12-slim

# Prevent Python from writing pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# System deps and pip upgrade
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential && \
    pip install --upgrade pip setuptools==78.1.1 && \
    apt-get purge -y --auto-remove gcc build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only the necessary files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
