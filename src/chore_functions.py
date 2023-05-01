import csv

def add_chore(file_name):
    print("Add chore")
    chore_title = input("Enter your chore title (use simple titles): ").lower()
    chore_day = input("Enter the day this chore needs to be completed: ").lower()
    chore_instructions = input("Enter instructions for this chore, e.g. put clothes in the washing machine: ").lower()
    chore_time = input("Enter the approx. time it will take to complete this chore: ").lower()
    with open(file_name, "a") as chore_file:
        writer = csv.writer(chore_file)
        writer.writerow([chore_title, chore_day, chore_instructions,chore_time , "Uncompleted"])

def remove_chore(file_name):
    print("Remove chore")
    print("CURRENT CHORES")
    view_chores(file_name)
    chore_title = input("Enter the chore title that you want to remove (write it exactly as it is shown): ").lower()
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

def mark_chore(file_name):
    print("Mark chore")
    view_chores(file_name)
    chore_title = input("Enter the chore title that you want to mark as complete (Write it exactly as shown): ").lower()
    chore_day = input("Enter the day you completed this chore: ").lower()
    chore_instructions = input("Enter any notes for this chore (if you would like to leave as blank, enter 'none'): ").lower()
    chore_time = input("Enter the time it took you to complete this chore: ").lower()
    chore_lists = []
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

def view_chores(file_name):
    with open(file_name, "r") as chore_file:
        reader = csv.reader(chore_file)
        reader.__next__()
        for row in reader:
            if(row[4] == "Completed"):
                print(f"Chore: '{row[0]}' was COMPLETED on {row[1]} in {row[3]}. Notes: {row[2]}.")
            else:
                print(f"Chore: '{row[0]}' is UNCOMPLETED. Day to complete: {row[1]}. Approx. time to complete: {row[3]}. Instructions: {row[2]}.")

def view_day(file_name):
    print("View chores for a specific day")
    chore_day = input("Enter the day you would like to view: ").lower()
    if (chore_day == "monday"):
        print("Monday's Chores:")
    elif (chore_day == "tuesday"):
        print("Tuesday's Chores:")
    elif (chore_day == "wednesday"):
        print("Wednesday's Chores:")
    elif (chore_day == "thursday"):
        print("Thursday's Chores:")
    elif (chore_day == "friday"):
        print("Friday's Chores:")
    elif (chore_day == "saturday"):
        print("Saturday's Chores:")
    elif (chore_day == "sunday"):
        print("Sunday's Chores:")
    else:
        print("Invalid Input")

    with open(file_name, "r") as chore_file:
        reader = csv.reader(chore_file)
        reader.__next__()
        for row in reader:
            if(row[1] == chore_day):
                print(f"Chore: '{row[0]}'. {row[4]}. Approx. time to complete: {row[3]}. Instructions: {row[2]}.")
    
def view_uncompleted(file_name):
    print("UNCOMPLETED CHORES:")
    with open(file_name, "r") as chore_file:
        reader = csv.reader(chore_file)
        reader.__next__()
        for row in reader:
            if(row[4] == "Uncompleted"):
                print(f"Chore: '{row[0]}'. Day to complete: {row[1]}. Approx. time to complete: {row[3]}. Instructions: {row[2]}.")
