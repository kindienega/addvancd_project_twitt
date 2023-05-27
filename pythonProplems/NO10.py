num_students = int(input("Enter the number of students who took the test: "))
marks = []

for i in range(num_students):
    mark = int(input(f"Enter the marks of student {i+1}: "))
    marks.append(mark)

num_passed = sum(mark > 20 for mark in marks)

print(f"{num_passed} students scored greater than 20 out of 30.")
