class koira:
    jalka_maara = 4
    tehty = 0
    def __init__(self, nimi, syntymavuosi, rotu, paino, haukahdus = "vuh vuh"):
        self.paino = paino
        self.rotu = rotu
        self.syntymavuosi = syntymavuosi
        self.nimi = nimi
        self.haukahdus = haukahdus
        koira.tehty = koira.tehty + 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)

#Pääohjelma

koira1 = koira("Churro", 1999, "Saksanpaimenkoira", 25, "Räyh Räyh")
print(f"koira1 \n "
      f"nimi:{koira1.nimi:s} \n "
      f"syntymävuosi:{koira1.syntymavuosi:d} \n "
      f"rotu:{koira1.rotu:s} \n "
      f"paino:{koira1.paino:d}")

koira2 = koira("Pulivari", 1938, "Berhandilainen", 40)
print(f"koira2 \n "
      f"nimi:{koira2.nimi} \n "
      f"syntymävuosi:{koira2.syntymavuosi} \n "
      f"rotu:{koira2.rotu} \n "
      f"paino:{koira2.paino}")

koira3 = koira("Pulla", 1997, "Suzuki", 30)

koira1.hauku(5)
koira2.hauku(2)

#print(koira.jalka_maara)
print(koira1.jalka_maara)
koira.jalka_maara = 3
print(koira2.jalka_maara)
print (f"Koiria on nyt {koira.tehty}.")
koira1.tehty = 10
print(koira1.tehty)
