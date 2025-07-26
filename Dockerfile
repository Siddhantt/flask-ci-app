# Use a slim Python image
FROM python:3.12-slim

# Set environment variables to prevent Python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install pip & setuptools updates (patch vulnerabilities here)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential && \
    pip install --upgrade pip setuptools==78.1.1 && \
    apt-get purge -y --auto-remove gcc build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose app port (optional)
EXPOSE 5000

# Run app (update as per your entry point)
CMD ["python", "app.py"]
