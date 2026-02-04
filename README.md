# AI Agent Content Generator & Reviewer

This project demonstrates a simple **agent-based system** where content is generated and then reviewed using predefined rules. The goal is to show how structured logic can be used to simulate feedback, validation, and refinement instead of relying only on raw output.

The system is intentionally kept lightweight and explainable.

---

## Overview

The project consists of two main agents that work together in a clear pipeline:

- **Generator Agent**  
  Responsible for generating explanations and multiple-choice questions (MCQs) based on a given grade and topic.

- **Reviewer Agent**  
  Responsible for validating the generated content using predefined rules such as length suitability and answer correctness.

This setup mirrors real-world workflows where work is produced first and then reviewed before approval.

---

## How the System Works

1. The user provides input such as grade level and topic.
2. The **Generator Agent** creates:
   - A short explanation
   - One or more MCQs
3. The **Reviewer Agent** checks:
   - Whether the explanation is appropriate for the grade
   - Whether MCQ answers are valid
4. The system outputs:
   - Generated content
   - Review status (pass or fail)
   - Feedback if improvements are required

The logic is fully transparent and rule-driven.

---

## Example Use Cases

This project can be used as:
- A demonstration of agent-based workflows
- A learning example for rule-based validation systems
- A starting point for more advanced AI or LLM-powered agents
- A simple educational content generation prototype

---

## Design Decisions

- The system uses **deterministic rules** to keep behavior predictable.
- Agent responsibilities are clearly separated.
- Validation logic is explicit and easy to modify.
- The focus is on clarity rather than complexity.

---

## Possible Improvements

- Add more validation rules in the Reviewer Agent
- Support multiple difficulty levels
- Add logging or basic unit tests
- Integrate LLMs while retaining rule-based checks

---

## License

This project is open-source and available for learning and experimentation.

---

## Author

Created by **Shravanthi K K**

---
## Running the Project
git clone https://github.com/Shravanthi-K/ai-agent-assignment.git

cd ai-agent-assignment

python app.py

---
## Project Structure

```text
.
├── app.py
├── agents.py
└── README.md
