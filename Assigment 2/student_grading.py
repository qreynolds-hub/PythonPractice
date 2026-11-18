"""calculate the student's grade based on the scores from the inpiut and 
the predefined weights for each category """

#defined the weights for each category
EXAM_WEIGHT = 0.5
QUIZ_WEIGHT = 0.3
HOMEWORK_WEIGHT = 0.2

#get the scores from the user
midterm_exam_grade = float(input("Enter the midterm exam grade (0-100): "))
final_exam_grade = float(input("Enter the final exam grade (0-100): "))
assignment_one = float(input("Enter the grade for assignment one (0-100): "))
assignment_two = float(input("Enter the grade for assignment two (0-100): "))
quiz_one = float(input("Enter the grade for quiz one (0-100): "))
quiz_two = float(input("Enter the grade for quiz two (0-100): "))

#calculate the average for each category and mulrtiply by the weight for that catyegory
exam_grade = (midterm_exam_grade + final_exam_grade) / 2
assignment_grade = (assignment_one + assignment_two) / 2
quiz_grade = (quiz_one + quiz_two) / 2
#calculate the final grade by adding the weighted averages and divide by 100 to convert to a percentage
final_grade = (exam_grade * EXAM_WEIGHT + assignment_grade * HOMEWORK_WEIGHT + quiz_grade * QUIZ_WEIGHT)

# print the final grade with 2 decimal places using f-string formatting
print(f"The final grade is: {final_grade:.2f}%")