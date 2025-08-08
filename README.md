# 📄 Resume Q&A API using Gemini and Flask

This project allows you to **ask questions based on the content of a given resume**.  
It uses **Google Gemini API** for language understanding and **HuggingFace embeddings** for semantic search within the resume content.

---

## 🚀 Features
- Upload a resume (PDF) and index its contents.
- Ask natural language questions about the resume.
- Get precise answers using AI and vector search.
- REST API built with Flask.
- Easily testable using **Postman**.

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Flask** (API framework)
- **Google Gemini API** (LLM)
- **HuggingFace Embeddings** (for semantic similarity)
- **llama_index** (for indexing and searching)
- **Postman** (for API testing)
---

## 📂 Project Structure
.
├── app.py # Main Flask API
├── resume.pdf # Resume file to query
├── requirements.txt # Python dependencies
└── README.md # Documentation
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/your-username/resume-qa-api.git
cd resume-qa-api

### 2️⃣ Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
### 3️⃣ Install dependencies
pip install -r requirements.txt
### 4️⃣ Add your Google Gemini API Key
In app.py, replace:

os.environ["GOOGLE_API_KEY"] = "Your Gemini Api key"
with your actual key.

### 5️⃣ Add your resume file
Place your resume.pdf in the project root.

🖥️ How It Works (Workflow)

flowchart TD
    A[Start] --> B[Load Resume PDF]
    B --> C[Create Embeddings using HuggingFace]
    C --> D[Index Resume using VectorStoreIndex]
    D --> E[Run Flask API Server]
    E --> F[POST /ask API with a query]
    F --> G[Query Engine searches vector index]
    G --> H[Gemini LLM generates answer]
    H --> I[Send JSON Response to Client]
    
#▶️ Running the Server

python app.py
Server will start at:

http://127.0.0.1:5000

#📬 API Endpoint
POST /ask
Request Body (JSON):

{
  "query": "What is the candidate's experience in Python?"
}
Response (JSON):

{
  "query": "What is the candidate's experience in Python?",
  "response": "The candidate has 3 years of Python experience in data science projects."
}
#🧪 Testing with Postman
Open Postman.

Create a new request.

Set Method → POST.

Set URL → http://127.0.0.1:5000/ask.

Go to the Body tab → select raw → choose JSON.

Enter your query:

{
  "query": "List the projects mentioned in the resume."
}
Click Send → You’ll get the AI-generated answer based on the resume.

📌 Notes
If the answer is not found in the resume, API will return:
"Not found in resume."
Works only with the resume file provided during server startup.

📜 License
This project is open-source under the MIT License.
