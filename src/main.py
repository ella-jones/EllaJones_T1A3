print("Welcome to your Chores list!")

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
        print("Add chore")
    elif (user_selection == "2"):
        print("Remove chore")
    elif (user_selection == "3"):
        print("Mark chore")
    elif (user_selection == "4"):
        print("View Chores")
    elif (user_selection == "5"):
        print("View Day")
    elif (user_selection == "6"):
        print("View Uncompleted Chores")
    elif (user_selection == "7"):
        break
    else:
       print("Invalid Input") 

    input("Press Enter to contunue...")


print("Thank you for using Chore List!")