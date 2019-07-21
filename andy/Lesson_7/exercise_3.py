"""
- Define class Worker derived from Human with:
  week_salary, work_hours_per_day properties
  money_per_hour() method, returns money earned per hour by the worker
  do_hobby - print 'reading' or some another hobby
"""
import andy.Lesson_7.exercise_1


class Worker(andy.Lesson_7.exercise_1.Human):

    def __init__(self, firstname, lastname, week_salary, work_hours):
        super().__init__(firstname, lastname)
        if self._is_valid(week_salary, work_hours):
            self.__week_salary = week_salary
            self.__work_hours = work_hours

    def money_per_hour(self):
        return self.__week_salary/self.__work_hours

    def _is_valid(self, __week_salary, __work_hours):
        return __week_salary, __work_hours is int and \
               __week_salary, __work_hours > 0

    def do_hobby(self):
        return self.full_name + " ebosit kak negr v 3 smeni"


a = Worker("Afro", "Black", 100, 5)
print(a.money_per_hour())
print(a.do_hobby())
