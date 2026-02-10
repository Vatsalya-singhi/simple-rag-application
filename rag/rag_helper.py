# RAG (Retrieval-Augmented Generation) related logic
import os

from langchain_chroma import Chroma
from langchain_classic.chains.combine_documents import \
    create_stuff_documents_chain
from langchain_classic.chains.history_aware_retriever import \
    create_history_aware_retriever
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

# Configuration
import shared.config
from shared.get_embedding_function import get_embedding_function

# Initialize ChromaDB and retriever
CHROMA_PATH = "chroma"
db = Chroma(persist_directory=CHROMA_PATH,
            embedding_function=get_embedding_function())
retriever = db.as_retriever(search_type="similarity")

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest",
                             google_api_key=os.environ['GEMINI_API_KEY'])


def contextualize_question():
    """
    Create a history-aware retriever to reformulate user queries into standalone questions.

    This function generates a retriever that uses a language model (LLM) to reformulate a user's
    latest question into a standalone question, ensuring it is understandable without requiring
    the context of prior chat history. The retriever is configured using a specified prompt
    template and associated components.

    Returns
    -------
    history_aware_retriever : object
        A retriever object capable of reformulating user queries into standalone questions
        by leveraging the provided language model, retriever, and prompt.
    """
    question_reformulation_prompt = """
    Given a chat history and the latest user question \
    which might reference context in the chat history, formulate a standalone question \
    which can be understood without the chat history. Do NOT answer the question, \
    just reformulate it if needed and otherwise return it as is."""

    question_reformulation_template = ChatPromptTemplate.from_messages(
        [
            ("system", question_reformulation_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, question_reformulation_template
    )

    return history_aware_retriever


def answer_question():
    """
    Creates a Retrieval-Augmented Generation (RAG) chain to answer user questions
    by leveraging a history-aware retriever and a question-answering chain.

    This function combines context retrieval and answer generation:
    - Reformulates user queries into standalone questions if necessary.
    - Retrieves relevant context from a knowledge base or vector database.
    - Generates concise, depthful answers based on the retrieved context.

    Returns
    -------
    rag_chain : RetrievalAugmentedGenerationChain
        A chain that reformulates questions, retrieves relevant context, and generates answers.
    """
    answer_question_prompt = """
    Use the following pieces of retrieved context to answer the question. \
    Use three to seven sentences maximum and keep the answer concise, while still giving depth.\

    {context}"""

    answer_question_template = ChatPromptTemplate.from_messages(
        [
            ("system", answer_question_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    answer_question_chain = create_stuff_documents_chain(
        llm, answer_question_template)

    history_aware_retriever = contextualize_question()

    rag_chain = create_retrieval_chain(
        history_aware_retriever, answer_question_chain)

    return rag_chain
