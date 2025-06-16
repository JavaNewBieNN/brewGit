import csv

def my_read():
    with open(r"/test_learning/pytest_/unit_tests\data.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def read_csv(filename):
    import os
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)
    with open(full_path, 'r', newline='') as f:
        reader = csv.reader(f)
        return list(reader)[1:]


statement = read_csv("data.csv")

print(statement)  # [['1', '1', '2'], ['2', '3', '5'], ['3', '3', '6'], ['4', '4', '7']]
print(type(statement))  # <class 'list'>

