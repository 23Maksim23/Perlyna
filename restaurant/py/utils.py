import os
import pandas as pd
from pathlib import Path
import sqlalchemy as sa
from sqlalchemy import text
from settings import *

engine = sa.create_engine(
    f'mssql+pyodbc://{db_name}:{db_password}@localhost/{db_name}?driver=SQL+Server+Native+Client+11.0')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def connection():
    with engine.connect() as con:
        if con.execute("SELECT COUNT(*) FROM SYSOBJECTS WHERE xtype = 'U'").fetchone()[0] == 0:
            with open(str(Path(os.getcwd()).parent) + r"\SQLQuery1.sql") as rest:
                rest_query = text(rest.read())
                con.execute(rest_query)


def all_menu():
    data = pd.read_sql_query("SELECT * FROM MENU;", engine)
    if data.empty:
        print("No data")
    else:
        print(data.to_markdown())


def all_supplier():
    data = pd.read_sql_query("SELECT * FROM SUPPLIER;", engine)
    if data.empty:
        print("No data")
    else:
        print(data.to_markdown())

def all_customer():
    data = pd.read_sql_query("SELECT * FROM CUSTOMER;", engine)
    if data.empty:
        print("No data")
    else:
        print(data.to_markdown())

def all_tables():
    data = pd.read_sql_query("SELECT * FROM TABLES;", engine)
    if data.empty:
        print("No data")
    else:
        print(data.to_markdown())


def all_staff():
    data = pd.read_sql_query(
        "SELECT Fname,Job.Name, Job.Salary, Lname,Contact,Address,Sex,date_of_birth,Join_Date FROM Staff INNER JOIN Job ON Job.Job_id = Staff.Job_id;",
        engine)
    if data.empty:
        print("No data")
    else:
        print(data.to_markdown())


# def all_clients():
#     data = pd.read_sql_query("SELECT * FROM Client;", engine)
#     if data.empty:
#         print("Table Client is empty")
#     else:
#         print(data.to_markdown())
#
#
# def all_orders():
#     data = pd.read_sql_query("SELECT * FROM Orders O INNER JOIN Order_Dish D ON D.orderID = O.orderID;", engine)
#     if data.empty:
#         print("Table Orders is empty")
#     else:
#         print(data.to_markdown())
#
#
# def new_dish():
#     name, description, price = None, None, None
#
#     def name_set():
#         nonlocal name
#         value = input("Input the name of dish: ")
#         if value == "exit":
#             return True
#         elif 2 < len(value) > 30 and re.search(r'\d', value):
#             print("The name you entered is invalid or empty")
#             name_set()
#         else:
#             name = value
#
#     def description_set():
#         nonlocal description
#         value = input("Input description to dish: ")
#         if value == "exit":
#             return True
#         elif 2 < len(value) > 500 and re.search(r'\d', value):
#             print("The name you entered is invalid or empty")
#             description_set()
#         else:
#             description = value
#
#     def price_set():
#         nonlocal price
#         value = input("Input price for dish: ")
#         if value == "exit":
#             return True
#         try:
#             value = float(value)
#             price = value
#         except ValueError:
#             print("The price you entered is invalid or empty")
#             price_set()
#
#     engine.execute(rf"""
#     INSERT INTO [Dish]
#            (name,
#            description,
#            price)
#      VALUES
#            {name}
#            {description}
#            {price}
#     """)
#
#
# def new_client():
#     clientID, first_name, last_name, date_of_birth, phone_number, email = None, None, None, None, None, None
#     data = pd.read_sql_query(f"USE {db_name}; SELECT phone_number, email FROM Client;", engine)
#
#     def fName_set():
#         nonlocal first_name
#         value = input("Input your first name: ")
#         if value == "exit":
#             return True
#         elif 2 < len(value) > 30 and re.search(r'\d', value):
#             print("The name you entered is invalid or empty")
#             fName_set()
#         else:
#             first_name = value
#
#     def lName_set():
#         nonlocal last_name
#         value = input("Input your last name: ")
#         if value == "exit":
#             return True
#         elif 2 < len(value) > 30 and re.search(r'\d', value):
#             print("The surname you entered is invalid or empty")
#             lName_set()
#         else:
#             last_name = value
#
#     def phone_number_set():
#         nonlocal phone_number
#         try:
#             value = int(input("Input your phone number without '+': "))
#             if value == "exit":
#                 return True
#             elif 11 < len(str(value)) > 15:
#                 print("Number you entered is invalid or empty")
#                 phone_number_set()
#             elif value in data[data.columns[0]]:
#                 print("That number is already registered")
#                 phone_number_set()
#             else:
#                 phone_number = value
#         except ValueError:
#             print("Phone number must be integer")
#             phone_number_set()
#
#     def email_set():
#         nonlocal email
#         value = input("Input your email: ")
#         if value == "exit":
#             return True
#         elif bool(is_email(value, check_dns=True)):
#             email = value
#         elif value in data[data.columns[1]].to_string(index=False):
#             print("That email is already registered")
#             email_set()
#         else:
#             print("The email you entered is invalid or empty")
#             email_set()
#
#     functions = [
#         fName_set,
#         lName_set,
#         phone_number_set,
#         email_set]
#     for i in functions:
#         if i():
#             return
#     try:
#         engine.execute(
#             f"""
#             USE {db_name};
#             INSERT INTO Client
#            (first_name,
#            last_name,
#            date_of_birth,
#            phone_number,
#            email)
#      VALUES(
#            N'{first_name}',
#            N'{last_name}',
#            N'{date_of_birth}',
#            N'{phone_number}',
#            N'{email}')
#             """)
#     except sa.exc.IntegrityError:
#         print("Duplicated value")
#
#
# def new_order():
#     order = list()
#     phone_number, client_id, dish_id = None, None, None
#
#     dishes = pd.read_sql_query(f"USE {db_name};SELECT id,name, price FROM Dish;", engine)
#
#     def phone_number_set():
#         nonlocal phone_number, client_id
#         data = pd.read_sql_query(f"USE {db_name};SELECT clientID, phone_number FROM Client;", engine)
#         value = int(input("Input your phone number without '+'(Keep blank if not registered): "))
#         if value == "exit":
#             return True
#         elif value == "":
#             client_id = ""
#         elif value in data[data.columns[1]]:
#             client_id = pd.read_sql_query(f"USE {db_name};SELECT clientID FROM Client WHERE phone_number = {value};",
#                                           engine)
#         else:
#             print("Number you entered is invalid or empty")
#             phone_number_set()
#
#     def add_dish_to_order():
#         value = input("Input the dish: ")
#         if value == "exit" or value == "":
#             return True
#         elif value not in dishes or len(value) == 0:
#             print("The dish name you entered is invalid or empty")
#             add_dish_to_order()
#         else:
#             value = pd.read_sql_query(f"USE {db_name};SELECT id FROM Dish WHERE name = '{value}';", engine)
#             order.append(value)
#             add_dish_to_order()
#
#     functions = [
#         phone_number_set,
#         add_dish_to_order]
#     for i in functions:
#         if i():
#             return
#     print(rf"""
#         USE {db_name};
#         INSERT INTO Orders(clientID, order_date)
#         VALUES({client_id}, {datetime.date.today()})
#
# """)
