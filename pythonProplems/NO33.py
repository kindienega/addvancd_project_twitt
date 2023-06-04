num_lines = int(input("Enter the number of the lines: "))
for i in range(1, num_lines+1):
    #Print spaces
    for j in range(num_lines-i):
        print(" ", end="")
    #Print decreasing numbers
    for j in range (i, 1, -1):
        print(j, end="")
    #Print increasing numbers
    for j in range(1, i+1):
        print(j, end="")
    #move to the next line
    print()