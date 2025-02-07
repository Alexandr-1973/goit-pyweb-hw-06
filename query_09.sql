SELECT DISTINCT s.student_name, sub.subject_title
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE s.student_name = ?;