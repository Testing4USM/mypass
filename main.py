import os
import time
from database import Database
from generator import GeneratorService

if __name__ == '__main__':
    #db = Database()

    print("Welcome to MyPass!\n")

    flag_pass = False # This flag will be used to check if the main password has already been entered

    while True:

        if not flag_pass:
            main_pass = input("Main password: ")
            flag_pass = True

        if True: # TODO: Check if main_pass is correct in DB
            os.system('cls' if os.name=='nt' else 'clear')

            print("----- MYPASS MENU -----\n")
            print("1. Add Password")
            print("2. Get Password")
            print("3. Generate Password")
            print("4. Exit\n")

            choice = input("Enter your choice: ")

            if choice == '1':
                platform = input("Enter platform: ")
                password = input("Enter password: ")
                # TODO: Implement add password

            elif choice == '2':
                platform = input("Enter platform: ")
                # TODO: Implement get password

            elif choice == '3':
                platform = input("Enter platform: ")
                length = int(input("Enter length: "))

                generator = GeneratorService("salt", length)
                generated_password = generator.generate_password(length)

                print(f"Generated password: {generated_password}")
                # TODO: Implement generator()

            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
            time.sleep(4)
        else:
            print("Incorrect password. Please try again.")
