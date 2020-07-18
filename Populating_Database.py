import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="",
    database="testdb"
)

mycursor = mydb.cursor()


sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)"
student1 = ("Rachel", 22)
students = [("Bob", 12),
            ("Amanda", 32),
            ("Jacob", 21),
            ("Avi", 28),
            ("Michel", 17), ]

mycursor.execute(sqlFormula, student1)

mycursor.executemany(sqlFormula, students)

# To make sure  of changing
mydb.commit()