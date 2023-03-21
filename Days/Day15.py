# from Day14functions import get_todos, write_todos
import Day14functions
import time

now = time.strftime("%A %b %d, %Y %H:%M:%S")
print("It is ", now)
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = Day14functions.get_todos()

        todos.append(todo.capitalize() + "\n")

        # Write todos in the file
        Day14functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = Day14functions.get_todos()

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

            todos = Day14functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            Day14functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = Day14functions.get_todos()

            removed = todos.pop(number - 1)
            print(f"{removed.strip()} was removed from the list")

            Day14functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("This command is not valid.")

print("Bye!")