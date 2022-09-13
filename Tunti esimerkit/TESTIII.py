import random


def say_hello(name):
    print(F"Moro {name}")
    print("hyvää päivää")


name = "aku"
say_hello("iines")
say_hello("minni hiiri")
print(name)


def sum_of_two_inst(number1, number2):
    result = number1+number2
    print(f"{number1}+{number2}={result}")
    return result #paluu arvo

# funktiokutsu
result_sum = sum_of_two_inst(1, 2)
print("Summa:", result_sum)
print("4+5:", sum_of_two_inst(4, 5))

#lottokone  arpoo n numeroa välillä 1-total_numbers
def create_lottery_row(numberamount, totalnumbers):
    row = []
    for i in range(7):
        rndnum = random.randint(1, 39)
        while row.count(rndnum) > 0:
            rndnum = random.randint(1, 39)
            #print("tuli tuplat: ", rndnum)
            rndnum = random.randint(1, totalnumbers)
        row.append(rndnum)
        print(f"{i+1}. nro: {rndnum}")
    row.sort()
    return row

myRow = create_lottery_row(7, 39)
print("Lottorivi:" , myRow)
