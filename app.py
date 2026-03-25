import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="My AI App", page_icon="🚀")
st.title("My AI Application")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # كود ذكي لجلب المحركات المتاحة لمفتاحك فعلياً
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            # اختيار أول محرك متاح (سواء كان gemini-3 أو غيره)
            model = genai.GenerativeModel(available_models[0])
            
            user_input = st.text_area("How can I help you today?")

            if st.button("Generate"):
                if user_input:
                    with st.spinner("Thinking..."):
                        try:
                            response = model.generate_content(user_input)
                            st.subheader("Response:")
                            st.write(response.text)
                        except Exception as e:
                            st.error(f"Error: {e}")
                else:
                    st.warning("Please enter a prompt.")
        else:
            st.error("No models found for this API Key.")
            
    except Exception as e:
        st.error(f"Authentication Error: {e}")
else:
    st.warning("Please enter your API Key to start.")
