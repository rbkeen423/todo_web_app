FILEPATH = 'todoList.txt'

def read_list(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        local_list = file_local.readlines()
    return local_list


def write_list(todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_arg)

if __name__ == "__main__":
    print("Hello")