from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from ..state import AgentState

def response_agent(state: AgentState):
    """
    Proposes a response plan based on the investigation findings.
    """
    print("\n[Agent] Response Agent is drafting a remediation plan...")
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a SOC Responder. Based on the Investigation Findings, propose a set of remediation actions (e.g., block IP, reset password, isolate host). Output a concise plan."),
        ("user", "Investigation Findings: {investigation_findings}")
    ])
    
    chain = prompt | llm
    
    response = chain.invoke({"investigation_findings": state.get("investigation_findings", "No findings provided.")})
    
    print(f"[Agent] Response Plan: {response.content}")
    
    return {
        "response_plan": response.content,
        "messages": [response]
    }
