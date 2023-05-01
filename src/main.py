from rich.console import Console

from colored import fg, bg, attr

from chore_functions import add_chore, remove_chore, mark_chore, view_chores, view_day, view_uncompleted

console = Console()
print(f"{fg('blue')}Welcome to your Chores list! {attr('reset')}")

file_name = "chore_list.csv"

try:
    todo_file = open(file_name, "r")
    todo_file.close()
except FileNotFoundError as e:
    todo_file = open(file_name, "w")
    todo_file.write("title, day to complete, instructions/notes, approx. time, completed/uncompleted\n")
    todo_file.close()

def menu_bar():
    console.print("1. Enter [bold]1[/] to [bold]add a chore[/] to your list")
    console.print("2. Enter [bold]2[/] to [bold]remove a chore[/] from your list")
    console.print("3. Enter [bold]3[/] to [bold]mark[/] a chore as [bold]completed[/]")
    console.print("4. Enter [bold]4[/] to [bold]view[/] your chores list")
    console.print("5. Enter [bold]5[/] to [bold]view[/] your chores for a [bold]specific day[/].")
    console.print("6. Enter [bold]6[/] to [bold]view[/] your [bold]uncompleted chores[/]")
    console.print("7. Enter [bold]7[/] to [bold]exit[/]")
    selection = input("Enter your selection: ")
    return selection

user_selection = str()

while user_selection != "7":
    user_selection = menu_bar()

    if (user_selection == "1"):
        add_chore(file_name)
    elif (user_selection == "2"):
        remove_chore(file_name)
    elif (user_selection == "3"):
        mark_chore(file_name)
    elif (user_selection == "4"):
       console.print("View Chores", style="bold")
       view_chores(file_name)
    elif (user_selection == "5"):
       view_day(file_name)
    elif (user_selection == "6"):
        view_uncompleted(file_name)
    elif (user_selection == "7"):
        break
    else:
       print("Invalid Input") 

    input("Press Enter to contunue...")


print("Thank you for using Chore List!")