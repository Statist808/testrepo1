class House():
    """описание дома"""
    def __init__(self, street, number):
      """свойства дома"""
        self.street = street
        self.number = number

    def build(self):
        """сторится дом"""
        print("дом на улице" + self.street + "под номером" + str(self.number + "построен.")
House1 = House("московская", 20)
House2 = House("московская", 21)
    def __dict__(House):
        return {House}

import json
object = House()
json.dumps(object.__dict__)
    with open('1.json', "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}



