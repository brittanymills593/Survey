import streamlit as st
import pandas as pd
import os

csv_file = "responses.csv"

st.title("NGS Analysis Website Feedback Survey")

menu = st.sidebar.selectbox("Menu", ["Fill Survey", "View Responses"])

# ---------------- SURVEY ----------------
if menu == "Fill Survey":

    st.write("Please answer the following questions about the new comments website.")

    q1 = st.slider("1. I feel confident using the new comments website", 1, 5, 3)
    st.caption("1 = Not confident | 5 = Very confident")

    q2 = st.radio(
        "2. Does the comments website have everything needed for NGS analysis?",
        ["Yes", "Most", "Significantly lacking", "No"]
    )

    q3 = st.text_area("3. How could the website be improved?")
    q4 = st.text_area("4. Is there anything else that would improve our current process of NGS analysis? (not related to Marsgen reporter)")
    q5 = st.text_area("5. Any comments or suggestions")

    if st.button("Submit Survey"):

        response = pd.DataFrame([{
            "Confidence": q1,
            "NGS Needs": q2,
            "Website Improvements": q3,
            "NGS Process Improvements": q4,
            "Other Comments": q5
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
