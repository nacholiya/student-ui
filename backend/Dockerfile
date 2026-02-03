FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps for mysql connector
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt ./backend/requirements.txt

# Install deps
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend package (IMPORTANT)
COPY . ./backend

EXPOSE 5001

# Run as module
CMD ["python", "-m", "backend.app"]
