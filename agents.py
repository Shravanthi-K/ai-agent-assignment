class GeneratorAgent:
    def generate(self, grade, topic, feedback=None):
        """
        Generates educational content based on grade and topic.
        If feedback is provided, content is simplified.
        """

        if feedback:
            explanation = (
                "An angle is made when two lines meet. "
                "Angles can be small or big."
            )
        else:
            explanation = (
                "An angle is formed when two lines meet at a point. "
                "Angles can be small or big."
            )

        mcqs = [
            {
                "question": "What is an angle?",
                "options": [
                    "A number",
                    "Two lines meeting at a point",
                    "A circle",
                    "A square"
                ],
                "answer": "Two lines meeting at a point"
            }
        ]

        return {
            "grade": grade,
            "topic": topic,
            "explanation": explanation,
            "mcqs": mcqs
        }


class ReviewerAgent:
    def review(self, content, grade):
        """
        Reviews generated content for correctness and age appropriateness.
        """
        feedback = []

        # Age-appropriateness check
        if len(content["explanation"].split()) > 25:
            feedback.append("Explanation is too complex for Grade 4")

        # Validate MCQs
        for i, mcq in enumerate(content["mcqs"]):
            if mcq["answer"] not in mcq["options"]:
                feedback.append(f"MCQ {i+1} has an invalid answer")

        if feedback:
            return {
                "status": "fail",
                "feedback": feedback
            }

        return {
            "status": "pass",
            "feedback": []
        }


if __name__ == "__main__":
    generator = GeneratorAgent()
    reviewer = ReviewerAgent()

    # First generation
    content = generator.generate(4, "Types of angles")
    print("GENERATOR OUTPUT:")
    print(content)

    # Review
    review = reviewer.review(content, 4)
    print("\nREVIEWER OUTPUT:")
    print(review)

    # One-time refinement if failed
    if review["status"] == "fail":
        refined = generator.generate(
            4,
            "Types of angles",
            feedback=review["feedback"]
        )
        print("\nREFINED OUTPUT:")
        print(refined)
