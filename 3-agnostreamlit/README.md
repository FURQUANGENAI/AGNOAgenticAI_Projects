# Thai Cuisine Expert Agent with AGNO and Streamlit

This project builds an AI-powered **Thai Cuisine Expert** using the AGNO framework (Wave 5, March 2025). It retrieves Thai recipes from a PDF knowledge base, supplements with DuckDuckGo web searches, and displays clean responses in a Streamlit web interface. Built with Python, it’s a simple tool for exploring Thai recipes and culinary history interactively.

## Features
- **Agentic Memory**: Stores recipes in a LanceDb vector database from a PDF source.
- **Web Search Fallback**: Uses DuckDuckGo for questions beyond the knowledge base (e.g., history).
- **Streamlit UI**: Displays responses directly in the web app, stripped of console formatting codes.
- **Interactive Queries**: Ask anything about Thai cuisine via a text input.

## Prerequisites
- **Python**: 3.8+  
- **Git**: Optional, for version control.  
- **OpenAI API Key**: Obtain from [platform.openai.com](https://platform.openai.com/).  
- **ThaiRecipes.pdf**: Optional local PDF (see Knowledge Base section).

## Key Components:
AGNO Agent: Uses GPT-4o, LanceDb for memory, and DuckDuckGo tools.
Knowledge Base: Loads recipes from a PDF URL or local file.
Streamlit UI: Captures print_response() output, strips ANSI codes, and displays with st.markdown().

## ANSI Codes in Output:
Problem: Early versions displayed junk data (e.g., [34m┃) from print_response() console formatting.
Resolution: Fixed with strip_ansi_codes() in the current version. If junk persists, ensure you’re using this code.