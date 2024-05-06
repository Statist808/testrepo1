class House():
    '''описание дома'''
    def __init__(self, street, number):
        '''свойства дома'''
        self.street = street
        self.number = number

    def build(self):
        '''строиться дом'''
        print('дом на улице' + self.street + 'под номером' + self.number + " построен.")
House1 = House("московская", 20)
House2 = House('московская', 21)

print(House2.number)
import json

# Создание словаря
data = {}
# Преобразование словаря в JSON-строку
json_string = json.dumps(data)

# Запись JSON-строки в .json-файл
with open("data.json", "w") as json_file:
    json_file.write(json_string)



