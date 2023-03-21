def get_todos():
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo.capitalize() + "\n")

        # Write todos in the file
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

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

            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            todos.pop(number - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("This command is not valid.")

print("Bye!")
