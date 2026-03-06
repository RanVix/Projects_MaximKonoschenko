# Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.

text = input("Введите обрабатываемую строку: ")
print("Исходная строка:", text)

def convert_to_lower(string):
    for char in string:
        yield char.lower()

result = ''.join(convert_to_lower(text))

print("Результат:", result)