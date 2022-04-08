import xlrd as xlrd
from xlutils.copy import copy


def admin_login():
    with open("db.txt", 'r') as file:
        admin_username, admin_password = file.read().split(",")
    return admin_username, admin_password


def user_registration():
    print("**** Create new Account ***** ")
    name = input("Enter name : ")
    email = input("Enter e-mail : ")
    mobile = int(input("Enter Mobile Number : "))
    age = int(input("Enter Age : "))
    password = input("Enter Password : ")
    rb = xlrd.open_workbook('userData.xls', formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    print("n ", r)
    count = 0
    for i in range(r):
        if name == r_sheet.cell_value(i, 0):
            count += 1
            print("Username Already exists..!!")
            user_registration()
    if count == 0:
        wb = copy(rb)
        sheet = wb.get_sheet(0)
        sheet.write(r, 0, name)
        sheet.write(r, 1, email)
        sheet.write(r, 2, mobile)
        sheet.write(r, 3, age)
        sheet.write(r, 4, password)
        wb.save('userData.xls')
        print("Registration Successful..!!")


def user_login(username, password):
    loc = "userData.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    r = sheet.nrows
    flag = 0
    for i in range(r):
        user_username = sheet.cell_value(i, 0)
        user_password = sheet.cell_value(i, 4)
        if username == user_username:
            if password == user_password:
                flag += 1
                return True
            else:
                print("Password Incorrect")
                return False
    if flag == 0:
        print("User not registered..!!")
        return False
