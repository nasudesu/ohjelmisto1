
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luovti_paino = 13.3
naulat_paino = 32*luovti_paino
leiviskat_paino = 20*naulat_paino

yhteensa_luoti = luodit*luovti_paino
yhteensa_naulat = naulat*naulat_paino
yheenta_leiviskat = leiviskat_paino*leiviskat

grammat_yhteensa = yheenta_leiviskat+yhteensa_luoti+yhteensa_naulat

kilot = int(grammat_yhteensa/1000)
grammat = grammat_yhteensa%1000

print(f"Kilot: {kilot} \nGrammat: {grammat:.2f}")
