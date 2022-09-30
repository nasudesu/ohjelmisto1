import random


def silmaluku():
    return random.randint(1, 6)



while True:
    noppa1 = silmaluku()
    print(noppa1)
    if noppa1 == 6:
        break