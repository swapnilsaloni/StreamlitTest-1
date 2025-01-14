import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "your_openai_api_key"

# Function to handle sequential questions
def personal_transformation_questions():
    # Initialize session state variables for the question flow
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "responses" not in st.session_state:
        st.session_state.responses = []

    # Define questions and their types
    questions = [
        {"text": "How confident are you in your abilities? (1-Not confident at all to 5-Extremely confident)", "type": "objective"},
        {"text": "What strengths do you believe you possess?", "type": "subjective"},
        {"text": "How often do you compare yourself to others? (1-Never to 5-Always)", "type": "objective"}
    ]

    # Show the current question
    current_question = questions[st.session_state.question_index]
    st.write(current_question["text"])

    # Capture user response
    if current_question["type"] == "objective":
        response = st.slider("", 1, 5)
    else:
        response = st.text_input("Your response:")

    # Button to submit response and move to the next question
    if st.button("Submit"):
        if response:
            st.session_state.responses.append(response)
            if st.session_state.question_index < len(questions) - 1:
                st.session_state.question_index += 1
            else:
                st.write("Thank you for completing the questions!")
                st.write("Your responses:")
                for i, res in enumerate(st.session_state.responses):
                    st.write(f"Q{i+1}: {questions[i]['text']} - Your answer: {res}")

# Streamlit Sidebar
st.sidebar.image("Mini DesktopBuddha Logo.png", use_container_width=True)
st.sidebar.title("DesktopBuddha")
st.sidebar.subheader("Select a category")
category = st.sidebar.radio("", ["Personal Transformation", "Relationships", "Career Growth"])

# Main Section Title
st.title("DesktopBuddha")
st.write("Hello! How can we assist you today?")

# Conditional flow based on category selection
if category == "Personal Transformation":
    personal_transformation_questions()
else:
    st.write(f"You selected {category}. Please proceed with your queries.")
