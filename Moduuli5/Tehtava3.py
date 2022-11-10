



luku = int(input("anna kokonais luku: "))
for i in range(2, luku):
    if luku % i == 0:
        print("ei ole alkuluku")
        break
else:
    print("on alkuluku")