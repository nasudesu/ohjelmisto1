

Season = ("Kevät", "Kesä", "Syksy", "Talvi")
while True:
    num = int(input("Anna kuukauden numerona : "))
    if num == "":
        print("Kiitos ohjelman käytöstä!")
    elif num in range(1, 3):
        print(Season[3])
    elif num in range(3, 6):
        print(Season[0])
    elif num in range(6, 9):
        print(Season[1])
    elif num in range(9, 12):
        print(Season[2])
    elif num == 12:
        print(Season[3])

        