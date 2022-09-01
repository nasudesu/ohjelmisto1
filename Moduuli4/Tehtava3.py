luku = input("Anna luku: ")
isoin = luku
pienin = luku
while True:
    if luku == "":
        print("Error")
        break
    luku = input("Anna luku: ")
    if luku == "":
        print("Isoin luku: " + str(isoin))
        print("Pienin: " + str(pienin))
        break
    elif float(luku) < float(pienin):
        pienin = luku
    elif float(luku) > float(isoin):
        isoin = luku