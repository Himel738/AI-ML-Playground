import streamlit as st
st.title("Calculator App", anchor = False)
st.divider()
num1 = st.number_input("Enter the first number", value = None, placeholder = "Enter the first number")
num2 = st.number_input("Enter the second number", value = None, placeholder = "Enter the second number")

operation = st.selectbox("Select the operation", options = ["Addition", "Subtraction", "Multiplication", "Division"])

button = st.button("Calculate")

if(button):
  if operation == "Addition":
    result = num1 + num2
    st.write(f"The result of {num1} + {num2} is: {result}")
  elif operation == "Subtraction":
    result = num1 - num2
    st.write(f"The result of {num1} - {num2} is: {result}")
  elif operation == "Multiplication":
    result = num1 * num2
    st.write(f"The result of {num1} * {num2} is: {result}")
  elif operation == "Division":
    if num2 != 0:
      result = num1 / num2
      st.write(f"The result of {num1} / {num2} is: {result}")
    else:
      st.write("Error: Division by zero is not allowed.")
  