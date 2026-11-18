"""Calculate the student's final grade based on user input
and the predefined weights for each category.
Validate all inputs before calculating the final grade.
"""

# Define the weights for each category
EXAM_WEIGHT = 0.5
QUIZ_WEIGHT = 0.3
HOMEWORK_WEIGHT = 0.2

# Define the maximum grade for each category
EXAM_MAX = 100
QUIZ_MAX = 100
HOMEWORK_MAX = 100


# Function to validate user input
def get_valid_grade(prompt, maximum):
    while True:
        try:
            grade = float(input(prompt))

            if 0 <= grade <= maximum:
                return grade
            else:
                print(f"Invalid grade! Enter a number between 0 and {maximum}.")

        except ValueError:
            print("Invalid input! Please enter a numeric grade.")


# Get the scores from the user
midterm_exam_grade = get_valid_grade(
    "Enter the midterm exam grade (0-100): ", EXAM_MAX
)

final_exam_grade = get_valid_grade(
    "Enter the final exam grade (0-100): ", EXAM_MAX
)

assignment_one = get_valid_grade(
    "Enter the grade for assignment one (0-100): ", HOMEWORK_MAX
)

assignment_two = get_valid_grade(
    "Enter the grade for assignment two (0-100): ", HOMEWORK_MAX
)

quiz_one = get_valid_grade(
    "Enter the grade for quiz one (0-100): ", QUIZ_MAX
)

quiz_two = get_valid_grade(
    "Enter the grade for quiz two (0-100): ", QUIZ_MAX
)


# Calculate the average for each category
exam_grade = (midterm_exam_grade + final_exam_grade) / 2
assignment_grade = (assignment_one + assignment_two) / 2
quiz_grade = (quiz_one + quiz_two) / 2

# Calculate the final grade using weighted averages
final_grade = (
    (exam_grade / EXAM_MAX) * EXAM_WEIGHT
    + (assignment_grade / HOMEWORK_MAX) * HOMEWORK_WEIGHT
    + (quiz_grade / QUIZ_MAX) * QUIZ_WEIGHT
) * 100

# Display the final grade with 2 decimal places
print(f"The final grade is: {final_grade:.2f}%")