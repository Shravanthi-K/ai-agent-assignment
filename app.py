import streamlit as st
from agents import GeneratorAgent, ReviewerAgent

st.set_page_config(page_title="AI Agent Assessment", layout="centered")

st.title("🧠 Agent-Based Educational Content Generator")

st.markdown("This app demonstrates a Generator Agent and a Reviewer Agent working together.")

grade = st.number_input("Enter Grade", min_value=1, max_value=12, value=4)
topic = st.text_input("Enter Topic", value="Types of angles")

if st.button("Run Agent Pipeline"):
    generator = GeneratorAgent()
    reviewer = ReviewerAgent()

    st.subheader("🔹 Generator Output")
    content = generator.generate(grade, topic)
    st.json(content)

    st.subheader("🔹 Reviewer Feedback")
    review = reviewer.review(content, grade)
    st.json(review)

    if review["status"] == "fail":
        st.subheader("🔄 Refined Output")
        refined = generator.generate(
            grade,
            topic,
            feedback=review["feedback"]
        )
        st.json(refined)
