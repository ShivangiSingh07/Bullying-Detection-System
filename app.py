import streamlit as st
import pickle
import gdown

# Download trained model from Google Drive
url_model = "https://drive.google.com/uc?id=1lLRqjWrimDrexmV2LxPrJwVPmyxu5Yre"
output_model = "cyberbullying_model.pkl"
gdown.download(url_model, output_model, quiet=False)

# Download vectorizer from Google Drive
url_vec = "https://drive.google.com/uc?id=1Mlq_zfmoxk6Ko-oV31X0oJqrhE29KQEX"
output_vec = "vectorizer.pkl"
gdown.download(url_vec, output_vec, quiet=False)

# Load model + vectorizer
with open(output_model, "rb") as f:
    model = pickle.load(f)

with open(output_vec, "rb") as f:
    tfidf = pickle.load(f)

labels = {0: "Not harmful", 1: "Insult", 2: "Threat"}

st.title("🚫 Cyberbullying Detection System")
st.write("Enter a message to check if it's harmful:")

user_input = st.text_area("Enter text here...")

if st.button("Predict"):
    if user_input:
        data = tfidf.transform([user_input])
        prediction = model.predict(data)
        st.subheader(f"Result: {labels[prediction[0]]}")
    else:
        st.warning("Please enter some text first!")
