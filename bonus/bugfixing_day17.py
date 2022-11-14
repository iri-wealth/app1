import PySimpleGUI as sg
def km_to_miles(km):
    return km * 1.6

label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter km", key="km")
miles_button = sg.Button("Convert")
output = sg.Text(key="output")

window = sg.Window('km to Miles Convertor',
                    layout=[[label, input_box], [miles_button, output]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    match event:
        case "Convert":
            km = float(values["km"])
            result = km_to_miles(km)
            window['output'].update(f"value={result} miles")
        case sg.WIN_CLOSED:
            break
window.close()
