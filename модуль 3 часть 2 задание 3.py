my_dict = {'яблоко':'красное', 'лимон':'желтый', 'апельсин': "оранжевый"}
new_dict = {}
for key, value in my_dict.items():
    if value in new_dict:
        new_dict[value].append(key)
    else:
        new_dict[value] = [key]
print(new_dict)
