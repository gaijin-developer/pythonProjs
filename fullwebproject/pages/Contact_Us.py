import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address", placeholder="test@gmail.com")
    message = st.text_area("Enter your message here", placeholder="message...")
    message = f"""{message} 
{user_email}"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Message sent successfully")
