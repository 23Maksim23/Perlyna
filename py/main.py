from utils import *


def interface():
    while True:
        print("\n\n")
        print("1) Print list of owners")
        print("2) Print list of restaurants")
        print("3) Add new owner")
        print("4) Add new restaurant")
        print("5) Print reports")
        print("6) Collect reports")
        value = input("Choose your option: ")
        if value == "exit":
            return
        value = int(value)
        if value == 1:
            all_users()
        elif value == 2:
            all_restaurants()
        elif value == 3:
            new_user()
        elif value == 4:
            new_restaurant()
        elif value == 5:
            all_reports()
        elif value == 6:
            collect_reports()


connection()
interface()
