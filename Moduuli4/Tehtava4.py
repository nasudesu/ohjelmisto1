import random
luku1 = random.randint(1, 10)
print(luku1)
noppa = int(input("Arvaa numero"))
while True:
     if noppa < luku1:
        print("Liian pieni arvaus")
        noppa = int(input("Arvaa numero"))
     elif noppa > luku1:
         print("Liian suuri arvaus")
         noppa = int(input("Arvaa numero"))
     elif noppa == luku1:
         print("Oikein!")
         break
