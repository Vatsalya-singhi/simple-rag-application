# Simple RAG Application

A Python-based Retrieval-Augmented Generation (RAG) application that combines AI-powered question answering with intelligent agent capabilities. This application uses Google's Generative AI and local embeddings to provide contextual responses from literary sources while also handling structured data queries through specialized tools.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![LangChain](https://img.shields.io/badge/framework-LangChain-green.svg)
![Google Gemini](https://img.shields.io/badge/LLM-Gemini-red.svg)
![GPT4All](https://img.shields.io/badge/Embeddings-GPT4All-orange.svg)

## 🌟 Features

### RAG Capabilities

- **Multi-Book Knowledge Base**: Trained on two classic literary works:
  - _Alice's Adventures in Wonderland_ by Lewis Carroll
  - _A Song of Ice and Fire_ by George R.R. Martin
- **Semantic Search**: Uses GPT4All embeddings for efficient local vector storage and retrieval
- **Contextual Responses**: Powered by Google's Generative AI (ChatGoogleGenerativeAI) for intelligent answer generation

### Agent-Based Tools

The application includes specialized tools for handling structured queries:

- **User Profile Tool**: Retrieve user information including name, email, and location
- **Statistics Tool**: Access user metrics such as follower counts, post counts, and engagement rates
- **Activity Tool**: Query recent user activities and actions

## 📋 Example Queries

### RAG Queries

Ask questions about the books in the knowledge base:

```
- "What happened when Alice fell down the rabbit hole?"
- "Who are the main characters in A Song of Ice and Fire?"
- "Describe the Mad Hatter's tea party"
- "What are the major houses in Westeros?"
```

### User Profile Queries

```python
- "What is Ana's profile?"
- "Tell me about Ana's profile"
- "Show me Ana's email and location"
- "Who is Ana?"
```

### Statistics Queries

```python
- "How many followers does Ana have?"
- "What are Ana's stats?"
- "How many posts has Ana made?"
- "What's Ana's engagement rate?"
```

### Activity Queries

```python
- "What has Ana been up to recently?"
- "Show me Ana's recent activity"
- "What did Ana do last week?"
- "List Ana's recent actions"
```

### Mixed Tool Queries

```python
- "Get Ana's profile and stats"
- "Show me Ana's followers and recent posts"
- "Tell me about Ana's engagement and activity"
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Google API key for Generative AI

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Vatsalya-singhi/simple-rag-application.git
cd simple-rag-application
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your Google API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

### Database Setup

Before running the application, you need to create the vector database:

```bash
python create_db.py
```

This script will:

- Load the book documents from the `data_sources` directory
- Generate embeddings using GPT4All
- Store the vectors in a local database for efficient retrieval

## 💻 Usage

### Running the Application

Launch the application to start the interactive recommendation loop:

```bash
streamlit run main.py
```

## 🐳 Running with Docker

You can run the entire application using Docker without installing Python or dependencies locally.

### Prerequisites

- Docker installed - https://docs.docker.com/get-docker/
- A `.env` file with your Google API key

```env
GEMINI_API_KEY=your_api_key_here
```

### Build the Docker Image

From the project root, build the Docker image:

```bash
docker build -t my-streamlit-app .
```

### Run the Application

Run the container and expose Streamlit on port 8501:

```bash
docker run --env-file .env -p 8501:8501 my-streamlit-app
```

### Access the Application

Once the container is running, open your browser and navigate to:

```bash
http://localhost:8501
```

### Notes

- The .env file is passed to the container using --env-file
- If you add new books or update embeddings, rebuild the vector database and Docker image
- To force a clean rebuild:

```bash
docker build --no-cache -t my-streamlit-app .
```

### Interacting with the Application

Once the application is running, you can:

1. Ask questions about the books in the knowledge base
2. Query user profiles and statistics using the agent tools
3. Combine different types of queries in natural language

Example interaction:

```python
> What is Ana's profile and tell me about Alice in Wonderland?

# The application will:
# 1. Use the User Profile tool to fetch Ana's information
# 2. Query the RAG system for Alice in Wonderland content
# 3. Combine both responses in a coherent answer
```

## 📁 Project Structure

```
simple-rag-application/
├── agent/                  # Agent-based tools and logic
├── data_sources/           # Source documents (books)
├── rag/                    # RAG implementation
├── shared/                 # Shared utilities and configurations
├── tests/                  # Test files
├── create_db.py           # Database creation script
├── langchain_helper.py    # LangChain integration helpers
├── main.py                # Main application entry point
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore file
```

## 🛠️ Technology Stack

- **LLM**: ChatGoogleGenerativeAI (Google's Generative AI)
- **Embeddings**: GPT4AllEmbeddings (local embeddings model)
- **Framework**: LangChain
- **Vector Store**: ChromaDB (for document storage and retrieval)
- **Agent Framework**: LangChain Agents with custom tools

## 🔧 Configuration

The application can be configured through various parameters in the code:

- **Chunk Size**: Adjust document chunking for optimal retrieval
- **Retrieval Count**: Number of relevant documents to retrieve (k parameter)
- **Temperature**: Control the creativity of generated responses
- **Model Selection**: Switch between different Google Generative AI models

## 📚 Data Sources

The application currently includes two books:

1. **Alice's Adventures in Wonderland** - A classic children's novel by Lewis Carroll
2. **A Song of Ice and Fire** - Fantasy series by George R.R. Martin

To add more books:

1. Place the text files in the `data_sources` directory
2. Run `create_db.py` to rebuild the vector database
3. The new content will be available for querying

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues & Limitations

- The application currently uses local embeddings which may have limitations in semantic understanding compared to cloud-based solutions
- Agent tools are currently configured with mock data for demonstration purposes
- Large documents may require significant memory for embedding generation
- The Query Router design is based on key word selection.
- The results can be fine tuned for better overall results.

## 🔮 Future Enhancements

- [ ] Implement conversation history and context management
- [ ] Add support for multiple LLM providers
- [ ] Implement real database integration for agent tools
- [ ] Add evaluation metrics for RAG performance
- [ ] Support for multi-language documents

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub or contact the repository owner.

## 🙏 Acknowledgments

- LangChain for the excellent RAG framework
- Google for providing Generative AI capabilities
- The authors of Alice's Adventures in Wonderland and A Song of Ice and Fire for their timeless works

---

**Note**: This is a demonstration project for learning purposes. The agent tools currently use mock data and should be connected to real data sources for production use.
