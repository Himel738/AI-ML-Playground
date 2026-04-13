import streamlit as st
st.title("Input your information", anchor = False)
st.divider()

name = st.text_input("Enter Your Name:",placeholder="Type your name here")
# st.write("Your name is:", name)

st.divider()

age = st.number_input("Enter Your Age:", min_value=0, max_value=120, step=1, value = None, placeholder="Type your age here")

profession = st.selectbox("Choose Your Profession:", options=["Developer", "Designer", "Manager", "Other"], accept_new_options=True)

pressed = st.button("Enter to Confirm", type="primary")

if pressed:
    st.write(f"Your name is: {name}, Your age is: {age}, and Your profession is: {profession}")


st.divider()

# password = st.text_input("Enter Your Password:", type="password", placeholder="Type your password here")
# st.write("Your password is:", password)