"""nimet = ["Nasse", "Mage", "Sipi", "Dansku", "Heidi"]

#print(nimet[3])
#print(nimet[-3])
#print(nimet[2:4])

nimet.append("Seppo")
print(nimet)
nimet.remove("Nasse")
print(nimet)
nimet.append("Nasse")
print(nimet)
nimet.remove("Nasse")
print(nimet)
nimet.insert(2,"nasu")
print(nimet)

nimet2 = ["Chorizo","Taco"]

nimet.extend(nimet2)
print(nimet)
print(nimet2)

nimet.append("Matti")

index = nimet.index("Matti")
print(index)

if "nasu" in nimet:
    print("nasu oli listassa")
else:
    print("ei ollu listassa")


nimet.sort()
print(nimet)"""

"""hedelmat = []
hedelma = input("Anna hedelmän nimi, jos haluat lopettaa paina enter ")

while hedelma != "":
    hedelmat.append(hedelma)
    hedelma = input("Anna hedelmän nimi, jos haluat lopettaa paina enter ")
#print(hedelmat)

for h in hedelmat:
    print(f"{h} on hyvää!")"""

#for luku in range(1,1000):
#    print(luku)

for i in range(1,101):
    print("Python on ihanaa! ")
    print("Sql on mahtavaa! ")

i = 0
while i < 100:
    print("Python on ihanaa! ")
    print("Sql on mahtavaa! ")
    i = i + 1
