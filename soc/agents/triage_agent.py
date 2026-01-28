from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from ..state import AgentState

def triage_agent(state: AgentState):
    """
    Analyzes the alert and decides if it warrants further investigation.
    """
    print("\n[Agent] Triage Agent is analyzing the alert...")
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Tier 1 SOC Analyst. Your job is to analyze incoming alerts and decide if they are 'incident' or 'false_positive'. Analyze the severity and context."),
        ("user", "Alert Data: {alert_data}")
    ])
    
    chain = prompt | llm
    
    response = chain.invoke({"alert_data": state["alert_data"]})
    decision = "incident" if "incident" in response.content.lower() else "false_positive"
    
    # Store the thought process
    print(f"[Agent] Triage Decision: {decision.upper()}")
    
    return {
        "triage_decision": decision,
        "messages": [response]
    }
