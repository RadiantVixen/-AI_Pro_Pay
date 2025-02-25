from pypdf import PdfReader
from llama_cpp import Llama
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from langchain.vectorstores import Chroma

llm = Llama(model_path="path/to/llama-2-7b.Q4_K_M.gguf")
db = Chroma(persist_directory="db")  # Stores document embeddings

def extract_text(pdf_file):
    text = ""
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

@api_view(["POST"])
def upload_pdf(request):
    file = request.FILES["file"]
    text = extract_text(file)
    db.add_texts([text])
    return Response({"message": "PDF Uploaded & Processed"})

@api_view(["POST"])
def ask_question(request):
    query = request.data.get("question", "")
    results = db.similarity_search(query)
    response = llm(results[0].page_content)
    return Response({"answer": response})
