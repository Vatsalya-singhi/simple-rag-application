import os
import shutil
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from shared.get_embedding_function import get_embedding_function

DATA_PATH = "data_sources/books"
CHROMA_PATH = "chroma"


def load_documents():
    "Load PDF documents from a folder."
    loader = DirectoryLoader(DATA_PATH,
                             recursive=True, show_progress=True)
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    "Split documents into chunks."
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks


def save_to_chroma(chunks: list[Document]):
    "Clear previous db, and save the new db."
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    # create db
    db = Chroma.from_documents(
        chunks, get_embedding_function(), persist_directory=CHROMA_PATH
    )
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


def create_vector_db():
    "Create vector DB from personal PDF files."
    documents = load_documents()
    doc_chunks = split_text(documents)
    save_to_chroma(doc_chunks)


if __name__ == "__main__":
    create_vector_db()
