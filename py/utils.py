import datetime
import hashlib
import os
import re
import shutil
import easygui
import pandas as pd
import pyodbc
from pyisemail import is_email
import pycountry
import getpass
from pathlib import Path
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text

engine = sa.create_engine('mssql+pyodbc://localhost/Perlyna?driver=SQL+Server+Native+Client+11.0')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def connection():
    global engine
    try:
        engine.connect()
    except (pyodbc.InterfaceError, sa.exc.InterfaceError, OperationalError):
        with sa.create_engine('mssql+pyodbc://localhost/master?driver=SQL+Server+Native+Client+11.0').connect() as con:
            with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\create_db.sql") as create_db:
                db_query = text(create_db.read())
                con.execute(db_query)
        engine = sa.create_engine('mssql+pyodbc://localhost/Perlyna?driver=SQL+Server+Native+Client+11.0')
        with engine.connect() as con:
            with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\Perlyna.sql") as perlyna:
                perlyna_query = text(perlyna.read())
                con.execute(perlyna_query)
    with engine.connect() as con:
        if con.execute("SELECT COUNT(*) FROM SYSOBJECTS WHERE xtype = 'U'").fetchone()[0] == 0:
            with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\Perlyna.sql") as perlyna:
                perlyna_query = text(perlyna.read())
                con.execute(perlyna_query)


def all_users():
    data = pd.read_sql_query(
        "SELECT [id],[passport_code],[tax_id],[first_name],[last_name],[date_of_birth],[phone_number],[email] FROM Franchise_Owner;",
        engine)

    if data.empty:
        print("Table Franchise_Owner is empty")
    else:
        print(data.to_markdown())


def all_reports():
    data = pd.read_sql_query(
        """SELECT restaurant_id, country, city, street, building_number, report_date, orders, revenue FROM Restaurant_report RR 
        INNER JOIN Restaurant R ON R.id=RR.restaurant_id""",
        engine)

    if data.empty:
        print("Table Restaurant_report is empty")
    else:
        print(data.to_markdown())


def collect_reports():
    print("Coming soon :)")
    # data = pd.read_sql_query(
    #     "SELECT City, Count(City) FROM Restaurant",
    #     engine)
    #
    # if data.empty:
    #     print("Table Restaurant_report is empty")
    # else:
    #     print(data.to_markdown())


def all_restaurants():
    data = pd.read_sql_query(
        "SELECT [id] ,[franchise_owner_id] ,[country] ,[city] ,[street] ,[building_number] FROM [Restaurant];", engine)
    if data.empty:
        print("Table Restaurants is empty")
    else:
        print(data.to_markdown())


def _password():
    value = getpass.getpass(prompt='Input your password(you will not see what you are typing):')
    if value == "exit":
        return True
    elif len(value) >= 8 and re.compile(r'\d.*?[A-Z].*?[a-z]'):
        if getpass.getpass(prompt='Confirm your password:') == value:
            return value
        else:
            print("Both passwords must be the same")
            _password()
    else:
        print("Password must be at least 8 symbols;contain a digit and at least 1 capital letter")
        _password()


