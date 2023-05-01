from chore_functions import add_chore, remove_chore, mark_chore, view_chores, view_day, view_uncompleted

print("Welcome to your Chores list!")

file_name = "chore_list.csv"

try:
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
except FileNotFoundError as e:
    todo_file = open(file_name, "w")
    todo_file.write("title, completed")
    todo_file.close()
    print("In except block")

def menu_bar():
    print("1. Enter 1 to add a chore to your list")
    print("2. Enter 2 to remove a chore from your list")
    print("3. Enter 3 to mark a chore as completed")
    print("4. Enter 4 to view your chores list")
    print("5. Enter 5 to view your chores for a specific day.")
    print("6. Enter 6 to view your uncompleted chores")
    print("7. Enter 7 to exit")
    selection = input("Enter your selection: ")
    return selection

user_selection = str()

while user_selection != "7":
    user_selection = menu_bar()

    if (user_selection == "1"):
        add_chore()
    elif (user_selection == "2"):
        remove_chore()
    elif (user_selection == "3"):
        mark_chore()
    elif (user_selection == "4"):
       view_chores()
    elif (user_selection == "5"):
       view_day()
    elif (user_selection == "6"):
        view_uncompleted()
    elif (user_selection == "7"):
        break
    else:
       print("Invalid Input") 

    input("Press Enter to contunue...")


print("Thank you for using Chore List!")