def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo.capitalize() + "\n")

        # Write todos in the file
        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        # new_todos = []

        # for item in todos:
        # new_item = item.strip("\n")
        # new_todos.append(new_item)

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            # item = item.strip("\n")
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos("todos.txt")

            removed = todos.pop(number - 1)
            print(f"{removed.strip()} was removed from the list")

            write_todos("todos.txt", todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("This command is not valid.")

print("Bye!")
