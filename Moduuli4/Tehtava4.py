import random
luku1 = random.randint(1, 10)
while True:
     numero = int(input("Arvaa numero"))
     if numero < luku1:
        print("Liian pieni arvaus")
     elif numero > luku1:
         print("Liian suuri arvaus")
         numero = int(input("Arvaa numero"))
     elif numero == luku1:
         print("Oikein!")
         break