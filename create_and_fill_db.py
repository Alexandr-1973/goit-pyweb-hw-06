import sqlite3
from data_for_fill import fill_dict

tables=["groups", "students", "teachers", "subjects", "grades"]

def create_db():
    with open('create_tables.sql', 'r') as f:
        sql = f.read()
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

def insert_data_to_db(table) -> None:
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.executemany(fill_dict[table]["sql"], fill_dict[table]["data"])
        con.commit()

def main():
    create_db()
    [insert_data_to_db(table) for table in tables]


if __name__ == "__main__":
    main()

