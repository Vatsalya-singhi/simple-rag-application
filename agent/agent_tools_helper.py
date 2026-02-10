# Agent and Tool-based logic
import json
import os

# from langchain_classic.agents import create_react_agent
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

# Configuration
import shared.config
from agent.external_tools import get_recent_activity as fetch_activity
from agent.external_tools import get_user_profile as fetch_profile
from agent.external_tools import get_user_stats as fetch_stats

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest",
                             google_api_key=os.environ['GEMINI_API_KEY'])


# Convert mock tools to LangChain tools
@tool
def get_user_profile(user_id: str) -> str:
    """Get user profile information"""
    result = fetch_profile(user_id)
    return json.dumps(result)


@tool
def get_user_stats(user_id: str) -> str:
    """Get user statistics"""
    result = fetch_stats(user_id)
    return json.dumps(result)


@tool
def get_recent_activity(user_id: str, limit: int = 5) -> str:
    """Get recent user activity"""
    result = fetch_activity(user_id, limit)
    return json.dumps(result)


tools = [get_user_profile, get_user_stats, get_recent_activity]


def call_model_with_tools(state) -> dict:
    """Execute tool-based Q&A using ReAct agent."""

    # Create the ReAct agent using LangGraph's prebuilt function
    agent = create_react_agent(model=llm, tools=tools)  # type: ignore

    # Prepare input for the agent
    messages = state.get("messages", [])
    if not messages:
        messages = [HumanMessage(content=state["input"])]

    agent_input = {"messages": messages}

    # Invoke the agent
    response = agent.invoke(agent_input)

    messages = response["messages"]
    last_ai = next(m for m in reversed(messages)
                   if getattr(m, "type", None) == "ai")
    answer_text = last_ai.text

    return {
        "messages": response["messages"],
        "context": "External service data",
        "answer": answer_text,
    }
