# Сгенерировать матрицу на произвольное количество элементов, в которой задается
# преобразование от предыдущего элемента к следующему на произвольное значение.

from random import randint
from functools import reduce

def generate_matrix(size):
    start_value = randint(1, 100)
    
    transformations = [randint(-20, 20) for _ in range(size - 1)]
    
    matrix = reduce(lambda acc, step: acc + [acc[-1] + step], transformations, [start_value])
    
    return matrix

size = randint(5, 10)
matrix1 = generate_matrix(size)
print(f"Матрица (всего элементов: {len(matrix1)}):")
print(matrix1)