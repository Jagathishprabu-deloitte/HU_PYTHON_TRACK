from xlwt import Workbook


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
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    print("****** Welcome Admin ******* ")
    sheet1.write(0, 0, 'Title')
    sheet1.write(0, 1, 'Genre')
    sheet1.write(0, 2, 'Length')
    sheet1.write(0, 3, 'Cast')
    sheet1.write(0, 4, 'Director')
    sheet1.write(0, 5, 'Admin Rating')
    sheet1.write(0, 6, 'Language')
    sheet1.write(0, 7, 'Number of Shows per a day')
    sheet1.write(0, 8, 'First Show')
    sheet1.write(0, 9, 'Interval Time')
    sheet1.write(0, 10, 'Gap Between Shows')
    sheet1.write(0, 11, 'Timings')
    sheet1.write(0, 12, 'Capacity')
    title = input("Enter the title: ")
    sheet1.write(1, 0, title)
    genre = input("Enter the Genre: ")
    sheet1.write(1, 1, genre)
    length = input("Enter the length of the movie: ")
    sheet1.write(1, 2, length)
    cast = input("Enter the cast: ")
    sheet1.write(1, 3, cast)
    director = input("Enter the director name: ")
    sheet1.write(1, 4, director)
    admin_rating = input("Enter the admin rating: ")
    sheet1.write(1, 5, admin_rating)
    language = input("Enter the language: ")
    sheet1.write(1, 6, language)
    shows = int(input("Enter Number of Shows per a day: "))
    sheet1.write(1, 7, shows)
    first_show = input("Enter the first show start time")
    sheet1.write(1, 8, first_show)
    interval_time = input("Enter the interval time: ")
    sheet1.write(1, 9, interval_time)
    gap_between_shows = input("Enter the gap between show: ")
    sheet1.write(1, 10, gap_between_shows)
    timings = "8.00-12.00, 1.00-4.00, 5.00-8.00, 8.00-11.00"
    sheet1.write(1, 11, timings)
    capacity = int(input("Enter the capacity"))
    sheet1.write(1, 12, capacity)
    wb.save('movieData.xls')


def edit_movie():
    print("--- Edit Movie Info---")
    print("****** Welcome Admin ******* ")


def delete_movie():
    print("***** Welcome Admin ******* ")
    print("delete movie")


def logout():
    print("logout")
