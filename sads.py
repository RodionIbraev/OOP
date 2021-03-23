class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        name = 'Имя: ' + self.name
        surname = 'Фамилия: ' + self.surname
        avrg_grade = 'Средняя оценка за домашнее задание: ' + str(self.average_grade())
        courses_in_progress = 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress)
        finished_courses = 'Завершенные курсы: ' + ', '.join(self.finished_courses)
        return '\n'.join([name, surname, avrg_grade, courses_in_progress, finished_courses])

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def average_grade(self):
        sum_grades = 0
        num_grades = 0
        for grades_for_course in self.grades.values():
            sum_grades += sum(grades_for_course)
            num_grades += len(grades_for_course)
        return sum_grades / num_grades

    def grading_lecturers(self, lect, course, grade):
        if isinstance(lect, Lecturer) and (course in self.courses_in_progress and course in lect.courses_attached):
            if 1 <= grade <= 10:
                lect.grades.append(grade)
            else:
                return 'Неккоректная оценка'
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        name = 'Имя: ' + self.name
        surname = 'Фамилия: ' + self.surname
        avrg_grade = 'Средняя оценка за лекции: ' + str(self.average_grade())
        return '\n'.join([name, surname, avrg_grade])

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        name = 'Имя: ' + self.name
        surname = 'Фамилия: ' + self.surname
        return '\n'.join([name, surname])

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (course in self.courses_attached and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grade_for_all_students(students, course):
    average_grades = []
    for student in students:
        grades = student.grades[course]
        average_grades.append(sum(grades) / len(grades))
    return sum(average_grades) / len(average_grades)


def average_grade_for_all_lecturers(lecturers, course):
    average_grades = []
    for lecturer in lecturers:
        grades = lecturer.grades[course]
        average_grades.append(sum(grades) / len(grades))
    return sum(average_grades) / len(average_grades)


if __name__ == '__main__':
    student_1 = Student('Rodion', 'Ibraev', 'Male')
    student_1.finished_courses = ['Введение в программирование', 'Основы Python']
    student_1.courses_in_progress = ['Python', 'Git']

    student_2 = Student('Alena', 'Shaidurova', 'Female')
    student_2.finished_courses = ['Python', 'Git']
    student_2.courses_in_progress = ['Введение в программирование', 'Основы Python']

    lect_1 = Lecturer('Steve', 'Jobs')
    lect_1.courses_attached = ['Введение в программирование', 'Python']

    lect_2 = Lecturer('Mark', 'Zuckerberg')
    lect_2.courses_attached = ['Основы Python', 'Git']

    revr_1 = Reviewer('Bill', 'Gates')
    revr_1.courses_attached = ['Введение в программирование', 'Python']
    revr_1.rate_hw(student_1, 'Python', 7)
    revr_1.rate_hw(student_1, 'Введение в программирование', 10)
    revr_1.rate_hw(student_2, 'Python', 8)
    revr_1.rate_hw(student_2, 'Введение в программирование', 9)

    revr_2 = Reviewer('Elon', 'Musk')
    revr_2.courses_attached = ['Основы Python', 'Git']
    revr_2.rate_hw(student_1, 'Основы Python', 5)
    revr_2.rate_hw(student_1, 'Git', 9)
    revr_2.rate_hw(student_2, 'Основы Python', 10)
    revr_2.rate_hw(student_2, 'Git', 8)

    student_1.grading_lecturers(lect_1, 'Введение в программирование', 9)
    student_1.grading_lecturers(lect_1, 'Python', 6)
    student_1.grading_lecturers(lect_2, 'Основы Python', 7)
    student_1.grading_lecturers(lect_2, 'Git', 10)

    student_2.grading_lecturers(lect_1, 'Введение в программирование', 8)
    student_2.grading_lecturers(lect_1, 'Python', 9)
    student_2.grading_lecturers(lect_2, 'Основы Python', 6)
    student_2.grading_lecturers(lect_2, 'Git', 7)

    print('Студенты:')
    print('---------------------1---------------------')
    print(student_1)
    print('---------------------1---------------------\n')
    print('---------------------2---------------------')
    print(student_2)
    print('---------------------2---------------------\n')
    print('------------Сравнение студентов------------')
    print('Студент1 > Студент2:', student_1 > student_2)
    print('Студент1 < Студент2:', student_1 < student_2)
    print('Студент1 == Студент2:', student_1 == student_2)
    print('Студент1 <= Студент2:', student_1 <= student_2)
    print('Студент1 >= Студент2:', student_1 >= student_2)
    print('-------------------------------------------\n')

    print('Лекторы:')
    print('---------------------1---------------------')
    print(lect_1)
    print('---------------------1---------------------\n')
    print('---------------------2---------------------')
    print(lect_2)
    print('---------------------2---------------------\n')
    print('------------Сравнение лекторов-------------')
    print('Лектор1 > Лектор2:', lect_1 > lect_2)
    print('Лектор1 < Лектор2:', lect_1 < lect_2)
    print('Лектор1 == Лектор2:', lect_1 == lect_2)
    print('Лектор1 <= Лектор2:', lect_1 <= lect_2)
    print('Лектор1 >= Лектор2:', lect_1 >= lect_2)
    print('-------------------------------------------\n')

    print('Проверяющие:')
    print('---------------------1---------------------')
    print(revr_1)
    print('---------------------1---------------------\n')
    print('---------------------2---------------------')
    print(revr_2)
    print('---------------------2---------------------\n')