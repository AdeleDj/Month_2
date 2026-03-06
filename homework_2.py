class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education = 'I have higher education'
        else:
            education = 'I do not have higher education'
        print(f'My name is {self.name}, my birthday is {self.birth_date}, '
              f'my profession is {self.occupation}, {education}')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f'Hello! My name is {self.name}. '
              f'I study in group {self.group_name}. '
              f'I was born on {self.birth_date}. '
              f'I work as a {self.occupation}. ')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'Hello! My name is {self.name}. '
              f'I was born on {self.birth_date}. '
              f'My hobby is {self.hobby}.')


classmate1 = Classmate('Alina', '25.04.1998', 'software engineer', True, 'Python-64/1')
classmate2 = Classmate('John', '13.12.1999', 'data science', False, 'Java-58/2')

friend1 = Friend('Carlos', '28.04.1990', 'power engineer', True, 'football')
friend2 = Friend('Mike', '05.07.1994', 'sales manager', True, 'bicycle')

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()