import streamlit as st

st.title("Input Your Files", anchor = False)
st.divider()
#Storage
st.image("images/himel.jpg")
#URL
st.image(
    "https://www.istockphoto.com/photo/eye-of-model-with-colorful-art-make-up-close-up-gm814423752-131755775",
    caption="Image from URL"
)
st.divider()

images = st.file_uploader("Enter Your Image",
                 type=["jpg", "jpeg", "png"],
                  accept_multiple_files=True
                )

if images:
  col = st.columns(len(images))
  for i,image in enumerate(images):
    with col[i]:
      st.image(image)