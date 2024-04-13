import time
from database import Database
from generator import GeneratorService
from getpass import getpass
from models.user import User
from utils import get_logfile
import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    db = Database()
    logging.basicConfig(filename=get_logfile(), level=logging.INFO)

    print("Welcome to MyPass!\n")

    flag_pass = False
    user = User(db)
 
    while True:
        print("----- MYPASS LOGIN -----\n")
        if not flag_pass:
            print("1. Login")
            print("2. Register")
            print("3. Exit\n")

            choice = int(input("> "))

            if choice == 1:
                email = input("Enter your email: ")
                password = getpass(prompt="Enter your main password: ")
        
                if user.login(email, password):
                    print("Login successful!\n")
                    flag_pass = True

                    logger.info(f"User {email} logged in.")
                else:
                    print("Invalid password! Try again.\n")

                    logger.error(f"User {email} failed to log in.")
            elif choice == 2:
                email = input("Enter an email: ")
                username = input("Enter a username: ")
                password = getpass(prompt="Enter a password: ")

                if user.register(username, email, password):
                    print("User registered successfully!\n")
                    flag_pass = True

                    logger.info(f"User {email} registered.")
                else:
                    print("User already exists! Try again.\n")
                    
                    logger.error(f"User {email} failed to register.")
            elif choice == 3:
                print("Exiting MyPass...")
                time.sleep(1)

                logger.info("MyPass exited.")
                break
        else:
            print("1. Create password")
            print("2. View passwords")
            print("3. Get password")
            print("4. Change password")
            print("5. Logout\n")

            choice = int(input("> "))
            keychain = user.keychain

            if not keychain:
                flag_pass = False

            if choice == 1:
                key = input("Enter the key name: ")
                password = ""

                print ("1. Generate password")
                print ("2. Enter password manually")

                choice = int(input("> "))

                if choice == 1:
                    length = int(input("Enter the length of the password: "))
                    chars = input("Enter the characters to be used: ")

                    password = GeneratorService(chars=chars).generate_password(length)
                elif choice == 2:
                    password = getpass(prompt="Enter your password: ")

                if keychain.add_password(key, password):
                    print(f"Password added successfully for {key}!\n")
                    logger.info(f"User {email} added password for {key}.")
                else:
                    print("Password for this key already exists!\n")
                    logger.error(f"User {email} failed to add password for {key}.")
            elif choice == 2:
                passwords = keychain.passwords

                if len(passwords) == 0:
                    print("No passwords found!\n")
                else:
                    for password in passwords:
                        print(f"Key: {password} | Password: {passwords[password]}")

                logger.info(f"User {email} viewed passwords.")
            elif choice == 3:
                service = input("Enter the key name: ")
                password = keychain.get_password(service)

                if password:
                    print(f"Password for {service}: {password}\n")
                else:
                    print("No password found!\n")

                logger.info(f"User {email} got password for {service}.")
            elif choice == 4:
                key = input("Enter the key name: ")
                password = ""

                print ("1. Generate password")
                print ("2. Enter password manually")

                choice = int(input("> "))

                if choice == 1:
                    length = int(input("Enter the length of the password: "))
                    chars = input("Enter the characters to be used: ")

                    password = GeneratorService(chars=chars).generate_password(length)
                elif choice == 2:
                    password = getpass(prompt="Enter your password: ")

                keychain.change_password(service, password)
                print("Password changed successfully!\n")

                logger.info(f"User {email} changed password for {key}.")
            elif choice == 5:
                flag_pass = False
                print("Logged out successfully!\n")

                logger.info(f"User {email} logged out.")


