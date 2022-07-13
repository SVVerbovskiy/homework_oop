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
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


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
        self.average_grades = sum(map(sum, self.grades.values())) / count
        return self.average_grades

    def __str__(self):
        pass


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
        res = f'''Имя: {self.name}
Фамилия: {self.surname}'''
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('Maks', 'Korz')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Git']

best_student.rate_lect(best_lecturer, 'Python', 10)
best_student.rate_lect(best_lecturer, 'Python', 10)
best_student.rate_lect(best_lecturer, 'Python', 10)

best_student.rate_lect(best_lecturer, 'Git', 7)
best_student.rate_lect(best_lecturer, 'Git', 4)
best_student.rate_lect(best_lecturer, 'Git', 9)

print(best_student.grades)
print(best_lecturer.grades)
print(reviewer)
print(best_lecturer.average_rating())

