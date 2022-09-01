

valid_username = "python"
valid_password = "rules"
tryCount = 0
maxTries = 5
while tryCount < maxTries:
    tryCount += 1
    input_username = input("käyttis? ")
    input_password = input("salis? ")
    if valid_username == input_username and input_password == valid_password:
        print("Terve")
        break
    print("Virheellinen kiirjautumistiedot yritä uudellee")