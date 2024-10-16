# Anime Otaku Helper Bot

Este proyecto es un asistente conversacional impulsado por inteligencia artificial que proporciona respuestas relacionadas con el mundo del anime. Utiliza una base de datos vectorial, Pinecone, para el almacenamiento y recuperación de documentos, y un modelo de lenguaje para responder preguntas de los usuarios en tiempo real. El frontend se ha implementado usando **Streamlit** para la interacción del usuario, mientras que el backend hace uso de **LangChain** para la integración de modelos de lenguaje y **Pinecone** para las búsquedas vectoriales.

## Características
- **Ingestión de datos HTML**: Carga y procesamiento de documentos HTML para extraer y almacenar datos relevantes en Pinecone.
- **Asistente AI**: Responde preguntas sobre anime usando modelos de lenguaje integrados con Pinecone.
- **Frontend con Streamlit**: Interfaz simple y fácil de usar para interactuar con el chatbot.

## Demostración

En el siguiente video se muestra el funcionamoento del chat:
[Anime Chat Bot.webm](https://github.com/user-attachments/assets/2ea9cbc0-d0b3-4864-99c0-64c231d47dbf)

## Requisitos previos

1. **Pinecone API Key**: Necesitas una cuenta de Pinecone y una clave de API para interactuar con la base de datos vectorial.
2. **OpenAI API Key**: Necesitas una clave de API de OpenAI para generar embeddings y respuestas del modelo de lenguaje.
3. **Python 3.8+**: Este proyecto está desarrollado en Python, por lo que debes tener instalada una versión compatible.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tuusuario/anime-otaku-helper-bot.git
   cd anime-otaku-helper-bot
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` y añade tus claves de API:

   ```bash
   PINECONE_API_KEY=tu_clave_pinecone
   OPENAI_API_KEY=tu_clave_openai
   INDEX_NAME=nombre_de_tu_indice
   ```

## Ingestión de Documentos

El archivo `ingestion.py` se encarga de cargar y procesar documentos HTML (específicamente archivos `index.html`) que contienen información relevante sobre animes.

### Ejecución del Script de Ingestión

Para cargar documentos en Pinecone:

```bash
python ingest_docs.py
```

Este script:
- Recorre un directorio con archivos `index.html`.
- Extrae el texto de cada archivo HTML usando **BeautifulSoup**.
- Divide los documentos en fragmentos más pequeños utilizando un **text splitter**.
- Almacena los fragmentos de texto en Pinecone como vectores.

## Ejecución del Chat Assistant

El asistente responde preguntas del usuario en tiempo real. Se conecta a Pinecone para recuperar documentos y utiliza un modelo de lenguaje para generar respuestas contextualizadas.

### Ejecución del Chat

1. Corre el servidor de **Streamlit** para la interfaz del chatbot:

   ```bash
   streamlit run app.py
   ```

2. En tu navegador, accede a la URL `http://localhost:8501` y comienza a interactuar con el asistente.

### Funcionalidades del Chat:
- Responde preguntas relacionadas con anime.
- Muestra la conversación completa, junto con las fuentes de información extraídas.

## Archivos principales

- **`ingestion.py`**: Carga y procesa documentos HTML para almacenarlos en Pinecone.
- **`main.py`**: Interfaz del chatbot usando Streamlit.
- **`backend/core.py`**: Contiene la lógica principal del asistente, que se conecta a Pinecone y utiliza el modelo de lenguaje.

## Tecnologías utilizadas

- **Pinecone**: Base de datos vectorial para búsqueda y almacenamiento de documentos.
- **OpenAI**: API para generar embeddings y respuestas del modelo de lenguaje.
- **LangChain**: Framework para construir cadenas de lenguaje utilizando LLMs (Large Language Models).
- **BeautifulSoup**: Biblioteca para procesar y extraer texto de archivos HTML.
- **Streamlit**: Framework para crear aplicaciones web interactivas con Python.

## Contribución
Si encuentras algún problema o tienes alguna idea para mejorar este proyecto, siéntete libre de abrir un **issue** o hacer un **pull request**.
