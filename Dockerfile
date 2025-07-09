FROM python:3.10-slim

WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    libasound2 \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy minimal requirements and install them
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy your agent script
COPY voice_agent.py .

# Prevent Python from buffering stdout
ENV PYTHONUNBUFFERED=1

# Start the agent
CMD ["python", "voice_agent.py", "start"]
