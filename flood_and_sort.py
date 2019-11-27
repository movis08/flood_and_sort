import json
from FakePeopleGenerator import FakePeopleGenerator
from Human import Human


def flood_file():
    people_count = 100001
    people_list = []
    fake_people_generator = FakePeopleGenerator()
    with open("fake_people.json", "w", encoding='UTF-8') as json_file:
        for index in range(1, people_count):
            fake_human = fake_people_generator.generate_new()
            people_list.append(fake_human)
            if index % 10000 == 0:
                print("Всего: {0:,}. Создано: {1:,}".format(people_count - 1, index).replace(',', ' '))
        json.dump(people_list, json_file)


def sort_people_in_file():
    with open("fake_people.json", "r", encoding='UTF-8') as json_file:
        people_list = json.load(json_file)
        for index in range(len(people_list)):
            people_list[index] = Human(**people_list[index])
        people_list.sort()

    with open("fake_people.json", "w", encoding='UTF-8') as json_file:
        json.dump(people_list, json_file)


if __name__ == '__main__':
    flood_file()
    sort_people_in_file()
