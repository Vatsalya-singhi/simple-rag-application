# Standard library imports
from typing import Sequence

# LangChain core components
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
# LangGraph imports
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict

# Configuration
import shared.config
from agent.agent_tools_helper import call_model_with_tools
# Import helper modules
from rag.rag_helper import answer_question


class State(TypedDict):
    """
    Represents the application state for a conversational workflow.

    Attributes
    ----------
    input : str
        The latest user query or input.
    chat_history : Annotated[Sequence[BaseMessage], add_messages]
        A sequence of messages representing the chat history, including user and AI messages.
    context : str
        The retrieved context relevant to the current query.
    answer : str
        The generated response to the user's query.
    """
    input: str
    chat_history: Annotated[Sequence[BaseMessage], add_messages]
    context: str
    answer: str


def determine_query_type(query_text: str) -> str:
    """
    Determine if query should use RAG (knowledge base) or tools (external service).

    Returns: "rag" or "tools"
    """
    tool_keywords = ["profile", "stats", "activity",
                     "followers", "posts", "engagement", "recent activity"]
    
    # User names that have external service data
    user_names = ["ana", "sarah", "james", "priya", "marco"]
    
    query_lower = query_text.lower()

    # Check for tool-specific keywords
    if any(keyword in query_lower for keyword in tool_keywords):
        return "tools"
    
    # Check for user names (indicates interest in user data from tools)
    if any(name in query_lower for name in user_names):
        return "tools"
    
    return "rag"


def call_model(state: State):
    """Route to appropriate QA method based on query type."""
    query_type = determine_query_type(state["input"])

    if query_type == "tools":
        return call_model_with_tools(state)
    else:
        # Original RAG implementation
        rag_chain = answer_question()
        response = rag_chain.invoke(state)

        return {
            "chat_history": [
                HumanMessage(state["input"]),
                AIMessage(response["answer"]),
            ],
            "context": response["context"],
            "answer": response["answer"],
        }


# Defines and compiles a stateful workflow for managing a conversational application.
# Attributes
# ----------
# workflow : StateGraph
#     A directed graph that defines the flow of tasks (nodes) and their connections (edges).
# memory : MemorySaver
#     A persistence mechanism that saves and restores the workflow's state in memory.
# app : CompiledStateGraph
#     The final compiled workflow, ready to execute with state management.
workflow = StateGraph(state_schema=State)
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


def execute_user_query(query_text):
    """
    - The function uses a precompiled `app` to execute the workflow.
    - A configuration dictionary is passed, which includes a `thread_id` for tracking.
    - The `app.invoke` method processes the query, retrieves relevant context, and generates a response.
    """
    config: RunnableConfig = {
        "configurable": {
            "thread_id": "thread-123",
        }
    }

    result = app.invoke(
        input=query_text,
        config=config,
    )

    return result["answer"]


# Questions to test:
# What is Ana's profile?
# What are the names of the Stark children's direwolves?
# User Profile Queries
# - "What is Ana's profile?"
# - "Tell me about Ana's profile"
# - "Show me Ana's email and location"
# - "Who is Ana?"

# Statistics Queries
# - "How many followers does Ana have?"
# - "What are Ana's stats?"
# - "How many posts has Ana made?"
# - "What's Ana's engagement rate?"

# Activity Queries
# - "What has Ana been up to recently?"
# - "Show me Ana's recent activity"
# - "What did Ana do last week?"
# - "List Ana's recent actions"

# Mixed Tool Queries
# - "Get Ana's profile and stats"
# - "Show me Ana's followers and recent posts"
# - "Tell me about Ana's engagement and activity"
