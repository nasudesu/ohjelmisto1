

def remove_even_nums_from_list(list_of_numbers):
    list_with_even_numbers = []
    for number in list_of_numbers:
        if(number % 2) == 0:
            list_with_even_numbers.append(number)
    return list_with_even_numbers


original_list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(original_list_of_numbers)
print(remove_even_nums_from_list(original_list_of_numbers))