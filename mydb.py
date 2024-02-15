import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

# prepare a cusor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crm")

print("All Done!")