```markdown
# 🩺 MediBot – Your Health Companion

MediBot is a friendly health assistant chatbot that provides intelligent answers to your medical and mental health queries using a combination of **Sentence Transformers** and **Streamlit**. It’s powered by curated datasets from real doctor-patient interactions.

> ⚠️ **Disclaimer**: This chatbot is for informational purposes only and not a substitute for professional medical advice.

---

## 📸 Demo Screenshot

![MediBot Demo]
<img width="956" alt="screensot5" src="https://github.com/user-attachments/assets/7606faba-e136-4027-b01c-bf8329741053" />
<img width="956" alt="screensot4" src="https://github.com/user-attachments/assets/57cb4a14-add7-40aa-8a0a-f5eab0db2a69" />
<img width="956" alt="Screenshot57" src="https://github.com/user-attachments/assets/96233d65-f932-4769-8ca3-5c3622706d9d" />
---

## 🚀 Features

- 🔍 Semantic search over medical & mental health conversations
- 🧠 Uses **SentenceTransformer (`all-MiniLM-L6-v2`)** for embedding medical questions
- 🤖 Chatbot trained on **two datasets** with 10,000+ samples
- 🌐 Deployed using **Streamlit** with a clean UI
- 💡 Provides context-aware answers with real-world tone
- 🏥 Trained on topics including depression, anxiety, sleep issues, breathing techniques, CBT, and more

---

## 🧰 Tech Stack

| Technology        | Purpose                      |
|-------------------|-------------------------------|
| Python            | Core programming language     |
| Pandas            | Data processing               |
| SentenceTransformers | NLP embeddings            |
| Joblib            | Model & data serialization    |
| Scikit-learn      | Cosine similarity             |
| Streamlit         | Web UI framework              |
| TQDM              | Progress bar during training  |

---

## 📂 Folder Structure

```bash
├── app.py                  # Streamlit app
├── embeddings.joblib       # Precomputed sentence embeddings
├── answers.joblib          # Saved answers
├── ai-medical-chatbot.csv  # Medical Q&A dataset
├── mental-health.csv       # Mental health Q&A dataset
├── Screenshot57.PNG        # UI screenshot
└── README.md               # This file
```

---

## 📦 How to Run Locally

1. **Clone the repo**  
```bash
git clone https://github.com/Haseeb-01/HealthCare-Chatbot.git
cd HealthCare-Chatbot
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Download datasets (if not present) and generate embeddings**  
```bash
python generate_embeddings.py
```

4. **Run the Streamlit app**  
```bash
streamlit run app.py
```

---

## 🧪 Sample Questions to Try

- "How can I deal with anxiety?"
- "Why do I feel worthless all the time?"
- "What are some natural remedies for insomnia?"
- "How do breathing techniques help depression?"

---

## 📈 How it Works

1. User inputs a question via the Streamlit UI.
2. The input is encoded into a sentence vector using `all-MiniLM-L6-v2`.
3. This embedding is compared (via cosine similarity) with all precomputed embeddings.
4. The most semantically similar question’s answer is returned as a response.

---

## 🏁 Future Improvements

- Add live voice support using SpeechRecognition.
- Expand to include disease-specific datasets (e.g., diabetes, cardiac health).
- Add real-time chatbot-like chat flow.
- Deploy permanently on Hugging Face or Streamlit Cloud.

---

## 🧑‍💻 Developed By

Muhammad Haseeb Cheema

---

## 🙏 Acknowledgements

- Hugging Face for their awesome models
- Streamlit for enabling quick deployment
- Open-source contributors of the original datasets

---

## 📜 License

This project is open-source and free to use under the **MIT License**.

---

## 📋 Requirements:

```txt
streamlit
sentence-transformers
numpy
joblib
pandas
scikit-learn
requests
tqdm


---

#### ✅ 3. **Final Touches**
- ✅ Add a clickable LinkedIn badge in the **Developed By** section:
```markdown
## 🧑‍💻 Developed By

**Muhammad Haseeb Cheema**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/haseeb01/)  
[![GitHub](https://img.shields.io/badge/GitHub-121013?style=flat&logo=github&logoColor=white)](https://github.com/Haseeb-01)








