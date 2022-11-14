FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH): # '"todos.txt"):
    """
    defines parameter which reads the text
    file and returns the list of
    todo item :param filepath: :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH): # "todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__=="__main__":
    print("hello from functions")
    print(get_todos())

