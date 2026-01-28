from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from ..state import AgentState
from ..tools.mock_tools import mock_tools_list

def investigation_agent(state: AgentState):
    """
    Investigates the confirmed incident using available tools.
    """
    print("\n[Agent] Investigation Agent is gathering context...")
    
    # In a real LangGraph agent, we would use `create_react_agent` or similar.
    # Here, for simplicity in the reference architecture, we illustrate a simple call 
    # that has access to tools. For a more complex loop, we would make this checking loop explicitly.
    # But to keep this step atomic (one node), we will just ask the LLM to use tools if needed.
    
    # NOTE: For the purpose of this atomic node in the graph, we are currently not looping 
    # back for tool execution within this function (unless we use a prebuilt agent executor).
    # To demonstrate LangGraph's power properly, usually we would have a 'ToolNode'.
    # For this simplified agentic step, I'll simulate a 'plan and execute' or just bind tools.
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    llm_with_tools = llm.bind_tools(mock_tools_list)
    
    # We construct a history.
    messages = [
        SystemMessage(content="You are a Senior SOC Analyst. Your job is to investigate alerts. Use the provided tools (search_sim_logs, virustotal_lookup) to gather more context about the IP addresses or users involved. Provide a summary of your findings."),
        HumanMessage(content=f"Investigate this alert: {state['alert_data']}")
    ]
    
    # This single call might generate tool calls.
    # In a full ReAct loop, we'd execute them. 
    # For this specific reference, let's assume we want to show the tool calls being generated.
    # *However*, without a tool-executing loop, they won't run. 
    # So I will actually instantiate a mini-agent executor here just for this node to ensure tools actually run.
    
    from langchain.agents import create_tool_calling_agent, AgentExecutor
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Senior SOC Analyst. Investigate the alert. Use tools freely."),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    agent = create_tool_calling_agent(llm, mock_tools_list, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=mock_tools_list, verbose=True)
    
    result = agent_executor.invoke({"input": f"Alert Data: {state['alert_data']}"})
    
    return {
        "investigation_findings": result['output'],
        # We append the final result as a message too
        "messages": [SystemMessage(content=result['output'])]
    }
