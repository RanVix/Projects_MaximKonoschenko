# Дан список А ненулевых целых чисел размера 10. Вывести значение первого из тех
# его элементов Ак, которые удовлетворяют неравенству Ак < А10. Если таких
# элементов нет, то вывести 0.

try:
    A = []

    while len(A) < 10:
        A.append(int(input()))
        
    result = 0

    for i in range(0, 9):
        if A[i] < A[9]:
            result = A[i]
            break

    print(result)
    
except ValueError:
    print("Вы ввели не число!")
except Exception as e:
    print(e)
