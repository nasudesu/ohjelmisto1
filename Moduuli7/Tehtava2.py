#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
#syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
#mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.


nimilista = set()

while True:
    newname = input("Anna uusi nimi!: ")
    if newname in nimilista:
        print("Aiemmin syötetty nimi.")
    elif newname.lower() == "":
        break
    else:
        print("Uusi nimi")
    nimilista.add(newname)

print("---Nimet listassa---")
for j in nimilista:
    print(j)