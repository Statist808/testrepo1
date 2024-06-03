import json
class Model:
         a = 1
         b = 2
         def save(self):
             dct = {"a": 1, "b": 2}
             with open('data.json', 'w', encoding='utf-8') as fout:
                json.dump(dct, fout)
obj = Model()
obj.save()
