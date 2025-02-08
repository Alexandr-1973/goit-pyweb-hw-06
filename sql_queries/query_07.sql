SELECT g.grade, s.student_name, g2.group_name, s2.subject_title
FROM grades g
JOIN students s ON s.id=g.student_id
JOIN groups g2 ON g2.id = s.group_id
JOIN subjects s2 ON  s2.id = g.subject_id
WHERE s2.subject_title=? and g2.group_name=?