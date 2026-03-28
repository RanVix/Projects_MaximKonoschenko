get_lower_gen = lambda s: map(str.lower, s)

text = input("Введите обрабатываемую строку: ")
print(f"Исходная строка: {text}")

result = ''.join(get_lower_gen(text))

print(f"Результат: {result}")