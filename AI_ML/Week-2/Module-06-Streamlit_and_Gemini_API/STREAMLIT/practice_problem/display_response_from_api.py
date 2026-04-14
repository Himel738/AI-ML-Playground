from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
  model = "gemini-3-flash-preview",
  contents = "Tell me a joke about study"
)

st.title(f"Response from API Depends on Given Input:", anchor = False)

st.divider()

st.markdown(response.text)

st.divider()

st.title(f"Response from API Depends on Given Input:", anchor = False)
content = st.text_input("Enter your input here:",placeholder="Type something here...")

generate = st.button("Generate Text")

if generate:
    if content:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Improve this sentence professionally: " + content
        )
        st.divider()
        st.markdown(response.text)
    else:
        st.warning("⚠️ Please enter some text first!")