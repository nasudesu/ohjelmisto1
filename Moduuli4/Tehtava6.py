import random

user_N = int(input("Anna pisteiden lukumäärä: "))
N = 0
n = 0

while N != user_N:
    N += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
if N == user_N:
    pii = 4 * n / N
    print(f"Likiarvo on: {pii}")