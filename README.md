# 📚 AI Study Routine Mapper

A simple AI/ML pet project that creates a personalized study routine based on:

- Subject difficulty
- Number of days left until the exam
- Available study hours per day

## AI/ML used

- Python
- Scikit-learn
- Decision Tree Classifier
- Pandas
- Streamlit

## How it works

1. The user enters the number of days remaining.
2. The user enters available study hours.
3. The user adds subjects and rates their difficulty.
4. A Decision Tree model predicts the priority level.
5. The application allocates study time and generates a daily routine.

## Run locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

## Example

If the user has:

- 7 days left
- 4 study hours per day
- Finance = Hard
- Marketing = Medium
- Communication = Easy

The application gives higher priority and more study time to Finance.

## Project purpose

This is a small student-focused AI/ML pet project designed to demonstrate how machine learning can be used for simple recommendation and prioritization problems.
