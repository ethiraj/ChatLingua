import streamlit as st
from langchain.llms import Cohere

cohere = Cohere(model='command-xlarge')

st.set_page_config(page_title="LinguaBot App", page_icon=":guardsman:", layout="wide")

st.markdown(
    """
    <style>
    .navbar {
        background-color: orange;
    }
    .navbar-brand {
        color: white;
        font-size: 30px;
        font-weight: bold;
        text-transform: uppercase;
    }
    </style>
    """,
    unsafe_allow_html=True
)

menu = ["Home"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Home":
    st.title("LinguaBot App")
    st.header("A fun and interactive way to explore the world of natural language processing with support for a variety of LLMs")
    text = st.text_input("Enter a text:")
    if st.button("Submit"):
        response = cohere(text)
        st.write("You entered:")
        st.write(text)
        st.write("Response:")
        st.write(response)
