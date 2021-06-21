
USE Perlyna
COMMIT
IF OBJECT_ID(N'Franchise_Owner', N'U') IS NULL
CREATE TABLE Franchise_Owner(
	id INT PRIMARY KEY IDENTITY,
	passport_code VARCHAR(11) NOT NULL,
	tax_id VARCHAR(11) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	date_of_birth DATE NOT NULL,
	phone_number VARCHAR(15) NOT NULL UNIQUE,
	email VARCHAR(255) NOT NULL UNIQUE CHECK (email LIKE '%_@__%.__%'),
	password VARBINARY(32) NOT NULL,
	registered DATE NULL DEFAULT GETDATE(),
	activity BIT DEFAULT 1
)


IF OBJECT_ID(N'Restaurant', N'U') IS NULL
CREATE TABLE Restaurant
(
	id INT PRIMARY KEY IDENTITY,
	franchise_owner_id INT 
			CONSTRAINT fk_restaurant_franchise_owner_id 
			FOREIGN KEY REFERENCES Franchise_Owner(id),
	country VARCHAR(40) NOT NULL,
	city VARCHAR(40) NOT NULL,
	street VARCHAR(100) NOT NULL,
	building_number VARCHAR(10) NULL,
	database_name VARCHAR(100) NOT NULL,
	database_password VARBINARY(32) NOT NULL,
	date_opened DATE NULL DEFAULT GETDATE(),
	activity BIT DEFAULT 1
)


IF OBJECT_ID(N'Restaurant_report', N'U') IS NULL
CREATE TABLE Restaurant_report(
	restaurant_id INT FOREIGN KEY REFERENCES Restaurant(id),
	report_date DATE NOT NULL,
	orders INT NOT NULL,
	revenue MONEY NOT NULL
)


INSERT INTO [Franchise_Owner](passport_code,tax_id,first_name,last_name,date_of_birth,phone_number,email,password)
        VALUES(N'1234567890',N'1234567890',N'Ivan',N'Ivanov',N'1995-03-12',N'380973895122',N'ivanov@gmail.com',HASHBYTES('SHA2_256','ivanov1995')),
			(N'9876543210',N'9876543210',N'Petro',N'Petrov',N'1986-09-07',N'380678156691',N'petro.petrov@mail.com',HASHBYTES('SHA2_256','petr0vp1'))


INSERT INTO Restaurant(franchise_owner_id,country,city,street,building_number,database_name, database_password )
VALUES
(1,N'Ukraine',N'Lviv',N'Shevchenka',N'11',N'g',HASHBYTES('SHA2_256','ivanov1995')),
(2,N'Ukraine',N'Lviv',N'Liubinska',N'168',N'k',HASHBYTES('SHA2_256','petr0vp1'))


INSERT INTO Restaurant_report(restaurant_id,report_date,orders,revenue)
VALUES(1,'2021-06-08',6,1500),
(2,'2021-06-08',9,2100),
(1,'2021-06-09',7,1700),
(2,'2021-06-09',11,2400)
