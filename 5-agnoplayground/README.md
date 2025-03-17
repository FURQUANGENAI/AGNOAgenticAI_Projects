# Healthcare Stocks Analyzer with AGNO Playground

This project builds a multi-agent **Healthcare Stocks Analyzer** integrated with the AGNO Playground (Wave 5, March 2025). It features a `Web Agent` for sourcing top healthcare stock lists via web searches and a `Finance Agent` for retrieving financial data, all accessible through an interactive web interface powered by AGNO’s Playground. Built with Python, it’s a tool for exploring healthcare stock rankings and financial insights with persistent session history.

## Features
- **Multi-Agent System**:  
  - `Web Agent`: Uses DuckDuckGo to search for top healthcare stocks.  
  - `Finance Agent`: Fetches financial data (stock prices, analyst ratings, company info, news) via Yahoo Finance.  
- **AGNO Playground**: Provides a web-based chat UI to interact with agents.  
- **Persistent Storage**: Stores session history in a SQLite database (`tmp/agents.db`).  
- **Contextual History**: Includes up to 5 previous responses and current datetime in queries.  
- **Markdown Formatting**: Enhances readability with tables and structured output.

## Prerequisites
- **Python**: 3.8+  
- **Git**: Optional, for version control.  
- **OpenAI API Key**: Obtain from [platform.openai.com](https://platform.openai.com/).  

## Imports
yfinance
fastapi
sqlalchemy
uvicorn