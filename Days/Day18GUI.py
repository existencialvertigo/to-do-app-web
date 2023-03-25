import Day14functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=Day14functions.get_todos(), key="todos",
                      enable_events=True, size=(30, 15))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]

window = sg.Window("My To-Do App",
                   layout=layout,
                   font=("Helvetica", 15))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = Day14functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo.capitalize())
            Day14functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = Day14functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                Day14functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.Popup("Please select an item first", font=("Helvetica", 15))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = Day14functions.get_todos()
                todos.remove(todo_to_complete)
                Day14functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.Popup("Please select an item first", font=("Helvetica", 15))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()
