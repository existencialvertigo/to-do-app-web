import PySimpleGUI as sg
import Exec17functions as functions

label1 = sg.Text("Enter feet:")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.InputText(key="inches")
exit_button = sg.Button("Exit")

meters = sg.Text(key="result")

convert_button = sg.Button("Convert")
window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button, meters, exit_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Convert":
            try:
                converted_value = functions.convert(values["feet"], values["inches"])
                window["result"].update(value=converted_value)
            except ValueError:
                sg.Popup("Try again")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
