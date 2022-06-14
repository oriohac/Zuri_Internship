import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)

# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)