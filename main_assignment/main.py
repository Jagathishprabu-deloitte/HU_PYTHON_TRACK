from main_assignment.data import admin_login, user_login, register_user


class Main:
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
            print("1.Login")
            print("****** Welcome to BookMyShow *******")
            username = input("Enter Username : ")
            password = input("Enter Password : ")
            admin_user, admin_password = admin_login()
            user_username, user_password = user_login()
            if admin_user == username:
                if admin_password == password:
                    print("Login Successful")
                else:
                    print("Password Wrong")
                    self.home_page()
            elif user_username == username:
                if user_password == password:
                    print("Login Successful")
                else:
                    print("Password Wrong")
                    self.home_page()
            else:
                print("Username Wrong, Register")
                self.home_page()
        if option == 2:
            register_user()

    def return_page(self):
        self.home_page()


obj = Main()
obj.home_page()

