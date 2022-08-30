#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
#ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
#Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#1  LUX on parvekkeellinen hytti yläkannella.
#2  A on ikkunallinen hytti autokannen yläpuolella.
#3  B on ikkunaton hytti autokannen yläpuolella.
#4  C on ikkunaton hytti autokannen alapuolella.

#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hytti = input("Mikä hyttiluokka: ")
if hytti.upper == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti.upper == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti.upper == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti.upper == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")#else:
#    print("Virheellinen hyttiluokka. ")









