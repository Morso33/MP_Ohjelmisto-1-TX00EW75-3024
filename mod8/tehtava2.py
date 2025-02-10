import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_mod_8"
)
myCursor = mydb.cursor()

country = input("Anna maa: ")

myCursor.execute("SELECT * FROM airports WHERE iso_country = %s", (country,))

myresult = myCursor.fetchall()

small_airports = 0
medium_airports = 0
large_airports = 0
helicopter_airports = 0
for x in myresult:
    if x[2] == "small_airport":
        small_airports += 1
    elif x[2] == "medium_airport":
        medium_airports += 1
    elif x[2] == "large_airport":
        large_airports += 1
    elif x[2] == "heliport":
        helicopter_airports += 1

print("Pieniä lentoasemia: " + str(small_airports))
print("Keskikokoisia lentoasemia: " + str(medium_airports))
print("Suuria lentoasemia: " + str(large_airports))
print("Helikopterikenttiä: " + str(helicopter_airports))
