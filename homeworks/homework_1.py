class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education_text = "I have higher education"
        else:
            education_text = "I don't have higher education"
        print(f'My name is {self.name}, my birthday is {self.birth_date}, '
              f'my profession is {self.occupation}, {education_text}')


person1 = Person(name='Maria', birth_date='15.03.1995', occupation='graphic designer', higher_education=True)
person2 = Person(name='Alice', birth_date='28.09.1998', occupation='actress', higher_education=False)
person3 = Person(name='Jordan', birth_date='04.06.1988', occupation='doctor', higher_education=True)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

person1.introduce()
person2.introduce()
person3.introduce()

