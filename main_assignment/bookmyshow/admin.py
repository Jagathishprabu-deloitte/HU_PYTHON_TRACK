import sys
import xlrd
from xlutils.copy import copy
import datetime as dt


def admin_options():
    print("****** Welcome Admin ******* ")
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
    print("--- Add New Movie ---")
    rb = xlrd.open_workbook('movieData.xls', formatting_info=True)
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
    n = 0
    sheet.write(r, 11, timings)
    sheet.write(r, 12, capacity)
    sheet.write(r, 13, n)
    wb.save('movieData.xls')


def edit_movie():
    print("--- Edit Movie Info---")
    print("****** Welcome Admin ******* ")
    loc = "movieData.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    print("Available Movies")
    for i in range(rows):
        if i > 0:
            print(i, ".", sheet.cell_value(i, 0))
            last = i
    print(last + 1, ". Exit the Edit option")
    option = int(input("Enter valid option to Update Movie : "))
    if option < last + 1:
        movie(option)
    elif option == last + 1:
        admin_options()
    else:
        print("Enter a valid option ")
        edit_movie()


def movie(options):
    print("****** Welcome Admin ******* ")
    loc = "movieData.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    col = sheet.ncols
    print("--- Movie description ---")
    for i in range(col):
        print(sheet.cell_value(0, i), ":", sheet.cell_value(options, i))
    rb = xlrd.open_workbook('movieData.xls', formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    print("--- Select Any Option to Update Movie Info---")
    print("1.Title\n2.Genre\n3.Length\n4.Cast\n5.Director\n6.Admin Rating\n7.Language\n8.Number of Shows\n"
          "9.First Show\n10.Interval Time\n11.Gap Between Shows\n12.Timings\n13.Capacity\n14.Exit Update Movie")
    choice = int(input("Enter a valid option to Update Movie Info : "))
    if choice == 1:
        print("--- Edit Title ---")
        title = input("Enter New Title of the Movie : ")
        sheet.write(options, 0, title)
    elif choice == 2:
        print("--- Edit Genre of the Movie ---")
        genre = input("Enter New Genre of the Movie : ")
        sheet.write(options, 1, genre)
    elif choice == 3:
        print("--- Edit Length of the Movie ---")
        length = input("Enter New Length of the Movie : ")
        sheet.write(options, 2, length)
    elif choice == 4:
        print("--- Edit Cast of the Movie ---")
        cast = input("Enter New Cast of the Movie : ")
        sheet.write(options, 3, cast)
    elif choice == 5:
        print("--- Edit Director of the Movie ---")
        director = input("Enter New Director of the Movie : ")
        sheet.write(options, 4, director)
    elif choice == 6:
        print("--- Edit Admin Rating of the Movie ---")
        rating = input("Enter New Rating of the Movie : ")
        sheet.write(options, 5, rating)
    elif choice == 7:
        print("--- Edit Language of the Movie ---")
        language = input("Enter New Language of the Movie : ")
        sheet.write(options, 6, language)
    elif choice == 8:
        print("--- Edit Number of Shows for the Movie ---")
        show = input("Enter New Number of Shows for the Movie : ")
        sheet.write(options, 7, show)
    elif choice == 9:
        print("--- Edit First Show Timing of the Movie ---")
        first_show = input("Enter New First Show Timing of the Movie : ")
        sheet.write(options, 8, first_show)
    elif choice == 10:
        print("--- Edit Interval Time of the Movie ---")
        interval = input("Enter New Interval Time of the Movie : ")
        sheet.write(options, 9, interval)
    elif choice == 11:
        print("--- Edit Gap Time between Shows of the Movie ---")
        gap = input("Enter New Gap Timing between the Shows of the Movie : ")
        sheet.write(options, 10, gap)
    elif choice == 12:
        print("--- Edit Timing of the Movie ---")
        timing = input("Enter New Timing of the Movie : ")
        sheet.write(options, 11, timing)
    elif choice == 13:
        print("--- Edit Capacity of the Theatre ---")
        capacity = input("Enter New Capacity of the Theatre : ")
        sheet.write(options, 12, capacity)
    elif choice == 14:
        edit_movie()
    else:
        print("Enter a valid choice between 1 to 13..!!")
        movie(options)
    print("--- Movie Info Updated Successfully..!!! ---")
    wb.save('movieData.xls')
    movie(options)


def delete_movie():
    print("***** Welcome Admin ******* ")
    print("delete movie")
    loc = "movieData.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    print("Available Movies")
    for i in range(rows):
        if i > 0:
            print(i, ".", sheet.cell_value(i, 0))
            last = i
    print(last + 1, ". Exit the Delete option")
    option = int(input("Enter valid option to Delete Movie : "))
    if option < last + 1:
        delete(option)
    elif option == last + 1:
        admin_options()
    else:
        print("Enter a valid option ")
        delete_movie()


def delete(option):
    rb = xlrd.open_workbook('movieData.xls', formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    cols = r_sheet.ncols
    for i in range(cols):
        sheet.write(option, i, "")
        wb.save("movieData.xls")
    delete_movie()


def logout():
    sys.exit()
