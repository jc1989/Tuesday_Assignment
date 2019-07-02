import json
#Showing the user their options, returning their input
print("\n--Welcome to the ToDoList App!--")
def menu():
    user_input = input("\n\n--------------Menu--------------\n" + "Press 1 to add task\n" + "Press 2 to delete task\n" + "Press 3 to view all tasks\n" +  "Press q to quit: \n\n")
    menu_checker(user_input)

#checking the user selection and returning the value
def menu_checker(user_input):
    
    if user_input != 'q':
        if user_input == '1':
            print("\n--You have chosen to add a task--")
            add_task()
        elif user_input == '2':
            print("\n\n*Warning* You have chosen to delete a task *WARNING*\n")
            del_task()
        elif user_input == '3':
            print("\n\nYou have chosen to view all tasks")
            view_tasks()
        else:
            print("Please try again")
    else:
        quit()

tasks = [] #task array
#tasks = {"title": , "priority": "Medium"}

def write_json():
    with open("TaskList.json","w") as file:
        json.dump(tasks,file)

with open("TaskList.json") as file:
        openjson = json.load(file)

# with open("TaskList.json") as file:
#     openjson = json.load(file)

# def open_json():
    # return openjson
        
tasks = openjson

def add_task():
    title_input = input("What task would you like to add to your To Do List?\n\n")
    priority = int(input("\nWhat is the priority of the task?\nChoose 1 for High\nChoose 2 for Medium\nChoose 3 for Low\n\n"))
    if priority == 1:
        priority = "High"
    elif priority == 2:
        priority = "Medium"
    elif priority == 3:
        priority = "Low"
    task = {"title": title_input, "priority": priority}
    tasks.append(task)
    write_json()
    add_task_loop = input("Would you like to add another task? Type 'Y' or 'N'\n")
    while add_task_loop.upper != 'N' or 'n':
        if add_task_loop.upper() == 'Y':
            add_task()
        else:
            menu()
    menu()
    

def del_task():
    del_choice = input("\nTo continue, press 1\n" + "To quit to the menu, press q\n\n")
    print("-----------To Do List-----------\n")
    while del_choice != 'q':
        if del_choice == '1':
            index = 0
            for t in tasks:
                print(f"{index} - " + tasks[index]["title"] + " - " +  tasks[index]["priority"] + "\n--------------------------------")
                index += 1
            #try:
            index_choice = int(input("What task would you like to delete?\n"))
            try:
                del tasks[index_choice]
                write_json()
                menu_choice = input("\nDo you want to return to the menu?\nChoose 'Y' or 'N'\n")
            except:
                import time
                #index_choice = int(input(f"ERROR: Please enter a value between 0 and {len(tasks)-1}"))
                print(f"\nERROR: Please enter a value between 0 and {len(tasks)-1}")
                time.sleep(1.25)
                del_task()
                write_json()
        else:
            break
    else:
        menu()


def view_tasks():
    print("-----------To Do List-----------\n")
    index = 0
    for t in tasks:
        print(f"{index} - " + tasks[index]["title"] + " - " +  tasks[index]["priority"] + "\n--------------------------------")
        index += 1
    menu_choice = input("\nDo you want to return to the menu?\nChoose 'Y' or 'N'\n")
    if menu_choice.upper() == 'Y':
        menu()
    else:
        print("Thank you for using the To Do List Application! Goodbye.\n")
        quit()
#menu_checker('3')
menu()
