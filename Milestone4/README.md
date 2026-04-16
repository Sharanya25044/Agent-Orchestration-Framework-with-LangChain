# 🔍 Multi-Agent Research System

A powerful LangChain-based multi-agent system with a professional Streamlit UI for intelligent research, analysis, and summarization.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Files Overview](#files-overview)
- [Troubleshooting](#troubleshooting)

---

## ✨ Features

- **🤖 Multi-Agent Architecture**: Research Agent, Summarizer Agent, and shared memory
- **💻 Professional Web UI**: Beautiful Streamlit interface with tabs and export options
- **📊 Demo & Live Modes**: Test with mock data or use real Google Gemini API
- **💾 Shared Context Memory**: Agents share findings and maintain conversation history
- **📥 Export Capabilities**: Download results as markdown or copy to clipboard
- **⚡ Production Ready**: Error handling, API key validation, rate limit awareness

---

## 🔧 Prerequisites

- **Python 3.8+** (Tested on Python 3.14)
- **pip** (Python package manager)
- **Virtual Environment** (recommended)
- **Google Gemini API Key** (optional for demo mode)

---

## 📦 Installation

### Step 1: Clone or Download Project
```bash
cd p:\Langchain-ag
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```powershell
# On Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `langchain` - LLM framework
- `langchain-community` - Community extensions
- `langchain-google-genai` - Google Gemini integration
- `python-dotenv` - Environment variable management
- `streamlit` - Web UI framework

---

## 🚀 Quick Start

### Option 1: Run Web UI (Recommended for Presentation)

```bash
streamlit run app.py
```

The application will open automatically at: **http://localhost:8501**

### Option 2: Run Command-Line Version

```bash
python multi_agent.py
```

---

## ⚙️ Configuration

### Google Gemini API Key (Optional)

1. **Get Free API Key**:
   - Visit: https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Copy the key

2. **Add to `.env` File**:
   ```bash
   GOOGLE_API_KEY=your_key_here
   ```

3. **Or leave it for Demo Mode**: The system works perfectly in demo mode with mock responses!

---

## 💡 Usage

### Using the Web UI

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Enter a Research Topic**:
   - Click on the input field
   - Type your research question (e.g., "The future of quantum computing")

3. **Select Mode** (Sidebar):
   - **Demo Mode**: Uses mock data (always works)
   - **Live API**: Requires valid API quota

4. **Analyze**:
   - Click the **"🚀 Analyze"** button
   - Wait for results

5. **View Results**:
   - **Research Findings**: 3 key research points about your topic
   - **Summary**: Comprehensive analysis summary
   - **Follow-up Analysis**: Additional insights and emerging considerations
   - **Shared Memory**: View agent context and cached data

6. **Export Results**:
   - Copy all results to clipboard
   - Download as markdown file
   - Start a new analysis

### Using Command-Line

```bash
python multi_agent.py
```

Output shows:
- Research Agent findings
- System memory operations
- Summarizer Agent output
- Follow-up analysis

---

## 📁 Files Overview

### Core Files

| File | Purpose |
|------|---------|
| `multi_agent.py` | Main multi-agent logic (CLI version) |
| `app.py` | Streamlit web UI application |
| `requirements.txt` | Python dependencies |
| `.env` | Environment variables (API keys) |
| `README.md` | This file |

### Configuration
- `.env` - API keys and secrets
- `.venv/` - Virtual environment (auto-created)

---

## 🎯 Features Walkthrough

### 🔬 Research Agent
- Analyzes topics in depth
- Generates 3 specific, factual points
- Maintains research context

### 📋 Summarizer Agent
- Reads from shared memory
- Integrates research findings
- Creates comprehensive summaries

### 💾 Shared Memory
- Stores research context
- Enables agent-to-agent communication
- Maintains conversation history

### 🌐 Web Interface
- Intuitive tabs for different outputs
- Real-time agent status
- Professional styling with custom CSS
- Responsive design

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**:
```bash
pip install streamlit
```

### Issue: "GOOGLE_API_KEY not found"
**Solution**: Create `.env` file in project root:
```
GOOGLE_API_KEY=your_key_here
```
Or just use Demo Mode (no API key needed!)

### Issue: API Quota Exceeded (429 Error)
**Solution**:
- Switch to demo mode in sidebar (no API calls)
- Or upgrade to paid Google Cloud plan
- Or wait for free tier quota reset (typically monthly)

### Issue: Port 8501 Already in Use
**Solution**:
```bash
streamlit run app.py --server.port 8502
```

### Issue: Streamlit Won't Start
**Solution**:
1. Activate virtual environment: `.\.venv\Scripts\Activate.ps1`
2. Verify installation: `pip list | findstr streamlit`
3. Reinstall if needed: `pip install --upgrade streamlit`

---

## 📊 System Architecture

```
┌─────────────────────────────────────┐
│      Web UI (Streamlit)             │
│   - Input topic                     │
│   - Display results                 │
│   - Export options                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Multi-Agent System                │
│  ┌──────────────────────────────┐   │
│  │  Research Agent              │   │
│  │  - Analyzes topic            │   │
│  │  - Generates 3 key points    │   │
│  └──────────────────────────────┘   │
│                 │                    │
│                 ▼                    │
│  ┌──────────────────────────────┐   │
│  │  Shared Memory               │   │
│  │  - Stores research context   │   │
│  │  - Enables communication     │   │
│  └──────────────────────────────┘   │
│                 │                    │
│                 ▼                    │
│  ┌──────────────────────────────┐   │
│  │  Summarizer Agent            │   │
│  │  - Reads shared memory       │   │
│  │  - Creates summary           │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   LLM (Google Gemini / Mock)        │
│   - Processes requests              │
│   - Returns responses               │
└─────────────────────────────────────┘
```

---

## 🎓 Example Workflows

### Workflow 1: Research & Present
```
1. streamlit run app.py
2. Enter topic: "Climate Solutions"
3. Click Analyze
4. View all 3 tabs
5. Download results
6. Present in meeting!
```

### Workflow 2: Batch Analysis
```
1. python multi_agent.py
2. Results appear in terminal
3. Analyze multiple topics
4. Export summaries
```

### Workflow 3: Development/Testing
```
1. Edit multi_agent.py
2. Test with: python multi_agent.py
3. Refine agents and prompts
4. Deploy UI when ready: streamlit run app.py
```

---

## 📈 Performance Tips

- **Demo Mode** is instant (uses mock data)
- **Live Mode** depends on API response time (~5-30 seconds)
- Results are cached in browser session
- No database needed - stateless design

---

## 🔒 Security Notes

- **Never commit `.env` file** with real API keys
- Keep `GOOGLE_API_KEY` private
- Demo mode uses no real API calls
- All data stays local (no external databases)

---

## 📚 Resources

- **LangChain Docs**: https://python.langchain.com/
- **Streamlit Docs**: https://docs.streamlit.io/
- **Google Gemini API**: https://aistudio.google.com/
- **Python Virtual Environments**: https://docs.python.org/3/tutorial/venv.html

---

## 💬 Support

If you encounter issues:

1. **Check Troubleshooting section** above
2. **Verify all requirements installed**: `pip list`
3. **Check Python version**: `python --version` (3.8+ recommended)
4. **Review `.env` configuration**: Ensure API key format is correct
5. **Try Demo Mode**: Isolates UI issues from API issues

---

## 🎯 Next Steps

1. ✅ Install requirements
2. ✅ Configure `.env` (optional)
3. ✅ Run: `streamlit run app.py`
4. ✅ Enter a research topic
5. ✅ Analyze and present!

---

**Happy analyzing! 🚀**

*Multi-Agent Research System v1.0 - Built with LangChain & Streamlit*
