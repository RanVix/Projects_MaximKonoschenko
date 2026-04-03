# В матрице наити сумму элементов первых двух строк.

def sum_first_two_rows(matrix):
    return sum(map(sum, matrix[:2])) if len(matrix) >= 2 else "У вас недостаточно строк, добавьте еще"

test_matrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

print(sum_first_two_rows(test_matrix))