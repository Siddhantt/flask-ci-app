# Use a slim Python image
FROM python:3.12-slim

# Prevent Python from writing pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies and upgrade pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential && \
    pip install --upgrade pip setuptools==78.1.1 && \
    apt-get purge -y --auto-remove gcc build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only required files to avoid leaking secrets or dev files
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy only necessary application files
COPY app.py .

# Create a non-root user and switch to it
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

USER appuser

# Expose port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]
