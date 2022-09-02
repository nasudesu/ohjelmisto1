import random
luku1 = random.randint(1, 10)
numero = int(input("Arvaa numero"))
while True:
     if numero < luku1:
        print("Liian pieni arvaus")
        numero = int(input("Arvaa numero"))
     elif numero > luku1:
         print("Liian suuri arvaus")
         numero = int(input("Arvaa numero"))
     elif numero == luku1:
         print("Oikein!")
         break
