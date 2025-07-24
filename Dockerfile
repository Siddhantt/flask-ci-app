FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy calculator script
COPY app.py .

# Default command to run the calculator
CMD ["python", "app.py"]
