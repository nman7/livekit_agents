import os
from dotenv import load_dotenv
import asyncio

from livekit.agents import (
    Agent,
    AgentSession,
    RoomInputOptions,
    JobContext,
    WorkerOptions,
    cli
)
from livekit.plugins import google

# Load your LIVEKIT_URL, LIVEKIT_API_KEY, and LIVEKIT_API_SECRET from .env
load_dotenv()

class VideoAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a helpful assistant with live video input. Describe what you see in the video.",
            llm=google.beta.realtime.RealtimeModel(
                model="gemini-2.0-flash-exp",  # ✅ Supports video
                voice="Puck",
                temperature=0.7,
            )
        )

async def entrypoint(ctx: JobContext):
    await ctx.connect()  # Auto uses LIVEKIT_URL and credentials

    session = AgentSession()

    await session.start(
        agent=VideoAssistant(),
        room=ctx.room,  # Matches room in Playground (e.g., "vision-room")
        room_input_options=RoomInputOptions(
            video_enabled=True,  # ✅ Required for Gemini Live to get camera
        ),
    )

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            port=8100  # Any free port (unused when using Cloud Agents)
        )
    )
