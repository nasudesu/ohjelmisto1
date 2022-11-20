import random


def silmaluku():
    return random.randint(1, 6)


while True:
    cube = silmaluku()
    print(cube)
    if cube == 6:
        break
