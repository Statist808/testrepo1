import json
class Model:
    def __init__(self):
        self.a = 1
        self.b = 2
    def save(self):
        dct = {k: v for k, v in  self.__dict__.items() if not k.startswith('_')}
        with open('data.json', 'w', encoding='utf-8') as fout:
            json.dump(dct,fout)
model_instance = Model()
model_instance.save()
