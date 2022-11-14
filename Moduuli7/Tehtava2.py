#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
#syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
#mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.


nimi_lista = set()

while True:
    newname = input("Anna uusi nimi!: ")
    if newname in nimi_lista:
        print("Aiemmin syötetty nimi.")
    elif newname.lower() == "":
        break
    else:
        print("Uusi nimi")
    nimi_lista.add(newname)

print("---Nimet listassa---")
for i in nimi_lista:
    print(i)