from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
import sys
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file.")
    sys.exit(1)
os.environ["OPENAI_API_KEY"] = api_key

agent=Agent(
    model=OpenAIChat(id="gpt-4o",temperature=0.7),
    description="You are an expert news aggregator specializing in AI advancements and job opportunities."
    " Use DuckDuckGo to fetch the latest updates and provide concise, accurate summaries. ",
    tools=[DuckDuckGoTools()],
    markdown=True  # display mechanism like HTML 
)

# Query with refined prompt
try:
    agent.print_response(
        "Provide the latest news on AI developments and current AI job openings "
        "as of March 2025, sourced from DuckDuckGo.",
        stream=True
    )
except Exception as e:
    print(f"Error during execution: {e}")