def new_user():
    passport_code, tax_id, fName, lName, date_of_birth, phone_number, email, password = None, None, None, None, None, None, None, None
    data = pd.read_sql_query("SELECT passport_code,tax_id,phone_number,email FROM Franchise_Owner;", engine)

    def passport_code_set():
        nonlocal passport_code
        value = input("Input your passport code: ")
        if value == "exit":
            return True
        elif len(value) != 10:
            print("The passport code you entered is invalid or empty")
            passport_code_set()
        elif value in data[data.columns[0]].to_string(index=False):
            print("That passport code is already registered")
            passport_code_set()
        else:
            passport_code = value

    def tax_id_set():
        nonlocal tax_id
        value = input("Input your Taxpayer Identification Number: ")
        if value == "exit":
            return True
        elif len(value) != 10:
            print("The TIN you entered is invalid or empty")
            tax_id_set()
        elif value in data[data.columns[1]].to_string(index=False):
            print("That TIN is already registered")
            tax_id_set()
        else:
            tax_id = value

    def fName_set():
        nonlocal fName
        value = input("Input your first name: ")
        if value == "exit":
            return True
        elif len(value) < 2 or len(value) > 30 or re.search(r'\d', value):
            print("The name you entered is invalid or empty")
            fName_set()
        else:
            fName = value

    def lName_set():
        nonlocal lName
        value = input("Input your last name: ")
        if value == "exit":
            return True
        elif len(value) < 2 or len(value) > 30 or re.search(r'\d', value):
            print("The surname you entered is invalid or empty")
            lName_set()
        else:
            lName = value

    def date_of_birth_set():
        nonlocal date_of_birth
        year, month, day = None, None, None

        def year_set():
            nonlocal year
            try:
                i_year = int(input("Input your year of birth: "))
                if not datetime.datetime.now().year - 100 <= i_year <= datetime.datetime.now().year - 18:
                    print(
                        f"Year should be between {datetime.datetime.now().year - 100} and {datetime.datetime.now().year - 18}")
                    year_set()
                else:
                    year = i_year
            except ValueError:
                print("Year must be integer")
                year_set()

        def month_set():
            nonlocal month
            try:
                i_month = int(input("Input your month of birth: "))
                if not 1 <= i_month <= 12:
                    print(f"Month should be between 1 and 12")
                    month_set()
                else:
                    month = i_month
            except ValueError:
                print("Month must be integer")
                month_set()

        def day_set():

            nonlocal day
            try:
                i_day = int(input("Input your day of birth: "))
                if not 1 <= i_day <= 31:
                    print(f"Day should be between 1 and 31")
                    day_set()
                else:
                    day = i_day
            except ValueError:
                print("Day must be integer")
                day_set()

        year_set()
        month_set()
        day_set()
        date_of_birth = datetime.date(year, month, day)

    def phone_number_set():
        nonlocal phone_number
        try:
            value = int(input("Input your phone number without '+': "))

            if value == "exit":
                return True
            for i in data[data.columns[2]]:
                if str(value) == i:
                    print("That number is already registered")
                    return phone_number_set()
            if len(str(value)) < 11 or len(str(value)) > 15:
                print("Number you entered is invalid or empty")
                return phone_number_set()
            else:
                phone_number = value
        except ValueError:
            print("Phone number must be integer")
            phone_number_set()

    def email_set():
        nonlocal email
        value = input("Input your email: ")

        if value == "exit":
            return True
        for i in data[data.columns[3]]:
            if str(value) == i:
                print("That email is already registered")
                return email_set()
        if not bool(is_email(value, check_dns=True)):
            print("The email you entered is invalid or empty")
            return email_set()
        else:
            email = value
            return

    def password_set():
        nonlocal password
        value = _password()
        if value:
            password = value

    functions = [
        passport_code_set,
        tax_id_set,
        fName_set,
        lName_set,
        date_of_birth_set,
        phone_number_set,
        email_set,
        password_set]
    for i in functions:
        if i():
            return
    engine.execute(
        f"""INSERT INTO[dbo].[Franchise_Owner]
        ([passport_code],
        [tax_id],
        [first_name],
        [last_name],
        [date_of_birth],
        [phone_number],
        [email],
        [password])
    VALUES(
        N'{passport_code}',
        N'{tax_id}',
        N'{fName}',
        N'{lName}',
        N'{date_of_birth}',
        N'{phone_number}',
        N'{email}',
        HASHBYTES('SHA2_256','{password}'))
        """)


