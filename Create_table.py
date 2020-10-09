import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="",
)

mycursor = mydb.cursor()

mycursor.execute("USE testdb")

mycursor.execute("CREATE TABLE students (name VARCHAR(255),age INTEGER(10))")

print('Table students created!')

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
