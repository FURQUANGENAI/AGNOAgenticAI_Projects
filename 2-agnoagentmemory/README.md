# Thai Cuisine Expert Agent with AGNO - Done by Furquan

This project implements an AI-powered **Thai Cuisine Expert** using the AGNO framework (Wave 5, March 2025). The agent retrieves Thai recipes from a PDF knowledge base, supplements answers with DuckDuckGo web searches, and provides interactive, streaming responses in the Python console. It’s a simple demonstration of AGNO’s agentic memory and tool integration for exploring Thai culinary recipes and history.

## Features
- **Agentic Memory**: Stores Thai recipes in a LanceDb vector database for quick retrieval.
- **Web Search**: Falls back to DuckDuckGo for questions not covered by the knowledge base (e.g., history).
- **Streaming Responses**: Outputs answers live in the console, chunk-by-chunk, using OpenAI’s GPT-4o.
- **Interactive Console**: Users can ask questions via a command-line interface.

## Prerequisites
- **Python**: 3.8+  
- **Git**: Optional, for version control.  
- **OpenAI API Key**: Get one from [platform.openai.com](https://platform.openai.com/).  
- **ThaiRecipes.pdf**: Optional local PDF file (see Knowledge Base section).

## Project Structure
thai-cuisine-agent/
├── thai_agent_console.py  # Main script with AGNO agent and console interface
├── ThaiRecipes.pdf        # Local PDF for knowledge base (optional fallback)
├── .env                   # Environment variables (API key)
└── README.md              # This file