def new_restaurant():

    #owner_id, country, city, street, building_number, db_name, db_location, db_password = 5, "Ukraine", 'Lviv', 'Naukova', '60', 'Naukova_60', 'D:\\', 'Qwertyu1'
    owner_id, country, city, street, building_number, db_name, db_location, db_password = None, None, None, None, None, None, None, None

    def country_set():
        nonlocal country
        value = input("Input the country: ")
        if value == "exit":
            return True
        elif not pycountry.countries.search_fuzzy(value) or len(value) == 0:
            print("The country name you entered is invalid or empty")
            country_set()
        else:
            country = value

    def city_set():
        nonlocal city
        value = input("Input the city: ")
        if value == "exit":
            return True
        elif len(value) < 3 and re.search(r'\d', value):
            print("The city you entered is invalid or empty")
            city_set()
        else:
            city = value

    def street_set():
        nonlocal street
        value = input("Input the street: ")
        if value == "exit":
            return True
        elif len(value) < 3 and re.search(r'\d', value):
            print("The city you entered is invalid or empty")
            street_set()
        else:
            street = value

    def building_number_set():
        nonlocal building_number
        value = input("Input the building number: ")
        if value == "exit":
            return True
        elif len(value) < 3 and not re.search(r'\d', value):
            print("The building number you entered is invalid or empty")
            building_number_set()
        else:
            building_number = value

    def find_password(code):
        data = pd.read_sql_query(
            f"SELECT password FROM Franchise_Owner WHERE passport_code = '{code}';",
            engine)
        value = getpass.getpass(prompt='Input your password(you will not see what you are typing):')
        secret = hashlib.sha256(value.encode('UTF-8')).digest()
        if secret in [i for i in data[data.columns[0]]]:
            return True
        else:
            print("Wrong password")
            return find_password(code)

    def database_set():
        nonlocal db_name, db_location, db_password
        db_location = easygui.diropenbox(default=r"D:\\")
        print(f"Database location :{db_location}")

        def db_name_set():
            nonlocal db_name
            value = input("How would you call your database: ")

            if value == "exit":
                return True
            elif not value.isascii():
                print("The database name must be latin")
                db_name_set()
            else:
                db_name = value

        def password_set():
            print("Password to your database")
            value = _password()
            if value:
                print("Your password is stored")
                return value

        db_password = password_set()
        db_name_set()

    functions = [
        country_set,
        city_set,
        street_set,
        building_number_set,
        database_set
    ]

    def authorize():
        nonlocal owner_id
        data = pd.read_sql_query("SELECT passport_code FROM Franchise_Owner;", engine)
        value = input("Input your passport code: ")
        if len(value) <= 9 or len(value) >= 11:
            print("Wrong format")
            authorize()
        elif value in [i for i in data[data.columns[0]]]:
            data = pd.read_sql_query(f"SELECT id FROM Franchise_Owner WHERE passport_code = '{value}';", engine)
            owner_id = [i for i in data[data.columns[0]]][0]
            if find_password(value):
                print("You are logged in")

                for i in functions:
                    if i():
                        return
                return True
            else:
                pass
        else:
            print(f"Passport code '{value}' not found")
            authorize()

    if authorize():

        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        shutil.copytree(os.path.join(file_path, "restaurant\\"), os.path.join(db_location, db_name))
        with engine.connect() as conn:
            conn.execute(rf"""
            COMMIT
            USE Perlyna;
            SET NOCOUNT ON;
            INSERT INTO Restaurant
               (franchise_owner_id,
               country,
               city,
               street,
               building_number,
               database_name,
               database_password)
             VALUES
                   ({owner_id},
                   N'{country}',
                   N'{city}',
                   N'{street}',
                   N'{building_number}',
                   N'{db_name}',
                   HASHBYTES('SHA2_256','{db_password}'))
            """)

        with engine.connect() as conn:
            conn.execute(rf"""
            COMMIT
            USE master;
            SET NOCOUNT ON;
            CREATE DATABASE {db_name}
            ON(
                Name = {db_name},
                FileName = '{db_location}\{db_name}\db\db.mdf',
                Size = 8192KB,
                MAXSIZE = UNLIMITED,
                FILEGROWTH = 65536KB)
            Log ON(
                Name = {db_name}_log,
                FileName = '{db_location}\{db_name}\db\db_log.ldf',
                Size = 10,
                MAXSIZE = UNLIMITED,
                FILEGROWTH = 65536KB);""")

        with engine.connect() as conn:
            conn.execute(rf"""
            COMMIT
            USE master;
            SET NOCOUNT ON;
            create LOGIN {db_name} WITH PASSWORD='{db_password}', CHECK_POLICY = OFF;
            DENY VIEW ANY DATABASE TO {db_name};
            ALTER AUTHORIZATION ON DATABASE::{db_name} TO {db_name};
            """)

        with open(str(db_location + fr"\{db_name}\py\settings.py").replace('\\\\', '\\'), "w+") as file:
            file.write(f"db_name = '{db_name}'\ndb_password = '{db_password}'")


