leiviskät = input('anna leiviskät: ')
naulat = input('anna naulat: ')
luodit = input('anna luodit: ')

luoti = 13.3
naula = 32*luoti
leiviskä = 20*naula

luotipaino = luoti*float(luodit)
naulapaino = naula*float(naulat)
leiviskäpaino = leiviskä*float(leiviskät)

grammatyheensä = luotipaino+naulapaino+leiviskäpaino

kiloiks = grammatyheensä//1000
grammat = f'{(grammatyheensä/1000-kiloiks)*1000:.2f}'

print(f'Massa nykymittojen mukaan: {int(kiloiks)} kilogrammaa ja {grammat} grammaa. ')