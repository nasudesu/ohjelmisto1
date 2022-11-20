import math
countlist = ["ekan", "toisen"]
count = 0



def pizzaCalc(biground, hunnie):
    return hunnie/(math.pi*((biground/2)**2))


while count < 2:
        priceperarea = pizzaCalc(float(input("Anna " + countlist[count] + " pizzan halkaisija senttimetreinä: ")),
                                 float(input("Anna " + countlist[count] + " pizzan hinta: ")))
        if count == 0:
            price1 = round(priceperarea, 2)
        elif count == 1:
            price2 = round(priceperarea, 2)
        count = count + 1

if price1 == price2:
    print("Molemilla pizzoilla on sama hinta per bite.")
elif price1 < price2:
    print("Ekalla pizzalla on parempi hinta.")
else:
    print("Toisella pizzalla on parempi hinta.")