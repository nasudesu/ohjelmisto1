import random


def silmaluku(lol):
    return random.randint(1, lol)


question = int(input("Nopan maksimi silmäluku?: "))

while True:
    cube = silmaluku(question)
    print(cube)
    if cube == question:
        break
