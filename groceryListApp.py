
import os

def clear_list():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    print("What should we pick up at the store?")
    print("Enter 'DONE' to stop adding items.")
    print("Enter 'HELP' for help window.")
    print("Enter 'PRINT LIST' to print your entire list.")
    print("Enter 'REMOVE' if you wish to remove an item from your list.")
def add_to_list(grocery_list):
    print_full_list(grocery_list)
    if len(grocery_list):
        position = input("Where should I add the {}? \n"
                         "Press ENTER to add to the end of the list.\n"
                         "> ".format(new_item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except:
        position = None
    if position is not None:
        grocery_list.insert(position - 1, new_item)
    else:
        grocery_list.append(new_item)
    print_full_list(grocery_list)
def print_full_list(grocery_list):
    list_number = 1
    clear_list()
    print("")
    print("YOUR CURRENT LIST IS:")
    print("")
    for index, item in enumerate(grocery_list):
        print("{}: {}".format(index + 1, item))
    print("----------")
    print("")

def finish(grocery_list):
    list_number = 1
    print("")
    print("YOUR GROCERY LIST:")
    for item in grocery_list:
        print("{}. {}".format(list_number, item))
        list_number += 1
    print("----------")
    print("")

grocery_list = []

show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        finish(grocery_list)
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        print_full_list(grocery_list)
        continue
    elif new_item.upper() == 'REMOVE':
        item_number = int(input("Enter the number of the item you wish to remove. ({} to {})  ".format(1, len(grocery_list))))
        del grocery_list[item_number - 1]
        continue
    else:
        add_to_list(grocery_list)
