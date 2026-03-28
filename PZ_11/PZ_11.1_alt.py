# В последовательности на n целых чисел умножить все элементы на последний
# минимальный элемент.

import random

def find_last_min_index(arr):
    min_element = min(arr)

    for i in range(len(arr)-1, -1, -1):
        if arr[i] == min_element:
            return i

def multiply(arr):
    last_min_index = find_last_min_index(arr)
    last_min_value = arr[last_min_index]

    return [i * last_min_value for i in arr]

def main():
    n = int(input("Введите кол-во элементов: "))
    arr = [random.randint(-10, 10) for i in range(n)]

    print("Последовательность: ", arr)

    result = multiply(arr)

    print("Результат: ", result)

if __name__ == "__main__":
    main()