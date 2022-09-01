import random
luku1 = random.randint(1, 10)
print(luku1)
noppa = input("Arvaa numero")
while True:
     if float(noppa) < float(luku1):
        print("Liian pieni arvaus")
        noppa = input("Arvaa numero")
     elif float(noppa) > float(luku1):
         print("Liian suuri arvaus")
         noppa = input("Arvaa numero")
     else:
         print("Oikein!")
         break
