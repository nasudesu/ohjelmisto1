def change(gallon_amount):
    liter_change = gallon_amount * 3.785
    return liter_change


gallons = float(input("Gallona määrä?: "))

while gallons >= 0:
    changer = change(gallons)
    liter = changer
    if gallons >= 0:
        print(f"{gallons} gallonaa on n. {liter}L bensaa")
    gallons = float(input("Gallona määrä?: "))