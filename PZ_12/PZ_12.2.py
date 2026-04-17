# В матрице наити сумму элементов первых двух строк.

def sum_two(matrix):
    return sum(map(sum, matrix[:2]))

test_matrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

print(sum_two(test_matrix))