# Дан список А ненулевых целых чисел размера 10. Вывести значение первого из тех
# его элементов Ак, которые удовлетворяют неравенству Ак < А10. Если таких
# элементов нет, то вывести 0.

import random

try:
    A = []

    while len(A) < 10:
        num = random.randint(-100, 100)
        if num != 0: 
            A.append(num)
        
    result = 0

    print(f"Исходный список: {A}")

    for i in range(0, 9):
        if A[i] < A[9]:
            result = A[i]
            break
        else:
            result = 0

    print(result)
    
except ValueError:
    print("Вы ввели не число!")
except Exception as e:
    print(e)
