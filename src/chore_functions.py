from rich.console import Console

from colored import fg, bg, attr

import csv

class WeekDayError(Exception):
    pass
def check_day(a):
    if not (a == "monday" or a == "tuesday" or a == "wednesday" or a == "thursday" or a == "friday" or a == "saturday" or a == "sunday"):
        raise WeekDayError ('That is not a week day, silly!')

console = Console()

def add_chore(file_name):
    console.print("Add Chore", style="bold underline deep_pink1")
    try:
        chore_title = input(f"Enter your {attr('bold')}{fg('dark_slate_gray_1')}chore title{attr('reset')} (use simple titles): ").lower().strip()
    except Exception as e:
        print(e)
    try:
        chore_day = input(f"Enter the {attr('bold')}{fg('dark_slate_gray_1')}day{attr('reset')} this chore needs to be completed: ").lower().strip()
        check_day(chore_day)
    except WeekDayError as e:
        print(e)
    else:
        try:
            chore_instructions = input(f"Enter {attr('bold')}{fg('dark_slate_gray_1')}instructions{attr('reset')} for this chore, e.g. put clothes in the washing machine: ").lower()
        except Exception as e:
            print(e)
        try:
            chore_time = input(f"Enter the {attr('bold')}{fg('dark_slate_gray_1')}approx. time{attr('reset')} it will take to complete this chore: ").lower()
        except Exception as e:
            print(e)
        try:
            with open(file_name, "a") as chore_file:
                writer = csv.writer(chore_file)
                writer.writerow([chore_title, chore_day, chore_instructions, chore_time, "Uncompleted"])
        except FileNotFoundError as e:
            print("oops, there was an error writing in this file!")
        except Exception as e:
            print(e)

def remove_chore(file_name):
    console.print("Remove Chore", style="bold underline dark_orange")
    console.print("CURRENT LIST OF CHORES:", style="bold yellow")
    view_chores(file_name)
    try:
        chore_title = input(f"Enter the {attr('bold')}{fg('purple_3')}'chore title'{attr('reset')} that you want to remove: ").lower().strip()
    except Exception as e:
        print(e)
    chore_lists = []
    try:
        with open(file_name, "r") as chore_file:
            reader = csv.reader(chore_file)
            for row in reader:
                if (chore_title != row[0]):
                    chore_lists.append(row)
        with open(file_name, "w") as chore_file:
            writer = csv.writer(chore_file)
            writer.writerows(chore_lists)
    except FileNotFoundError as e:
        print("oops, there was an error removing this chore from your chores list file!")
    except Exception as e:
        print(e)
    console.print("EDITED LIST:", style="bold yellow")
    view_chores(file_name)

def mark_chore(file_name):
    console.print("Mark Chore", style="bold underline yellow")
    view_chores(file_name)
    try:
        chore_title = input(f"Enter the {attr('bold')}{fg('purple_3')}'chore title'{attr('reset')} that you want to mark as complete: ").lower().strip()
    except Exception as e:
        print(e)
    try:
        chore_day = input(f"Enter the {attr('bold')}{fg('dark_slate_gray_1')}day{attr('reset')} that you completed this chore: ").lower().strip()
        check_day(chore_day)
    except WeekDayError as e:
        print(e)
    else:
        try:
            chore_instructions = input(f"Enter any {attr('bold')}{fg('dark_slate_gray_1')}notes{attr('reset')} for this chore (if you would like to leave as blank, enter 'none'): ").lower()
        except Exception as e:
            print(e)
        try:
            chore_time = input(f"Enter the {attr('bold')}{fg('dark_slate_gray_1')}time{attr('reset')} it took you to complete this chore: ").lower()
        except Exception as e:
            print(e)
        chore_lists = []
        try:
            with open(file_name, "r") as chore_file:
                reader = csv.reader(chore_file)
                for row in reader:
                    if (chore_title == row[0]):
                        chore_lists.append([chore_title, chore_day, chore_instructions,chore_time , "Completed"])
                    else:
                        chore_lists.append(row)
            with open(file_name, "w") as chore_file:
                writer = csv.writer(chore_file)
                writer.writerows(chore_lists)
        except FileNotFoundError as e:
            print("Oops, there was an error in marking your chore in your chores list file!")
        except Exception as e:
            print(e)

def view_chores(file_name):
    try:
        with open(file_name, "r") as chore_file:
            reader = csv.reader(chore_file)
            reader.__next__()
            for row in reader:
                if(row[4] == "Completed"):
                    print(f"Chore: {attr('bold')}{fg('purple_3')}'{row[0]}'{attr('reset')} was {attr('bold')}{fg('pale_green_1a')}COMPLETED{attr('reset')} on {row[1]} in {row[3]}. Notes: {row[2]}.")
                else:
                    print(f"Chore: {attr('bold')}{fg('purple_3')}'{row[0]}'{attr('reset')} is {attr('bold')}{fg('indian_red_1a')}UNCOMPLETED{attr('reset')}. Day to complete: {row[1]}. Approx. time to complete: {row[3]}. Instructions: {row[2]}.")
    except FileNotFoundError as e:
        print("Oops, there was an error in reading your chores list file!")
    except Exception as e:
        print(e)

def view_day(file_name):
    console.print("View chores for a specific day", style="bold underline bright_cyan")
    try:
        chore_day = input(f"Enter the {attr('bold')}{fg('dark_slate_gray_1')}day{attr('reset')} you would like to view: ").lower().strip()
        check_day(chore_day)
    except WeekDayError as e:
        print(e)
    else:
        if (chore_day == "monday"):
            console.print("Monday's Chores:", style="bold plum1")
        elif (chore_day == "tuesday"):
            console.print("Tuesday's Chores:", style="bold plum1")
        elif (chore_day == "wednesday"):
            console.print("Wednesday's Chores:", style="bold plum1")
        elif (chore_day == "thursday"):
            console.print("Thursday's Chores:", style="bold plum1")
        elif (chore_day == "friday"):
            console.print("Friday's Chores:", style="bold plum1")
        elif (chore_day == "saturday"):
            console.print("Saturday's Chores:", style="bold plum1")
        elif (chore_day == "sunday"):
            console.print("Sunday's Chores:", style="bold plum1")
        else:
            console.print("Invalid Input", style="red")
        try:
            with open(file_name, "r") as chore_file:
                reader = csv.reader(chore_file)
                reader.__next__()
                for row in reader:
                    if(row[1] == chore_day):
                        print(f"Chore: {attr('bold')}{fg('purple_3')}'{row[0]}'{attr('reset')}. {attr('bold')}{fg('sandy_brown')}{row[4]}{attr('reset')}. Approx. time to complete: {row[3]}. Instructions: {row[2]}.")
        except FileNotFoundError as e:
            print("Oops, there was an error in reading your chores list file!")
        # except Exception as e:
        #     print(e)
    
def view_uncompleted(file_name):
    console.print("UNCOMPLETED CHORES:", style="bold underline slate_blue1")
    try:
        with open(file_name, "r") as chore_file:
            reader = csv.reader(chore_file)
            reader.__next__()
            for row in reader:
                if(row[4] == "Uncompleted"):
                    print(f"Chore: {attr('bold')}{fg('yellow')}'{row[0]}'{attr('reset')}. Day to complete: {row[1]}. Approx. time to complete: {row[3]}. Instructions: {row[2]}.")
    except FileNotFoundError as e:
        print("Oops, there was an error in reading your chores list file!")
    except Exception as e:
        print(e)
