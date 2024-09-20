# Comments:
# Simple web app deployed on streamlit cloud platform
# Streamlit provides the library to create the web app and also the cloud service to host the app
# Streamlit apps can also be deployed on other servers (but the
# deployment process is more demanding) such as:
# Infrastructure as a Service (IaaS): Digital Ocean, AWS, Google Cloud (more flexible and cheaper than PaaS, but more difficult to use)
# PaaS Options (best option, no server/OS maintenance, focus on coding/dev): Heroku, PythonAnywhere, Google App Engine, AWS
# PhysicaL servers (hardest to use, maintain the OS and the physical COMPONENTS of servers themselves)

# to have multiple pages for the web app:
# - create a "pages" folder in the project root directory
# - add the .py files for each of the pages in the pages folder. e.g. about.py
# - refresh browser
# the name of the .py file reflects the names of the pages in the tabs in the web app menu panel
# if any file name is changed the program should be interrupted with ctrl c and re-run
# (just refreshing the browser wont work)

# Git notes: before and after making changes
# Commit the initial state before making any changes
# If I do not want to keep the changes:
# - go to git (bottom-left menu of the screen)
# - right click onn the las commit
# - Reset Current Branch to Here... - Hard - Reset
# Right click on root directory - Reload from disk - voila!


import streamlit as st
import web_app_functions

my_todos = web_app_functions.get_todos()

st.set_page_config(layout="wide") #this method allows page configuration

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
