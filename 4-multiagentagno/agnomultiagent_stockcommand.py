from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

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

agent_team.print_response("Top 10 healthcare stocks to buy and when?", stream=True)