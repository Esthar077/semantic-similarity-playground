import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

@st.cache_resource(show_spinner="Loading embedding model...")
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(sentence_a, sentence_b):
    model = load_model()

    embeddings = model.encode([sentence_a, sentence_b])

    vector_a, vector_b = embeddings

    dot_product = np.dot(vector_a, vector_b)
    magnitude = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)

    similarity = np.clip(dot_product / magnitude, -1.0, 1.0)
    angle = np.degrees(np.arccos(similarity))

    return float(similarity), float(angle)