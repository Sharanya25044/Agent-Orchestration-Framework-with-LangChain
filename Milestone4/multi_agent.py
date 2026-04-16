import os
from dotenv import load_dotenv

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================
load_dotenv()

# Debug: Check if API key is loaded
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key or api_key.startswith("YOUR_"):
    print("❌ ERROR: GOOGLE_API_KEY not set or still has placeholder value")
    print("Please get a valid API key from: https://aistudio.google.com/app/apikey")
    exit(1)
print(f"✓ API Key loaded: {api_key[:10]}...{api_key[-4:]}")
# ==========================================

def main():
    print("Initializing Multi-Agent System (DEMO MODE)...")
    print("Note: Running in demo mode with mock responses (free tier quota exhausted)")

    # 1. Simple memory storage
    shared_memory_data = {"context": "", "findings": ""}

    # --- Orchestration ---
    print("\n--- Scenario Execution ---")
    topic = "The integration of AI in modern space exploration"
    
    print(f"\n[Research Agent] Received topic: {topic}")
    
    # Mock research output
    research_output = """Here are 3 key points about the integration of AI in modern space exploration:

1. **Autonomous Navigation & Decision Making**: AI systems enable spacecraft to autonomously navigate, avoid obstacles, and make critical decisions during deep space missions without waiting for commands from Earth. This is essential given the light-delay communication constraints (up to 20+ minutes round trip for Mars missions).

2. **Predictive Maintenance & Anomaly Detection**: Machine learning algorithms continuously monitor satellite and spacecraft systems, predicting component failures before they occur and detecting anomalies in real-time, significantly reducing mission risks and extending operational lifespans.

3. **Data Analysis & Scientific Discovery**: AI processes vast amounts of raw data collected by space instruments (images, spectroscopy, telemetry), identifying patterns and anomalies that human analysts might miss, accelerating scientific discoveries about exoplanets, cosmic phenomena, and the origins of the universe."""
    
    print(f"\n[Research Agent] Generated Facts:\n{research_output}")

    # Saving the research agent's findings into shared memory
    print("\n[System] Saving Research Agent's findings into Shared Memory...")
    shared_memory_data["context"] = topic
    shared_memory_data["findings"] = research_output
    
    request = f"Write a brief summary on the facts we just gathered about {topic}."
    print(f"\n[Summarizer Agent] Received request: {request}")
    
    print("\n[System] Summarizer Agent is reading from Shared Memory...")
    shared_context = shared_memory_data["findings"]
    
    # Mock summarizer output
    summary_output = """## Summary: AI in Modern Space Exploration

The integration of artificial intelligence into space exploration has become transformative across three critical dimensions. First, AI enables autonomous spacecraft operations, allowing missions to function independently despite communication delays inherent in deep space environments. Second, intelligent monitoring systems predict and prevent equipment failures, enhancing mission reliability and extending operational durations. Third, AI dramatically accelerates scientific discovery by processing enormous datasets from space instruments, identifying patterns and anomalies that advance our understanding of the universe.

Collectively, these AI applications have made modern space exploration safer, more efficient, and more scientifically productive than ever before."""
    
    print(f"\n[Summarizer Agent] Final Summary:\n{summary_output}")
    
    print("\n--- Testing Individual Agent Memory ---")
    follow_up_research = "Can you add one more point to the topic we just discussed?"
    print(f"\n[Research Agent] Follow up: {follow_up_research}")
    
    # Mock follow-up response
    follow_up_output = """In addition to the previous three points, here's a fourth important aspect:

4. **Optimization of Resource Management**: AI systems optimize fuel consumption, power distribution, and resource allocation across spacecraft systems, enabling longer missions with limited resources and reducing the cost per mission. Machine learning algorithms continuously learn from mission data to improve efficiency in future operations."""
    
    print(f"\n[Research Agent] Follow up Facts:\n{follow_up_output}")
    
    print("\n✅ Multi-Agent System executed successfully!")
    print("\nTo use this with actual Gemini API calls, you need:")
    print("   - Upgrade to a paid Google Cloud plan")
    print("   - Or wait for free tier quota to reset (usually monthly)")


if __name__ == "__main__":
    main()

