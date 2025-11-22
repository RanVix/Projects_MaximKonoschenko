# Дан список размера N. Найти номера двух ближайших элементов из этого списка (то
# есть элементов с наименьшим модулем разности) и вывести эти номера в порядке
# возрастания.
import random

try:
    n = int(input("Введите размер списка: "))   
    arr = []

    while len(arr) < n:
        num = random.randint(-100, 100)
        arr.append(num)

    if len(arr) < 2:
        print("Нужно ввести минимум 2 элемента!")
    else:
        print(f"Исходный список: {arr}")
        min_diff = abs(arr[1] - arr[0])
        index1, index2 = 0, 1

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                diff = abs(arr[i] - arr[j])

                if diff < min_diff:
                    min_diff = diff
                    index1, index2 = i, j

        print(index1, index2)

except ValueError:
    print("Вы ввели не число!")
except Exception as e:
    print(e)