Here’s the translation of your text into English:

# Anime Otaku Helper Bot

This project is an AI-powered conversational assistant that provides responses related to the world of anime. It uses a vector database, Pinecone, for document storage and retrieval, and a language model to answer user questions in real-time. The frontend is implemented using **Streamlit** for user interaction, while the backend utilizes **LangChain** for integrating language models and **Pinecone** for vector searches.

## Features
- **HTML Data Ingestion**: Uploading and processing HTML documents to extract and store relevant data in Pinecone.
- **AI Assistant**: Answers anime-related questions using language models integrated with Pinecone.
- **Streamlit Frontend**: Simple and user-friendly interface for interacting with the chatbot.

## Demonstration

In the following video, you can see how the chat works:
[Anime Chat Bot.webm](https://github.com/user-attachments/assets/2ea9cbc0-d0b3-4864-99c0-64c231d47dbf)

## Prerequisites

1. **Pinecone API Key**: You need a Pinecone account and an API key to interact with the vector database.
2. **OpenAI API Key**: You need an OpenAI API key to generate embeddings and language model responses.
3. **Python 3.8+**: This project is developed in Python, so you must have a compatible version installed.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/anime-otaku-helper-bot.git
   cd anime-otaku-helper-bot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your API keys:

   ```bash
   PINECONE_API_KEY=your_pinecone_key
   OPENAI_API_KEY=your_openai_key
   INDEX_NAME=your_index_name
   ```

## Document Ingestion

The `ingestion.py` file is responsible for loading and processing HTML documents (specifically `index.html` files) containing relevant information about anime.

### Running the Ingestion Script

To load documents into Pinecone:

```bash
python ingest_docs.py
```

This script:
- Iterates through a directory of `index.html` files.
- Extracts text from each HTML file using **BeautifulSoup**.
- Splits the documents into smaller chunks using a **text splitter**.
- Stores the text chunks in Pinecone as vectors.

## Running the Chat Assistant

The assistant responds to user questions in real-time. It connects to Pinecone to retrieve documents and uses a language model to generate contextualized responses.

### Running the Chat

1. Run the **Streamlit** server for the chatbot interface:

   ```bash
   streamlit run app.py
   ```

2. In your browser, go to `http://localhost:8501` and start interacting with the assistant.

### Chat Features:
- Answers anime-related questions.
- Displays the full conversation along with extracted information sources.

## Main Files

- **`ingestion.py`**: Loads and processes HTML documents for storing them in Pinecone.
- **`main.py`**: Chatbot interface using Streamlit.
- **`backend/core.py`**: Contains the main assistant logic, connecting to Pinecone and utilizing the language model.

## Technologies Used

- **Pinecone**: Vector database for document search and storage.
- **OpenAI**: API for generating embeddings and language model responses.
- **LangChain**: Framework for building language model chains (LLMs).
- **BeautifulSoup**: Library for processing and extracting text from HTML files.
- **Streamlit**: Framework for creating interactive web apps with Python.

## Contribution
If you encounter any issues or have ideas to improve this project, feel free to open an **issue** or submit a **pull request**.
