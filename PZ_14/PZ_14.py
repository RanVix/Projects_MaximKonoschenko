# Создать приложение по картинке
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Testform")
root.geometry("500x450")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Name
tk.Label(main_frame, text="Name").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(main_frame, width=30)
name_entry.grid(row=0, column=1, sticky="w", padx=10)

# Password
tk.Label(main_frame, text="Password").grid(row=1, column=0, sticky="w", pady=5)
pass_entry = tk.Entry(main_frame, width=30, show="*")
pass_entry.grid(row=1, column=1, sticky="w", padx=10)

# Gender
tk.Label(main_frame, text="Gender").grid(row=2, column=0, sticky="nw", pady=5)
gender_var = tk.StringVar()
gender_frame = tk.Frame(main_frame)
gender_frame.grid(row=2, column=1, sticky="w", padx=10)

tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(anchor="w")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(anchor="w")

# Continent
tk.Label(main_frame, text="Continent").grid(row=3, column=0, sticky="w", pady=5)
continent_var = tk.StringVar(value="Please select...")
continent_menu = ttk.OptionMenu(main_frame, continent_var, "Please select...")
continent_menu.grid(row=3, column=1, sticky="w", padx=10)

# Meals
tk.Label(main_frame, text="Meals").grid(row=4, column=0, sticky="nw", pady=5)
meals_frame = tk.Frame(main_frame)
meals_frame.grid(row=4, column=1, sticky="w", padx=10)

meal_breakfast = tk.IntVar()
meal_lunch = tk.IntVar()
meal_dinner = tk.IntVar()

tk.Checkbutton(meals_frame, text="breakfast", variable=meal_breakfast).pack(anchor="w")
tk.Checkbutton(meals_frame, text="lunch", variable=meal_lunch).pack(anchor="w")
tk.Checkbutton(meals_frame, text="dinner", variable=meal_dinner).pack(anchor="w")

# Remark
tk.Label(main_frame, text="Remark").grid(row=5, column=0, sticky="nw", pady=5)
remark_text = tk.Text(main_frame, width=40, height=5)
remark_text.grid(row=5, column=1, sticky="w", padx=10, pady=5)

# Кнопки
button_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
button_frame.pack(fill=tk.X, side=tk.BOTTOM)

cancel_btn = tk.Button(button_frame, text="Cancel", width=10)
cancel_btn.pack(side=tk.RIGHT, padx=10)

send_btn = tk.Button(button_frame, text="Send", width=10)
send_btn.pack(side=tk.RIGHT)

root.mainloop()