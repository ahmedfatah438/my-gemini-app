import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="My AI App", page_icon="🚀")
st.title("My AI Application")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # سنحاول تجربة الأسماء البرمجية الأكثر شيوعاً والمتاحة حالياً
        model_names = ['gemini-3-flash', 'gemini-1.5-flash', 'gemini-pro']
        
        # محاولة الاتصال بأول محرك متاح
        model = genai.GenerativeModel(model_names[0])
        
        user_input = st.text_area("How can I help you today?")

        if st.button("Generate"):
            if user_input:
                with st.spinner("Thinking..."):
                    try:
                        response = model.generate_content(user_input)
                        st.subheader("Response:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Try another model or check key: {e}")
            else:
                st.warning("Please enter a prompt.")
    except Exception as e:
        st.error("Connection Error. Please check your API Key.")
else:
    st.warning("Please enter your API Key to start.")
