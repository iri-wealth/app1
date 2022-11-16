import streamlit as st
import functions

todos = functions.get_todos()

st.title("My First To Do App")
st.subheader("Welcome to my To Do list")
st.write("My To Do list helps me to improve my learning process")

st.checkbox("Learn Python fundamentals")
st.checkbox("Master Python advanced level")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a Todo", placeholder="Add new todo...")

