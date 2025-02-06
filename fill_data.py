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


def generate_fake_data(number_students, number_groups, number_teachers, number_grades, number_subjects ) -> tuple():
    fake_groups = []  # тут зберігатимемо компанії
    fake_students = []  # тут зберігатимемо співробітників
    fake_teachers =[]
    fake_grades = []
    fake_subjects=[]# тут зберігатимемо посади
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    # Створимо набір компаній у кількості number_companies
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_groups):
        fake_groups.append(fake_data.bs())

    # Та number_post набір посад
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.random_element(random_subjects_list))

    for _ in range(number_grades*number_students):
        fake_grades.append(randint(1,100))

    return fake_groups, fake_students, fake_teachers, fake_grades, fake_subjects


def prepare_data(companies, employees, posts) -> tuple():
    for_companies = []
    # готуємо список кортежів назв компаній
    for company in companies:
        for_companies.append((company, ))

    for_employees = []  # для таблиці employees

    for emp in employees:
        '''
        Для записів у таблицю співробітників нам потрібно додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        '''
        for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))

    '''
   Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
    виконувалася з 10 по 20 числа кожного місяця. Діапазон зарплат генеруватимемо від 1000 до 10000 у.о.
    для кожного місяця, та кожного співробітника.
    '''
    for_payments = []

    for month in range(1, 12 + 1):
        # Виконуємо цикл за місяцями'''
        payment_date = datetime(2021, month, randint(10, 20)).date()
        for emp in range(1, NUMBER_EMPLOYESS + 1):
            # Виконуємо цикл за кількістю співробітників
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments


def insert_data_to_db(groups, employees, payments) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('database.db') as con:

        cur = con.cursor()

        '''Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
        знаком заповнювача (?) '''

        sql_to_groups = """INSERT INTO groups(company_name)
                               VALUES (?)"""

        '''Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипта, а другим - дані (список кортежів).'''

        cur.executemany(sql_to_groups, groups)

        # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

        sql_to_employees = """INSERT INTO employees(employee, post, company_id)
                               VALUES (?, ?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_employees, employees)

        # Останньою заповнюємо таблицю із зарплатами

        sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
                              VALUES (?, ?, ?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_payments, payments)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_GRADES, NUMBER_SUBJECTS))
    insert_data_to_db(companies, employees, posts)
