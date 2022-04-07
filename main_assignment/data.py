import csv


def register_user():
    print("******Welcome to Registration Page*****")
    user = input("Enter username: ")
    password = input("Enter password: ")
    rows = []
    k = 0
    with open("users.csv", "r") as file:
        csv_reader = csv.reader(file)
        j = 0
        for i in csv_reader:
            rows.append(i)
            if rows[j][0] == user:
                print("User already exists")
                register_user()
                break
            j = j + 1
        with open("users.csv", "a+", newline="") as obj:
            csv_writer = csv.writer(obj)
            csv_writer.writerow([user, password])
            k = k + 1


def admin_login():
    with open("db.txt", 'r') as file:
        username, password = file.read().split(",")
    return username, password


def user_login():
    with open("users.csv", 'r') as file:
        username, password = file.read().split(",")
    return username, password
