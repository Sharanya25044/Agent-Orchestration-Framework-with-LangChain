# Agent-Orchestration-Framework-with-LangChain - Infosys Virtual Internship 6.0

A comprehensive learning journey through multi-agent systems, LangChain framework, and AI-powered applications. This project is developed as part of **Infosys Virtual Internship 6.0**.

---

## 📚 Project Overview

This repository contains four progressive milestones that build upon each other, demonstrating the evolution from foundational LangChain concepts to a production-ready multi-agent research system with a professional web interface.

### Learning Path

```
Milestone 1: Foundations
    ↓
Milestone 2: Dynamic Tool Calling
    ↓
Milestone 3: Collaborative Agents with Memory
    ↓
Milestone 4: Production-Ready Web Interface
```

---

## 🎯 Milestones

### [Milestone 1: Foundational LangChain Agent]

**Focus**: Core LangChain building blocks

- **LLMs** — Integration with Google Gemini (`gemini-2.5-flash`)
- **Prompts** — `PromptTemplate` and `ChatPromptTemplate` structures
- **Chains** — LCEL (LangChain Expression Language) with pipe operators
- **Agents** — Zero-shot ReAct architecture with tool calling

**Key Files**:
- `agent.py` — Main agent implementation

**Setup**:
```powershell
cd Milestone_1
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python agent.py
```

---

### [Milestone 2: LangChain Agent Console]

**Focus**: Dynamic multi-tool agent in a console environment

- **Google Gemini Integration** — High-speed intelligent reasoning
- **Calculator Tool** — Symbolic math with `sympy`
- **Weather Tool** — Real-time weather data from OpenWeatherMap API
- **LangGraph React Agent** — Intelligent tool selection and invocation

**Key Features**:
- Context-aware tool switching
- Real-time API integration
- Console-based interaction

**Key Files**:
- `agent_console.py` — Multi-agent console setup

**Setup**:
```powershell
cd Milestone_2
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python agent_console.py
```

---

### [Milestone 3: Multi-Agent System with Memory]

**Focus**: Agent collaboration with individual and shared memory

- **Research Agent** — Gathers and processes information
- **Summarizer Agent** — Creates executive summaries
- **Individual Memory** — Per-agent `ConversationBufferMemory` (short-term)
- **Shared Memory** — FAISS vector store for cross-agent context (long-term)

**Architecture**:
```
User Input (topic)
       ↓
    Research Agent
    (reads shared memory, researches, saves findings)
       ↓
    Summarizer Agent
    (reads findings, creates summary, saves to memory)
       ↓
    Output + Updated Memory
```

**Key Files**:
- `agents.py` — Agent definitions
- `memory_setup.py` — Memory configuration
- `orchestrator.py` — Workflow orchestration

**Setup**:
```powershell
cd Milestone_3
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python orchestrator.py
```

---

### [Milestone 4: Production-Ready Multi-Agent Research System]

**Focus**: Enterprise-grade UI and deployment

- **Professional Streamlit Interface** — Beautiful, responsive web UI
- **Multi-Agent Architecture** — Research and summarizer agents
- **Shared Context Memory** — FAISS-backed vector store
- **Demo & Live Modes** — Mock data testing and real API integration
- **Export Capabilities** — Download results as markdown or copy to clipboard
- **Production Ready** — Error handling, API validation, rate limit awareness

**Key Files**:
- `app.py` — Main Streamlit application
- `multi_agent.py` — Multi-agent orchestration logic

**Setup**:
```powershell
cd Milestone_4
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

---

## 🛠️ General Setup Instructions

### Prerequisites

- **Python 3.8+** (Tested on Python 3.14)
- **pip** (Python package manager)
- **Virtual Environment** (recommended)

### Required API Keys

1. **Google Gemini API Key**
   - Get it from [Google AI Studio](https://aistudio.google.com/)
   - Free tier available with generous rate limits

2. **OpenWeatherMap API Key** (For Milestone 2+)
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Free tier provides current weather data

### Environment Configuration

Create a `.env` file in each milestone directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_openweather_api_key_here
```

### Activating Virtual Environments

**Windows PowerShell**:
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt**:
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux**:
```bash
source venv/bin/activate
```

---

## 📊 Technology Stack

| Technology | Purpose |
|---|---|
| **LangChain** | Agent and chain orchestration framework |
| **LangGraph** | Graph-based agent execution and tool calling |
| **Google Gemini** | Large Language Model (LLM) backend |
| **FAISS** | Vector database for shared memory |
| **Streamlit** | Web UI framework (Milestone 4) |
| **SymPy** | Symbolic mathematics (Milestone 2) |
| **OpenWeatherMap API** | Real-time weather data (Milestone 2+) |

---

## 🚀 Quick Start

### Option 1: Start with Fundamentals (Recommended for Beginners)

```powershell
cd Milestone_1
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python agent.py
```

### Option 2: Jump to Production UI

```powershell
cd Milestone_4
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
Sharanya_MIlestones/
├── Milestone_1/              # Foundational concepts
│   ├── agent.py
│   ├── requirements.txt
│   ├── README.md
│   └── .venv/
├── Milestone_2/              # Dynamic tool calling
│   ├── agent_console.py
│   ├── requirements.txt
│   ├── README.md
│   └── .venv/
├── Milestone_3/              # Multi-agent with memory
│   ├── agents.py
│   ├── memory_setup.py
│   ├── orchestrator.py
│   ├── requirements.txt
│   ├── README.md
│   └── .venv/
├── Milestone_4/              # Production UI
│   ├── app.py
│   ├── multi_agent.py
│   ├── requirements.txt
│   ├── README.md
│   └── .venv/
└── README.md                 # This file
```

---

## 🎓 Learning Outcomes

By completing this project, you will understand:

✅ **LangChain Fundamentals** — How to build LLM applications with chains and agents  
✅ **Agent Architecture** — ReAct framework and tool calling patterns  
✅ **Memory Systems** — ConversationBuffer and vector-based long-term memory  
✅ **Multi-Agent Collaboration** — How agents share context and build on each other's work  
✅ **Real-world Integration** — APIs, external tools, and production patterns  
✅ **Web UI Development** — Creating professional interfaces with Streamlit  
✅ **Best Practices** — Error handling, configuration management, and deployment  

---

## 🔍 Key Concepts

### ReAct (Reasoning + Acting)
A framework where agents:
1. **Reason** — Analyze the problem using the LLM
2. **Act** — Call appropriate tools
3. **Observe** — Receive tool results
4. Repeat until problem is solved

### Vector Memory (FAISS)
Stores information as embeddings, allowing:
- Semantic similarity search
- Cross-agent knowledge sharing
- Persistent learning across sessions

### LCEL (LangChain Expression Language)
A modern syntax for composing chains:
```python
chain = prompt | llm | output_parser
```

---

## 📝 Notes

- All milestones use **Google Gemini** as the primary LLM
- Each milestone builds on the previous one's concepts
- Virtual environments are pre-created; activate them before installing dependencies
- API keys must be configured in `.env` files
- For production deployments, consider using environment variables or secret management tools

---

## 🤝 Support

For issues or questions:
1. Check the individual milestone README files for specific troubleshooting
2. Verify API keys are correctly configured
3. Ensure all dependencies are installed: `pip install -r requirements.txt`
4. Check Python version: `python --version` (Should be 3.8+)

---

## 📜 License

This project is created as part of Infosys Virtual Internship 6.0 for educational purposes.

---

