#Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево.

import tkinter as tk

def reverse_number():
    entry_value = entry.get()

    num = int(entry_value)
    
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    reversed_num = units * 100 + tens * 10 + hundreds

    label_result.config(text=f"Результат: {reversed_num}")

root = tk.Tk()
root.title("PZ_14")
root.geometry("350x200")

label_instruction = tk.Label(root, text="Введите трехзначное число:")
label_instruction.pack(pady=15)

entry = tk.Entry(root, width=10, justify="center")
entry.pack(pady=5)

button_calc = tk.Button(root, text="Перевернуть", command=reverse_number)
button_calc.pack(pady=15)

label_result = tk.Label(root, text="Результат: ")
label_result.pack(pady=5)

root.mainloop()