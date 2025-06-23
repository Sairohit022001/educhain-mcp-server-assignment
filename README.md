# EduChain MCP Server

This repository contains the implementation of an MCP (Multi-Modal Command Protocol) server that integrates with a simulated `educhain` library to generate educational content. This project addresses an assignment from "Build Fast with AI" and demonstrates how to expose AI capabilities as tools and resources for an MCP host like Claude Desktop.

## Project Overview

The server provides endpoints for generating:
1.  **Multiple-Choice Questions (MCQs)**: A tool to create MCQs on a specified topic.
2.  **Lesson Plans**: A resource to retrieve a detailed lesson plan for a given subject.
3.  **Flashcards (Bonus)**: A tool to generate flashcards with terms and definitions for a topic.

## Technical Stack

* **Python**: Core programming language.
* **FastAPI**: Web framework for building the MCP server API.
* **`educhain_utils.py`**: A simulated module representing the `educhain` library's content generation capabilities. In a real scenario, this would be replaced by the actual `educhain` library.
* **LangChain**: A framework for developing applications powered by language models (used within `educhain_utils.py` for LLM prompting, if configured).
* **Uvicorn**: ASGI server to run the FastAPI application.
* **`requests`**: For generating sample responses by programmatically interacting with the server.

## Project Structure

Yes, I know exactly what we have done. We've built an MCP server with FastAPI and a simulated EduChain, configured Claude Desktop, and thoroughly troubleshooted the setup.

Here is the complete README.md in one code cell, ready for your submission.

Markdown

# EduChain MCP Server

This repository contains the implementation of an MCP (Multi-Modal Command Protocol) server that integrates with a simulated `educhain` library to generate educational content. This project addresses an assignment from "Build Fast with AI" and demonstrates how to expose AI capabilities as tools and resources for an MCP host like Claude Desktop.

## Project Overview

The server provides endpoints for generating:
1.  **Multiple-Choice Questions (MCQs)**: A tool to create MCQs on a specified topic.
2.  **Lesson Plans**: A resource to retrieve a detailed lesson plan for a given subject.
3.  **Flashcards (Bonus)**: A tool to generate flashcards with terms and definitions for a topic.

## Technical Stack

* **Python**: Core programming language.
* **FastAPI**: Web framework for building the MCP server API.
* **`educhain_utils.py`**: A simulated module representing the `educhain` library's content generation capabilities. In a real scenario, this would be replaced by the actual `educhain` library.
* **LangChain**: A framework for developing applications powered by language models (used within `educhain_utils.py` for LLM prompting, if configured).
* **Uvicorn**: ASGI server to run the FastAPI application.
* **`requests`**: For generating sample responses by programmatically interacting with the server.

## Project Structure

educhain_mcp_server/
├── educhain_mcp_server/            # Main application source code
│   ├── main.py                     # FastAPI server application
│   ├── educhain_utils.py           # Helper functions for EduChain content generation
│   ├── claude_desktop_config.json  # Project's copy of the Claude Desktop config
│   └── requirements.txt            # Python dependencies
├── venv/                           # Python virtual environment (ignored by Git)
├── .gitignore                      # Specifies files/folders to ignore in Git
├── generate_sample_responses.py    # Script to generate Sample_Responses.txt
├── Sample_Responses.txt            # Generated output: sample commands and server responses
└── README.md                       # This documentation file


## Setup Instructions

### 1. Clone the Repository

