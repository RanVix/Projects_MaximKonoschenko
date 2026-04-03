# 2.Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.

get_lower_gen = lambda s: map(str.lower, s)

text = input("Введите обрабатываемую строку: ")
print(f"Исходная строка: {text}")

result = ''.join(get_lower_gen(text))

print(f"Результат: {result}")