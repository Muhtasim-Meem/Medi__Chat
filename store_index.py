from src.helper import load_pdf, text_split, download_huggingface_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import  PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY =os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


extracted_data = load_pdf(data ='Data/')
texts_chunks = text_split(extracted_data)
embeddings = download_huggingface_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medichat"

pc.create_index(
    index_name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-west-2",
    )
)

docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunks,
    index_name='medichat',
    embedding=embeddings,
)

