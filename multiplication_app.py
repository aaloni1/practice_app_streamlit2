import streamlit as st
import pandas as pd

st.title("Calculator")

# Define the calculator's functionality
def calculator(num1, num2, operator):
    """
    Performs basic mathematical operations.

    Args:
        num1: The first number.
        num2: The second number.
        operator: The mathematical operator.

    Returns:
        The result of the operation.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

# Create input fields for the numbers and operator
num1 = st.number_input("Enter the first number")
operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])
num2 = st.number_input("Enter the second number")

# Calculate and display the result
if st.button("Calculate"):
    result = calculator(num1, num2, operator)
    st.success(f"The result is: {result}")

# Display the calculator's layout
st.markdown("## Calculator Layout")
st.write(pd.DataFrame(
    [["C", "%", "X"],
     ["7", "8", "9", "÷"],
     ["4", "5", "6", "-"],
     ["1", "2", "3", "+"],
     ["0", ".", "="]],
    columns=["", "", "", ""]
).to_html(escape=False, index=False))
