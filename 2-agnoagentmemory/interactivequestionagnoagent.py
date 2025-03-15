"""
Thai Cuisine Expert Agent with Agentic Memory using AGNO
This agent retrieves Thai recipes from a PDF knowledge base, supplements with web searches,
and supports interactive user queries.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file.", file=sys.stderr)
    sys.exit(1)
os.environ["OPENAI_API_KEY"] = api_key

# Define the AGNO agent with Thai cuisine expertise
agent = Agent(
    model=OpenAIChat(id="gpt-4o", temperature=0.7),  # Factual responses
    description="You are a Thai cuisine expert specializing in recipes and history.",
    instructions=[
        "Prioritize your knowledge base (ThaiRecipes.pdf) for recipe-related queries.",
        "Use DuckDuckGo to search the web for broader questions (e.g., history) or missing details.",
        "Provide concise, accurate answers with source attribution where possible."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="./tmp/lancedb",  # Relative path
            table_name="thai_recipes",  # Descriptive
            search_type=SearchType.hybrid,  # Keyword + semantic
            embedder=OpenAIEmbedder(id="text-embedding-3-small")
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,  # Debug tool usage
    markdown=True  # Pretty output
)

def load_knowledge_base():
    """Load or reload the knowledge base if it exists."""
    if agent.knowledge is not None:
        print("Loading Thai recipes into knowledge base...")
        try:
            agent.knowledge.load()
            print("Knowledge base loaded successfully.")
        except Exception as e:
            print(f"Error loading knowledge base: {e}", file=sys.stderr)
            sys.exit(1)

def query_agent(question: str):
    """Query the agent with streaming output and error handling."""
    print(f"\nQuery: {question}")
    try:
        agent.print_response(question, stream=True)
    except Exception as e:
        print(f"Error processing query: {e}", file=sys.stderr)

def run_interactive_mode():
    """Run the agent in interactive mode for user queries."""
    print("Welcome to the Thai Cuisine Expert! Ask me anything about Thai recipes or history.")
    print("Type 'exit' to quit.\n")
    
    # Load knowledge base once at startup
    load_knowledge_base()
    
    # Interactive loop
    while True:
        question = input("Your question: ").strip()
        if question.lower() in ["exit", "quit"]:
            print("Goodbye! Thanks for exploring Thai cuisine with me.")
            break
        if not question:
            print("Please enter a question.")
            continue
        query_agent(question)

if __name__ == "__main__":
    # Start interactive mode
    run_interactive_mode()