n = int(input("Введите число:"))
tot = 0
while n > 0:
    dig = n % 10
    tot = tot + dig
    n = n//10
print("Сумма цифр равна:", tot)