#	code 	: RyoXHans
#	github	: RyoXHans
#	date 	: Jumat 31 Maret 2023
#	note 	: Ingin recode silahkan :b sc ini terbuka untuk publik
import mysql.connector
import os
import platform
import sys
try:
	username = sys.argv[1]
	password = sys.argv[2]
	host = sys.argv[3]
	conn = mysql.connector.connect(username=username,password=password,host=host)
	cursor = conn.cursor()
	def clear():
		if platform.system() == "Windows":
			os.system('cls')
		elif platform.system() == "Linux":
			os.system('clear')
		elif platform.system() == "Darwin":
			os.system('clear')
	banner = """ ____  _                     ____        _        
/ ___|| |__   _____      __ |  _ \  __ _| |_ __ _ 
\___ \| '_ \ / _ \ \ /\ / / | | | |/ _` | __/ _` |
 ___) | | | | (_) \ V  V /  | |_| | (_| | || (_| |
|____/|_| |_|\___/ \_/\_/   |____/ \__,_|\__\__,_|	v0.0

Tools by RyoXHans
Github: https://www.github.com/RyoXHans/"""
	def selectedDatabase(dbName):
		cursor.execute("use {};".format(dbName))
		cursor.execute("select database();")
		selectedDb = cursor.fetchone()[0]
		return selectedDb
	def main():
		try:
			clear()
			print(banner)
			print("Username: {}\nHost: {}".format(username, host))
			cursor.execute("SHOW DATABASES;")
			res = cursor.fetchall()
			print("Databases:")
			for x in res:
				x = ' '.join(map(str, x))
				print('\t> ',x)
			dbName = input("[]> ")
			if selectedDatabase(dbName):
				cursor.execute('show tables;')
				res = cursor.fetchall()
				print("Tables:")
				for x in res:
					x = ' '.join(map(str, x))
					print('\t> ',x)
				tbName = input("[{}][]> ".format(dbName))
			clear()
			print(banner)
			print("Username: {}\nHost: {}\nDatabase: {}\nTable: {}".format(username, host, dbName, tbName))
			cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}'".format(tbName))
			res = cursor.fetchall()
			for x in res:
				x = ' '.join(map(str, x))
				print('\t> ',x)
			print("Ketik help untuk bantuan")
			while True:
				command = input("query@find-data:~$ ")
				command = command.split()
				if command[0] == "exit":
					break
				if command[0] == "show":
					cursor.execute("SELECT {} FROM {}".format(command[1],tbName))
					res = cursor.fetchall()
					for x in res:
						x = ' '.join(map(str, x))
						print('\t> ',x)
				if command[0] == "h" or command[0] == "help":
					f = open('command-help.txt', 'r')
					print(f.read())
		except:
			print("\nError: ",sys.exc_info()[0])
	if __name__ == '__main__':
		main()
except:
	print("\nError: ",sys.exc_info()[0])
