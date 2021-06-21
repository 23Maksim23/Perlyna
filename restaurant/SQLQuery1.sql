COMMIT
IF OBJECT_ID(N'CUSTOMER ', N'U') IS NULL
create table CUSTOMER (
	 Customer_Id INT NOT NULL IDENTITY PRIMARY KEY,
	 Fname VARCHAR(30) NOT NULL,
	 Lname VARCHAR(30) NOT NULL,
	 Contact VARCHAR(20) DEFAULT NULL,
	 Email_Id VARCHAR(50) DEFAULT NULL
)

IF OBJECT_ID(N'BILL', N'U') IS NULL
create table BILL (
	 Order_Id INT NOT NULL IDENTITY PRIMARY KEY,
	 Customer_Id INT NOT NULL FOREIGN KEY REFERENCES CUSTOMER(Customer_Id),
	 Total_Amount MONEY NOT NULL
)

IF OBJECT_ID(N'MENU_BILL', N'U') IS NULL
create table MENU_BILL (
	 Order_Id INT NOT NULL FOREIGN KEY REFERENCES BILL(Order_Id),
	 Name NVARCHAR(100) NOT NULL,
	 Quantity INT NOT NULL,
	 Price MONEY NOT NULL
)


IF OBJECT_ID(N'Job', N'U') IS NULL
create table Job (
	 Job_id INT NOT NULL IDENTITY PRIMARY KEY,
	 Name NVARCHAR(100) NOT NULL,
 	 Salary MONEY DEFAULT NULL
)

IF OBJECT_ID(N'Staff', N'U') IS NULL
create table Staff (
	 Staff_Id INT NOT NULL IDENTITY PRIMARY KEY,
	 Job_id INT FOREIGN KEY REFERENCES Job(Job_id),
	 Fname NVARCHAR(15) NOT NULL,
	 Lname NVARCHAR(15) NOT NULL,
	 Contact VARCHAR(20) NOT NULL,
 	 Address NVARCHAR(30) DEFAULT NULL,
	 Sex char(1) DEFAULT NULL,
	 date_of_birth date DEFAULT NULL,
	 Join_Date date NOT NULL
)


IF OBJECT_ID(N'MENU', N'U') IS NULL
create table MENU (
	 Menu_Id INT NOT NULL IDENTITY PRIMARY KEY,
	 Name NVARCHAR(100) NOT NULL,
	 Price VARCHAR(20) NOT NULL,
	 Type NVARCHAR(20) DEFAULT NULL
)



IF OBJECT_ID(N'SALE_DETAIL', N'U') IS NULL
create table SALE_DETAIL (
	 Date date NOT NULL,
	 Daily INT NOT NULL,
	 Weekly INT DEFAULT NULL,
	 Monthly INT DEFAULT NULL,
	 Rname VARCHAR(30) DEFAULT NULL
)

IF OBJECT_ID(N'SUPPLIER', N'U') IS NULL
create table SUPPLIER (
	Supplier_id INT NOT NULL IDENTITY PRIMARY KEY,
	 Fname VARCHAR(15) NOT NULL,
	 Lname VARCHAR(15) NOT NULL,
	 Address VARCHAR(30) NOT NULL,
	 Contact VARCHAR(20) NOT NULL,
	 Details VARCHAR(500) DEFAULT NULL
)

IF OBJECT_ID(N'TABLES', N'U') IS NULL
create table TABLES (
	 Table_Number INT NOT NULL PRIMARY KEY,
	 Details VARCHAR(200) DEFAULT NULL
)

IF OBJECT_ID(N'BOOKING', N'U') IS NULL
create table BOOKING (
	 Booking_Id INT NOT NULL IDENTITY PRIMARY KEY,
	 Table_Num INT NOT NULL FOREIGN KEY REFERENCES TABLES(Table_Number ),
	 Date VARCHAR(30) NOT NULL,
	 Time VARCHAR(30) NOT NULL,
	 Cust_Id INT NOT NULL FOREIGN KEY REFERENCES CUSTOMER ( Customer_Id )
)

IF OBJECT_ID(N'INGREDIENT', N'U') IS NULL
create table INGREDIENT (
	 Ingredient_Id INT NOT NULL IDENTITY PRIMARY KEY,
	 Name nVARCHAR(30) NOT NULL,
	 Quantity VARCHAR(15) NOT NULL,
	 Description nVARCHAR(100) DEFAULT NULL,
	 Supplier_id INT NOT NULL FOREIGN KEY REFERENCES SUPPLIER(Supplier_id)
)
insert INTo Job ( Name,Salary)
values
('MANAGER', 30000),
('WAITER', 8000),
('CASHIER', 12000),
('COOK', 15000),
('DELIVERY_BOY', 10000)


