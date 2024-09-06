import streamlit as st
import web_app_functions

my_todos = web_app_functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    my_todos.append(new_todo)
    web_app_functions.write_todos(my_todos)

st.title("My Todo App")
st.subheader("This is my simple todo app.")
st.write("The purpose of this app is to checkout this thing called <b>streamlit</b>.",
         unsafe_allow_html=True)

# st.checkbox("Buy grocery")
# st.checkbox("Check me out")

#todo_count = 0

#for todo in my_todos:
for index, todo in enumerate(my_todos):
    #todo_count += 1
    #checkbox = st.checkbox(todo, key=f"todo{todo_count}")
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #print(checkbox)
        my_todos.pop(index)
        updated_todos = web_app_functions.write_todos(my_todos)
        del st.session_state[todo] #also delete the completed todo from the session sttae dictionary

        #to rerun the code:
        st.rerun()

st.text_input(label="", placeholder="add new todo...", on_change=add_todo, key="new_todo")
# when the user presses enter in the input box, the fnx add_todo is called, and the script is executed
# the todos.txt file is updated
# the for todo.. loop will run with the list of updated todos, thus a textbox will be
# creatd for the new todo item


#st.session_state
