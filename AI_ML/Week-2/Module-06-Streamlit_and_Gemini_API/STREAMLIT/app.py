from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
  model = "gemini-3-flash-preview",
  contents = "Tell me a joke"
)

print(response.text)
st.markdown(response.text)

st.divider()

st.title(f"Response from API Depends on User Input:", anchor = False)
user_input = st.text_input("Enter your input here:")


