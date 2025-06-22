from google.adk.agents import Agent
from agents.sub_agents.bohr.agent import bohr_agent
from agents.sub_agents.curie.agent import curie_agent
from agents.sub_agents.deng.agent import deng_agent
from agents.sub_agents.edison.agent import edison_agent
from .prompt import render_prompt

atlas_agent = Agent(
    name="atlas_agent",
    model="gemini-1.5-pro",
    instruction=render_prompt(parent_agent="atlas_agent"),
    # instruction=SYSTEM_PROMPT,
    description="Atlas: orchestrates literature, synthesis, robot and evaluation agents.",
    sub_agents=[
        bohr_agent,
        curie_agent,
        deng_agent,
        edison_agent,
    ]
)
