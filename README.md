# 🤖 AI Research Agent

Automated research and report generation using multi-agent AI system.

## 🎯 Features

- ✅ Web search (Tavily API)
- ✅ LLM-powered analysis (Claude Sonnet 4)
- ✅ Automated report generation (Markdown)
- ✅ ReAct pattern (Reasoning + Acting)

## 🚀 Installation
```bash
# 1. Clone the repository
git clone https://github.com/your-username/agentic-ai-project.git
cd agentic-ai-project

# 2. Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Add your API keys
```

## 🔑 API Keys

Create a `.env` file:
```bash
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
```

Get your keys:
- Anthropic: https://console.anthropic.com/
- Tavily: https://tavily.com/

## 💻 Usage
```bash
python main.py
```

**Example:**
```
📝 Research topic: Tesla 2024 performance

🔍 Researching...
✅ Report saved: reports/Tesla_2024_performance_20241203_123045.md
```

## 📁 Project Structure
```
agentic-ai-project/
├── agent.py           # Main agent logic
├── main.py            # Entry point
├── requirements.txt   # Dependencies
├── .env              # API keys (not in git)
├── .gitignore        # Git ignore rules
└── reports/          # Generated reports
```

## 🛠️ Tech Stack

- **LangGraph**: Agent orchestration
- **Claude Sonnet 4**: Large Language Model
- **Tavily**: Web search API
- **Python 3.11+**

## 📊 How It Works

1. User provides research query
2. Agent uses ReAct pattern (Reasoning + Acting)
3. Searches web using Tavily API
4. LLM analyzes and synthesizes information
5. Generates professional markdown report
6. Saves report to `reports/` directory

## 🎓 Learning Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [DeepLearning.AI Course](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)

## 📝 License


## 👤 Author

Fatmanur Ertaş
