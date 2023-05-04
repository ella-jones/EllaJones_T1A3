import pytest
import csv
from chore_functions import remove_chore, view_chores

test_file_name = "tests/test_remove.csv"

def pytest_sessionstart(session):
    print("--------------------setup-------------------------")
    with open(test_file_name, "w") as f:
                writer = csv.writer(f)
                writer.writerow(["test chore", "monday", "test", "test", "Uncompleted"])

def pytest_sessionfinish(session, exitstatus):
    print("--------------------teardown-------------------------")

# Test 2:
# This test checks if the remove_chore() function (located in chore_functions.py) correctly removes an 
# line from the corresponding csv file (chore_list.csv). This test uses the test_remove.csv file
# (located in the tests folder) to test this function.
def test_remove(monkeypatch):
    original_length = 0
    with open(test_file_name) as f:
        reader = csv.reader(f)
        original_length = sum(1 for row in reader)
    monkeypatch.setattr('builtins.input', lambda _: "test chore")
    remove_chore(test_file_name)
    with open(test_file_name) as f:
        reader = csv.reader(f)
        new_length = sum(1 for row in reader)
    print(original_length)
    print(new_length)
    assert new_length == original_length - 1

    

