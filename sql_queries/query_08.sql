SELECT t.teacher_name , s.subject_title, Round(AVG(g.grade),2)
FROM teachers t
JOIN subjects s ON s.teacher_id = t.id
JOIN grades g ON g.subject_id = s.id
WHERE t.teacher_name=?
GROUP BY t.teacher_name , s.subject_title