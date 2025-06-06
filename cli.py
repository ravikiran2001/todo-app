#from  functions import get_todos,write_todos
import time

import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
while True:
    user_action = input("Type add or show or edit or exit or complete: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)


    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row= f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            number =  number-1

            todos = functions.get_todos()

            new_todo = input("enter the new one: ")
            todos[number] = new_todo +'\n'

            functions.write_todos(todos)

        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index=number-1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} has been removed."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command")
print("Thank you Bye")