import streamlit as st
def calculator(num1, num2, operation):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'
    else:
        return 'Invalid Operation'

# Streamlit app layout
st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Selectbox for operations
operation = st.selectbox(
    "Select operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)
