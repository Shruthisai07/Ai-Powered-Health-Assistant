import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# download necessary nltk
nltk.download('punkt')
nltk.download('stopwords')
chatbot = pipeline("text-generation", model="distilgpt2")

def healtcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule a appointment with the doctor."
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly, if you have concerns, consult your doctor. "
    else:
        response = chatbot(user_input,max_length=800,num_return_sequences=1)
        return response[0]['generated_text']
    

def main():
    st.title("Health Care Assistant Chatbot")
    user_input = st.text_input("How Can I Help You")
    if st.button("Submit"):
        if user_input:
            st.write("User : ",user_input)
            with st.spinner("Processing your query, Please wait....."):
                response=healtcare_chatbot(user_input)
            st.write("Healthcare Assistant : ",response)
            print(response)
        else:
            st.write("Please enter a message to help you")
main()
