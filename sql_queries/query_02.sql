SELECT s.id, s.student_name, Round(AVG(g.grade),2) AS avg_grade, sub.subject_title
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.subject_title=?
GROUP BY s.id, s.student_name, sub.subject_title
ORDER BY avg_grade DESC
LIMIT 1;
