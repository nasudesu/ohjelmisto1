import random

# Var
ind = 0
number_of_entries = 0
inside_of_circle = 0
# Code
# Number of coordinates generated.
while number_of_entries == 0:
    try:
        number_of_entries = int(input("Montakohan pistettä generoidaan?: "))
    except ValueError:
        print("Syötä kokonaisnumero.")

# Evaluating positions.
for i in range(number_of_entries):
    xcor = random.uniform(-1, 1)
    ycor = random.uniform(-1, 1)
    if (xcor ** 2) + (ycor ** 2) < 1:
        inside_of_circle += 1
        ind += 1

# Calculating pi
print(4*inside_of_circle / number_of_entries)