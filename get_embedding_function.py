from langchain_community.embeddings import GPT4AllEmbeddings


def get_embedding_function():
    "Get the embedding function for the vector DB."
    gpt4all_embeddings = GPT4AllEmbeddings(
        model_name="all-MiniLM-L6-v2.gguf2.f16.gguf",
        gpt4all_kwargs={'allow_download': 'True'},
        client=None
    )
    return gpt4all_embeddings
