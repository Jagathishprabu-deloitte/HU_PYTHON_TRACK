import xlrd as xlrd
from xlwt import Workbook


def user_options():
    print("******Welcome User******* ")
    loc = "addMovies.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    print("Available Movies")
    for i in range(rows):
        if i > 0:
            print(i, ".", sheet.cell_value(i, 0))
            last = i
    print(last + 1, ". Logout")
    option = int(input("Enter valid option : "))
    if option < last:
        movie(option)
    elif option == last + 1:
        logout()
    else:
        print("Enter a valid option ")
        user_options()


def movie(options):
    print("******Welcome User******* ")
    loc = "addMovies.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    col = sheet.ncols
    print("Movie description")
    col = col - 6
    for i in range(col):
        print(sheet.cell_value(0, i), ":", sheet.cell_value(options, i))
    user_choice()


def user_choice():
    print("1.Book Ticket")
    print("2.Cancel Ticket")
    print("3.User Rating")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        book_ticket()
    elif choice == 2:
        cancel_ticket()
    elif choice == 3:
        user_rating()
    else:
        print("Enter valid option")
        user_choice()


def book_ticket():
    print("******Welcome User*******")

    user_choice()


def cancel_ticket():
    print("cancel ticket")
    user_choice()


def user_rating():
    print("user Rating")
    user_options()


def logout():
    print("logout")
