x = int(input("в ведите сумму вклада:"))
p = int(input("в ведите процент %:"))
y = int(input("в ведите сколько :"))
i = 0
while x < y:
    x += 1 * p / 100
    x = int(100 * x) / 100
    i += 1
print(i)