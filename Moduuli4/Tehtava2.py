

tuumat = 0
while tuumat >= 0:
    tuumat = float(input("Anna tuuma: "))
    cm = tuumat * 2.54
    if tuumat >= 0:
        print(cm)
else:
     print("Väärä numero")