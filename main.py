class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

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
        self.average_hw = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_hw

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_hw() < other.average_hw()

    def __str__(self):
        res = f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_hw()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'''
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

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

student_2 = Student('Helen', 'Park', 'woman')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']

reviewer.rate_hw(student_1, 'Python', 9)
reviewer.rate_hw(student_1, 'Python', 7)
reviewer.rate_hw(student_1, 'Python', 8)

reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 9)
reviewer.rate_hw(student_2, 'Python', 6)

best_lecturer = Lecturer('Maks', 'Korz')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']

student_1.rate_lect(best_lecturer, 'Python', 10)
student_1.rate_lect(best_lecturer, 'Python', 10)
student_1.rate_lect(best_lecturer, 'Python', 10)

student_1.rate_lect(best_lecturer, 'Git', 7)
student_1.rate_lect(best_lecturer, 'Git', 4)
student_1.rate_lect(best_lecturer, 'Git', 9)

print(student_1.grades)
print(student_2.grades)
print(best_lecturer.grades)
print(reviewer)
print(best_lecturer)
print(student_1)
print(student_2)
