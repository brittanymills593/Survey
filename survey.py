import streamlit as st
import pandas as pd
import os

csv_file = "responses.csv"

st.title("Feedback to discuss")

menu = st.sidebar.selectbox("Menu", ["Fill Survey", "View Responses"])

# ---------------- SURVEY ----------------
if menu == "Fill Survey":

    st.write("Please answer the following questions.")

    # Question 1
    q1 = st.multiselect(
        "1. What should the Monday and Friday morning meetings look like?",
        [
            "What we do currently works well",
            "No meeting",
            "Split into haemonc and solid",
            "What we currently do without going through the rota"
        ]
    )

    q1_other = st.text_area("Other suggestions for Question 1")

    # Question 2
    q2 = st.multiselect(
        "2. What do we want included in the CS meeting?",
        [
            "The current structure is good",
            "The overview of solid and haemonc is repetitive from individual meetings and could be removed",
            "More feedback on projects going on within the department",
            "Presentations on interesting cases"
        ]
    )

    q2_other = st.text_area("Other suggestions for Question 2")

    # Question 3
    q3 = st.multiselect(
        "3. How could our current appraisal process be improved?",
        [
            "More guidance and structure for goals",
            "Mikel to attend",
            "Feedback from colleagues to be included"
        ]
    )

    q3_other = st.text_area("Other suggestions for Question 3")

    if st.button("Submit"):

        response = pd.DataFrame([{
            "Morning Meetings": ", ".join(q1),
            "Morning Meetings Other": q1_other,
            "CS Meeting": ", ".join(q2),
            "CS Meeting Other": q2_other,
            "Appraisal Process": ", ".join(q3),
            "Appraisal Process Other": q3_other
        }])

        if os.path.exists(csv_file):
            response.to_csv(csv_file, mode='a', header=False, index=False)
        else:
            response.to_csv(csv_file, index=False)

        st.success("Thank you! Your response has been saved.")


# ---------------- ADMIN VIEW ----------------
elif menu == "View Responses":

    st.subheader("Admin Access Required")

    password = st.text_input("Enter password", type="password")

    if password == "NGS":

        st.success("Access granted")

        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            st.dataframe(df)

            st.download_button(
                "Download Responses",
                df.to_csv(index=False),
                file_name="NGS_survey_responses.csv"
            )
        else:
            st.warning("No responses yet.")

    elif password != "":
        st.error("Incorrect password")
