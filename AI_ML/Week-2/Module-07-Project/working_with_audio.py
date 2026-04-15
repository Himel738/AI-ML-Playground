from gtts import gTTS
import streamlit as st
import io

text = "Hello, welcome to the world of audio processing with Python!"

speech = gTTS(text=text, lang='en', slow=False)


audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)

st.audio(audio_buffer.getvalue())