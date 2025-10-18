# Составить программу, в которой функция построит изображение, в котором в первой
# строке 1 звездочка, во второй - 2, в третьей -3, …, в строке с номером m - m звездочек.


try:
    def draw_stars(m):
        for i in range(1, m + 1):
            print('*' * i)

    m = int(input("Введите количество строк m: "))
    draw_stars(m)

except ValueError:
    print("Вы ввели не число!")
except Exception as e:
    print(f"У нас ошибка {e}")