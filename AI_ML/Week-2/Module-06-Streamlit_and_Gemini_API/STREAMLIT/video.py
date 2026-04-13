import streamlit as st
st.title("Input Your Files-", anchor = False)
st.divider()

st.video("video/bike.mp4", loop = True)

videos = st.file_uploader("Enter Your Video Files",
                 type=["mp4", "avi", "mov"]
                )
button = st.button("Submit")

if button:
  if videos:
    st.video(videos)
    st.success("Video uploaded successfully!")
  else:
    st.error("Please upload a video file before submitting.")
