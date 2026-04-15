from google import genai
import os, io
from dotenv import load_dotenv
from gtts import gTTS


# Load environment variables from .env file
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = my_api_key)

# Note Generation
def note_generator(images):
  prompt = """Summarize the picture in note format at max 100 words 
  Use bullet points and subheadings where necessary."""
  response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = [images, prompt]
  )
  return response.text

def audio_transcription(text):
  speech = gTTS(text=text, lang='en', slow=False)
  audio_buffer = io.BytesIO()
  speech.write_to_fp(audio_buffer)
  return audio_buffer.getvalue()

def quiz_generator(image,difficulty):
  prompt = """Generate a quiz based on the content of the image.
  The quiz should consist of 5 questions with multiple-choice answers.
  The difficulty level of the quiz should be {difficulty}.
  Use a mix of question types, including true/false, multiple-choice, and fill-in-the-blank. 
  Ensure that the questions are clear and concise, and that the answer choices are plausible to make the quiz engaging and challenging for learners."""
  response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = [image, prompt]
  )
  return response.text

