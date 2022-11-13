import PySimpleGUI as sg

label = sg.Text("What are dolphins? ")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
close_button = sg.Button("Exit")

window = sg.Window("What are dolphins App", layout=[[label],
                                              [option1], [option2], [option3],
                                              [option4], [close_button]])

window.read()
print("Thank you for your answer")
window.close()
