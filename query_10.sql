SELECT DISTINCT s.student_name , t.teacher_name, s2.subject_title
FROM students s
JOIN grades g ON g.student_id = s.id
JOIN subjects s2 ON g.subject_id = s2.id
JOIN teachers t ON s2.teacher_id = t.id
WHERE s.student_name = ? and t.teacher_name = ?