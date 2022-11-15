import PySimpleGUI as sg
import functions1
import time

sg.theme("DarkGrey")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions1.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=10, image_source="complete.png", tooltip="Complete Todo", key="Complete")
exit_button = sg.Button("Exit")

layout = [[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions1.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions1.write_todos(todos)
            window['todos'].update(values='todos')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions1.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions1.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions1.get_todos()
                todos.remove(todo_to_complete)
                functions1.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select the item first", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

print("Thank you.Bye")
window.close()

