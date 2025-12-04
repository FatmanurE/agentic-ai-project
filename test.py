from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

# LLM test
llm = ChatAnthropic(model="claude-sonnet-4-20250514")
response = llm.invoke("Merhaba! Kurulum başarılı mı?")
print("Claude:", response.content)

# Search test
search = TavilySearchResults(max_results=2)
results = search.invoke({"query": "Python nedir"})
print("\nSearch:", results)