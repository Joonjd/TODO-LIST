import json
def save_data(todo):
    try:
        with open("todo_list", "w") as file:
            json.dump(todo, file)
    except FileNotFoundError:
        todo = []
def list_all_files(todo):
    if not todo:
        print("No Task")
    else:
        for x,y in enumerate(todo):
            print(f'{x+1} {y}')
def load_list():
    try:
        with open("todo_list", "r") as file:
            content = file.read().strip()
            if content == "":
                return []
            else:
                return json.loads(content)
    except FileNotFoundError:
        return []
def add_task(a, todo):
    todo.append(a)
    save_data(todo)

def update_task(todo, b, c):
    list_all_files(todo)
    todo[b-1] = c
    save_data(todo)

def delete_videos(todo, d):
    todo.pop(d-1)
    save_data(todo)    

def __main__():
    todo = load_list()
       
    while True:
        print("^"*20)
        print("1. Create a task\n2. Update a task\n3. Delete a task\n4. View tasks\n5. Exit\n") 
        print("^"*20)
        opt = int(input("Enter your choice\n"))
        match opt:
            case 1:
                a = input("Enter task\n")
                add_task(a, todo)
            case 2:
                list_all_files(todo)
                b = int(input("Enter task no:\n"))
                c = input("Enter new task\n")
                update_task(todo, b, c)
            case 3:
                list_all_files(todo)
                d = int(input("Enter no to delete"))
                delete_videos(todo, d)
            case 4:
                list_all_files(todo)

            case 5:
                break
if __name__  == "__main__":
    __main__()