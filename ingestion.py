import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document  # Importamos el tipo de documento correcto

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def load_documents(directory_path):
    raw_documents = []
    html_file_path = os.path.join(directory_path, "index.html")
    
    # Verifica si el archivo HTML existe
    if not os.path.exists(html_file_path):
        print(f"HTML file not found at {html_file_path}")
        return []

    # Abre y analiza el HTML usando BeautifulSoup
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Crea el objeto BeautifulSoup para parsear el HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extraemos el texto visible del HTML
    text_content = soup.get_text(strip=True)
    
    # Verifica si hay texto visible en el contenido
    if not text_content:
        print("No visible text content found in HTML.")
        return []

    # Crear un documento de LangChain
    raw_documents.append(Document(
        page_content=text_content,
        metadata={"source": html_file_path}
    ))
    
    print(f"Loaded {len(raw_documents)} raw document with visible text")
    return raw_documents

def ingest_docs():
    directory_path = "anilist-docs/anilist.co/anime/1/Cowboy-Bebop"
    raw_documents = load_documents(directory_path)

    if not raw_documents:
        print("No raw documents to process.")
        return

    # Usamos el text_splitter para dividir los documentos
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    
    print(f"After splitting, loaded {len(documents)} documents")
    
    if not documents:
        print("No documents after splitting.")
        return

    # Añadimos los documentos a Pinecone
    print(f"Going to add {len(documents)} documents to Pinecone")
    PineconeVectorStore.from_documents(
        documents, embeddings, index_name=os.environ["INDEX_NAME"]
    )

if __name__ == "__main__":
    ingest_docs()
