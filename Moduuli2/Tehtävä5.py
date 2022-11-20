leiviskat = input('anna leiviskat: ')
naulat = input('anna naulat: ')
luodit = input('anna luodit: ')

luoti = 13.3
naula = 32*luoti
leiviska = 20*naula

luotipaino = luoti*float(luodit)
naulapaino = naula*float(naulat)
leiviskapaino = leiviska*float(leiviskat)

grammatyheensa = luotipaino+naulapaino+leiviskapaino

#2954595 / 1000 => 29.54595
#2954595 // 1000 => 29.0
#2954595 % 1000 => 54595

kiloiks = grammatyheensa//1000
grammat = f'{(grammatyheensa/1000-kiloiks)*1000:.2f}'

print(f'Massa nykymittojen mukaan: {int(kiloiks)} kilogrammaa ja {grammat} grammaa. ')