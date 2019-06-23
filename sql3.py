import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
#Функция занесения пользователя в базу
def add_user(username,userpass):
    c.execute("INSERT INTO users (name,password) VALUES ('%s','%s')"%(username,userpass))
    conn.commit()

#Вводим данные
name = input("Введите Логин\n")
passwd = input("Введите Пароль\n")
print('\n')

conn.execute




	cursor.execute()
	conn.commit()

