# Use the required Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependency definition
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy all application source files
COPY service/ ./service/

# Copy application configuration and supporting files
COPY setup.cfg .
COPY run.py .

# Create a dedicated non-root user
RUN useradd --uid 1000 --create-home appuser && \
    chown -R appuser:appuser /app

# Switch from root to non-root user
USER appuser

# Application port
EXPOSE 8080

# Configure application port
ENV PORT=8080

# Start the Customer Accounts microservice with Gunicorn
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]
