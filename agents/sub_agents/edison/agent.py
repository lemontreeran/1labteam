from google.adk.agents import Agent
# from .prompt import SYSTEM_PROMPT
from .prompt import render_prompt

edison_agent = Agent(
    name="edison_agent",
    model="gemini-1.5-pro",
    # instruction=SYSTEM_PROMPT,
    instruction=render_prompt(parent_agent="atlas_agent"),
    description="Edison: recommends lab equipment based on data."
)
