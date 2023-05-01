import csv

def add_chore(file_name):
    print("Add chore")
    chore_title = input("Enter your chore title (use simple titles): ")
    chore_day = input("Enter the day this chore needs to be completed: ")
    chore_instructions = input("Enter instructions for this chore, e.g. put clothes in the washing machine: ")
    chore_time = input("Enter the approx. time to complete this chore: ")
    with open(file_name, "a") as chore_file:
        writer = csv.writer(chore_file)
        writer.writerow([chore_title, chore_day, chore_instructions,chore_time , "Uncompleted"])

def remove_chore(file_name):
    print("Remove chore")
    view_chores(file_name)
    chore_title = input("Enter the chore title that you want to remove (write it exactly as it is shown): ")
    chore_lists = []
    with open(file_name, "r") as chore_file:
        reader = csv.reader(chore_file)
        for row in reader:
            if (chore_title != row[0]):
                chore_lists.append(row)
    with open(file_name, "w") as chore_file:
        writer = csv.writer(chore_file)
        writer.writerows(chore_lists)
    print("EDITED LIST:")
    view_chores(file_name)

def mark_chore():
    print("Mark chore")

def view_chores(file_name):
    with open(file_name, "r") as chore_file:
        reader = csv.reader(chore_file)
        reader.__next__()
        for row in reader:
            if(row[4] == "Completed"):
                print(f"Chore: '{row[0]}' was COMPLETED on {row[1]}.")
            else:
                print(f"Chore: '{row[0]}' is UNCOMPLETED. Day to complete: {row[1]}. Approx. time to complete: {row[3]}. Instructions: {row[2]}.")

def view_day():
    print("View chores for a specific day")

def view_uncompleted():
    print("View uncompleted chores.")