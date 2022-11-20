
def numbers(nlist):
    summing = sum(nlist)
    return summing


numlist = []
reduce = 10

for i in range(0, 10):
    numlist.append(int(input(f"Anna kokonaislukuja ({reduce})kpl: ")))
    reduce -= 1

numsum = numbers(numlist)
print(f"Lukujen summa: {numsum}")