#Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево


try:
    number = int(input("Введите трехзначное число: "))

    if number < 100 or number > 999:
        print("Вы ввели не трехзначное число!")
        exit()

    first_number = number // 100
    second_number = (number // 10) % 10
    third_number = number % 10
    
    reversed_number = third_number * 100 + second_number * 10 + first_number

    print(f"Реверснутое число: {reversed_number}")

except ValueError:
    print(f"Вы ввели не число!")

except Exception as e:
    print(f"У нас ошибка... Будем чинить...: {e}")