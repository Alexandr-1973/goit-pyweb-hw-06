SELECT Round(AVG(g.grade ),2) AS avg_grade, t.teacher_name, s2.student_name
FROM grades g
JOIN subjects s ON s.id = g.subject_id
JOIN teachers t ON s.teacher_id = t.id
JOIN students s2 ON s2.id = g.student_id
WHERE t.teacher_name =? and s2.student_name =?
GROUP BY t.teacher_name, s2.student_name