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
st.title("Simple Chatbot with Streamlit")
st.text_input("Enter your User ID", key="userid")
user_query = st.text_input("Ask a Yes/No question")

# Handle CrewAI Request
if st.button("Ask CrewAI"):
    crewai_response = requests.get(f"https://api.crewai.com/ask?question={user_query}")
    crewai_answer = crewai_response.json().get("answer", "No response available")

    # Display CrewAI response
    st.write(f"CrewAI Answer: {crewai_answer}")
    save_to_database(st.session_state.userid, user_query, crewai_answer)

# Handle OpenAI Chat
if st.button("Ask OpenAI"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_query}]
    )
    openai_answer = response['choices'][0]['message']['content']
    st.write(f"OpenAI Answer: {openai_answer}")
    save_to_database(st.session_state.userid, user_query, openai_answer)

# Generate Summary Report
if st.button("Generate Summary Report"):
    report = generate_summary_report()
    for entry in report:
        st.write(f"User ID: {entry[0]} | Question: {entry[1]} | Answer: {entry[2]}")
