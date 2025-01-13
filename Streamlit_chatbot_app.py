import streamlit as st
import openai
import sqlite3
import requests

# OpenAI API Key
openai.api_key = "your_openai_api_key"

# Function to insert data into the database
def save_to_database(userid, question, answer):
    conn = sqlite3.connect('chatbot_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO chat_log (userid, question, answer) VALUES (?, ?, ?)", 
              (userid, question, answer))
    conn.commit()
    conn.close()

# Function to generate summary report
def generate_summary_report():
    conn = sqlite3.connect('chatbot_data.db')
    c = conn.cursor()
    c.execute("SELECT userid, question, answer FROM chat_log")
    rows = c.fetchall()
    conn.close()
    return rows

# Streamlit UI
# Add a logo at the top
st.image("https://via.placeholder.com/150", width=150)  # Replace with your logo URL

# Update title and subtitle
st.title("Desktop Buddha")
st.subheader("A personal transformation tool")

# Add a label and text input for choosing help options
st.text("Please choose an option that you need help with:")

# Arrange the three buttons horizontally
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Personal Transformation"):
        user_query = st.text_input("Describe your personal transformation query:")
        if user_query:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_query}]
            )
            answer = response['choices'][0]['message']['content']
            st.write(f"Answer: {answer}")

with col2:
    if st.button("Relationships"):
        user_query = st.text_input("Describe your relationship query:")
        if user_query:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_query}]
            )
            answer = response['choices'][0]['message']['content']
            st.write(f"Answer: {answer}")

with col3:
    if st.button("Career Growth"):
        user_query = st.text_input("Describe your career growth query:")
        if user_query:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_query}]
            )
            answer = response['choices'][0]['message']['content']
            st.write(f"Answer: {answer}")
