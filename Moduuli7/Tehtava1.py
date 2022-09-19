


Season = ("Kevät", "Kesä", "Syksy", "Talvi")
while True:
    num = float(input("Anna kuukauden numerona : "))
    if num == "":
        break
    else:
        if num in range(1, 3):
            print(Season[3])
        if num in range(3, 6):
            print(Season[0])
        if num in range(6, 9):
            print(Season[1])
        if num in range(9, 12):
            print(Season[2])
        if num == 12:
            print(Season[3])