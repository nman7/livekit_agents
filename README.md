## 🎙️ LiveKit Voice Agent (Dockerized)
- This project contains a LiveKit-powered AI Voice Agent using Google Gemini Realtime API, fully containerized with Docker for easy deployment.

## 🚀 Features
- Real-time voice interaction via LiveKit

- Gemini LLM (Google Generative AI) integration

- Containerized using python:3.10-slim

- Environment-based configuration

- Lightweight and production-ready

## 📁 Folder Structure

- ├── Dockerfile
- ├── voice_agent.py
- ├── requirements.txt
- ├── .env
- └── README.md

## ⚙️ Setup Instructions
1. Clone the repo
 - git clone <your-repo-url>
 - cd livekit_agents

2. Add your .env file
- Create a .env file in the root directory with the following (replace with your keys):

`LIVEKIT_URL=wss://<your-project-id>.livekit.cloud`

`LIVEKIT_API_KEY=<your-api-key>`

`LIVEKIT_API_SECRET=<your-secret-key>`

`GOOGLE_API_KEY=<your-gemini-api-key>`

❗ Make sure there are no extra spaces or quotes around the values.

## 3. Build Docker Image
docker build -t voice-agent .

## 4. Run the Agent
docker run --env-file .env voice-agent start

Or, for development mode:

docker run --env-file .env voice-agent dev
