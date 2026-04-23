import streamlit as st

from src.database.db import create_subject


@st.dialog("Create New Subject")

def create_subject_dialog(teacher_id):
    st.write("Enter the details of the new subject below:")
    subject_code = st.text_input("Subject code", placeholder="e.g. MATH101")
    name = st.text_input("Subject name", placeholder="e.g. Calculus I")
    section = st.text_input("Section", placeholder="e.g. A")


    if st.button("Create Subject", type='primary', width='stretch'):
        if subject_code and name and section:
            try:
                create_subject(subject_code, name, section, teacher_id)
                st.toast("Subject created successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error creating subject: {str(e)}")

        else:
            st.warning("Please fill  all the fields to create a subject.")