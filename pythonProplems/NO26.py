tuition = 10000
yearly_increase = 0.05

# Calculate tuition in ten years
for i in range(10):
    tuition = tuition * (1 + yearly_increase)

print("Tuition in ten years:", tuition)

# Calculate total cost of four years' worth of tuition starting ten years from now
total_cost = 0
for i in range(10, 14):
    total_cost += tuition * (1 + yearly_increase)**(i-10)

print("Total cost of four years' tuition starting ten years from now:", total_cost)
