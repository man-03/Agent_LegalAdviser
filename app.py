import streamlit as st
from agent import HybridAgent

st.title("Indian Law Assistant (Hybrid)")
st.caption("📄 Answers from Indian Acts | 🌐 Fallback to Groq if needed")

agent = HybridAgent()
query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        answer = agent.query(query)
        st.markdown(answer)
