"""
Thai Cuisine Expert Agent with AGNO and Streamlit
Displays clean responses in the Streamlit UI.
"""

import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from dotenv import load_dotenv
import os
import io
import sys
from contextlib import redirect_stdout
import re

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Error: OPENAI_API_KEY not found in .env file.")
    st.stop()
os.environ["OPENAI_API_KEY"] = api_key

# Initialize agent
@st.cache_resource
def initialize_agent():
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        description="You are a Thai cuisine expert!",
        instructions=[
            "Search your knowledge base for Thai recipes.",
            "If the question is better suited for the web, search the web to fill in gaps.",
            "Prefer the information in your knowledge base over the web results."
        ],
        knowledge=PDFUrlKnowledgeBase(
            urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
            vector_db=LanceDb(
                uri="tmp/lancedb",
                table_name="recipes",
                search_type=SearchType.hybrid,
                embedder=OpenAIEmbedder(id="text-embedding-3-small"),
            ),
        ),
        tools=[DuckDuckGoTools()],
        show_tool_calls=True,
        markdown=True
    )
    with st.spinner("Loading Thai recipes..."):
        try:
            agent.knowledge.load()
            st.success("Knowledge base loaded!")
        except Exception as e:
            st.warning(f"Error loading knowledge base: {e}")
    return agent

agent = initialize_agent()

# Strip ANSI escape codes (enhanced regex)
def strip_ansi_codes(text):
    """Remove all ANSI escape codes from text."""
    # Match any ANSI sequence starting with ESC (\x1B or \033) followed by control codes
    ansi_pattern = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]|\x1B[@-Z\\-_]')
    return ansi_pattern.sub('', text)

# Query function with clean output
def query_agent(agent, question):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        agent.print_response(question, stream=True)
    output = strip_ansi_codes(buffer.getvalue())
    if not output.strip():
        st.warning("No response generated. Check knowledge base or question.")
    return output

# Streamlit UI
st.title("🥘 Thai Cuisine Expert")
st.write("Ask me anything about Thai cuisine! - Developed by Furquan")

with st.form("query_form"):
    user_input = st.text_input("Enter your question:", placeholder="e.g., How do I make Pad Thai?")
    submit_button = st.form_submit_button("Ask")

# Display response
if submit_button:
    if user_input:
        with st.spinner("Thinking..."):
            response = query_agent(agent, user_input)
            st.markdown(response)  # Display clean response in Streamlit
    else:
        st.warning("Please enter a question!")