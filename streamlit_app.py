import streamlit as st
import webbrowser

st.title("ODR AI ASSISTANTS")

input_text = st.text_input("Enter your text:")
output = 0

if input_text:
    # Perform processing on input_text here to get the output
    output = 1

if output == 0:
    additional_input = st.text_input("Additional Input:")

if output == 1:
    st.write("Output:", output)

if st.button("Analytics"):
    webbrowser.open_new_tab("https://www.example.com/bar-graph")
