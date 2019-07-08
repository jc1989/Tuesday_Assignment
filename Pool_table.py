import json

tables = []
tables_availablity = []

class Tables:
    def __init__(self, table):
        self.table_num = table
        self.table_start = None
        self.table_end = None
        self.table_play_time = ""
        self.table_open = True

    def json_text(self):
        return f"""
        Table: {self.table_num}
        Table Start: {self.table_start}
        Table End: {self.table_end}
        Play Time: {self.table_play_time}
        Availibility: {self.table_open}"""

for i in range(1,13):
    table = Tables(i)
    tables_availablity.append(table.__dict__)
    tables.append(table)

def menu():
    print("""Welcome to the University Center Games Room\nPool Table Management Application!\n""")
    user_menu = str(input("""Choose one of the following:\n1. View all tables\n2. Open or Close a table\n3. Quit\n"""))

    if(user_menu == '1'):
        choice_one()

    elif(user_menu == '2'):
        choice_two(Tables)

    elif(user_menu == '3'):
        quit

def choice_one():
    table_menu = str(input("""Choose one of the following:\n1. View all tables\n2. View occupied tables\n3. View unoccupied tables\n"""))
    if(table_menu == '1'):
        print("You have chosen to view all tables:\n")
        for table in tables:
            print(table.json_text())

    elif(table_menu == '2'):
        print("You have chosen to view occupied tables:\n")
        for table in tables:
            if table.table_open != True:
                print(table.table_num)
    elif(table_menu == '3'):
        print("You have chosen to view unoccupied tables:\n")
        for table in tables:
            if table.table_open == True:
                print(table.table_num)
    else:
        print("Please select a valid entry:\n")
        menu()

def choice_two(Tables):
    while True:
        table_edit_menu = input("""Choose one of the twelve tables using 1-12\n""")
        if(table_edit_menu < 1 or table_edit_menu > 12):
            print("You must choose a valid option.")
            choice_two(Tables)
        elif(table_edit_menu >= 1 or table_edit_menu <= 12):
            if(table_edit_menu.table_open == True):
                table_occupied = input("Enter the starting time: ")
                table_occupied = table_edit_menu.table_start
                table_occupied.tables_availablity = False
            elif(table_edit_menu.table_open == False):
                table_unoccupied = input("Enter the ending time: ")
                table_unoccupied = table_edit_menu.table_start
                table_unoccupied.tables_availablity = True
        else:
            menu()
        return table_edit_menu
    
with open("table.json","w") as file:
    json.dump(tables_availablity,file, indent = 2)

menu()