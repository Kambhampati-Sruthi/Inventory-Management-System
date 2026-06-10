class Auth:

    def login(self):

        print("\n===== LOGIN =====")

        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "admin123":
            print("\nLogin Successful")
            return True

        print("\nInvalid Credentials")
        return False