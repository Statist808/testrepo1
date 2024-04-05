import json
try:
    with open('1.json', "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

q1 = input('Вход или регистрация?')
if q1 == 'Вход':
    log = input("Введите логин:")
    psswd = input('Введите пароль:')
    if log in data.keys():
        if data[log] == psswd:
            print('успешный вход')
        else:
             print('неверный пароль')
    else:
        print('пользователь не найден')
elif q1 == "регистрация":
    log = input("Введите логин:")
    psswd = input('Введите пароль:')
    if log in data.keys():
        print('логин занят')
    else:
        data[log] = psswd
        with open('1.json', 'w') as f:
            json.dump(data, f)
        print("Регистрация успешна")



