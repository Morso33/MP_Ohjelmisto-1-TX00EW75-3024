import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_mod_8"
)
myCursor = mydb.cursor()

ICAOCode = input("Anna ICAO-koodi: ")

myCursor.execute("SELECT * FROM airports WHERE ident = %s", (ICAOCode,))

myresult = myCursor.fetchall()

print("Lentoaseman nimi: " + myresult[0][3])
print("Kaupunki: " + myresult[0][10])