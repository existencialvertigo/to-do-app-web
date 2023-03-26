import streamlit as st
import functions

todos = functions.get_todos("Days/todos.txt")


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My Todo App")
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

for todo in todos:
    st.checkbox(todo)

st.session_state



