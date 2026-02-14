# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Количество пар, для которых произведение элементов делится на 3 (элементы пары в
# последовательности являются соседними):

import random

numbers_count = int(input("Введите кол-во элементов в последовательности: "))
numbers = [random.randint(-50, 50) for i in range(numbers_count)]

print(f"Исходный список: {numbers}")

with open("input_numbers.txt", "w", encoding="utf-8") as file:
    file.write(' '.join(map(str, numbers)))

product = 1
for num in numbers:
    product *= num

print(f"Прозведение всех элементов = {product}")

pairs_count = 0
for i in range(len(numbers) - 1):
    if (numbers[i] * numbers[i + 1]) % 3 == 0:
        pairs_count += 1

print(f"Количество пар, произведение элементов которых делится на 3: {pairs_count}")
print(f"Количество элементов: {len(numbers)}")

with open("output_numbers.txt", "w",encoding="utf-8") as file:
    file.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
    file.write(f"Количество элементов: {len(numbers)}\n")
    file.write(f"Произведение элементов: {product}\n")
    file.write(f"Количество пар, произведение элементов которых делится на 3: {pairs_count}\n")