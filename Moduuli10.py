class Auto:
    def __init__(self, rekkari, vari):
        self.rekkari = rekkari
        self.vari = vari

class Maalaamo:
    def maalaa(self, auto, vari):
        auto.vari = vari


#Pääohjelma

kotsa = Auto("ABC-123", "Ruskea")
print(kotsa.vari)
penamaalaamo = Maalaamo()
penamaalaamo.maalaa(kotsa, "Punainen")
print(kotsa.vari)

