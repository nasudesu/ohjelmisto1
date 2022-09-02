yer = int(input("Anna vuosi: "))
if yer % 4 == 0 and yer % 100 != 0 or yer % 400 == 0:
    print("on karkausvuosi")
else:
    print("ei ole karkausvuosi")