# Дан список А размера N и целое число К (1 < K < 4, К < N ). Осуществить
# циклический сдвиг элементов списка влево на К позиций (при этом An перейдет в
# An k, An-1 - b An-K-1, …, A1- b An-K+1). Допускаeтся использовать вспомогательный
# список из 4 элементов.

try:
    n = int(input("Введите размер списка: "))
    A = []

    while len(A) < n:
        A.append(int(input()))

    K = int(input("Введите число позиций для сдвига: "))

    if not (1 < K < 4 and K < n):
        print("Ошибка! K не удовлетворяет условиям!")
    else:
        helper_list = [0] * 4
        for i in range(K):
            helper_list[i] = A[i]
        for i in range(n - K):
            A[i] = A[i + K]
        for i in range(K):
            A[n - K + i] = helper_list[i]
        print(A)

except ValueError:
    print("Вы ввели не число!")
except Exception as e:
    print(e)
