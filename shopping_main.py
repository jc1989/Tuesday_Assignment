#from modulename import Class or Function
from shopping_list import ShoppingList 
from grocery_item import GroceryItem

#keeps track of all shopping lists 
shopping_lists = [] 

# display all shopping lists 
def display_all_lists():
    for index in range(0,len(shopping_lists)):
        print(f"{index+1} - {shopping_lists[index].name}")

#display 
def view_all_lists():
    for index in range(0,len(shopping_lists)):
        lists = shopping_lists[index]
        print(f"{lists.name} - {lists.address}")
        for grocery_item in lists.grocery_items:
            print(f"{grocery_item.name} - ${grocery_item.price} - {grocery_item.quantity}")

#make a menu:
def user_menu():
    choice = input("\nEnter 1 to view all lists.\nEnter 2 to add an item to a list.\nEnter 3 to add a grocery item to the list.\nEnter q to quit.\n\n")
    return choice

#ask what list to add an item to
def add_item():
    while True:
        try:
            display_all_lists()
            add_input = int(input("\nWhich list do you want to add an item to? Enter the number of the list index: \n"))
            store_index = shopping_lists[add_input - 1]
            name = input("\nPlease enter a name for the store: \n")
            price = float(input("\nPlease enter a price \n"))
            quantity = int(input("\nPlease enter a quantity: \n" ))
            item = GroceryItem(name, price, quantity)
            store_index.grocery_items.append(item)
            break
        except:
            print("Something went wrong\n")

def add_list():
    name = input("\nEnter list name: \n")
    address = input("\nEnter an address: \n")
    store = ShoppingList(name, address)
    shopping_lists.append(store)

quit = False

while(quit != True):
    user_input = user_menu()

    if(user_input == 'q'):
        quit = True
    elif(user_input == '1'):
        view_all_lists()
    elif(user_input == '2'):
        add_list()
    elif(user_input == '3'):
        add_item()