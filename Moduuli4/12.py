import random

computernum = random.randint(1, 10)
print("Olen arponut kokonaisluvun (1-10)")
playerguess = int(input("Koita keksiä luku: "))

if playerguess == computernum:
    print(f"Oikein arvattu! Luku oli {computernum}.")
elif playerguess < computernum:
    print(f"Lukusi on liian pieni (Lukusi oli {playerguess})")
elif playerguess > computernum:
    print(f"Lukusi on liian suuri (Lukusi oli {playerguess})")

while playerguess != computernum:
    playerguess = int(input("Arvaa uudelleen: "))
    if playerguess == computernum:
        print(f"Oikein arvattu! Luku oli {computernum}.")
    elif playerguess < computernum:
        print(f"Lukusi on liian pieni (Lukusi oli {playerguess})")
    elif playerguess > computernum:
        print(f"Lukusi on liian suuri (Lukusi oli {playerguess})")