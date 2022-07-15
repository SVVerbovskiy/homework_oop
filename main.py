class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_homework = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_homework

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_hw() < other.average_hw()

    def __str__(self):
        res = f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_hw()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_grades = None

    def average_rating(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_grades = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_grades

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rating() < other.average_rating()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Вводный курс по программированию']

student_2 = Student('Helen', 'Park', 'woman')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Вводный курс по дизайну']

reviewer_1 = Reviewer('Geoffrey', 'Cameron')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Charles', 'Pitts')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 6)

reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 9)

reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)

lecturer_1 = Lecturer('Maks', 'Korz')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Agnes', 'Stokes')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

student_1.rate_lect(lecturer_1, 'Python', 10)
student_1.rate_lect(lecturer_1, 'Python', 9)
student_1.rate_lect(lecturer_1, 'Python', 10)

student_1.rate_lect(lecturer_1, 'Git', 9)
student_1.rate_lect(lecturer_1, 'Git', 5)
student_1.rate_lect(lecturer_1, 'Git', 9)

student_2.rate_lect(lecturer_2, 'Python', 9)
student_2.rate_lect(lecturer_2, 'Python', 8)
student_2.rate_lect(lecturer_2, 'Python', 10)

student_2.rate_lect(lecturer_2, 'Git', 9)
student_2.rate_lect(lecturer_2, 'Git', 6)
student_2.rate_lect(lecturer_2, 'Git', 9)

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]


def average_grade(list, course):
    grades_all = []
    for current_student in list:
        for key, value in current_student.grades.items():
            if key == 'Python':
                for grade in value:
                    grades_all.append(grade)
    average_grades = round(sum(grades_all) / len(grades_all), 2)
    if list == students:
        print(f'Средняя оценка для всех студентов по курсу "Python": {average_grades}')
    if list == lecturers:
        print(f'Средняя оценка для всех лекторов по курсу "Python": {average_grades}')


print(student_1)
print()
print(student_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)
print()
average_grade(students, 'Python')
average_grade(lecturers, 'Python')
