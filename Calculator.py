import streamlit as st
import math

# Set page layout to centered
st.set_page_config(layout="centered")

# Inject custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1A1A1A, #1A1A1A); /* Darker background color */
        padding: 20px;
        border-radius: 15px;
        border: 4px solid #333;
    }
    .stNumberInput input {
        border: 4px solid #333;
        border-radius: 5px;
        padding: 4px; /* Further reduced padding */
        background-color: #fff;
        color: black;
        text-align: right;
        font-size: 16px; /* Adjusted font size */
        font-weight: bold;
        width: 100%;
        margin-bottom: 2px; /* Reduced margin between input fields */
    }
    .stButton {
        font-size: 16px; /* Adjusted font size */
        font-weight: bold;
        width: 100%;
        margin-bottom: 2px; /* Reduced margin between buttons */
    }
    .result-container {
        color: white; /* Font color for result */
    }
    .history-container {
        color: white; /* Font color for history container */
    }
    .history-entry {
        color: white; /* Font color for individual history entries */
        margin-top: 2px; /* Space between history entries */
    }
    /* Custom CSS for specific headings and text */
    .stMarkdown h1 {
        font-size: 28px; /* Font size for "Calculator" */
        color: white; /* Font color for "Calculator" */
        margin-top: 0; /* Remove top margin */
        margin-bottom: 10px; /* Reduced space below the title */
        text-align: center; /* Center align the title */
    }
    .stMarkdown h3 {
        font-size: 20px; /* Font size for section headings */
        color: white; /* Font color for section headings */
        margin-top: 2px; /* Reduced space above each section */
        margin-bottom: 2px; /* Reduced space below each section */
        text-align: left; /* Left align section headings */
        display: flex; /* Align items in a row */
        align-items: center; /* Center align items vertically */
    }
    .stMarkdown h3 span {
        margin-left: 10px; /* Space between title and result */
        font-size: 18px; /* Font size for result */
        color: white; /* Font color for result */
    }
    .stMarkdown p {
        color: white; /* Font color for descriptions and other paragraphs */
        text-align: center; /* Center align description */
        margin-top: 0; /* Remove top margin */
        margin-bottom: 2px; /* Reduced space below paragraphs */
    }
    /* Specific CSS for Number 1 and Number 2 labels */
    .stTextInput label, .stNumberInput label {
        color: white; /* Change label color to white */
        font-size: 18px; /* Optional: Adjust font size */
    }
    /* Add space below input fields */
    .stNumberInput {
        margin-bottom: 20px; /* Increased space below input fields */
    }
    </style>
""", unsafe_allow_html=True)

# Title and header with HTML for styling
st.markdown("<h1>Calculator</h1>", unsafe_allow_html=True)
st.write("Perform basic and advanced calculations with ease.")

# Create a container for the calculator
with st.container():
    # Input fields for numbers without the extra heading
    num1_str = st.text_input("Enter Number 1", value="", key="num1")
    num2_str = st.text_input("Enter Number 2", value="", key="num2")

    # Convert text inputs to float if not empty
    try:
        num1 = float(num1_str) if num1_str else 0.0
        num2 = float(num2_str) if num2_str else 0.0
    except ValueError:
        st.write("Error: Invalid input. Please enter valid numbers.")
        num1 = 0.0
        num2 = 0.0

    # Initialize session state for history if it doesn't exist
    if "history" not in st.session_state:
        st.session_state.history = []

    # Operation buttons without the title
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    operation = None

    with col1:
        if st.button("➕", key="add"):
            operation = "add"
    with col2:
        if st.button("➖", key="subtract"):
            operation = "subtract"
    with col3:
        if st.button("✖️", key="multiply"):
            operation = "multiply"
    with col4:
        if st.button("➗", key="divide"):
            operation = "divide"
    with col5:
        if st.button("√", key="sqrt"):
            operation = "sqrt"
    with col6:
        if st.button("^", key="power"):
            operation = "power"
    with col7:
        if st.button("log", key="log"):
            operation = "log"

    # Perform calculation
    result = None
    if operation:
        try:
            if operation == "add":
                result = num1 + num2
                symbol = "+"
            elif operation == "subtract":
                result = num1 - num2
                symbol = "-"
            elif operation == "multiply":
                result = num1 * num2
                symbol = "*"
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                    symbol = "/"
                else:
                    result = "Error: Division by zero"
            elif operation == "sqrt":
                if num1 >= 0:
                    result = math.sqrt(num1)
                    symbol = "√"
                else:
                    result = "Error: Square root of negative number"
            elif operation == "power":
                result = math.pow(num1, num2)
                symbol = "^"
            elif operation == "log":
                if num1 > 0 and num2 > 0:
                    result = math.log(num1, num2)
                    symbol = "log"
                else:
                    result = "Error: Invalid logarithm operation"

            # Add to history, ensure most recent entry is first
            st.session_state.history.insert(0, f"{num1} {symbol} {num2} = {result}")
            # Limit history to last three calculations
            if len(st.session_state.history) > 3:
                st.session_state.history = st.session_state.history[:3]

        except Exception as e:
            result = f"Error: {str(e)}"

    # Display result
    st.markdown("<h3>Result: <span class='result-text'>{}</span></h3>".format(result if result is not None else ""), unsafe_allow_html=True)

    # Display history
    st.write("### Calculation History")
    with st.container():
        st.markdown('<div class="history-container">', unsafe_allow_html=True)
        for entry in st.session_state.history:
            st.markdown(f'<div class="history-entry">{entry}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
