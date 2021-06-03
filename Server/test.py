import mysql.connector

mydb = mysql.connector.connect(
    host="104.238.205.84",
    user="u1543_SRDLH1a89I",
    passwd="B.KimFW@rO=qqCdplUB+^cXX",
    database="s1543_libraries",
    port="3306"
)

mysql_cursor = mydb.cursor()
sql_statement = "INSERT INTO s1543_libraries.user(name,email,password) VALUES('Jeff Malik','jeff@gmail.com','1111');"
print(sql_statement)
print("antes de insertar usuario")
mysql_cursor.execute(sql_statement)
print("luego de insertar usuario")
mysql_cursor.close()