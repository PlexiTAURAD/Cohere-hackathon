import streamlit as st

st.title("ODR AI ASSISTANTS")

first_input = st.text_input("Enter your text:")

if first_input:
    result = "Output"
    output = st.write(result)

    if output == 0:
        st.write("Please provide additional information:")
        second_input = st.text_input("Additional Information:")

if first_input or second_input:
    st.write("Analysis button")
    if st.button("Analytics"):
        st.write("Displaying bar graph")
