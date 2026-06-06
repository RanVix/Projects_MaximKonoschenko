# Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации. БД
# должна содержать таблицу Работник со следующей структурой записи: фамилия, имя,
# отчество, возраст, пол, профессия, стаж работы.

import sqlite3
from AddDataToDB import insert_initial_data

DB_NAME = "employment.db"


def print_table(title, rows):
    print(f"\n Название операции: {title} ")
    for row in rows:
        print(row)

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            profession TEXT NOT NULL,
            experience INTEGER NOT NULL
        )
    """)

insert_initial_data()

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM workers")
    print_table("Исходное состояние базы данных", cursor.fetchall())
    
    cursor.execute("SELECT * FROM workers WHERE profession = 'Программист'")
    print_table("Поиск работников с профессией 'Программист'", cursor.fetchall())

    cursor.execute("SELECT * FROM workers WHERE experience >= 5 AND age <= 40")
    print_table("Поиск сотрудников со стажем >= 5 лет и возрастом <= 40 лет", cursor.fetchall())

    cursor.execute("SELECT * FROM workers WHERE last_name LIKE 'П%'")
    print_table("Поиск сотрудников, у которых фамилия начинается на 'П'", cursor.fetchall())
    
    # Запросы на редакт
    cursor.execute("UPDATE workers SET profession = 'Lead Дизайнер' WHERE id = 2")

    cursor.execute("UPDATE workers SET experience = experience + 1 WHERE profession = 'Инженер'")
    
    cursor.execute("UPDATE workers SET profession = 'Стажер' WHERE experience = 0")
    conn.commit()

    cursor.execute("SELECT * FROM workers")
    print_table("Состояние базы данных после операций редактирования", cursor.fetchall())
    
    # Запросы на удаление
    cursor.execute("DELETE FROM workers WHERE id = 1")
    
    cursor.execute("DELETE FROM workers WHERE age > 45")
    
    cursor.execute("DELETE FROM workers WHERE gender = 'Ж'")
    conn.commit()

    cursor.execute("SELECT * FROM workers")
    print_table("Состояние базы данных после операций удаления", cursor.fetchall())