import streamlit as st
import google.generativeai as genai

# Set the page title and icon
st.set_page_config(page_title="My AI App", page_icon="🚀")

st.title("My AI Application")
st.info("Built with Gemini & Google AI Studio")

# Input for the API Key (Safety first!)
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3-flash')

    # Input for the user prompt
    user_input = st.text_area("How can I help you today?", placeholder="Type your message here...")

    if st.button("Generate"):
        if user_input:
            with st.spinner("Thinking..."):
                response = model.generate_content(user_input)
                st.subheader("Response:")
                st.write(response.text)
        else:
            st.warning("Please enter a prompt first.")
else:
    st.warning("Please enter your API Key to start using the app.")
