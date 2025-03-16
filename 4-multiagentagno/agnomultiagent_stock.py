"""
Multi-Agent Healthcare Stocks Analyzer with AGNO and Streamlit
Displays top healthcare stocks in a web UI using web search and financial data, without box-drawing symbols.
"""

import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
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

# Clean output by removing ANSI codes and box-drawing characters
def clean_output(text):
    """Remove ANSI escape codes and box-drawing characters from text."""
    # Strip ANSI codes
    text = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]|\x1B[@-Z\\-_]', '', text)
    # Remove box-drawing characters (e.g., ┏, ━, ┓, ┃, ┗, ┛)
    text = re.sub(r'[┃┏┓┗┛━]', '', text)
    return text

# Initialize agents
@st.cache_resource
def initialize_team():
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGoTools()],
        instructions="Always include sources",
        show_tool_calls=True,
        markdown=True,
    )

    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_info=True)],
        instructions="Use Markdown tables to display stock name, ticker, market cap, price, and analyst rating",
        show_tool_calls=True,
        markdown=True,
    )

    agent_team = Agent(
        team=[web_agent, finance_agent],
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "Web Agent: Identify a list of top healthcare stocks from reliable web sources.",
            "Finance Agent: Provide financial data (stock price, market cap, etc.) for the stocks identified by Web Agent.",
            "Combine results into a single table with stock name, ticker, market cap, and source.",
            "Always include sources",
            "Use tables to display data"
        ],
        show_tool_calls=True,
        markdown=True,
    )
    return agent_team

# Query function with clean output
def query_team(agent, question):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        agent.print_response(question, stream=True)
    output = clean_output(buffer.getvalue())
    if not output.strip():
        st.warning("No response generated. Check API key or query.")
    return output

# Streamlit UI
st.title("📈 Healthcare StocksBot Developed by Furquan")
st.write("Ask about the top healthcare stocks and get detailed financial data!")

with st.form("query_form"):
    user_input = st.text_input("Enter your question:", value="What are the top 10 healthcare stocks by market capitalization?")
    submit_button = st.form_submit_button("Ask")

# Display response
if submit_button:
    if user_input:
        with st.spinner("Fetching data..."):
            agent_team = initialize_team()
            response = query_team(agent_team, user_input)
            st.markdown(response)  # Display clean response in Streamlit
    else:
        st.warning("Please enter a question!")