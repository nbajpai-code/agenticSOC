from langgraph.graph import StateGraph, END
from .state import AgentState
from .agents.triage_agent import triage_agent
from .agents.investigation_agent import investigation_agent
from .agents.response_agent import response_agent

def build_graph():
    """
    Constructs the SOC Agent Graph.
    """
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("triage", triage_agent)
    workflow.add_node("investigation", investigation_agent)
    workflow.add_node("response", response_agent)
    
    # Set Entry Point
    workflow.set_entry_point("triage")
    
    # Define Conditional Edges for Triage
    def triage_routing(state: AgentState):
        decision = state.get("triage_decision")
        if decision == "incident":
            return "investigation"
        else:
            print("\n[Graph] Alert routed to archive (False Positive).")
            return END

    workflow.add_conditional_edges(
        "triage",
        triage_routing,
        {
            "investigation": "investigation",
            END: END
        }
    )
    
    # Connect Remaining Edges
    workflow.add_edge("investigation", "response")
    workflow.add_edge("response", END)
    
    # Compile
    app = workflow.compile()
    return app
