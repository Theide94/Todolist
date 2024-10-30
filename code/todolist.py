import json

help_text = """
Here is a list of possible commands:

Add - Add a task to your todo list
View - View all todo tasks
Mark - Mark a task as completed on your todo list
Delete - Delete todo list
Clear - Clear completed tasks off of todo list
Quit - Exit the program

"""

initial = "{\"todo_tasks\": []}"
file = "todo.json"

def initialize_database():
    try:
        open(file, "r")
    except:
        with open(file, "w") as todofile:
            todofile.write(initial)


if __name__ == '__main__':

    initialize_database()

    print("Welcome to your todo list! Please enter a command. Enter \"help\" to get a list of possible commands.")
    while(1):

        inputcommand = input().lower().strip()

        if inputcommand == "help":
            print(help_text)


        elif inputcommand == "add":

            todo_name = input("Enter todo task name:\n")
            todo_description = input("Enter todo task description:\n")

            with open(file, "r+") as todofile:
                todoentry = {
                    "name": todo_name,
                    "description": todo_description,
                    "status": "Not completed"
                }

                todo_data = json.load(todofile)
                todo_data["todo_tasks"].append(todoentry)

                todofile.seek(0)
                json.dump(todo_data, todofile)
            print("Added \"" + todo_name + "\" to the todo list")


        elif inputcommand == "view":
            print("\nHere is your todo list!\n")

            with open(file, "r+") as todofile:
                todo_list = json.load(todofile)

                if len(todo_list["todo_tasks"]) <= 0:
                    print("Your todo list is empty! Try adding some by entering \"add\"!")
                    continue

                for task in todo_list["todo_tasks"]:
                    print(task["name"] + " - Desc: " + task["description"] + " - Status: " + task["status"])


        elif inputcommand == "mark":

            mark_todo_name = input("Enter the name of the todo list entry you want to mark as completed\n")
            marked = False

            with open(file, "r+") as todofile:
                todo_list = json.load(todofile)

                for task in todo_list["todo_tasks"]:
                    if task["name"] == mark_todo_name:
                        task["status"] = "Completed!"
                        marked = True

                if not marked:
                    print("There are no tasks with the name \"" + mark_todo_name + "\".")
                else:
                    print("\n" + mark_todo_name + " is now marked as completed!")

                todofile.seek(0)
                todofile.truncate(0)
                json.dump(todo_list, todofile)


        elif inputcommand == "delete":

            open(file, "w").close()
            with open(file, "w") as todofile:
                todofile.write(initial)
            print("Deleted todo list!")


        elif inputcommand == "clear":

            with open(file, "r+") as todofile:
                todo_list = json.load(todofile)

                new_list = []

                for task in todo_list["todo_tasks"]:
                    if task["status"] != "Completed!":
                        new_list.append(task)
                    else: 
                        print("Clearing " + task["name"])
                        
                todofile.seek(0)
                todofile.truncate(0)
                todo_list["todo_tasks"] = new_list
                json.dump(todo_list, todofile)

                print("Cleared completed tasks!")


        elif inputcommand == "quit":
            break


        else:
            print("That is not a supported command. Enter \"help\" to get a list of possible commands.\n")





