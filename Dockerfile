FROM python:3.10-slim

# Prevent Python from writing pyc files & enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

# Run Django using Daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "OrderManagmentSystem.asgi:application"]
