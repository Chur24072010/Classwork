print('Lesson 3: Work with several classes\n')

class StudyGroup:
    group_name: str
    study_day: int
    teacher_name: str

    def __init__(self, group_name: str, study_day: int, teacher_name: str):
        self.group_name= group_name
        self.study_day = study_day
        self.teacher_name = teacher_name


    def __str__(self):
       return f'{self.group_name} {self.teacher_name}, день навчання {self.study_day}'



class StudySubject:
    name: str
    hours: int
    level: str
    def __init__(self, name: str, hours: int, level: str):
        self.name = name
        self.hours = hours
        self.level = level
    def __str__(self):
        return f'{self.name} {self.level}, кількість годин {self.hours}'
class Student:
    first_name: str
    second_name: str
    age: int
    is_offline: bool
    study_subject: StudySubject
    study_group: StudyGroup
    def __init__(self, second_name: str, first_name: str, age: int, study_subject: StudySubject,study_group: StudyGroup, is_offline=True):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.is_offline = is_offline
        self.study_subject = study_subject
        self.study_group = study_group

    def __str__(self):
        study_type: str
        if self.is_offline:
            study_type = 'offline'
        else:
            study_type = 'online'

        student_info = f'{self.second_name} {self.first_name}, вік {self.age}, навчається {study_type}'

        return f'{student_info}\n{self.study_subject}\n{self.study_group}'


py_senior = StudySubject('Python', 18, 'Senior')
C2118 = StudyGroup('C2118', 'Seturday', 'Полішко Костянтин')
DushlyukMakar = Student('Дишлюк', "Макар", 13, py_senior, C2118)
print(DushlyukMakar)