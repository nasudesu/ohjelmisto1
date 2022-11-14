list_of_numbers = []
first_five_in_list = 5
while True:
    user_input = input("anna luku : ")
    if user_input == "":
        break
    else:
        list_of_numbers.append(int(user_input))
list_of_numbers.sort(reverse=True)
answer = list_of_numbers[:first_five_in_list]
print(answer)