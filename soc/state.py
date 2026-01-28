from typing import TypedDict, List, Annotated
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    """
    Represents the state of the agentic SOC workflow.
    """
    messages: Annotated[List[BaseMessage], operator.add]
    alert_data: dict
    triage_decision: str  # "incident" or "false_positive"
    investigation_findings: str
    response_plan: str
