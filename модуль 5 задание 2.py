import json
class Model:
         a = 1
         b = 2
         def save(self):
             dct = {k: str(v) for k, v in vars(Model).items()}
             with open('data.json', 'w', encoding='utf-8') as fout:
                json.dump(dct, fout)
obj = Model()
obj.save()
