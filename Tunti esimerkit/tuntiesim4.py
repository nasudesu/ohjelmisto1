
import numbers

print("----\njoukko\n----")

#joukko (set)
inventory = {"Valomiekka", "Pyssy", "kolikko"}
print(inventory)
inventory.add("Porkkana")
print(inventory)
#inventory.remove("Pyssy")
print(inventory)
if "Pyssy" in inventory:
    inventory.remove("Pyssy")
else:
    print("Ei löytynyt pyssyä")
print(inventory)

new_set = set()
print(type(new_set))
new_set.add("item 1")
new_set.add("item 2")
for item in new_set:
    print(item)

print(len(new_set))


##sanakirja

phone_numbers = {"Aku": "040-12345678", "Minni": "045-12334567"}
phone_numbers["Viivi"] = "050-12345678"
print("1", phone_numbers)
print("Akun numero:", phone_numbers["Aku"])
phone_numbers["Aku"] = phone_numbers["Viivi"]
print("2", phone_numbers)

for n in phone_numbers:
    print("avaimella " + n + " palautuu " + phone_numbers[n])
    print(n)


#mod7 th3

def add_ariport():
    # TODO: ask & add airport airports dict

def search_ariport():
    # TODO: ask for search string (key) & print vaalue from airports dict

airport = {}
program_running = True

while program_running:
    userinput = ""
    # TODO: input user command
    if userinput == "lopeta":
        add_ariport()
    elif userinput == "Lisää":
        add_ariport()
    elif userinput == "Hae":
        search_ariport()