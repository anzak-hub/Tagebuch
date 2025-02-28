from tools import add


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name
    
person_1 = Person("sss", 12)
person_2 = Person("Mathilde", 14)

personen_avg_age = add(person_1.age, person_2.age) / 2
print(personen_avg_age)