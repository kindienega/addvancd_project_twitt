# define the starting and ending years
start_year = 2001
end_year = 2100

# iterate over each year in the range
for year in range(start_year, end_year+1):
    # check if the year is a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # print the year followed by a space
        print(year, end=" ")
        # if we have printed ten years, start a new line
        if (year - start_year + 1) % 10 == 0:
            print()
