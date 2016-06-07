# coding: utf-8
class City(object):

    def __init__(self, city_name, districts_number, buildings_number, citizens_number):
        self.city_name = city_name
        self.districts_number = districts_number
        self.buildings_number = buildings_number
        self.citizens_number = citizens_number

    def average_citizens_per_building(self):
        # return self.citizens_number / (self.buildings_number * self.districts_number)
        return self.citizens_number / self.buildings_number  # к вопросу в письме - считал как (дома в городе), вариант (дома в районе) закомментирован выше


data = {}  # данные для создания экземпляров класса
cities = []  # список экземпляров класса City
with open('in.txt') as file_in:  # читаем данный из файла
    raw_data = file_in.readlines()
for raw_line in raw_data:  # обходим список, прочтенный из файла
    line = raw_line.rstrip('\n').split()  # приводоим в удобоваримый вид
    data[line[0]] = [int(i) for i in line[1:]]  # добавляем данные в исходный словарь (ключ - название города, значение - список аттрибутов), использую генератор списка
for city_name in data:  # обходим словарь с данными и создаем список с экземплярами класса City
    cities.append(City(city_name, *data[city_name]))
with open('out.txt', 'w') as file_out:
    for city in cities:
        file_out.write('{0:<8} - {1}\n'.format(city.city_name, city.average_citizens_per_building()))
        # print '{0:<8} - {1}'.format(city.city_name, city.average_citizens_per_building())
