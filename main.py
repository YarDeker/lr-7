students = {"Vitaly_Prikhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10, 7, 4], 
            "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4, 2, 1], 
            "Mikhail_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4, 8, 4], 
            "Maxim_Derizemlya": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7, 6, 8], 
            "Victoria_Zhuk": [10, 10, 10, 9, 10, 9, 10, 8, 7 , 12, 11, 4], 
            "Andrey_Kuryanov": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8, 4, 8], 
            "Oksana_Dubovets": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10, 7, 4], 
            "Nikita_Stroganov": [6, 7, 8, 9, 10, 10 , 10, 10, 10, 9, 3, 12], 
            "Karina_Nikolaenko": [2, 3, 5, 4, 5, 4, 3, 3, 5 , 8, 3, 10], 
            "Eugenia_Dron": [12, 12, 12, 10, 10, 9, 8, 9, 9 , 8, 5, 2]}

def print_all_grades():
    for student, marks in students.items():
        print(f"{student}: {marks}")

def add_student():
    grades = 12
    student_marks = []
    print("\nВведіть оцінки студента: ")
    for i in range(grades):
        print(f"{i + 1}:", end=" ")
        mark = int(input())
        if mark > 12 : mark = 12
        elif mark < 1 : mark = 1
        student_marks.append(mark)
    student_name = input("Введіть ім'я та прізвище студента: ")
    students[student_name] = student_marks
    print("Студента додано до словника")

def remove_student():
    student_name = input("\nВведіть студента: ")
    if student_name in students: 
        del students[student_name]
    else:
        print(f"Учень {student_name} не знайдений у словнику.")

def sorted_grades():
    for student in sorted(students.keys()):
        print(f"{student}: {students[student]}")

def average_marks():
    averages = {}
    for student, marks in students.items():
        averages[student] = sum(marks) / len(marks)
    aver_class_mark = average_class_mark(averages)
    print(f"Середня оцінка по класу: {aver_class_mark:.2f}")
    return averages

def average_class_mark(averages):
    aver_class_mark = sum(averages.values())/len(averages)
    return aver_class_mark

def above_average_mark_students():
    averages = average_marks()
    aver_class_mark = average_class_mark(averages)
    print("Учні з середньою оцінкою вище середньої по класу:")
    for student, average in averages.items():
        if average > aver_class_mark:
            print(f"{student}: {average:.2f}")

while True:
    print("Якщо ви бажаєте вивести всі значення словника, тоді натисніть -> 1 <-")
    print("Якщо ви бажаєте додати новий запис до словника, тоді натисніть -> 2 <-")
    print("Якщо ви бажаєте видалити запис зі словника, тоді натисніть -> 3 <-")
    print("Якщо ви бажаєте перегляд вмісту словника за відсортованими ключами, тоді натисніть -> 4 <-")
    print("Якщо ви бажаєте визначити середню оцінку кожного учня і всього класу, тоді натисніть -> 5 <-")
    print("Якщо ви бажаєте виведести учнів з середньою оцінкою вище середньої по класу, тоді натисніть -> 6 <-")
    print("Якщо ви бажаєте вийти з програми, тоді натисніть -> 0 <-")

    choice = input("Введіть пункт меню: ")
    match choice:
        case '1': print_all_grades()
        case '2': add_student()
        case '3': remove_student()
        case '4': sorted_grades()
        case '5': 
            averages = average_marks()
            for aver in averages: print(f"{aver}: {averages[aver]:.2f}")
        case '6': above_average_mark_students()
        case '0': break
