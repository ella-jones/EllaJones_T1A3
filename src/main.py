from rich.console import Console

from colored import fg, bg, attr

from chore_functions import add_chore, remove_chore, mark_chore, view_chores, view_day, view_uncompleted

console = Console()
print(f"{fg('blue')}Welcome to your Chores list! {attr('reset')}")

file_name = "chore_list.csv"

# The below code checks if the chore_list.csv file already exists, if it doesn't exist it it creates
# the file for the user and adds the first line (example line)
try:
    chore_file = open(file_name, "r")
except FileNotFoundError as e:
    chore_file = open(file_name, "w")
    chore_file.write("title, day to complete, instructions/notes, approx. time, completed/uncompleted\n")
    chore_file.close()
except Exception as e:
    print(e)
else:
    chore_file.close()

# The following function displays the menu bar to the user and allows them to input their selection.
def menu_bar():
    console.print("1. Enter [bold deep_pink1]1[/] to [bold deep_pink1]add a chore[/] to your list")
    console.print("2. Enter [bold dark_orange]2[/] to [bold dark_orange]remove a chore[/] from your list")
    console.print("3. Enter [bold yellow]3[/] to [bold yellow]mark[/] a chore as [bold]completed[/]")
    console.print("4. Enter [bold green1]4[/] to [bold green1]view[/] your chores list")
    console.print("5. Enter [bold bright_cyan]5[/] to [bold bright_cyan]view[/] your chores for a [bold]specific day[/].")
    console.print("6. Enter [bold slate_blue1]6[/] to [bold slate_blue1]view[/] your [bold]uncompleted chores[/]")
    console.print("7. Enter [bold dark_magenta]7[/] to [bold dark_magenta]exit[/]")
    try:
        selection = input("Enter your selection: ").strip()
    except Exception as e:
        print(e)
    else:
        return selection

user_selection = str()

# The below while loop runs the function for the user's selection. (These functions are located in chore_functions.py)
while user_selection != "7":
    user_selection = menu_bar()

    if (user_selection == "1"):
        add_chore(file_name)
    elif (user_selection == "2"):
        remove_chore(file_name)
    elif (user_selection == "3"):
        mark_chore(file_name)
    elif (user_selection == "4"):
       console.print("View Chores", style="bold underline green1")
       view_chores(file_name)
    elif (user_selection == "5"):
       view_day(file_name)
    elif (user_selection == "6"):
        view_uncompleted(file_name)
    elif (user_selection == "7"):
        break
    else:
       print("Invalid Input") 

    input(f"Press {attr('bold')}{fg('wheat_1')}Enter{attr('reset')} to contunue...")


print(f"{attr('bold')}{bg('purple_1b')}Thank you for using Chore List!{attr('reset')}")