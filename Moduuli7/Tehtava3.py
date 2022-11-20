
terminal = {}

while True:
    path = int(input("1 Lopeta\n"
                    "2 Lisää lentoasema\n"
                    "3 Etsi lentoasema\n"
                    "Valitse: "))
    if path == 1:
        print("Heippa..")
        exit()
    elif path == 2:
        terminal.update({input("Anna lentoaseman ICAO koodi: ").upper():
                         input("Anna lentoaseman nimi: ")})
    elif path == 3:
        try:
            print(terminal[input("Anna haettavan lentoaseman ICAO koodi: ").upper()])
        except KeyError:
            print("404\n"
                  "Ei tuloksia..")
    else:
        print("1, 2, tai 3.")