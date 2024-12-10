import streamlit as st

st.title("Multiplication App")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

if st.button("Multiply"):
    result = num1 * num2
    st.success(f"The result of {num1} * {num2} is: {result}")
