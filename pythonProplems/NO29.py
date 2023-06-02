num_students = int(input("Enter the number of students: "))

# Initialize variables to keep track of highest score and corresponding student name
highest_score = -1
highest_scoring_student = ""

# Loop through each student and prompt for their name and score
for i in range(num_students):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))

    # Check if the current student has a higher score than the previous highest score
    if score > highest_score:
        highest_score = score
        highest_scoring_student = name

# Display the name of the student with the highest score
print(f"The student with the highest score is {highest_scoring_student} with a score of {highest_score}.")
