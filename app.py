import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(page_title="AI Study Routine Mapper", page_icon="📚")

# -----------------------------
# Load simple training data
# -----------------------------
data = pd.read_csv("study_data.csv")

X = data[["difficulty", "days_left", "hours_available"]]
y = data["priority"]

# Train a small ML model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

# -----------------------------
# App interface
# -----------------------------
st.title("📚 AI Study Routine Mapper")
st.write(
    "A simple AI/ML pet project that recommends study priority "
    "and creates a practical daily routine."
)

st.sidebar.header("Your Study Details")

days_left = st.sidebar.number_input(
    "Days until exam", min_value=1, max_value=365, value=7
)

hours = st.sidebar.number_input(
    "Study hours available per day", min_value=1.0, max_value=16.0, value=4.0, step=0.5
)

st.subheader("Add Your Subjects")

subjects = []

for i in range(5):
    col1, col2 = st.columns([3, 1])

    with col1:
        name = st.text_input(
            f"Subject {i+1}",
            placeholder="e.g. Marketing",
            key=f"name_{i}"
        )

    with col2:
        difficulty = st.selectbox(
            "Difficulty",
            [1, 2, 3],
            format_func=lambda x: {1:"Easy", 2:"Medium", 3:"Hard"}[x],
            key=f"difficulty_{i}"
        )

    if name.strip():
        subjects.append((name, difficulty))

if st.button("✨ Create My Study Routine"):

    if not subjects:
        st.warning("Please enter at least one subject.")
    else:
        results = []

        for name, difficulty in subjects:
            features = pd.DataFrame([{
                "difficulty": difficulty,
                "days_left": days_left,
                "hours_available": hours
            }])

            priority = model.predict(features)[0]

            # Score used only to allocate study time
            score = difficulty * 2 + (1 / days_left) * 10

            results.append({
                "Subject": name,
                "Difficulty": {1:"Easy", 2:"Medium", 3:"Hard"}[difficulty],
                "Priority": priority,
                "Score": score
            })

        result_df = pd.DataFrame(results)
        result_df = result_df.sort_values("Score", ascending=False)

        # Allocate time proportionally
        total_score = result_df["Score"].sum()
        result_df["Hours"] = (
            result_df["Score"] / total_score * hours
        ).round(1)

        st.success("Your personalized routine is ready! 🎯")

        st.subheader("📊 Recommended Priorities")

        display_df = result_df[[
            "Subject", "Difficulty", "Priority", "Hours"
        ]]

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("🗓️ Today's Routine")

        for _, row in result_df.iterrows():
            st.write(
                f"**{row['Subject']}** — "
                f"{row['Hours']} hour(s) — "
                f"{row['Priority']} Priority"
            )

        st.info(
            "The recommendation is based on subject difficulty, "
            "days remaining and available study time."
        )

st.divider()

st.caption(
    "Built with Python • Scikit-learn • Decision Tree • Streamlit"
)
