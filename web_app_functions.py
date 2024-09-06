# To-Dos App - The Backend - The codebase that does the data processing, and sends data to the FE

FILEPATH = "todos.txt"

# Define function to grab existing todo list file and read it:
def get_todos(local_filepath = FILEPATH): #with parameter
    """ Reads an existing text file and returns the list of to-do items.""" #doc strings
    #with open('todos.txt', 'r') as local_file: #previously, I hard coded the file path, with args the file path can be requested as an input
    with open(local_filepath, 'r') as local_file: #when the interpreter reads the fnx, it will only
                                            # read the fnx syntax but wont execute the lines.
                                            #upon the function call with "todo_list = get_todos('todos.txt')" for example, where the input/arg is provided,
                                            #the interpreter goes back to the fnx definition and executes the function lines - so filepath will be replaced 
                                            #with 'todos.txt' as parameter (local_filepath) argument/input.

        local_todo_list = local_file.readlines() #local variable declaration
    return local_todo_list

# print(help(get_todos)) #doc strings

###########################################################################

# Function requiring multiple arguments: filepath, and what to write in the file
def write_todos(the_list, local_filepath = FILEPATH): #there is always a different list in each of the if elif blocks, so the_list cannot be set as a default param -  always put non-default params before deault params
    """ Writes a to-do list item in a text file."""
    with open(local_filepath, 'w') as local_file:
        local_todo_list = local_file.writelines(the_list)
    #return local_todo_list
    #no need to return anything, because this fnx is more like a procedure - it modifies the textfile inherently, but I do not need it to return any value
    #the fnx just has to go on an asignment, do it and thats it, I need no feedback from it
    #due to this, we do not need to capture any returned value in a variable, e.g new_todo_list = write_todos('todos.txt', todo_list)
    #instead just use: write_todos('todos.txt', todo_list)
    #the function returns a none object

# print("hello")
# print(hello)
#print(get_todos())

print()

if __name__ == "__main__":
    print(get_todos())
    print(__name__) #when directly run from this file, it is "__main__", but when run externally, it is "functions"
    print(type(__name__))