class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        if self.higher_education:
            education = 'I have higher education'
        else:
            education = 'I do not have higher education'
        print(f'My name is {self.name}, '
              f'my profession is {self.occupation}, {education}')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        if self.higher_education:
            education = 'I have higher education'
        else:
            education = 'I do not have higher education'

        print(f'Hello! My name is {self.name}. '
              f'I am a {self.occupation}. '
              f'I study in group {self.group_name}. '
              f'{education}. ')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        if self.higher_education:
            education = 'I have higher education'
        else:
            education = 'I do not have higher education'

        print(f'Hello! My name is {self.name}. '
              f'I am a {self.occupation}. '
              f'My hobby is {self.hobby}. '
              f'{education}.')


clssmt = Classmate("Ivan", "20.02.2000", "Student", True, "11D")
clssmt.introduce()

frnd = Friend("Aibek", "20.02.2000", "Student", True, "football")
frnd.introduce()