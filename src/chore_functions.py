import csv

def add_chore(file_name):
    print("Add chore")
    chore_title = input("Enter your chore title (use simple titles): ")
    chore_day = input("Enter the day this chore needs to be completed: ")
    chore_instructions = input("Enter instructions for this chore, e.g. use vanish for washing: ")
    chore_time = input("Enter the approx. time to complete this chore: ")
    with open(file_name, "a")as chore_file:
        writer = csv.writer(chore_file)
        writer.writerow([chore_title, chore_day, chore_instructions,chore_time , "Incomplete"])

def remove_chore():
    print("Remove chore")

def mark_chore():
    print("Mark chore")

def view_chores():
    print("View Chores")

def view_day():
    print("View chores for a specific day")

def view_uncompleted():
    print("View uncompleted chores.")