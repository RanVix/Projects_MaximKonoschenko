# Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно поставив последнюю строку между первой и второй.

with open("text18-17.txt", "r", encoding="utf-16-le") as file:
    content = file.read()

print("Содержимое файла:\n" + content + "\n")

marks = ".,—!:"
count = 0
for char in content:
    if char in marks:
        count += 1

print(f"Кол-во знаков препинания: {count}\n")

lines = content.split('\n')
    
last_line = lines[-1]

lines_without_last = lines[:-1]

lines_without_last.insert(1, last_line)

new_content = '\n'.join(lines_without_last)

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(new_content)

print("Текст после перестановки:")
print(new_content)