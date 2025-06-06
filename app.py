from flask import Flask, request, jsonify, render_template
from src.helper import load_pdf, text_split, download_huggingface_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from src.prompt import *

app = Flask(__name__)
load_dotenv()

# Direct API keys (keep these in a .env file ideally)
os.environ["PINECONE_API_KEY"] = "pcsk_79KcCc_LixCQEpCghNk34g8auDrNmt8eaazkgi2GnZyggsUPKbuh8UeTDPc23qxNo2JPPa"
os.environ["GOOGLE_API_KEY"] = "AIzaSyC0dCTs-psW6o7606iSk0OeZpcUpVT8AXE"

# Load embeddings and documents
embeddings = download_huggingface_embeddings()
extracted_data = load_pdf(data='Data/')
text_chunks = text_split(extracted_data)

# Vector store setup
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name='medichat',
    embedding=embeddings,
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Language model setup
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_output_tokens=50,
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# RAG chain
question_answer_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
rag_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=question_answer_chain)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get', methods=['POST'])
def chat():
    msg = request.form['msg']
    print("User Input:", msg)
    response = rag_chain.invoke({"input": msg})
    
    answer = response["answer"]
    prefix = "Based on the provided text, "
    if answer.startswith(prefix):
        answer = answer[len(prefix):]

    return answer


if __name__ == '__main__':
    app.run(debug=True)
