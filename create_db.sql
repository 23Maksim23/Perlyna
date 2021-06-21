USE master
COMMIT
IF EXISTS (SELECT name FROM sys.databases WHERE name = N'Perlyna')
	DROP DATABASE Perlyna
COMMIT
CREATE DATABASE Perlyna
ON(
	Name = Perlyna,
	FileName = 'D:\Perlyna\database\db.mdf',
	Size =8192KB,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 65536KB)
Log ON(
	Name = Perlyna_log,
	FileName = 'D:\Perlyna\database\db_log.ldf',
	Size =10,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 65536KB)

