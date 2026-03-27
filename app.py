import streamlit as st
import pickle
import pandas as pd

# 1. Load the saved "Brain"
# Make sure these filenames match your .pkl files exactly
try:
    model = pickle.load(open('cyberbullying_model.pkl', 'rb'))
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Please upload cyberbullying_model.pkl and vectorizer.pkl to GitHub.")

# 2. Website UI
st.set_page_config(page_title="SafeGuard AI", page_icon="🛡️")

st.title("🛡️ Cyberbullying Detection System")
st.markdown("---")
st.write("This system uses Machine Learning to identify harmful messages including hate speech or harassment.")

# Sidebar for extra info (Great for Student B's Dashboard focus)
st.sidebar.header("About Project")
st.sidebar.info("This project classifies text into Bullying or Non-Bullying categories using NLP.")

# User Input
user_input = st.text_area("Enter a message to check if it's harmful:", placeholder="Type here...")

if st.button("Analyze Message"):
    if user_input:
        # 3. Process and Predict
        # Transform the input text just like we did in training
        data = tfidf.transform([user_input])
        prediction = model.predict(data)
        
        # 4. Display Result with some color
        st.markdown("### Analysis Result:")
        if prediction[0] == "Bullying": # Adjust this label based on your specific model output
            st.error(f"⚠️ Warning: This message is classified as **{prediction[0]}**")
        else:
            st.success(f"✅ Safe: This message is classified as **{prediction[0]}**")
    else:
        st.warning("Please enter some text first!")
