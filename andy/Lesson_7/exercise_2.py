"""
- Define a new class Student which is derived from Human and has:
  grade field.
  do_hobby - print 'dancing' or some another hobby
"""
import andy.Lesson_7.exercise_1


class Student(andy.Lesson_7.exercise_1.Human):

    def __init__(self, firstname, lastname, grade):
        super().__init__(firstname, lastname)
        self.grade = grade

    def do_hobby(self):
        return self.full_name + " ebet Petra Kovarskogo"


a = Student("Artem", "Nizhnik", "Shkolnik")
print(a.do_hobby())
print(a.grade)
