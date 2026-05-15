import streamlit as st
import pandas as pd
import os

csv_file = "responses.csv"

st.title("Feedback Survey")

menu = st.sidebar.selectbox("Menu", ["Fill Survey", "View Responses"])

# ---------------- SURVEY ----------------
if menu == "Fill Survey":

    st.write("Please enter any issues or topics you would like to discuss.")

    issues = st.text_area(
        "",
        height=250
    )

    if st.button("Submit"):

        response = pd.DataFrame([{
            "Issues to discuss": issues
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
