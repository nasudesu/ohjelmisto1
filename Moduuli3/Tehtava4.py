yer = int(input("Anna vuosi: "))
if yer % 4 and yer % 100 and yer % 400:
    print("on karkausvuosi")
else:
    print("ei ole karkausvuosi")