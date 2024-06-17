import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkTeal2")
label = sg.Text("Type in a to-do")
input_box = sg.Input(tooltip="enter a todo",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
clock = sg.Text('', key="clock")

window = sg.Window('My Todo App', 
                   layout=[
                             [clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]
                   ],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=300)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
            window['todos'].Update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = ''.join(values["todo"].split("\n"))+"\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].Update(values=todos)
                window['todo'].Update(value='')
            except IndexError:
                sg.popup("please select an item ",font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todo']
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Select an Item")
        case "Exit":
            break
        case "todos":
            window["todo"].Update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()


