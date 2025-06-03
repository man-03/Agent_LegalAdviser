import chromadb
from sentence_transformers import SentenceTransformer
from langchain_groq import ChatGroq

persist_directory = "chroma_storage"
collection_name = "indian_laws"

class HybridAgent:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name=collection_name)
        self.llm = ChatGroq(
            model_name="llama3-70b-8192",
            groq_api_key="ENTER GROQ API KEY"
        )

    def query(self, user_input):
        query_embedding = self.model.encode([user_input]).tolist()[0]
        results = self.collection.query(query_embeddings=[query_embedding], n_results=3)
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        #if documents and distances[0] < 1.0:
        if documents and distances[0] < 1.0:
            return "\n\n".join(
                f"• {doc}\n(Source: {meta['source']})"
                for doc, meta in zip(documents, metadatas)
            )
        else:
            #return self.llm.invoke(user_input)
            response = self.llm.invoke(user_input)
            return response.content

