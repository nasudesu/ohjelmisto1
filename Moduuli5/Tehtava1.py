import random

summa = 0
kuutiot = input("montako kuutiota haluat heittää? ")
for i in range(int(kuutiot)):
    noppa = random.randint(1, 6)
    print(noppa)
    summa += noppa
print(f"Noppien summa: {summa}")

