from bookmyshow.admin import admin_options
from bookmyshow.datahandling import user_registration, admin_login, user_login
from bookmyshow.user import user_options


class HomePage:
    def home_page(self):
        print("****** Welcome to BookMyShow *******")
        print("1.Login")
        print("2.Register new account")
        print("3.Exit")
        option = int(input("Enter a valid option : "))
        if option <= 0 or option > 3:
            print("Please enter a valid option between 1 to 3..!!")
            self.home_page()
        if option == 1:
            print("--- Login ---")
            print("****** Welcome to BookMyShow *******")
            username = input("Enter Username : ")
            password = input("Enter Password : ")
            admin_user, admin_password = admin_login()
            if admin_user == username:
                if admin_password == password:
                    print("--- Admin Login Successful ---")
                    admin_options()
                    self.home_page()
                else:
                    print("Incorrect Password..!!")
                    self.home_page()
            elif admin_user != username:
                res = user_login(username, password)
                if res:
                    print("User Login Successful")
                    user_options()
                    self.home_page()
                else:
                    print("Retry Login or Register User..!!")
                    self.home_page()
            else:
                print("Incorrect Username, Register to Login..!!")
                self.home_page()
        elif option == 2:
            print("--- Register New Account ---")
            user_registration()
            self.home_page()
        elif option == 3:
            print("--- Exit ---")


obj = HomePage()
obj.home_page()
