import streamlit as st
import numpy as np
import joblib
import requests
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import time
import os

# URL of your CSV file on Google Drive (shared link format)
CSV_URL = "https://drive.google.com/uc?id=YOUR_FILE_ID"
CSV_PATH = "ai-medical-chatbot.csv"

# Download the CSV file from Google Drive if it doesn't exist locally
def download_file(url, save_path):
    if not os.path.exists(save_path):
        with st.spinner("📥 Downloading dataset... Please wait."):
            response = requests.get(url)
            with open(save_path, 'wb') as file:
                file.write(response.content)
            st.success("✅ Dataset successfully downloaded!")

# Download the CSV file
download_file(CSV_URL, CSV_PATH)

# Load precomputed embeddings and answers
try:
    embeddings = joblib.load('embeddings.joblib')
    answers = joblib.load('answers.joblib')
except FileNotFoundError:
    st.error("⚠️ Error: 'embeddings.joblib' or 'answers.joblib' not found. Please ensure they are in the same directory.")
    st.stop()

# Load the embedding model (same as used for embedding generation)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to find the most similar answer
def get_response(query):
    query = query.lower()
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    most_similar_idx = np.argmax(similarities)
    return answers[most_similar_idx]

# Streamlit UI Setup
st.set_page_config(page_title="MediBot - Your Health Companion", page_icon="🩺", layout="wide")

with st.sidebar:
    st.image("image1.png", caption="MediBot")
    st.markdown("### About MediBot\n MediBot is your friendly health assistant.")

st.title("🩺 MediBot - Your Health Companion")
st.markdown("Hello! I'm here to help with your health-related questions.")

with st.container():
    query = st.text_area("Your Question:", placeholder="E.g., What are the symptoms of anxiety?", height=120)
    submit_button = st.button("Get Answer", use_container_width=True, type="primary")

# Process the query and display the response
if submit_button:
    if not query.strip():
        st.warning("⚠️ Please enter a question to get a response.")
    else:
        with st.spinner("🤖 MediBot is thinking..."):
            time.sleep(1)
            response = get_response(query)
        
        # Display response in an attractive format
        st.markdown("### MediBot's Response")
        st.info(response)
        st.balloons()
