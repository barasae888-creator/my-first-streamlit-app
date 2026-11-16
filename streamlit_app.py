import streamlit as st

st.set_page_config(
    page_title="My First App",
    page_icon="📊"
)

st.title("My very first Streamlit Application lol")

st.write("Welcome! My application is running online.How about yours?")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name.strip():
        st.success(f"Welcome, {name}!")
    else:
        st.warning("Please enter your name.")
