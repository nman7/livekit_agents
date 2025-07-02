
import os
import asyncio
from dotenv import load_dotenv

from livekit.plugins import google
from livekit import agents
from livekit.agents import Agent, AgentSession, AutoSubscribe, JobContext, WorkerOptions, cli

class Assistant(Agent):
    def __init__(self):
        super().__init__(instructions="You're a friendly assistant in a shared room. Respond helpfully to whoever is talking.")

    async def on_message(self, msg, participant):
        print(f"[{participant.identity}] said: {msg.text}")
        await self.say(f"{participant.identity} said: {msg.text}")

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    

    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Puck",
            instructions="You are a helpful assistant",
            temperature=0.7,
        ),
        tts=google.TTS()
    )

    await session.start(room=ctx.room, agent=Assistant())
    await asyncio.sleep(1)
    await session.say("Hello! How can I help you today?", allow_interruptions=True)

    # 👇 This enables real-time voice chat!
    await session.run()

if __name__ == "__main__":
    load_dotenv()
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, port=8100))


