import mysql.connector
import geopy
from geopy.distance import geodesic

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_mod_8"
)
myCursor = mydb.cursor()

airport1 = input("Anna ICAO koodi: ")

myCursor.execute("SELECT * FROM airports WHERE ident = %s", (airport1,))

result1 = myCursor.fetchall()

airport2 = input("Anna ICAO koodi: ")

myCursor.execute("SELECT * FROM airports WHERE ident = %s", (airport2,))

result2 = myCursor.fetchall()

coords1 = (result1[0][4], result1[0][5])
coords2 = (result2[0][4], result2[0][5])
print("Distance between airports: " + str(geodesic(coords1, coords2).kilometers) + " km")
