from agent import ResearchAgent
from datetime import datetime

def main():
    print("🤖 AI Research Agent Starting...\n")
    
    # Create agent
    agent = ResearchAgent()
    
    # Get user query
    query = input("📝 Research topic: ")
    
    if not query.strip():
        print("❌ Please enter a topic!")
        return
    
    print(f"\n🔍 Researching: {query}")
    print("⏳ Please wait...\n")
    
    # Conduct research
    try:
        report = agent.research(query)
        
        # Print to console
        print("=" * 80)
        print(report)
        print("=" * 80)
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{query.replace(' ', '_')}_{timestamp}"
        filepath = agent.save_report(report, filename)
        
        print(f"\n✅ Report saved: {filepath}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()