```bash
git clone [YOUR_GITHUB_REPO_URL_HERE]
cd educhain_mcp_server


# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r educhain_mcp_server/requirements.txt


# Ensure your virtual environment is active: (venv) should be in your prompt
# Navigate into the application subfolder where main.py is located
cd educhain_mcp_server

# Start the Uvicorn server
uvicorn main:app --reload --port 8000


# Open a NEW terminal window in VS Code
# Activate the virtual environment in this new terminal
.\venv\Scripts\Activate.ps1

# Navigate back to the project's ROOT folder
cd .. 

# Run the script to generate sample responses
python generate_sample_responses.py


You are correct!

Since the task of configuring Claude Desktop's config.json is a step you, the user, perform on your local machine to get the integration working, it's not something the assessors need to do themselves when they clone your GitHub repository.

The README.md is meant to guide them on how to set up and run your submitted code.

So, we can remove Section 5: Configure Claude Desktop from the README.md as a step they need to perform to run your code.

However, the explanation of the Claude Desktop integration and observations is still crucial, as it explains your setup and your findings during the assignment. This information is currently part of the "Note on Claude Desktop Integration Observation" and also implicitly explained by the presence of claude_desktop_config.json in your repository.

Let's remove that section from the README.md's instructions.

Here is the revised README.md content:

Markdown

# EduChain MCP Server

This repository contains the implementation of an MCP (Multi-Modal Command Protocol) server that integrates with a simulated `educhain` library to generate educational content. This project addresses an assignment from "Build Fast with AI" and demonstrates how to expose AI capabilities as tools and resources for an MCP host like Claude Desktop.

## Project Overview

The server provides endpoints for generating:
1.  **Multiple-Choice Questions (MCQs)**: A tool to create MCQs on a specified topic.
2.  **Lesson Plans**: A Resource to retrieve a detailed lesson plan for a given subject.
3.  **Flashcards (Bonus)**: A tool to generate flashcards with terms and definitions for a topic.

## Technical Stack

* **Python**: Core programming language.
* **FastAPI**: Web framework for building the MCP server API.
* **`educhain_utils.py`**: A simulated module representing the `educhain` library's content generation capabilities. In a real scenario, this would be replaced by the actual `educhain` functions.
* **LangChain**: A framework for developing applications powered by language models (used within `educhain_utils.py` for LLM prompting, if configured).
* **Uvicorn**: ASGI server to run the FastAPI application.
* **`requests`**: For generating sample responses by programmatically interacting with the server.

## Project Structure

educhain_mcp_server/
├── educhain_mcp_server/         # Main application source code
│   ├── main.py                  # FastAPI server application
│   ├── educhain_utils.py        # Helper functions for EduChain content generation
│   ├── claude_desktop_config.json # Project's copy of the Claude Desktop config
│   └── requirements.txt         # Python dependencies
├── venv/                        # Python virtual environment (ignored by Git)
├── .gitignore                   # Specifies files/folders to ignore in Git
├── generate_sample_responses.py # Script to generate Sample_Responses.txt
├── Sample_Responses.txt         # Generated output: sample commands and server responses
└── README.md                    # This documentation file


## Setup Instructions

### 1. Clone the Repository

```bash
git clone [YOUR_GITHUB_REPO_URL_HERE]
cd educhain_mcp_server
(Important: Remember to replace [YOUR_GITHUB_REPO_URL_HERE] with the actual URL of your public GitHub repository after you create it and push your code.)

2. Install Dependencies
It's highly recommended to use a virtual environment for dependency management.

Bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r educhain_mcp_server/requirements.txt
Note on LLM Integration in educhain_utils.py:
The educhain_utils.py file includes commented-out sections for integrating with Large Language Models (LLMs) like Ollama (for local models) or OpenAI.

By default, without uncommenting these lines, the EduChainContentGenerator will use mock data generation for all educational content (MCQs, lesson plans, flashcards). This is sufficient for the assignment's demonstration.
If you wish to use a real LLM, uncomment the relevant imports and initialization lines in educhain_utils.py and ensure the corresponding libraries are installed via pip (e.g., pip install ollama or pip install openai langchain-openai).
3. Run the EduChain MCP Server
You will need to run the FastAPI application using Uvicorn. Keep this terminal window open as it will host your server.

Bash

# Ensure your virtual environment is active: (venv) should be in your prompt
# Navigate into the application subfolder where main.py is located
cd educhain_mcp_server

# Start the Uvicorn server
uvicorn main:app --reload --port 8000
The server will be accessible at http://127.0.0.1:8000. You should see INFO: Application startup complete. in your terminal.

4. Generate Sample Commands and Responses
While the MCP server is running (from Step 3), you can generate the Sample_Responses.txt file by running the provided script. This script programmatically makes requests to your server and captures the outputs.

Bash

# Open a NEW terminal window in VS Code
# Activate the virtual environment in this new terminal
.\venv\Scripts\Activate.ps1

# Navigate back to the project's ROOT folder
cd .. 

# Run the script to generate sample responses
python generate_sample_responses.py
This script will make HTTP requests to your running server (from Step 3) and save the commands and their corresponding JSON responses into Sample_Responses.txt in your project's root directory. You will see logs of these requests appear in your server's terminal (from Step 3).

Usage and Observation with Claude Desktop
This project demonstrates an MCP server designed for integration with clients like Claude Desktop. While direct setup of Claude Desktop is specific to the user's environment, this section describes how the integration was tested and observed during development.

Configuration for Claude Desktop Integration:
The file educhain_mcp_server/claude_desktop_config.json provides the necessary configuration snippet for connecting a Claude Desktop instance to this local MCP server. During development, this snippet was merged into the local Claude Desktop's config.json file (typically located at C:\Users\YOUR_USERNAME\AppData\Roaming\Claude\config.json).

Observed Behavior during Testing:
Once configured and with the server running, manual queries from the Claude Desktop chat interface demonstrated successful integration. Specific prompts aligned with the server's tools and resources (e.g., "Generate 5 multiple-choice questions on Python loops.") resulted in:

Corresponding specific tool invocation logs (e.g., POST /tools/generate_mcqs) appearing in the local server's terminal, confirming Claude Desktop routed the request to the local server.
Claude Desktop displaying the generated educational content (MCQs, lesson plans, flashcards) directly in its chat interface.