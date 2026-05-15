import random

a = [random.randint(1, 100) for _ in range(10)]

b = list(filter(lambda x: x % 4 != 0 and x % 10 == 8, a))

result = max(b) if b else "Список B пустой, не подошли по условию"

print(f"A: {a}")
print(f"B: {b}")
print(f"Максимум в B: {result}")