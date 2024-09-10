def grade(number_of_student, number_of_subject):
    student_grade = [[0 for _ in range(number_of_subject)]for _ in range(number_of_student)]
    addition = [0 for _ in range (number_of_student)]
    new_addition = [0 for _ in range (number_of_student)]
    average = [0 for _ in range (number_of_student)]
    position = [0 for _ in range (number_of_student)]

    for index in range(number_of_student):
        for subject in range(number_of_subject):
            student_grade[index][subject] = int(input(f"Entering score for student{index + 1}\nEnter score for subject{subject + 1}: "))
            if student_grade[index][subject] < 0:
                student_grade[index][subject] = 0
            if student_grade[index][subject] > 100:
                student_grade[index][subject] = 100
            addition[index] += student_grade[index][subject]
            new_addition[index] += student_grade[index][subject]
        average[index] = addition[index] / number_of_subject

    new_addition.sort()
    for index in range(number_of_student):
        for subject in range(number_of_student):
            if addition[index] == new_addition[subject]:
                position[index] = number_of_student - subject


