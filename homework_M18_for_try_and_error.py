import random
students = ['Алина', 'Павел', 'Карлыгаш', 'Даурен', 'Вика']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks['Алина'] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks['Алина']['Математика'] = marks
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks['Алина']['Русский язык'] = marks
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks['Алина']['Информатика'] = marks
for student in students:
    print(f'''{student}
            {students_marks['Алина']}''')


print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалять оценки ученика по предмету
        5. Редактировать оценки ученки по предмету
        6. Удалить ученика
        7. Выход из программы
        ''')
while True :
    command = int(input('Введите команду: '))
    if command == 1:
        print('1.Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Ввдетие предмет:')
        mark =int(input('Введите оценку:'))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student]
            [class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка  {mark}')
        else:
            print ('ОЩИБКА:неверное имя ученика или название предмета' )
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалять оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет:')
        mark = int(input('Введите оценку,которую нужно удалить:'))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student]
            del students_marks[student]
            print(f'Для {student} по предмету {class_} удалена оценка  {mark}')
        else:
            print('ОЩИБКА:неверное имя ученика или название предмета')
    elif command == 5:
        print('5.Редактировать оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет:')
        mark = int(input('Введите оценку,которую нужно отредактировать:'))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            del students_marks[student]
            print(f'Для {student} по предмету {class_} удалена оценка  {mark}')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет:')
        mark = int(input('Введите оценку,которую нужно добавить вместо удаленной:'))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student]
            [class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка, вместо удаленной {mark}')
        else:
            print('ОЩИБКА:неверное имя ученика или название предмета')
    elif command == 6:
        print('6.Удалить ученика из списка.')
        del_student = input('Введите имя ученика,которого нужно удалить из списка : ')
        if del_student in students_marks.keys():
            del  students_marks[del_student]
        else:
            print('Данного ученик в списке нет.')
    elif command == 7:
        print('7. Выход из программы')
        break