insert into Staff (Job_id, fName, Lname, Contact, Address, Sex, date_of_birth, Join_Date)
values
(1, 'Eirena', 'Rotherforth', '9011302212', '0196 Fallview Court', 'F', '1976-12-11', '2016-10-06'),
(1, 'Poul', 'Garnett', '1644411927', '6295 Loeprich Place', 'M', '2002-06-26', '2019-09-26'),
(2, 'Bethany', 'Costerd', '9064392541', '06 Haas Place', 'F', '1983-03-19', '2021-05-04'),
(2, 'Sibella', 'Laundon', '8877158901', '60 Troy Hill', 'F', '1958-03-07', '2018-11-24'),
(2, 'Cilka', 'Brizland', '4317953760', '55572 Memorial Plaza', 'F', '1968-07-31', '2018-09-21'),
(2, 'Jamill', 'Vellender', '6124931722', '06585 Armistice Crossing', 'M', '1964-06-05', '2017-08-25'),
(2, 'Almira', 'Gockelen', '4412960184', '916 Canary Trail', 'F', '1983-03-07', '2020-03-09'),
(2, 'Liana', 'Durward', '8194842305', '561 Chive Plaza', 'F', '1976-02-22', '2018-08-02'),
(2, 'Maribel', 'Truggian', '5321401323', '3 Kenwood Center', 'F', '1968-06-02', '2017-10-12'),
(2, 'Halimeda', 'Mattussevich', '8252764280', '489 Pleasure Park', 'F', '1980-07-09', '2018-02-23'),
(2, 'Marabel', 'Birts', '1857101225', '28238 Pond Place', 'F', '1993-05-24', '2019-05-02'),
(3, 'Annemarie', 'Phillput', '6019024426', '78 Park Meadow Avenue', 'F', '1979-06-06', '2019-08-29'),
(3, 'Conchita', 'Nurcombe', '4414688202', '2138 Farragut Circle', 'F', '2001-02-11', '2018-01-20'),
(3, 'William', 'Walkling', '6137884964', '17 Melvin Road', 'M', '1986-06-05', '2017-09-02'),
(3, 'Levey', 'Ranvoise', '5176910606', '41525 Corben Lane', 'M', '1952-03-26', '2015-08-22'),
(3, 'Gelya', 'Lightwing', '3224762200', '21 Garrison Way', 'F', '1970-03-25', '2017-01-04'),
(3, 'Maury', 'Legging', '1979088200', '33090 Judy Avenue', 'M', '1994-01-30', '2017-08-17'),
(3, 'Lynnett', 'Morecomb', '7027057177', '2 Fisk Circle', 'F', '1979-07-18', '2017-05-14'),
(3, 'Shandie', 'Clementucci', '9052397277', '00 Schiller Crossing', 'F', '1970-07-07', '2020-07-21'),
(4, 'Marty', 'Scoular', '7493756340', '583 Browning Circle', 'F', '2002-08-01', '2021-01-06'),
(4, 'Bradney', 'Parade', '2514990253', '0 Oriole Place', 'M', '1961-06-26', '2016-10-14'),
(4, 'Farica', 'Witz', '6134752442', '56618 Kenwood Street', 'F', '1960-10-12', '2019-03-07'),
(4, 'Malvina', 'Portigall', '8281506482', '45 Monterey Park', 'F', '1960-02-16', '2016-12-18'),
(5, 'Ruy', 'Hexum', '8792193082', '589 Anniversary Way', 'M', '2005-04-12', '2015-11-21'),
(5, 'Arri', 'Risom', '2434189714', '55 Cardinal Center', 'M', '1965-05-26', '2018-04-15'),
(5, 'Alys', 'Markwick', '6829044256', '4 Gina Lane', 'F', '1998-06-19', '2019-04-13'),
(5, 'Oralia', 'Harewood', '7673164576', '699 Sugar Place', 'F', '1985-01-11', '2020-12-20'),
(5, 'Bartholomew', 'Bloss', '3262064148', '36716 Monterey Court', 'M', '1979-05-28', '2016-11-30'),
(5, 'Sarah', 'Copley', '8108444267', '92004 Armistice Crossing', 'F', '1973-01-09', '2019-06-04'),
(5, 'Siana', 'todor', '4418429428', '97 Dunning Court', 'F', '1953-03-10', '2021-02-05')


insert INTO MENU ( Name,Price,Type)
values
('Голубці з рисом та м''ясом',N'30',N'Друга страва'),
('Голубці з картоплею',N'30',N'Друга страва'),
('Червоний борщ',N'25',N'Перша страва'),
('Холодець',N'30',N'Холодна страва'),
('Сирники',N'18',N'Друга страва'),
('Вареники із сиром',N'23',N'Друга страва'),
('Вареники із капустою',N'23',N'Друга страва'),
('Деруни',N'17',N'Друга страва'),
('Котлети по-київськи',N'15',N'Друга страва'),
('Гречаники',N'13',N'Друга страва'),
('Сало',N'20',N'Холодна страва'),
('Капусняк',N'25',N'Перша страва'),
('Полядвиця',N'60',N'М''ясне'),
('Галушки',N'20',N'Друга страва'),
('Ліниві вареники з сиру',N'25',N'Друга страва')

insert INTo SUPPLIER ( Fname,Lname,Address,Contact,Details )
values
('Varun',N'Vashisht',N'E-121 OBH,IIIT Hyderabad',N'123211',N'Provides Non-Veg Stuff.'),
('Aneeq',N'Dholakia',N'E-15 OBH,IIIT Hyderabad',N'678668',N'Provides Sea Food.'),
('Sharad',N'Gupta',N'E-16 OBH,IIIT Hyderabad',N'856855',N'Provides Grocery.');

insert INTo TABLES ( Table_Number,Details )
values
('1',N'Capacity 4 People'),
('2',N'Capacity 4 People Near Window'),
('3',N'Capacity 3 People'),
('4',N'Capacity 2 People'),
('5',N'Capacity 8 People Family Table');

insert INTo CUSTOMER ( Fname,Lname,Contact,Email_Id )
values
('Arpit',N'Sharma',N'938912',N'arpit.sharma@students.iiit.ac.in'),
('Yash',N'Shah',N'289374',N'yash.shah@students.iiit.ac.in'),
('Darshit',N'Serna',N'234322',N'darshit.serna@students.iiit.ac.in'),
('Aditya',N'Sharma',N'778989',N'aditya.sharma@students.iiit.ac.in'),
('Pallav',N'Shah',N'364932',N'pallav.shah@students.iiit.ac.in'),
('Rajat',N'Bharadwaj',N'734277',N'rajat.bharadwaj@students.iiit.ac.in'),
('AchINTya',N'Madhav',N'347534',N'achINTya.madhav@students.iiit.ac.in');
