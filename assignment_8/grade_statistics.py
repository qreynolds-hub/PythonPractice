
from pathlib import Path
import csv

GRADES_FILE = Path(__file__).resolve().parent / "grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range.
    """
    try:
        weight_final_list = []

        with open(GRADES_FILE, "r", newline="") as file:
            reader = csv.reader(file)

            # Skip the header row
            next(reader, None)

            # Process each student's grades
            for row in reader:
                if row:
                    weight_final_list.append(process_row(row))

        # Print the grade summary
        analyze_grade(weight_final_list)

    except FileNotFoundError:
        print("Error: Grades file not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except (ValueError, csv.Error) as err:
        print(f"Error processing grades: {err}")

    except Exception as err:
        print(f"An unexpected error occurred: {err}")


def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns).
    """
    if len(row) != 11:
        raise ValueError("Each student row must contain 11 columns.")

    # Skip Name and StudentID
    test_scores = [float(score) for score in row[2:6]]
    exam_scores = [float(score) for score in row[6:8]]
    discussion_scores = [float(score) for score in row[8:10]]
    project_score = float(row[10])

    # Calculate subject averages
    test_avg = average_subject(test_scores)
    exam_avg = average_subject(exam_scores)
    discussion_avg = average_subject(discussion_scores)

    # Calculate weighted final grade
    return weight_final(
        test_avg,
        exam_avg,
        discussion_avg,
        project_score
    )


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    return sum(subject_list) / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above.
    """
    return (
        test_avg * TEST_WEIGHT
        + exam_avg * EXAM_WEIGHT
        + discussion_avg * DISCUSSION_WEIGHT
        + project_score * PROJECT_WEIGHT
    )


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60.
    """
    grade_90 = 0
    grade_80 = 0
    grade_70 = 0
    grade_60 = 0
    below_60 = 0

    for grade in weight_final_list:
        if grade >= 90:
            grade_90 += 1
        elif grade >= 80:
            grade_80 += 1
        elif grade >= 70:
            grade_70 += 1
        elif grade >= 60:
            grade_60 += 1
        else:
            below_60 += 1

    print("\nFinal Grade Summary")
    print("-------------------")
    print(f"90 or above: {grade_90}")
    print(f"80-89:       {grade_80}")
    print(f"70-79:       {grade_70}")
    print(f"60-69:       {grade_60}")
    print(f"Below 60:    {below_60}")
    print("-------------------")
    print(f"Total students: {len(weight_final_list)}")


if __name__ == "__main__":
    main()

