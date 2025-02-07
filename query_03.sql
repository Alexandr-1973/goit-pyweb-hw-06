SELECT gr.id AS group_id, gr.group_name, Round(AVG(g.grade),2) AS avg_grade, sub.subject_title
FROM groups gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.subject_title = ?
GROUP BY gr.id, gr.group_name, sub.subject_title
ORDER BY group_id;