import streamlit as st

import segno
import io


@st.dialog("Create New Subject")

def share_subject_dialog(subject_name, subject_code):
    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to join")

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind='png', scale = 10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link')
        st.code(join_url, language='text')
        st.code(subject_code, language='text')
        st.info('Copy this link to share on whatsapp or Email')

    with col2:
        st.markdown('###  Scan to join')
        st.image(out.getvalue(),caption='QRCODE for class joining')
        
    # st.write("Enter the details of the new subject below:")
    # subject_code = st.text_input("Subject code", placeholder="e.g. MATH101")
    # name = st.text_input("Subject name", placeholder="e.g. Calculus I")
    # section = st.text_input("Section", placeholder="e.g. A")


    # if st.button("Create Subject", type='primary', width='stretch'):
    #     if subject_code and name and section:
    #         try:
    #             create_subject(subject_code, name, section, teacher_id)
    #             st.toast("Subject created successfully!")
    #             st.rerun()

    #         except Exception as e:
    #             st.error(f"Error creating subject: {str(e)}")

    #     else:
    #         st.warning("Please fill  all the fields to create a subject.")