gender = input("Biological gender male or female: ")
hemoglobin = int(input("Hemoglobin value: "))
if gender == "male":
    if hemoglobin >= 134 and hemoglobin <= 195:
      print("Hemoglobin value is normal thank you bye!")
if gender == "female":
    if hemoglobin >= 117 and hemoglobin <= 175:
        print("Hemoglobin value is normal thank you bye!")
    else:
        print("Hemoglobin value not normal get help!")
