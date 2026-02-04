# Use Python slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY api/ ./api/
COPY static/ ./static/

# Expose port
EXPOSE 8000

# Run the application
WORKDIR /app/api
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
