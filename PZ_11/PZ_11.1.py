import random

generate_seq = lambda n: [random.randint(-10, 10) for i in range(n)]

process_seq = lambda arr: list(map(lambda x: x * min(arr), arr))

def main():
    n = int(input("Введите кол-во элементов: "))
    
    arr = generate_seq(n)
    print(f"Последовательность: {arr}")
    
    result = process_seq(arr)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()