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
            if response or response == 0:
                st.session_state.responses.append(response)
                st.session_state.question_index += 1

    # If all questions are answered, redirect to summary page
    elif st.session_state.question_index == len(questions):
        show_summary_and_analysis()
