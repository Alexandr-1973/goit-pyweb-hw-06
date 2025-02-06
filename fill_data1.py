from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20
NUMBER_SUBJECTS = 8
random_subjects_list = [
    "Mathematics", "Physics", "Chemistry", "Biology", "History",
    "Literature", "Geography", "Computer Science", "English",
    "Philosophy", "Economics", "Law"
]
fake=faker.Faker()

def insert_data_to_db_groups() -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('database.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, [(fake.bs()[:30],) for _ in range(NUMBER_GROUPS)])
        #
        # # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні
        #
        # sql_to_employees = """INSERT INTO employees(employee, post, company_id)
        #                        VALUES (?, ?, ?)"""
        #
        # # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію
        #
        # cur.executemany(sql_to_employees, employees)
        #
        # # Останньою заповнюємо таблицю із зарплатами
        #
        # sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
        #                       VALUES (?, ?, ?)"""
        #
        # # Вставляємо дані про зарплати
        #
        # cur.executemany(sql_to_payments, payments)
        #
        # # Фіксуємо наші зміни в БД

        con.commit()

def insert_data_to_db_students() -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('database.db') as con:

        cur = con.cursor()

        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?,?)"""

        cur.executemany(sql_to_students, [(fake.name()[:50],randint(1,NUMBER_GROUPS)) for _ in range(NUMBER_STUDENTS)])
        #
        # # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні
        #
        # sql_to_employees = """INSERT INTO employees(employee, post, company_id)
        #                        VALUES (?, ?, ?)"""
        #
        # # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію
        #
        # cur.executemany(sql_to_employees, employees)
        #
        # # Останньою заповнюємо таблицю із зарплатами
        #
        # sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
        #                       VALUES (?, ?, ?)"""
        #
        # # Вставляємо дані про зарплати
        #
        # cur.executemany(sql_to_payments, payments)
        #
        # # Фіксуємо наші зміни в БД

        con.commit()

insert_data_to_db_groups()
insert_data_to_db_students()