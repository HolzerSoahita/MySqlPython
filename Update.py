import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

mycursor = mydb.cursor()

sql = "UPDATE students SET age = 13 WHERE name = 'Bob' "

mycursor.execute(sql)

mydb.commit()