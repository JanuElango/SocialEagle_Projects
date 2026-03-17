import pandas as pd
import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

# -----------------------------
# CACHE SYSTEM (VERY IMPORTANT)
# -----------------------------
@st.cache_resource
def load_system():
    df = pd.read_excel("IT_Banking_Onboarding_Incident_Tickets.xlsx")

    docs, texts = [], []

    for _, row in df.iterrows():
        text = " | ".join([f"{c}: {row[c]}" for c in df.columns])
        docs.append(Document(page_content=text))
        texts.append(text)

    # Semantic (FAISS)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Keyword (BM25)
    bm25 = BM25Okapi([t.split() for t in texts])

    return retriever, bm25, texts

retriever, bm25, texts = load_system()

# -----------------------------
# HYBRID SEARCH
# -----------------------------
def hybrid_search(query):
    sem_docs = retriever.invoke(query)

    scores = bm25.get_scores(query.split())
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]
    key_docs = [texts[i] for i in top]

    combined = list(set([d.page_content for d in sem_docs] + key_docs))
    return "\n".join(combined[:4])  # limit tokens

# -----------------------------
# LLM
# -----------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# -----------------------------
# CHAT FUNCTION
# -----------------------------
def chat_agent(query, chat_history):

    context = hybrid_search(query)

    history = "\n".join(
        [f"User: {h['user']}\nAssistant: {h['bot']}" for h in chat_history[-3:]]
    )

    prompt = f"""
You are a professional IT Incident Analysis Assistant.

- Answer clearly and concisely
- Use bullet points where helpful
- If data is tabular, return ONLY a clean table

Table format strictly:
Column1 | Column2 | Column3
------- | ------- | -------
value1  | value2  | value3

Conversation:
{history}

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    return response.content