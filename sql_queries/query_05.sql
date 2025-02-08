SELECT s.subject_title , t.teacher_name
FROM subjects s
JOIN teachers t ON t.id=s.teacher_id
WHERE t.teacher_name=?