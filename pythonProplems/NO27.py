def convert():
    choice = input("Enter the conversion you'd like to perform (1 for kg to lbs, 2 for miles to km, 3 for hours to minutes): ")

    if choice == '1':
        kg = float(input("Enter weight in kilograms: "))
        lbs = kg * 2.20462
        print(f"{kg} kilograms is {lbs} pounds")

    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles * 1.60934
        print(f"{miles} miles is {km} kilometers")

    elif choice == '3':
        hours = float(input("Enter time in hours: "))
        minutes = hours * 60
        print(f"{hours} hours is {minutes} minutes")

    else:
        print("Invalid choice. Please enter a valid conversion option (1, 2, or 3).")

convert()
