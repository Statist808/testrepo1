# подключаем модуль datetime
import datetime

# фиксируем и выводим время старта работы кода
start = datetime.datetime.now()
print('Время старта: ' + str(start))

# код, время работы которого измеряем
import  time
from threading import Thread

def start_potok(number):
    time.sleep(1)
    print(f"Potok № {number} started")

for i in range (5):
    start_potok(i + 1)
#фиксируем и выводим время окончания работы кода
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))

# вычитаем время старта из времени окончания
print('Время работы: ' + str(finish - start))