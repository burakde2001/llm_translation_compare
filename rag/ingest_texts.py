import os

from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.init_pinecone import vectorstore

def load_files(directory):
    texts = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(os.path.join(directory, file), "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts


def ingest_texts_to_pinecone(texts, metadata=None):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    for text in texts:
        chunks = text_splitter.split_text(text)
        metadata = metadata or [{} for _ in chunks]
        vectorstore.add_texts(texts=chunks, metadatas=metadata)


texts = load_files("filepath")
ingest_texts_to_pinecone(texts)
