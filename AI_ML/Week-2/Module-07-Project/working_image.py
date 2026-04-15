import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = my_api_key)

images =st.file_uploader(
        "Upload the Photos of Your Note",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )


if images:
  pil_images = [Image.open(image) for image in images]
  prompt = """Summarize the picture in note format at max 100 words 
  Use bullet points and subheadings where necessary."""
  response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = [pil_images, prompt]
  )
  st.text(response.text)
