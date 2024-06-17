from functions import get_todos,write_todos
import functions as functions
import time

now = (time.strftime("%b %d, %Y %H:%M:%S"))
print("It is ",now)
while True:
    user_input = input("Enter add, show, edit or complete : \n")
    user_input = user_input.strip()
    user_input = user_input.lower()

    # match user_input:
    if user_input.startswith("add"):
        todo = user_input[4:]
        add_todo = todo.capitalize()

        todos = functions.get_todos()
        todos.append(add_todo + "\n")

        write_todos(todos_arg=todos,filepath="todos.txt")
    elif user_input.startswith("show"):
        todos = functions.get_todos()

        for i, todo in enumerate(todos):
            todo = todo.strip('\n')
            o_todo = f"{i + 1}-{todo}"
            print(o_todo)
    elif user_input.startswith("complete"):
         try:
            number = int(user_input[9:])
            todos = functions.get_todos()
            number = number - 1
            with open('./todos.txt', 'r') as file:
                todos = file.readlines()
                removed_todo = todos.pop(number)
                removed_todo = removed_todo.strip("\n")
                message = f"{removed_todo} was removed from your todos"
                functions.write_todos("todos.txt",todos)
                print(message)
         except IndexError:
                print("there is no todo with that number")
                continue
    elif user_input.startswith("edit"):
         try:
            number = int(user_input[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("enter a new todo: \n")
            todos[number] = new_todo + "\n"
            write_todos(todos,"todos.txt")
         except ValueError:
             print("command not valid")
             continue

    elif user_input.startswith("exit"):
        break
    else:
        print("command is not valid")
print("Thank you, bye!")