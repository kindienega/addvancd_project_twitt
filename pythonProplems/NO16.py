# Initialize the sum variable
sum = 0
# Loop through the series and add each term to the sum
for i in range(1, 98, 2):
    term = i / (i + 2)
    sum += term

# Print the sum
print("The sum of the series is:", sum)
