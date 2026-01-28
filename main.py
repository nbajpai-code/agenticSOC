import os
import argparse
from soc.graph import build_graph

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, assuming env vars set manually


def main():
    parser = argparse.ArgumentParser(description="Agentic SOC Simulation")
    parser.add_argument("--alert", type=str, help="Alert description for simulation", required=False)
    args = parser.parse_args()

    # ensure API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("[Warning] OPENAI_API_KEY not found in environment. The agents may fail to run.")
        print("Please create a .env file with OPENAI_API_KEY=sk-...")
        # For demo purposes, we might want to stop here, but let's try to run so the user sees the error or can set it.
    
    app = build_graph()
    
    # Example Alert Data
    alert_input = args.alert if args.alert else (
        "High Severity Alert: Suspicious login attempts detected from IP 192.168.1.50 "
        "targeting user 'admin'. Multiple failures followed by a success."
    )
    
    initial_state = {
        "alert_data": {
            "raw": alert_input,
            "severity": "High",
            "source": "SIEM"
        },
        "messages": []
    }
    
    print("-" * 50)
    print("Starting Agentic SOC Workflow")
    print(f"Alert: {alert_input}")
    print("-" * 50)
    
    try:
        final_state = app.invoke(initial_state)
        
        print("\n" + "-" * 50)
        print("Workflow Completed")
        print("-" * 50)
        
        if final_state.get("triage_decision") == "incident":
            print("\n>> Final Response Plan <<\n")
            print(final_state.get("response_plan"))
        else:
            print("\n>> Alert Dismissed as False Positive <<")
            
    except Exception as e:
        print(f"\n[Error] Workflow Failed: {e}")
        print("Ensure you have a valid OPENAI_API_KEY set.")

if __name__ == "__main__":
    main()
