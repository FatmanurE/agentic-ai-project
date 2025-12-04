from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

class ResearchAgent:
    """AI Research Agent - Searches the web and writes reports"""
    
    def __init__(self):
        # LLM
        self.llm = ChatAnthropic(
            model="claude-sonnet-4-20250514",
            temperature=0.7
        )
        
        # Web search tool
        self.search_tool = TavilySearchResults(
            max_results=5,
            search_depth="advanced"
        )
        
        # Create agent
        self.agent = create_react_agent(
            self.llm,
            [self.search_tool]
        )
    
    def research(self, query: str) -> str:
        """Conduct research and return report"""
        
        prompt = f"""
        Conduct detailed research on: {query}
        
        Tasks:
        1. Search the web
        2. Find the most current information
        3. Prepare a professional report
        
        Report format:
        # {query} - Research Report
        
        ## Executive Summary
        [2-3 sentences]
        
        ## Key Findings
        - Finding 1
        - Finding 2
        - Finding 3
        
        ## Detailed Analysis
        [Paragraphs]
        
        ## Sources
        [Links]
        """
        
        result = self.agent.invoke({
            "messages": [("user", prompt)]
        })
        
        return result["messages"][-1].content
    
    def save_report(self, content: str, filename: str):
        """Save report to file"""
        os.makedirs("reports", exist_ok=True)
        
        filepath = f"reports/{filename}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        return filepath