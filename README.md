# Agent_Legal_Adviser
Indian Law AI Assistant (Hybrid)
This is an intelligent legal assistant that can answer questions about Indian laws using embedded PDFs and fallback to Groq LLM (LLaMA 3) when needed.

Features
Answers legal questions using Indian Acts embedded locally.
Supports offline semantic search via HuggingFace embeddings and ChromaDB.
Falls back to Groq (LLaMA 3) for general or global queries not found in documents.
Streamlit-based interface for interactive Q&A.

Setup Instructions
Clone the Repository

git clone https://github.com/your-username/indian-law-ai.git
cd indian-law-ai

Install Dependencies
1. pip install -r requirements.txt
2. Add Indian Acts
3. Download and add the following PDFs to data/acts/:
4. Constitution of India
5. Indian Penal Code (IPC)
6. Code of Criminal Procedure (CrPC)
7. Code of Civil Procedure (CPC)
8. Information Technology Act
9. Right to Information Act
10. GST Act
11. Environmental Protection Act
12. Consumer Protection Act
13. Code on Wages
14. Digital Personal Data Protection Act

All are available at:
https://legislative.gov.in
https://prsindia.org

Generate Embeddings
python embed.py

Run the Application
streamlit run app.py

How It Works
If the query matches content in your PDFs, it responds from local ChromaDB.
If not, it falls back to Groq (LLaMA 3) for a general answer.
Embeddings are generated using all-MiniLM-L6-v2.
