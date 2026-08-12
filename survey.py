import streamlit as st
import pandas as pd
import os

csv_file = "responses.csv"

st.title("Review of morning meeting")

menu = st.sidebar.selectbox("Menu", ["Fill Survey", "View Responses"])

# ---------------- SURVEY ----------------
if menu == "Fill Survey":

    st.write("Please answer the following questions.")

    # Question 1
    st.subheader("1. What should the Monday and Friday morning meetings look like?")

    q1_1 = st.checkbox("What we do currently works well")
    q1_2 = st.checkbox("Only one meeting - Friday")
    q1_3 = st.checkbox("Only one meeting - Monday")
    q1_4 = st.checkbox("Split into separate team meetings e.g. haemonc and solid")
    q1_5 = st.checkbox("What we currently do but with some changes to format (suggest below)")
    q1_6 = st.checkbox("Other (write below)")
    
    q1_other = st.text_area("Suggestions")


    # Question 2
#    st.subheader("2. What do we want included in the CS meeting?")

#    q2_1 = st.checkbox("The current structure is good")
#    q2_2 = st.checkbox("The overview of solid and haemonc is repetitive from individual meetings and could be removed")
#    q2_3 = st.checkbox("More feedback on projects going on within the department")
#    q2_4 = st.checkbox("Presentations on interesting cases")

#    q2_other = st.text_area("Other suggestions for Question 2")

    # Question 3
#    st.subheader("3. How could our current appraisal process be improved?")

#    q3_1 = st.checkbox("More guidance and structure for goals")
#    q3_2 = st.checkbox("Mikel to attend")
#    q3_3 = st.checkbox("Feedback from colleagues to be included")

#    q3_other = st.text_area("Other suggestions for Question 3")

#    if st.button("Submit"):

#        response = pd.DataFrame([{
 #           "Morning Meetings": ", ".join([
  #              option for option, selected in {
   #                 "What we do currently works well": q1_1,
    #                "No meeting": q1_2,
     #               "Split into haemonc and solid": q1_3,
      #              "What we currently do without going through the rota": q1_4
       #         }.items() if selected
        #    ]),
         #   "Morning Meetings Other": q1_other,

          #  "CS Meeting": ", ".join([
           #     option for option, selected in {
            #        "The current structure is good": q2_1,
             #       "The overview of solid and haemonc is repetitive from individual meetings and could be removed": q2_2,
              #      "More feedback on projects going on within the department": q2_3,
               #     "Presentations on interesting cases": q2_4
                #}.items() if selected
            #]),
 #           "CS Meeting Other": q2_other,

#            "Appraisal Process": ", ".join([
#                option for option, selected in {
#                    "More guidance and structure for goals": q3_1,
 #                   "Mikel to attend": q3_2,
  #                  "Feedback from colleagues to be included": q3_3
   #             }.items() if selected
    #        ]),
     #       "Appraisal Process Other": q3_other
     #   }])

#        if os.path.exists(csv_file):
 #           response.to_csv(csv_file, mode='a', header=False, index=False)
  #      else:
   #         response.to_csv(csv_file, index=False)

    #    st.success("Thank you! Your response has been saved.")


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
