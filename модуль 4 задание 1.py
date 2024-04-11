sequence = [-1, 0, 2, 3, 4, 6, 8, 9]


def find_element(sequence, required_element):
    l = 0                  #
    r = len(sequence) - 1  # условия границ массива -1 (начало с 0)
    while l <= r:
        m = (l + r) // 2   # вычесление среднего элемента
        element = sequence[m]
        if element == required_element:
            return m
        if element < required_element: # начинаем смещещение границ массива для поиска
            l = m + 1
        else:
            r = m - 1
    return -1


print(find_element(sequence,8))