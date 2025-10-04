# Даны три переменные вещественного типа: А, В, С. Если их значения упорядочены
# по возрастанию, то удвоить их; в противном случае заменить значение каждой
# переменной на противоположное. Вывести новые значения переменных А, В, С.


try:
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
    number3 = float(input("Введите третье число: "))

    if number1 < number2 <  number3:
        number1 *= 2
        number2 *= 2
        number3 *= 2
    else:
        number1 = -number1
        number2 = -number2
        number3 = -number3

    print(f"Первое число = {number1}\nВторое число = {number2}\nТретье число = {number3}")

except ValueError:
    print("Вы ввели не число!")

except Exception as e:
    print(f"У нас ошибка: {e}")