import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator",anchor=False)
st.markdown("Upload Upto 3 Images to Generate Note Summary and Quiz Questions")
st.divider()

with st.sidebar:
    images =st.file_uploader(
        "Upload the Photos of Your Note",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    pil_images = [Image.open(image) for image in images] # Convert uploaded files to PIL Images for API compatibility
    
    if images:
        if len(images) > 3:
            st.warning("Please upload a maximum of 3 images.")
        else:
            st.subheader("Uploaded Images:")
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
    selected_option = st.selectbox(
        "Enter the Difficulty Level of the Quiz",
        options=["Easy", "Medium", "Hard"],
        index = None
    )
    pressed = st.button("Click the Button to Initiate AI", type = "primary")

if pressed:
    if not images:
        st.warning("Please upload at least one image to generate the note summary and quiz questions.")
    if not selected_option:
        st.warning("Please select a difficulty level for the quiz.")
    if images and selected_option:
        # Note
        with st.container(border=True):
            st.subheader("Your Note")
            with st.spinner("Generating Note Summary..."):
                generated_note = note_generator(pil_images)
                st.markdown(generated_note)
          
        #Audio
        with st.container(border=True):
            st.subheader("Audio Transcription")
            with st.spinner("Generating Note Summary..."):
                generated_note = generated_note.replace("#", "").replace("*", "").replace("-", "")
                audio_transcript = audio_transcription(generated_note)
                st.audio(audio_transcript)
            
        # Quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Level")
            with st.spinner("Generating Quizes..."):
                quizes = quiz_generator(pil_images,selected_option)
                st.markdown(quizes)

