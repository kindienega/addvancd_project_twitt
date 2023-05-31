count_positives = 0
count_negatives = 0
total = 0
count = 0

while True:
    number = int(input("Enter an int value, the program exists if the input is 0 "))
    if number == 0:
        break
    elif number > 0:
        count_positives += 1
    elif number < 0:
        count_negatives += 1
    total += number
    count += 1

if count > 0:
    average = total / count
    print(f"The number of positives is  {count_positives}")
    print(f"The number of negatives is  {count_negatives}")
    print(f"The total is {total}")
    print(f"The average is  {average:.2f}")
else:
    print("No integers were entered.")
