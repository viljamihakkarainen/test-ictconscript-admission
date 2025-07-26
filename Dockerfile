FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY sample-data/ sample-data/

# Expose port
EXPOSE 8000

# Set environment variable for port (useful for deployment platforms)
ENV PORT=8000

# Run the application
CMD ["python", "main.py"]