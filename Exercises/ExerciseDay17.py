import PySimpleGUI as sg
import Exec17functions as functions

label1 = sg.Text("Enter feet:")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.InputText(key="inches")

meters = sg.Text(key="result")

convert_button = sg.Button("Convert")
window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button, meters]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    converted_value = functions.convert(values["feet"], values["inches"])
    window["result"].update(value=converted_value)

window.close()
