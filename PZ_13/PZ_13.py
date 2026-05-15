# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать кол-во полученных элементов.
import re

with open('experience.txt', 'r', encoding='utf-8') as file:
    content = " ".join(file.read().split())

pattern = r'\d+\s+(?:лет|года|год|месяцев|месяца|месяц)(?:\s+\d+\s+(?:месяцев|месяца|месяц))?'

results = re.findall(pattern, content)

print(f"Найдено элементов: {len(results)}\n")

for item in results:
    print(item)