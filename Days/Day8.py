while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo:") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo.capitalize())

            # Write todos in the file
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # new_todos = []

            # for item in todos:
            # new_item = item.strip("\n")
            # new_todos.append(new_item)

            new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(new_todos):
                # item = item.strip("\n")
                row = f"{index+1}.{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            number = int(input("Number of the todo to complete:"))
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            to_be_removed = todos[number-1]
            todos.pop(to_be_removed)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "exit":
            break
        case _:
            print("Sorry, wrong input!")

print("Bye!")
