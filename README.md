# Bullying Detection System

## 📌 Overview
This project is a Machine Learning based text classification system that detects whether a given message is Bullying or Non-Bullying.  
It combines a trained ML model (Student A’s role) with a simple web interface and dashboard (Student B’s role) to make the system interactive and easy to use.

---

## ⚙️ Features
- Text Classification: Input a sentence → get prediction (Bullying / Non-Bullying).  
- Preprocessing: Removes stop words, punctuation, and URLs from text.  
- Model Training: Experiments with Random Forest, SVM, and Naive Bayes.  
- Evaluation: Confusion Matrix and Accuracy Graphs included.  
- Web Interface: Built with Streamlit for real-time interaction.  
- Safety Dashboard: Visualizations showing dataset distribution (e.g., religion-based vs. age-based bullying).  

---

## 🛠️ Tech Stack
- Python  
- Scikit-learn (ML models)  
- NLTK / Regex (text preprocessing)  
- Streamlit (UI & dashboard)  
- Matplotlib / Plotly (visualizations)  

---

## 🚀 How to Run
1. Clone the repository:
   `bash
   git clone https://github.com/your-username/bullying-detection.git
   cd bullying-detection
   `
2. Install dependencies:
   `bash
   pip install -r requirements.txt
   `
3. Run the Streamlit app:
   `bash
   streamlit run app.py
   `
4. Open the local URL shown in terminal (usually http://localhost:8501) to use the system.

---

## 📊 Example Usage
- Input: "You’re so stupid" → Output: Bullying  
- Input: "Have a nice day" → Output: Non-Bullying

---

## 📈 Results
- Best performing model: [Fill in after training]  
- Accuracy: [Fill in %]  
- Confusion Matrix and Accuracy Graphs included in /results folder.

---

## 🧩 System Architecture
Flow:  
User Input → Preprocessing → ML Model → Prediction → UI Display → Dashboard Visualization  

---
