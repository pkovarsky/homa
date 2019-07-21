"""
- Initialize a list of 5 students and sort them by grade.
- Initialize a list of 5 workers and sort them by money per hour.
- Concatenate the lists and call do_hobby on each object.
Note: made these exercise at one file. As for me it's look better
"""
import andy.Lesson_7.exercise_2
import andy.Lesson_7.exercise_3

"""
- Initialize a list of 5 students and sort them by grade.
"""
first_student = andy.Lesson_7.exercise_2.Student("Artem", "Nizhnik", "Pezduk")
second_student = andy.Lesson_7.exercise_2.Student("Petr", "Kovarsky", "Batya")
third_student = andy.Lesson_7.exercise_2.Student("Pudel'", "Pudel'", "Pes")
fourth_student = andy.Lesson_7.exercise_2.Student("Homa", "Nude", "Pidor")
fifth_student = andy.Lesson_7.exercise_2.Student("Igor", "Kae", "Biiiiiiiig")

students = [first_student, second_student, third_student, fourth_student, fifth_student]
sorted_student_list = sorted(students, key=lambda x: x.grade)
for stud in sorted_student_list:
    print(stud.full_name, stud.grade)

"""
- Initialize a list of 5 workers and sort them by money per hour.
"""
first_worker = andy.Lesson_7.exercise_3.Worker("Artem", "Nizhnik", 70, 40)
second_worker = andy.Lesson_7.exercise_3.Worker("Petr", "Kovarsky", 150, 20)
third_worker = andy.Lesson_7.exercise_3.Worker("Pudel'", "Pudel'", 50, 8)
fourth_worker = andy.Lesson_7.exercise_3.Worker("Homa", "Nude", 60, 40)
fifth_worker = andy.Lesson_7.exercise_3.Worker("Igor", "Kae", 500, 30)

workers = [first_worker, second_worker, third_worker, fourth_worker, fifth_worker]
sorted_worker_list = sorted(workers, key=lambda x: x.money_per_hour())
for work in sorted_worker_list:
    print(work.full_name, work.money_per_hour())

"""
- Concatenate the lists and call do_hobby on each object.
"""

concatenate_lists = sorted_student_list + sorted_worker_list
for x in concatenate_lists:
    print(x.do_hobby())
