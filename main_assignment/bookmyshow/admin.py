import datetime as dt

import xlrd
from xlutils.copy import copy


def admin_options():
    print("******Welcome Admin******* ")
    print("1.Add New Movie Info")
    print("2.Edit Movie Info")
    print("3.Delete Movie Info")
    print("4.Logout")
    option = int(input("Enter valid option : "))
    if option == 1:
        add_new_movie()
        admin_options()
    elif option == 2:
        edit_movie()
        admin_options()
    elif option == 3:
        delete_movie()
        admin_options()
    elif option == 4:
        logout()
    else:
        print("Enter a valid option between 1 to 4")
        admin_options()


def add_new_movie():
    rb = xlrd.open_workbook('addMovies.xls', formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    print("******Welcome Admin******* ")
    title = input("Enter the title: ")
    sheet.write(r, 0, title)
    genre = input("Enter the Genre: ")
    sheet.write(r, 1, genre)
    length = int(input("Enter the length of the movie(in minutes): "))
    sheet.write(r, 2, length)
    cast = input("Enter the cast: ")
    sheet.write(r, 3, cast)
    director = input("Enter the director name: ")
    sheet.write(r, 4, director)
    admin_rating = int(input("Enter the admin rating: "))
    sheet.write(r, 5, admin_rating)
    language = input("Enter the language: ")
    sheet.write(r, 6, language)
    shows = int(input("Enter Number of Shows per a day: "))
    sheet.write(r, 7, shows)
    first_show = input("Enter the first show start time(HH:MM): ")
    sheet.write(r, 8, first_show)
    interval_time = int(input("Enter the interval time(in minutes): "))
    sheet.write(r, 9, interval_time)
    gap_between_shows = int(input("Enter the gap between show(in minutes): "))
    sheet.write(r, 10, gap_between_shows)
    capacity = int(input("Enter the capacity: "))
    date_time_first_show = dt.datetime.strptime(first_show, "%H:%M")
    time_first_show = date_time_first_show
    time1 = int(length + interval_time)
    delta = dt.timedelta(minutes=time1)
    delta2 = dt.timedelta(minutes=gap_between_shows)
    timings = []
    for i in range(shows):
        final_date_time = time_first_show + delta
        time_first = str(time_first_show.time())
        final_time = str(final_date_time.time())
        timings.append(time_first + "-" + final_time)
        time_first_show = final_date_time + delta2
    print(timings)
    sheet.write(r, 11, timings)
    sheet.write(r, 12, capacity)
    wb.save('addMovies.xls')


def edit_movie():
    print("******Welcome Admin******* ")
    print("edit movie")


def delete_movie():
    print("******Welcome Admin******* ")
    print("delete movie")


def logout():
    print("logout")
