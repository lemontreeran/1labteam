from google.adk.agents import Agent
# from .prompt import SYSTEM_PROMPT
from .prompt import render_prompt

bohr_agent = Agent(
    name="bohr_agent",
    model="gemini-1.5-pro",
    # instruction=SYSTEM_PROMPT,
    instruction=render_prompt(parent_agent="atlas_agent"),
    description="Bohr: literature mining specialist."
)
