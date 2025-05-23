import streamlit as st
import functions

todoList = functions.read_list()

def add_item():
    item = st.session_state["new_item"] + '\n'
    todoList.append(item)
    functions.write_list(todoList)

st.title("Your ToDo List")
st.subheader("Organize & plan your day")
st.write("You can click on the radio button to remove or type a new item below.")

for index, item in enumerate(todoList):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todoList.pop(index)
        functions.write_list(todoList)
        del st.session_state[item]
        st.rerun()

st.text_input(label='', placeholder="Enter new todo item here :)",
              on_change=add_item, key='new_item')
