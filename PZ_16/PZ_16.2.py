# Создание базового класса "Фигура" и его наследование для создания классов
# "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
# такие как вычисление площади и периметра, а классы-наследники будут иметь
# специфичные методы и свойства.

class Figure:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

square = Square(side=5)
rectangle = Rectangle(width=4, height=6)
circle = Circle(radius=3)

print("Квадрат:")
print(f"Площадь: {square.area()}")
print(f"Периметр: {square.perimeter()}")

print("\nПрямоугольник:")
print(f"Площадь: {rectangle.area()}")
print(f"Периметр: {rectangle.perimeter()}")

print("\nКруг:")
print(f"Площадь: {round(circle.area(), 2)}")
print(f"Периметр: {round(circle.perimeter(), 2)}")