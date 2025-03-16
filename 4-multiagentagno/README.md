# Healthcare Stocks Analyzer with AGNO and Streamlit

This project builds a multi-agent **Healthcare Stocks Analyzer** using the AGNO framework (Wave 5, March 2025). It combines a `Web Agent` for sourcing top healthcare stock lists and a `Finance Agent` for fetching financial data, displaying results in a clean Streamlit web interface. Built with Python, it’s an interactive tool for exploring healthcare stock rankings and financial insights.

## Features
- **Multi-Agent System**:  
  - `Web Agent`: Searches DuckDuckGo for top healthcare stocks.  
  - `Finance Agent`: Retrieves financial data (market cap, price, analyst ratings) via Yahoo Finance.  
  - `Agent Team`: Combines results into Markdown tables.  
- **Streamlit UI**: Displays responses in a web app, free of console formatting artifacts.  
- **Interactive Queries**: Ask about top stocks (e.g., by market cap) and get detailed data.

## Prerequisites
- **Python**: 3.8+  
- **Git**: Optional, for version control.  
- **OpenAI API Key**: Obtain from [platform.openai.com](https://platform.openai.com/).  

## Key Components:
AGNO Agents: Uses GPT-4o, DuckDuckGoTools, and YFinanceTools.
Output Cleaning: Strips ANSI codes and box-drawing characters (e.g., ┃).
Streamlit UI: Captures print_response() output and displays with st.markdown().