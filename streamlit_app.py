import streamlit as st

exec(open("model.ipynb").read())

st.title("ODR AI ASSISTANTS")

first_input = st.text_input("Enter your Query: ")

if first_input == '0' or '1':
     st.write(gen)
elif first_input == '5':
     warranty_input = st.text_input("Do you have warranty?")
     if warranty == 0:
        st.write("That's okay. You can visit our stores or connect with us at repairs@lenuwu.com to see how much it will cost you")
     if warranty == 1:
        st.write("Alright, you can come to our store or get a repairman to visit you and get your device repaired free of cost")
elif first_input == '6':
    if feelings == 8:
        st.write(feel)
    else:
        st.write(feel)
