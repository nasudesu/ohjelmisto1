

list_of_names = []
while True:
        name = input("uusi nimi : ")
        if name == "":
            print("kiitos käytöstä")
            break
        if name in list_of_names:
            print("Tämä on jo listassa anna uusi nimi")
        list_of_names.append(name)

set_list = set(list_of_names)
print("---set_list---")