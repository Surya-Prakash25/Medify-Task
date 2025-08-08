from flask import Flask, request, jsonify
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


# ==== STEP 1: Setup LLM with new API ====
llm = GoogleGenAI(model="models/gemini-1.5-flash")

# ==== STEP 2: Setup Embeddings ====
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ==== STEP 3: Apply settings globally ====
Settings.llm = llm
Settings.embed_model = embed_model

# ==== STEP 4: Load Resume ====
documents = SimpleDirectoryReader(input_files=["resume.pdf"]).load_data()

# ==== STEP 5: Create Index ====
index = VectorStoreIndex.from_documents(documents)

# ==== STEP 6: Setup Query Engine ====
query_engine = index.as_query_engine(similarity_top_k=3)

# ==== STEP 7: Create Flask API ====
app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Query is required"}), 400

    response = query_engine.query(
        f"You are an assistant that only answers using the resume content provided. "
        f"If the answer is not in the resume, say 'Not found in resume.'\nQuestion: {query}"
    )

    return jsonify({"query": query, "response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)
