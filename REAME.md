# AI Agent Orchestration System

A multi-agent system built with Python, FastAPI, and Groq LLM.

## Features

- **Multiple Specialized Agents**: Planner, Researcher, Writer
- **Agent Orchestration**: Agents work together on complex tasks
- **Tool Integration**: Web search and file operations
- **Output Validation**: Guardrails for safe responses
- **REST API**: Full API with FastAPI
- **Docker Support**: Containerized deployment

## Tech Stack

- Python 3.13
- FastAPI
- Groq LLM (Llama 3.1)
- Docker
- Pydantic

## Project Structure

```
ai-agent-system/
├── agents/
│   ├── base_agent.py        # Base agent class
│   ├── planner_agent.py     # Task planning agent
│   ├── researcher_agent.py  # Information gathering agent
│   ├── writer_agent.py      # Content writing agent
│   ├── orchestrator.py      # Agent coordinator
│   ├── tool_agent.py        # Agent with tool use
│   ├── validated_agent.py   # Agent with guardrails
│   └── guardrails.py        # Safety checks
├── api/
│   ├── routes.py            # API endpoints
│   └── schemas.py           # Request/response models
├── tools/
│   ├── web_search.py        # Web search tool
│   └── file_tool.py         # File operations tool
├── data/                    # File storage
├── main.py                  # FastAPI app
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker config
└── docker-compose.yml       # Docker compose config
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-agent-system.git
cd ai-agent-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at: https://console.groq.com

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Open the API docs

```
http://127.0.0.1:8000/docs
```

## Docker Deployment

### Build and run

```bash
docker-compose up --build
```

### Stop

```bash
docker-compose down
```

## API Endpoints

| Endpoint               | Method | Description               |
| ---------------------- | ------ | ------------------------- |
| `/api/workflow`        | POST   | Run full agent workflow   |
| `/api/agent`           | POST   | Run single agent          |
| `/api/tool-agent`      | POST   | Run agent with tools      |
| `/api/validated-agent` | POST   | Run agent with guardrails |
| `/api/health`          | GET    | Health check              |

## Usage Examples

### Run a workflow

```bash
curl -X POST http://127.0.0.1:8000/api/workflow \
  -H "Content-Type: application/json" \
  -d '{"task": "Write a blog post about AI"}'
```

### Use a single agent

```bash
curl -X POST http://127.0.0.1:8000/api/agent \
  -H "Content-Type: application/json" \
  -d '{"agent": "planner", "message": "Plan a website redesign"}'
```

### Use tool agent

```bash
curl -X POST http://127.0.0.1:8000/api/tool-agent \
  -H "Content-Type: application/json" \
  -d '{"message": "Search for Python tutorials"}'
```

## License

MIT License

```

---

## Update `.gitignore`

Make sure it includes everything:
```

# Environment variables

.env

# Python cache

**pycache**/
_.pyc
_.pyo

# Virtual environment

venv/
env/
.venv/

# IDE settings

.vscode/
.idea/

# OS files

.DS_Store
Thumbs.db

# Logs

\*.log

# Distribution

dist/
build/
\*.egg-info/

# Data files

data/\*.txt

# Test files

test\_\*.py

```

---

## Final Folder Structure
```

AI-Agent/
├── agents/
│ ├── **init**.py
│ ├── base_agent.py
│ ├── guardrails.py
│ ├── orchestrator.py
│ ├── planner_agent.py
│ ├── researcher_agent.py
│ ├── tool_agent.py
│ ├── validated_agent.py
│ └── writer_agent.py
├── api/
│ ├── **init**.py
│ ├── routes.py
│ └── schemas.py
├── tools/
│ ├── **init**.py
│ ├── file_tool.py
│ └── web_search.py
├── data/
├── .dockerignore
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
