from utils import *


def interface():
    while True:
        print("\nType exit to close\n")
        print("1) Print menu")
        print("2) Print suppliers")
        print("3) Print tables")
        print("4) Print clients")
        value = input("Choose your option: ")
        if value == "exit":
            return
        value = int(value)
        if value == 1:
            all_menu()
        elif value == 2:
            all_supplier()
        elif value == 3:
            all_tables()
        elif value == 4:
            all_customer()

connection()
interface()
