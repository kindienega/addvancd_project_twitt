# Get the number of students
num_students = int(input("Enter the number of students: "))

# Initialize a list to store the student names and scores
students = []

# Get each student's name and score and add them to the list
for i in range(num_students):
    name = input("Enter student {} name: ".format(i+1))
    score = float(input("Enter student {} score: ".format(i+1)))
    students.append((name, score))

# Sort the students by score in descending order
students.sort(key=lambda x: x[1], reverse=True)

# Display the student with the highest score and the student with the second-highest score
print("Student with the highest score: {} ".format(students[0][0], ))
print("Student with the second-highest score: {} ".format(students[1][0]))
