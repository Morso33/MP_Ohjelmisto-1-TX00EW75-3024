def tuumat_centtimetreiksi(tuumat):
    return tuumat * 2.54

while True:
    tuumat = float(input("Anna tuumat: "))
    if tuumat < 0:
        break
    centtimetrit = tuumat_centtimetreiksi(tuumat)
    print(centtimetrit)