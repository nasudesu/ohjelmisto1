#pituus = float(input('Kuinka pitkä olet:'))
#if 1.5 <= pituus <= 2.0 :
#    print("Olet Normi mittane")

#if pituus >= 1.5 and pituus <= 2.0:
 #   print("Olet normi pitunen")

#if pituus <1.5 or pituus > 2.0:
 #   print("Et ole normi mittane")

#mjono1 = input("Anna Eläin laji")
#mjono2 = input("Anna toinen eläin laji")

#if mjono1 == mjono2:
    #print("Annoit saman elainlajin")


"""ika = int(input("Anna ikäsi"))
if ika >= 15 and ika < 18 :
    paino = float(input("Anna painosi"))
if ika >= 18 or (ika >= 15 and paino >= 55):
    print("Lääkkeenkäyttö sallittu")
else:
    print("Lääkkeenkäyttö ei ole sallittua")

#Ei kaddu koska ikä testataan ennen kuin paino ja jos ika ei ei yli 15 niin paino ei ikinä päädytä vertaamaan


if ika >= 15 and ika <18:
   paino = float(input("Anna pianosi"))
if ika >= 18:
    print("Lääkkeen käyttösallittu")
if ika >= 15 and ika <18:
    if paino >= 55:
        print("Lääkkeen käyttö sallittu")

#Ei yhtään kikkaa versio, uutena asiana kaksi sisäkäistä if-rakennetta"""

ika = int(input("Anna ikäsi:"))
if ika >= 18:
    print("Lääkkeen käyttö sallittu!")
elif ika < 15 :
    print("Lääkkeen käyttö ei sallittu")
else:
    paino = float(input("Anna painosi"))
    if paino >= 55:
        print("Lääkkeen käyttö sallittu")
    else:
        print("Lääkkeen käyttö sallittua")
print("Kiitos Kun käytit Lääkeohjelmaa")









#Muuttuja = 5
#int tyyppi koska sinne sijoitettiin kokonais luku

#Muuttuja2 = 1.49
#Float/double-tyyppinen koska sinne sijoitettiin desimaalilku

#muuttuja3 = "Rakas"
#String-tyyppinen, koska sinne sijoitettiin merkkijono

#Muuttuja4 = input("Kirjota numero")
#String tyyppinen, jos halutaan vertailla suuruutta tai laske jotain



