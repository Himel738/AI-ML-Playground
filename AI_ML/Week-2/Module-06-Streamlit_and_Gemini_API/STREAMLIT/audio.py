import streamlit as st
st.title("Input Your Files-", anchor = False)
st.divider()

st.audio("audio/tomal.mpeg", loop = True)

audios = st.file_uploader("Enter Your Audio Files",
                 type=["mp3", "wav", "mpeg"]
                )

if audios:
  st.audio(audios)