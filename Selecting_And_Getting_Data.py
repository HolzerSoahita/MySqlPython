import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

mycursor.execute("SELECT age FROM students")

myresult = mycursor.fetchone()

for row in myresult:
    print(myresult)

