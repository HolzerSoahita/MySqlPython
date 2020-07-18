import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM students WHERE name = %s"

mycursor.execute(sql, ("Bob",))

myresult = mycursor.fetchall()

for result in myresult:
    print(result)