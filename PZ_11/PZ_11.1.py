# В последовательности на n целых чисел умножить все элементы на последний
# минимальный элемент.

import random

n = int(input("Введите кол-во элементов: "))

arr = [random.randint(-10, 10) for i in range(n)]

print("Последовательность:", arr)

min_element = min(arr)

last_min_index = None
for i in range(len(arr)-1, -1, -1):
    if arr[i] == min_element:
        last_min_index = i
        break

last_min_value = arr[last_min_index]

result = []
for i in arr:
    result.append(i * last_min_value)

print("Результат:", result)