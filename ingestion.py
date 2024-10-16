import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document  # Importamos el tipo de documento correcto

# Inicializamos el modelo de embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Función para cargar documentos desde múltiples archivos HTML
def load_documents(directory_path):
    raw_documents = []
    
    # Recorremos el árbol de directorios buscando archivos 'index.html'
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file == "index.html":  # Solo procesamos archivos 'index.html'
                html_file_path = os.path.join(root, file)
                
                # Abre y analiza el HTML usando BeautifulSoup
                with open(html_file_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Crea el objeto BeautifulSoup para parsear el HTML
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extraemos el texto visible del HTML
                text_content = soup.get_text(strip=True)
                
                # Verifica si hay texto visible en el contenido
                if not text_content:
                    print(f"No visible text content found in {html_file_path}.")
                    continue

                # Creamos un documento y lo agregamos a la lista de documentos crudos
                raw_documents.append(Document(
                    page_content=text_content,
                    metadata={"source": html_file_path}
                ))
    
    print(f"Loaded {len(raw_documents)} raw documents with visible text")
    return raw_documents

# Función para procesar y cargar documentos en Pinecone
def ingest_docs():
    directory_path = "mal-docs/myanimelist.net/anime"  # Ruta base de los archivos
    raw_documents = load_documents(directory_path)

    if not raw_documents:
        print("No raw documents to process.")
        return

    # Dividimos los documentos en fragmentos más pequeños
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
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
