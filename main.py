import streamlit as st

from langchain_helper import execute_user_query

st.title("Multi-Source AI Assistant (RAG + Tools)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
    st.write(
        """
        👋 **Hi! I'm your AI assistant.**  
        Ask me about *A Song of Ice and Fire* 📚 or real people 🧑‍💼.  
        I can handle book facts, profiles, stats, and recent activity!
        """
    )

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if query_text := st.chat_input("Ask about Westeros… or real people"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query_text)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query_text})

if query_text:
    response = execute_user_query({"input": query_text})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
