class Person:
    def __init__(self, first_name=None, last_name=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        fname = self.first_name if self.first_name is not None else "Ім'я не вказано"
        lname = self.last_name if self.last_name is not None else "Прізвище не вказано"
        age_str = f"{self.age} років" if self.age is not None else "Вік не вказано"
        return f"{fname} {lname}, {age_str}"


person1 = Person()
print(person1)

person2 = Person("Анна", "Пасмана",age="16")
print(person2)
