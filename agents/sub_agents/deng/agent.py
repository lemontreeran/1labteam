from google.adk.agents import Agent
from .prompt import render_prompt

deng_agent = Agent(
    name="deng_agent",
    model="gemini-1.5-pro",
    # instruction=SYSTEM_PROMPT,
    instruction=render_prompt(parent_agent="atlas_agent"),
    description="Deng: robot technician executing code."
)
