SELECT s.id, s.student_name, Round(AVG(g.grade),2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.student_name
ORDER BY avg_grade DESC
LIMIT 5;