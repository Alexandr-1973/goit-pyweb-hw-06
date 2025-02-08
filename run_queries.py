import random
import sqlite3
from pathlib import Path

def prepare_info(table, table_query):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute(f"SELECT {table}.{table_query} FROM {table}")
        return cur.fetchall()

def execute_query(sql, params_tuple) -> list:
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute(sql,params_tuple)
        result=cur.fetchall()
        return result

def main():
    sql_parameters_list=["subject_title=?", "teacher_name=?", "group_name=?", "student_name=?"]
    info_dict={
    "subject":prepare_info("subjects", "subject_title"),
    "teacher":prepare_info("teachers", "teacher_name"),
    "group":prepare_info("groups","group_name"),
    "student":prepare_info("students", "student_name")
    }

    for file_path in sorted(Path("sql_queries").iterdir()):
        with open(file_path, 'r') as f:
            sql = f.read()
        sql_params =[query_param for query_param in sql_parameters_list if query_param in sql]
        query_list = [sql_param.split("_")[0] for sql_param in sql_params]
        query_params_execute=tuple(random.choice(info_dict[param])[0] for param in query_list)
        print(f"{file_path}\n {execute_query(sql,query_params_execute)}\n")


if __name__ == "__main__":
    main()
