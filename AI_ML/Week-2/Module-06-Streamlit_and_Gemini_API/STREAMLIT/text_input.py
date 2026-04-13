import streamlit as st

# st.write("This is a text input example.")
st.title("Text Input Example", anchor = False)
st.header("Content 1", divider = True)
st.subheader("Content 1.1")
st.text("Hello World!")

st.markdown(":orange-background[This is a markdown text. You can use :red[**bold**] or *italic* formatting.]:world_map:")

a = 10
b = 10
st.write(a,b)