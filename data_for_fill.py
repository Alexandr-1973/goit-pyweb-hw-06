from datetime import datetime, timedelta
from itertools import cycle
import faker
from random import randint, choice

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20
NUMBER_SUBJECTS = 8
GRADES_PERIOD=90
random_subjects_list = [
    "Mathematics", "Physics", "Chemistry", "Biology", "History",
    "Literature", "Geography", "Computer Science", "English",
    "Philosophy", "Economics", "Law"
]

fake=faker.Faker()

teacher_cycle = cycle(range(1, NUMBER_TEACHERS + 1))
grades_data = [
            (randint(1, 100), student_id, randint(1, NUMBER_SUBJECTS), ((datetime.today() - timedelta(days=randint(0, GRADES_PERIOD))).date()).isoformat() )
            for student_id in range(1, NUMBER_STUDENTS + 1)
            for _ in range(NUMBER_GRADES)
        ]

fill_dict={
    "groups":{"sql":"""INSERT INTO groups(group_name)
                               VALUES (?)""", "data":[(fake.bs()[:30],) for _ in range(NUMBER_GROUPS)]},
    "students":{"sql":"""INSERT INTO students(student_name, group_id)
                               VALUES (?,?)""", "data":[(fake.name()[:50],randint(1,NUMBER_GROUPS)) for _ in range(NUMBER_STUDENTS)]},
    "teachers":{"sql":"""INSERT INTO teachers(teacher_name)
                               VALUES (?)""", "data":[(fake.name()[:50],) for _ in range(NUMBER_TEACHERS)]},
    "subjects":{"sql":"""INSERT INTO subjects(subject_title, teacher_id)
                                VALUES (?,?)""", "data":[(choice(random_subjects_list), next(teacher_cycle)) for _ in range(NUMBER_SUBJECTS)]},
    "grades":{"sql":"""INSERT INTO grades(grade, student_id, subject_id, created_at)
                                VALUES (?,?,?,?)""", "data":grades_data},
}