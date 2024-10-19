mport time
from threading import Thread

def start_potok(number):
    time.sleep(1)
    print(f"Potok № {number} started")

for i in range (5):
    start_potok(i + 1)