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
    if st.session_state.question_index < len(questions):
        current_question = questions[st.session_state.question_index]
        st.write(current_question["text"])

        # Capture user response
        if current_question["type"] == "objective":
            response = st.slider("", 1, 5, key=f"slider_{st.session_state.question_index}")
        else:
            response = st.text_input("Your response:", key=f"text_input_{st.session_state.question_index}")

        # Button to submit response and move to the next question
        if st.button("Submit", key=f"submit_{st.session_state.question_index}"):
            if "last_response" not in st.session_state or st.session_state.last_response != response:
                st.session_state.responses.append(response)
                st.session_state.last_response = response
                st.session_state.question_index += 1

    # If all questions are answered, redirect to summary page
    elif st.session_state.question_index == len(questions):
        show_summary_and_analysis()

# Function to display summary and reflection report
def show_summary_and_analysis():
    st.write("Thank you for completing the questions!")
    st.write("### Your Responses:")

    questions = [
        "How confident are you in your abilities? (1-Not confident at all to 5-Extremely confident)",
        "What strengths do you believe you possess?",
        "How often do you compare yourself to others? (1-Never to 5-Always)"
    ]

    for i, res in enumerate(st.session_state.responses):
        st.write(f"Q{i+1}: {questions[i]} - Your answer: {res}")

    # Analyze and reflect on responses
    analysis = analyze_responses(st.session_state.responses)
    st.write("\n### Reflection Report")
    st.write(analysis)

# Function to analyze user responses and generate a reflection report
def analyze_responses(responses):
    confidence_level = responses[0]
    strengths = responses[1]
    comparison_level = responses[2]

    # Analyze confidence
    if confidence_level <= 2:
        confidence_analysis = "You may have some doubts about your abilities. Building small successes can help improve confidence."
    elif confidence_level <= 4:
        confidence_analysis = "You seem moderately confident. Recognizing your achievements can further strengthen this."
    else:
        confidence_analysis = "You have strong self-confidence. Keep leveraging this strength while staying open to growth."

    # Analyze comparison tendency
    if comparison_level <= 2:
        comparison_analysis = "You rarely compare yourself to others, which indicates strong self-assurance and focus."
    elif comparison_level <= 4:
        comparison_analysis = "You occasionally compare yourself to others. Try focusing on personal growth instead of external benchmarks."
    else:
        comparison_analysis = "Frequent comparisons might affect your self-esteem. Practice self-compassion and celebrate your unique journey."

    # Create reflection summary with bullet points
    reflection_report = (
        f"- **Confidence Analysis:** {confidence_analysis}\n"
        f"- **Your Strengths:** {strengths}\n"
        f"- **Comparison Tendency Analysis:** {comparison_analysis}"
    )

    return reflection_report

# Streamlit Sidebar
st.sidebar.image("Mini DesktopBuddha Logo.png", use_container_width=True)
st.sidebar.title("DesktopBuddha")
st.sidebar.subheader("Select a category")
category = st.sidebar.radio("", ["Personal Transformation", "Relationships", "Career Growth"])

# Main Section Title
st.title("DesktopBuddha")
st.write("Hello! How can we assist you today?")

# Arrange the three boxes horizontally
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Personal Transformation"):
        st.session_state.category_selected = "Personal Transformation"

with col2:
    if st.button("Relationships"):
        st.session_state.category_selected = "Relationships"

with col3:
    if st.button("Career Growth"):
        st.session_state.category_selected = "Career Growth"

# Conditional flow based on category selection
if "category_selected" in st.session_state:
    if st.session_state.category_selected == "Personal Transformation":
        personal_transformation_questions()
    else:
        st.write(f"You selected {st.session_state.category_selected}. Please proceed with your queries.")
