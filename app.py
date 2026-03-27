import streamlit as st

st.title("🚫 Cyberbullying Detection System")
st.write("This is a test deployment. If you see this, Streamlit Cloud is working!")

user_input = st.text_area("Enter text here...")

if st.button("Predict"):
    if user_input:
        st.subheader(f"You typed: {user_input}")
    else:
        st.warning("Please enter some text first!")
