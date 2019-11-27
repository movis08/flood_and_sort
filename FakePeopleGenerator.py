import random
from mimesis import Person
from mimesis.enums import Gender
from Human import Human


class FakePeopleGenerator:
    """
    Генератор фейковых личностей
    """

    def __init__(self):
        self.people_generator = Person('ru')
        self.gender_enum = Gender
        self.random = random

    def generate_new(self):
        """
        Генерация нового человека

        :return: Возвращает словарь с данными о человеке
        """
        gender = self.gender_enum.MALE if self.random.random() % 2 == 0 else self.gender_enum.FEMALE
        human = Human(
            last_name=self.people_generator.last_name(gender=gender),
            name=self.people_generator.name(gender=gender),
            surname=self.people_generator.surname(gender=gender),
            username=self.people_generator.username(),
            age=self.people_generator.age(minimum=24, maximum=99),
            telephone=self.people_generator.telephone(),
            academic_degree=self.people_generator.academic_degree(),
            blood_type=self.people_generator.blood_type(),
            nationality=self.people_generator.nationality(gender=gender),
        )

        return human
