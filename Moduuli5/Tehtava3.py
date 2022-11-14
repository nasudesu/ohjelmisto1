user_input = int(input("Anna kokonaisluku: "))

for x in range(2, user_input):
    if user_input % x == 0:
        print(f"Luku {user_input} ei ole alkuluku!")
        break
else:
    print(f"Luku {user_input} on alkuluku!")



