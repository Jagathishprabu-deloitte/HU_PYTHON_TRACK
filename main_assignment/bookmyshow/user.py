import sys
import xlrd as xlrd
from xlutils.copy import copy


def user_options():
    print("******Welcome User******* ")
    loc = "movieData.xls"
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
    if option < last + 1:
        movie(option)
    elif option == last + 1:
        logout()
    else:
        print("Enter a valid option ")
        user_options()


def movie(options):
    print("******Welcome User******* ")
    loc = "movieData.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    col = sheet.ncols
    print("--- Movie description ---")
    col = col - 6
    for i in range(col):
        print(sheet.cell_value(0, i), ":", sheet.cell_value(options, i))
    user_choice(options)


def user_choice(option):
    print("1.Book Ticket")
    print("2.Cancel Ticket")
    print("3.User Rating")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        book_ticket(option)
    elif choice == 2:
        cancel_ticket(option)
    elif choice == 3:
        user_rating()
    else:
        print("Enter valid option")
        user_choice(option)


def book_ticket(option):
    print("****** Welcome User *******")
    print("--- Book Ticket ---")
    loc = "movieData.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    capacity = sheet.cell_value(option, 12)
    booked_seats = sheet.cell_value(option, 13)
    avail = capacity - booked_seats
    print("Total Capacity of the Theater : ", avail)
    book = int(input("Enter the number of seats to be booked: "))
    if book <= avail:
        booked_seats += book
        rb = xlrd.open_workbook('movieData.xls', formatting_info=True)
        r_sheet = rb.sheet_by_index(0)
        wb = copy(rb)
        sheet1 = wb.get_sheet(0)
        sheet1.write(option, 13, booked_seats)
        wb.save("movieData.xls")
        print("Ticket Booked Successfully..!!!")
        user_choice(option)
    else:
        print("Seats not Available..!!")
        user_choice(option)


def cancel_ticket(option):
    print("--- Cancel Ticket ---")
    loc = "movieData.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    booked_seats = sheet.cell_value(option, 13)
    print("Number of Booked seats : ", booked_seats)
    cancel = int(input("Enter number of seats you want to cancel : "))
    if cancel <= booked_seats:
        rb = xlrd.open_workbook('movieData.xls', formatting_info=True)
        r_sheet = rb.sheet_by_index(0)
        wb = copy(rb)
        sheet1 = wb.get_sheet(0)
        sheet1.write(option, 13, booked_seats - cancel)
        wb.save("movieData.xls")
        print("Ticket Cancellation Successful..!!")
        user_choice(option)
    else:
        print("Ticket Cancellation Failed..!!")
        user_choice(option)


def user_rating():
    print("--- User Rating ---")
    rating = int(input("Please enter rating for the following movie : "))
    print("Thanks for your Rating..!!!")
    user_options()


def logout():
    sys.exit()
