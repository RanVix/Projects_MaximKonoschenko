# В матрице наити сумму элементов первых двух строк.
import random

def sum_two(matrix):
    return sum(map(sum, matrix[:2]))

n = int(input("Введите размер матрицы: "))

test_matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

print("Сгенерированная матрица:")
for row in test_matrix:
    print(row)

print(f"\nСумма элементов первых двух строк: {sum_two(test_matrix)}")