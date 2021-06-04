import mysql.connector

mydb = mysql.connector.connect(
    host="sql5.freemysqlhosting.net",
    user="sql5416726",
    passwd="SPULe7hFzU",
    database="sql5416726",
    port="3306"
)

mysql_cursor = mydb.cursor()
sql_statement = "INSERT INTO s1543_libraries.user(name,email,password) VALUES('Jeff Malik','jeff@gmail.com','1111');"
print(sql_statement)
print("antes de insertar usuario")
mysql_cursor.execute(sql_statement)
print("luego de insertar usuario")
mysql_cursor.close()